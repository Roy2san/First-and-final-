#!/usr/bin/env python3
"""Проверка текста на типичные ИИ-паттерны и ровный ритм (русский и английский).

Использование:
    python3 slop_check.py story.txt
    cat story.txt | python3 slop_check.py -
    python3 slop_check.py story.txt --json

Это сигнал, а не вердикт: находки показывают, где стоит перечитать текст.
Только стандартная библиотека Python 3.8+.
"""
import json
import re
import statistics
import sys
from collections import Counter

# (категория, регулярка, подсказка). Регулярки ищутся без учёта регистра.
RU_PATTERNS = [
    ("канцелярит/вводные", r"\b(важно|стоит|следует) (отметить|подчеркнуть|учитывать|помнить)\b", "удали или скажи прямо"),
    ("канцелярит/вводные", r"\bв (современном мире|наше время|эпоху \w+)\b", "удали"),
    ("канцелярит/вводные", r"\b(таким образом|подводя итог|в заключение|в конечном (счёте|счете|итоге))\b", "удали вывод"),
    ("канцелярит/вводные", r"\bдавайте (разберёмся|разберемся|погрузимся|узнаем)\b", "начни сразу с сути"),
    ("пафос/значимость", r"\bигра\w* (ключевую|важную|огромную|решающую) роль\b", "что именно делает?"),
    ("пафос/значимость", r"\b(является|являлась|являются) неотъемлемой частью\b", "скажи проще"),
    ("пафос/значимость", r"\b(уникальн|невероятн|удивительн|незабываем)\w*", "замени конкретикой"),
    ("пафос/значимость", r"\bнастоящ\w+ (чудо|шедевр|праздник|испытание|магия)\b", "замени конкретикой"),
    ("пафос/значимость", r"\b(симфони|гармони|палитр)\w* (звуков|красок|эмоций|чувств)?", "торжественная метафора"),
    ("пафос/значимость", r"\bтан(ец|це|цу) света\b", "штамп"),
    ("пафос/значимость", r"\b(погрузиться|окунуться|погружаемся) в (мир|атмосферу)\b", "штамп"),
    ("пафос/значимость", r"\bраскры\w* (свой |её |его )?потенциал\w*", "штамп"),
    ("клише", r"\bсердце (пропустило удар|бешено колотилось|сжалось|замерло|ушло в пятки)\b", "клише: замени действием/деталью"),
    ("клише", r"\bвремя (словно |будто )?(остановилось|замерло)\b", "клише"),
    ("клише", r"\bтишин\w* (повисла|звенела|была оглушительной)|\bоглушительн\w* тишин\w*", "клише"),
    ("клише", r"\bмурашки (побежали|пробежали)\b", "клише"),
    ("клише", r"\bна (её|его) губах (заиграла|мелькнула|появилась) улыбка\b", "клише"),
    ("клише", r"\b(волна|вихрь|буря) (эмоций|чувств|облегчения|радости)\b", "клише"),
    ("клише", r"\bс замиранием сердца\b", "клише"),
    ("клише", r"\bсердце (было )?(полно|наполнилось|переполнено)\b", "клише"),
    ("клише", r"\bболь (не )?(утихала|отпускала|утихла)\b", "клише"),
    ("клише", r"\b(отпустить прошлое|двигаться дальше|начать (всё|все) с чистого листа|новая глава)\b", "клише"),
    ("клише", r"\bгде-то (вдалеке|вдали) (залаяла|лаяла) собака\b", "клише ИИ-прозы"),
    ("клише", r"\bвоздух был (пропитан|наполнен|густым)\b", "клише"),
    ("названные эмоции", r"\b(почувствовал|ощутил)\w* (грусть|радость|страх|облегчение|тревогу|боль|счастье|гордость|вину)\b", "покажи, не называй"),
    ("названные эмоции", r"\b(его|её|ее|их) (охватил|охватила|охватило|переполнял\w*|накрыл\w*)\b", "покажи, не называй"),
    ("названные эмоции", r"\bв (её|его|ее|их) глазах (читал\w*|блестел\w*|стоял\w*|светил\w*)\b", "покажи, не называй"),
    ("конструкции", r"\b(это|он|она|было|была|был) не просто\b[^.!?]{0,60}[,—–-]\s*(а|это)\b", "«не просто X, а Y»"),
    ("конструкции", r"\bне\s+\w+[,]?\s+а\s+\w+", "«не X, а Y»: проверь, нужен ли контраст"),
    ("конструкции", r"\bи знаете (что|почему)\?", "задушевный штамп"),
    ("конструкции", r"\b(служит|служат|стал\w*) (напоминанием|символом|доказательством|свидетельством)\b", "«служит символом»: скажи прямо"),
    ("мораль/вывод", r"\b(понял\w*|понима\w*|осознал\w*|осознава\w*)\b[^.!?]{0,15}(\bчто\b|:)", "вывод вслух: оставь зрителю"),
    ("мораль/вывод", r"\bглавное\s*[—–-]", "мораль"),
    ("мораль/вывод", r"\bведь (главное|самое важное|настоящ\w+)\b", "мораль"),
    ("хук-штамп", r"\bвы когда-нибудь (задумывались|замечали|думали)\b", "начни с конкретного образа"),
    ("хук-штамп", r"\bв этом (видео|ролике|выпуске) (мы|я) (расскажем|расскажу|разберём|узнаем)\b", "начни рассказывать"),
    ("хук-штамп", r"\bно (и )?это (ещё|еще) не всё\b", "конкретный рехук вместо фразы"),
    ("хук-штамп", r"\bоставайтесь до конца\b", "вопрос внутри истории вместо просьбы"),
    ("хук-штамп", r"\bпишите в комментариях\b", "конкретный спорный вопрос"),
    ("номинализации", r"\b\w{4,}(ение|ание|ость)\b", None),  # считается отдельно, без вывода каждой
]

EN_PATTERNS = [
    ("ai-lexicon", r"\b(delve|delves|delving|tapestry|testament|vibrant|intricate|pivotal|realm|unwavering|beacon|multifaceted|ever-evolving|seamless(ly)?|meticulous(ly)?|underscore[sd]?|showcas(e|es|ing)|foster(s|ing)?|bolster(ed)?|garner(ed)?|boasts?|interplay|nuanced)\b", "AI-marked word: replace with plain/concrete"),
    ("ai-lexicon", r"\b(embark(ed)? on|navigate the|navigating the|journey of|landscape of|symphony of|dance of)\b", "inflated metaphor"),
    ("ai-lexicon", r"\b(elevate|unleash|unlock|harness)\w*\b", "marketing verb"),
    ("filler", r"\b(it'?s worth noting|in today'?s (fast-paced )?world|at the end of the day|here'?s the thing|the truth is|let'?s dive in|in conclusion|ultimately)\b", "cut"),
    ("cliche", r"\b(a sense of|couldn'?t help but|little did (she|he|they) know|hung in the air|palpable|something shifted|time (seemed to )?st(ood|and) still)\b", "cliché"),
    ("cliche", r"\bbreath (she|he|they) didn'?t know (she|he|they) (was|were) holding\b", "cliché"),
    ("cliche", r"\b(eyes|eye) (sparkled|twinkled|glistened)\b|\bsmile tugged\b|\bthe weight of (the world|his words|her words|it all)\b", "cliché"),
    ("cliche", r"\bsomewhere,? (in the distance,? )?a dog barked\b|\bscent of ozone\b", "AI-fiction cliché"),
    ("named-emotion", r"\b(felt|feeling) (a )?(wave|surge|pang|rush|sense) of\b", "show, don't tell"),
    ("named-emotion", r"\b(she|he|they) felt (sad|happy|afraid|scared|relieved|angry|guilty|proud|anxious)\b", "show, don't tell"),
    ("construction", r"\b(it|this|that)(?:'s|\s+(?:is|was|isn'?t|wasn'?t))(?:\s+not)?\s+(just|only|merely)\b", "'not just X, it's Y'"),
    ("cliche", r"\bwind whisper\w*|\bwhisper\w* secrets\b", "cliché"),
    ("construction", r"\bnot \w+,? but \w+", "'not X but Y': is the contrast needed?"),
    ("construction", r"\b(serves|served|stands|stood) as (a |an )?(reminder|testament|symbol|beacon)\b", "use 'is' or show it"),
    ("construction", r",\s+(highlighting|underscoring|emphasizing|reflecting|symbolizing|showcasing|ensuring)\b", "trailing -ing 'analysis' clause"),
    ("construction", r"\b(and honestly|the result|the answer)\?\s", "rhetorical Q&A tic"),
    ("moral", r"\b(realized|understood) (that|then)\b|\bin the end,\b|\bthe (true|real) meaning of\b", "stated moral: let the reader infer"),
    ("hook-cliche", r"\bhave you ever (wondered|noticed|thought)\b|\bin this video,? (we|i)('ll| will)\b|\bbut that'?s not all\b|\bstay (tuned )?(un)?til the end\b", "start with a concrete image/conflict"),
    ("ai-names", r"\b(Elara|Kael|Lyra|Seraphina|Thorne|Aris|Sarah Chen|Marcus Chen)\b", "default AI-fiction name"),
]

SENT_SPLIT = re.compile(r"(?<=[.!?…])[\"»”')\]]*\s+|\n{2,}")
WORD = re.compile(r"[\w'’-]+", re.UNICODE)


def detect_lang(text):
    cyr = len(re.findall(r"[а-яё]", text, re.I))
    lat = len(re.findall(r"[a-z]", text, re.I))
    return "ru" if cyr >= lat else "en"


MARKUP_LINE = re.compile(r"^\s*(#.*|[-*_]{3,}|\|.*\||```.*)$")
LINE_PREFIX = re.compile(
    r"^\s*(?:[*_>]+\s*)*"                      # markdown bullets, bold, quotes
    r"(?:\[[^\]]{0,30}\]\s*)?"                   # [0–4 с], [0:00]
    r"(?:\d{1,2}:\d{2}(?:\s*[–-]\s*\d{1,2}:\d{2})?\s*)?"  # 0:00–0:04
    r"(?:[\w .()/-]{1,30}:\*{0,2}(?:\s+|$))?"         # labels: «Голос:», «VO:», «КАДР:»
)


def prose_only(text):
    """Убирает разметку сценария (заголовки, таймкоды, метки «Кадр:», «Голос:»),
    чтобы ритм и начала предложений считались по самому тексту."""
    out = []
    for line in text.splitlines():
        if MARKUP_LINE.match(line):
            out.append("")
            continue
        line = LINE_PREFIX.sub("", line, count=1).replace("**", "")
        out.append(line)
    return "\n".join(out)


def sentences(text):
    parts = [p.strip() for p in SENT_SPLIT.split(prose_only(text)) if p and p.strip()]
    return [p for p in parts if WORD.search(p)]


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def scan(text, patterns):
    hits, nominal = [], 0
    for cat, rx, hint in patterns:
        for m in re.finditer(rx, text, re.I | re.UNICODE):
            if hint is None:
                nominal += 1
                continue
            hits.append({"category": cat, "match": m.group(0), "line": line_of(text, m.start()), "hint": hint})
    return hits, nominal


def rhythm(sents):
    lens = [len(WORD.findall(s)) for s in sents]
    if len(lens) < 3:
        return {"sentences": len(lens)}
    mean = statistics.mean(lens)
    sd = statistics.pstdev(lens)
    cv = sd / mean if mean else 0.0
    band = sum(1 for n in lens if abs(n - mean) <= 0.3 * mean) / len(lens)
    starts = Counter(WORD.findall(s)[0].lower() for s in sents if WORD.findall(s))
    top = [(w, c) for w, c in starts.most_common(5) if c >= 3 and c / len(sents) >= 0.12]
    return {
        "sentences": len(lens),
        "mean_words": round(mean, 1),
        "stdev_words": round(sd, 1),
        "cv": round(cv, 2),
        "share_near_mean": round(band, 2),
        "short_sentences_le4": sum(1 for n in lens if n <= 4),
        "long_sentences_ge25": sum(1 for n in lens if n >= 25),
        "repeated_openers": top,
    }


def main(argv):
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    if not args or args[0] == "-":
        text = sys.stdin.read()
    else:
        with open(args[0], encoding="utf-8") as f:
            text = f.read()

    lang = detect_lang(text)
    words = len(WORD.findall(text))
    hits, nominal = scan(text, RU_PATTERNS if lang == "ru" else EN_PATTERNS)
    sents = sentences(text)
    rh = rhythm(sents)
    dashes = len(re.findall(r"\s[—–]\s|—", prose_only(text)))
    triads = len(re.findall(r"\b\w+,\s+\w+,?\s+(и|and)\s+\w+\b", text, re.I))
    per_k = (lambda n: round(n * 1000 / words, 1)) if words else (lambda n: 0)

    warnings = []
    if rh.get("cv") is not None and rh["cv"] < 0.4:
        warnings.append("Ритм ровный (CV длины предложений < 0.4): добавь очень короткие и длинные фразы.")
    if rh.get("share_near_mean", 0) > 0.6:
        warnings.append("Больше 60% предложений почти одной длины.")
    if rh.get("short_sentences_le4", 1) == 0 and rh.get("sentences", 0) >= 8:
        warnings.append("Нет ни одной короткой фразы (≤4 слов).")
    if rh.get("repeated_openers"):
        warnings.append("Повторяющиеся начала предложений: " + ", ".join(f"«{w}» ×{c}" for w, c in rh["repeated_openers"]))
    if dashes >= 3 and per_k(dashes) > 8:
        warnings.append(f"Много тире: {per_k(dashes)} на 1000 слов.")
    if triads >= 3 and per_k(triads) > 4:
        warnings.append(f"Много перечислений-троек: {triads}.")
    if lang == "ru" and per_k(nominal) > 35:
        warnings.append(f"Много отглагольных существительных и абстракций на -ение/-ание/-ость: {per_k(nominal)} на 1000 слов.")
    if sents:
        tail = " ".join(sents[-2:])
        rx = r"(понял\w*|осознал\w*|главное|ведь)" if lang == "ru" else r"(realized|in the end|the true meaning|learned that)"
        if re.search(rx, tail, re.I):
            warnings.append("Финал похож на мораль или вывод вслух: закончи образом или действием.")

    cats = Counter(h["category"] for h in hits)
    report = {
        "lang": lang,
        "words": words,
        "pattern_hits": len(hits),
        "hits_per_1000_words": per_k(len(hits)),
        "by_category": dict(cats),
        "rhythm": rh,
        "dashes_per_1000_words": per_k(dashes),
        "triads": triads,
        "warnings": warnings,
        "hits": hits,
    }

    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    print(f"Язык: {lang} | слов: {words} | предложений: {rh.get('sentences', 0)}")
    print(f"ИИ-паттернов: {len(hits)} ({per_k(len(hits))} на 1000 слов)")
    if cats:
        print("  по категориям: " + ", ".join(f"{c}: {n}" for c, n in cats.most_common()))
    if "cv" in rh:
        print(f"Ритм: в среднем {rh['mean_words']} слов, σ={rh['stdev_words']}, CV={rh['cv']}, "
              f"коротких(≤4): {rh['short_sentences_le4']}, длинных(≥25): {rh['long_sentences_ge25']}")
    print(f"Тире: {per_k(dashes)} на 1000 слов | тройки: {triads}")
    if warnings:
        print("\nПредупреждения:")
        for w in warnings:
            print("  • " + w)
    if hits:
        print("\nНаходки:")
        for h in sorted(hits, key=lambda h: h["line"]):
            print(f"  стр.{h['line']:>4} [{h['category']}] «{h['match']}» → {h['hint']}")
    if not hits and not warnings:
        print("\nЯвных сигналов нет. Это не значит, что текст интересный: проверь конфликт, неудачи и сюрприз.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
