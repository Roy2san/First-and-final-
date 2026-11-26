# Исследования: почему тексты ИИ «слишком идеальные» и что на самом деле держит внимание

Обзор собран в ноябре 2026 года. У каждой работы указан тип источника: рецензируемая статья или препринт. Цифры приведены по аннотациям и материалам авторов.

## Содержание
1. Коротко
2. Что именно не так с ИИ-текстами
3. Почему так происходит
4. Что делает человеческие истории увлекательными
5. Восприятие и важные оговорки
6. Соцсети и YouTube: успешные и провальные ролики
7. Кино и длинные форматы: что затягивает
8. Как это превращено в правила скилла
9. Источники

---

## 1. Коротко

- **Предсказуемость.** ИИ-текст «идеальный» в смысле «самый вероятный». Модель выбирает типичное: типичную идею, типичный поворот, типичную фразу. Человеческий текст статистически не самый вероятный, и это не дефект, а источник интереса.
- **Сюжет и язык.** Сюжеты ИИ однородно позитивные: мало неудач, ранние повороты, нет саспенса. Язык полон клише, лишних объяснений, общих слов и «пурпурной прозы».
- **Причины.** Отчасти виновато обучение на человеческих оценках: оно снижает разнообразие и поощряет знакомое. Отчасти виновата безопасность: модели избегают конфликта, злодейства и острого юмора.
- **Восприятие.** Люди стабильно занижают оценки текстам, которые считают написанными ИИ, и меньше погружаются в них. Узнаваемые ИИ-паттерны напрямую стоят вовлечённости.
- **Что лечит.** Разнообразие на этапе идеи, явное планирование поворотов и неудач, конкретика, сильный голос (лучше всего по образцам) и прицельная редактура по известным категориям ошибок.

## 2. Что именно не так с ИИ-текстами

### Креативность и оригинальность

- **Torrance Test for Creative Writing** (Chakrabarty et al., CHI 2024, рецензируемая). 14 бинарных тестов по осям «беглость», «гибкость», «оригинальность», «проработка». 10 писателей оценили 48 рассказов. Истории LLM проходят в 3–10 раз меньше тестов, чем рассказы профессионалов. LLM к тому же плохо оценивают креативность сами, поэтому ИИ-судья здесь ненадёжен.
- **Creativity Index** (Lu et al., ICLR 2025, рецензируемая). Измеряли, насколько текст можно собрать из готовых фрагментов из интернета. У профессиональных авторов индекс в среднем на 66,2% выше, чем у LLM. Выравнивание (alignment) снижает индекс моделей в среднем на 30,1%.
- **Pron vs Prompt** (Marco et al., EMNLP 2024, рецензируемая). Писатель Патрисио Прон против GPT-4 Turbo, по 30 рассказов. Эксперты признали, что модель не готова конкурировать с топ-автором. При этом GPT-4 писал лучше по всем параметрам, когда названия рассказов давал Прон. Человеческая затравка поднимает качество.

### Сюжет и драматургия

- **Are LLMs Capable of Generating Human-Level Narratives?** (Tian et al., EMNLP 2024, рецензируемая).
  - Человеческие истории напряжённые, эмоционально возбуждающие и разнообразные по структуре. Истории LLM однородно позитивные и лишены напряжения.
  - Модели ставят поворотные точки раньше, делают меньше неудач и плохо прорабатывают «большую неудачу» и кульминацию.
  - Явное знание о сюжетных дугах повысило разнообразие на 45%. Знание о поворотных точках повысило саспенс и вовлечённость на 40% по сравнению с обычным промптом.
- **Experimental Narratives** (Beguš, Humanities and Social Sciences Communications 2024, рецензируемая). 250 историй людей против 80 историй GPT-3.5/4 на одинаковые промпты. Люди писали богаче и разнообразнее. ИИ выдавал «одну и ту же историю с небольшими изменениями»: формульную, без напряжения, с клише.
- **Echoes in AI** (Xu et al., PNAS 2025, рецензируемая). Метрика Sui Generis показывает, насколько уникален элемент сюжета среди альтернативных генераций той же модели. У человеческих историй она значительно выше. Сюжеты LLM состоят из элементов, которые повторяются от генерации к генерации. Метрика умеренно коррелирует с тем, насколько людей удивляет фрагмент. Лексическое разнообразие эту проблему не ловит: дело в повторяющихся сюжетах, а не в словах.
- **Too Good to be Bad** (Yi et al., ACL Findings 2026, рецензируемая). Чем аморальнее персонаж, тем хуже модели его играют: средняя оценка падает с 3,21 для «образцов добродетели» до 2,62 для злодеев. Сильнее всего проседают персонажи с эгоистичными мотивами. Сильно «выровненные» модели страдают больше.

### Язык и стиль

- **Can AI writing be salvaged?** (Chakrabarty, Laban, Wu, 2025, arXiv 2409.14509). Профессиональные писатели согласовали таксономию дефектов ИИ-текста:
  - клише;
  - лишняя экспозиция;
  - пурпурная проза;
  - неудачная структура предложений;
  - недостаток конкретики;
  - неуклюжий выбор слов;
  - несогласованность времён.

  Корпус LAMP содержит 1 057 абзацев LLM, отредактированных писателями. Проблемы общие для GPT-4o, Claude 3.5 Sonnet и Llama 3.1 70B. Эксперты больше всего предпочитают тексты, отредактированные экспертами, но и автоматическая правка по этой таксономии помогает. Многословие связывают с verbosity bias: при разметке предпочтений длинные ответы получают более высокие оценки.
- **Do LLMs write like humans?** (Reinhart et al., PNAS 2025, рецензируемая). По 66 признакам Байбера тексты LLM систематически отличаются от человеческих: плотный стиль с упором на существительные, причастные обороты в 2–5 раз чаще, номинализации в 1,5–2 раза чаще. У инструктивно дообученных моделей разрыв больше, и им труднее имитировать другие стили.
- **Delving into ChatGPT usage…** (Kobak et al., 2024–2025, arXiv 2406.07016). По 14 млн аннотаций PubMed частота слов вроде *delves* выросла в 28 раз сверх тренда, *underscores* в 10,9 раза, *showcasing* в 10,2 раза.
- **Antislop** (Paech et al., ICLR 2026, рецензируемая). Некоторые «слоп»-паттерны встречаются в выводе LLM более чем в 1000 раз чаще, чем у людей. Отпечатки паттернов специфичны для семейств моделей.
- **Wikipedia: Signs of AI writing** (полевое руководство редакторов, не научная работа). Описывает «регрессию к среднему»: конкретные необычные факты заменяются общей позитивной значимостью. Плюс отрицательные параллелизмы («не просто X, а Y»), правило трёх, «служит», «является» вместо «есть», рекламный тон. Сами редакторы предупреждают, что отдельный признак ничего не доказывает.

### Юмор и сценарии

- **A Robot Walks into a Bar** (Mirowski et al., FAccT 2024, рецензируемая). 20 комиков: шутки LLM пресные, держатся на стандартных тропах, редко удивляют. Модерация «срабатывает слишком рано», ещё до того, как найдена грань между оскорблением и сатирой.
- **Dramatron** (Mirowski et al., CHI 2023, рецензируемая). 15 профессиональных драматургов и сценаристов: выдача слишком проговорённая, мало субтекста, «просто рассказывает, а не показывает».

## 3. Почему так происходит

1. **Самый вероятный путь скучен.** Holtzman et al. (ICLR 2020, «The Curious Case of Neural Text Degeneration») показали, что человеческий текст не следует пути максимальной вероятности: распределения вероятностей человеческого текста и текста при максимизации сильно различаются. Максимизация вероятности даёт тусклый, повторяющийся текст.
2. **Дообучение на предпочтениях сужает разнообразие.** Kirk et al. (ICLR 2024): RLHF заметно снижает разнообразие ответов на один и тот же промпт по сравнению с обычным дообучением. Padmakumar & He (ICLR 2024): соавторство с InstructGPT, в отличие от базовой GPT-3, статистически значимо делает тексты разных людей похожими друг на друга.
3. **Люди-разметчики предпочитают знакомое.** Zhang et al. («Verbalized Sampling», ICML 2026) нашли typicality bias в данных предпочтений: разметчики систематически выбирают более привычный текст. Поэтому «схлопывание» к типичному произошло бы даже при идеальном обучении. Лекарство без дообучения: просить модель сгенерировать несколько вариантов с вероятностями. В творческом письме это дало в 1,6–2,1 раза больше разнообразия.
4. **Многословие вознаграждается.** Verbosity bias в разметке ведёт к лишней экспозиции и «цветистости» (Chakrabarty et al. 2025).
5. **Безопасность гасит конфликт.** Позитивный уклон сюжетов (Tian), беззубые злодеи (Yi) и цензура в юморе (Mirowski) объясняются одной логикой выравнивания: избегать негатива. А история без негатива почти невозможна.
6. **Сборка из готового.** ИИ-текст в большой степени собирается из фрагментов, уже существующих в интернете (Lu et al. 2025). Отсюда ощущение «где-то я это уже читал».

## 4. Что делает человеческие истории увлекательными

- **Саспенс и сюрприз** (Ely, Frankel, Kamenica, Journal of Political Economy 2015). Формальная модель развлекательной ценности информации. Саспенс — это дисперсия будущих убеждений: зритель понимает, что исход может пойти по-разному. Сюрприз — это величина изменения убеждения. Применения: детективы, спорт, игровые шоу. Вывод для сценария: держи исход неопределённым и меняй ожидания зрителя.
- **Информационный разрыв** (Loewenstein, Psychological Bulletin 1994). Любопытство возникает, когда внимание фокусируется на разрыве между тем, что человек знает, и тем, что хочет знать. Это ощущается как дефицит, который хочется закрыть. Отсюда открытые петли и «вопрос зрителя» в каждом бите.
- **Транспортация** (Green & Brock 2000; мета-анализ van Laer et al., Journal of Consumer Research 2014: 132 размера эффекта). Погружение в историю усиливает эмоциональный отклик и убеждающее действие. Ключевой механизм — мысленные образы, которые вызывает сюжет, отсюда ставка на конкретные детали.
- **Нарративная дуга** (Boyd, Blackburn, Pennebaker, Science Advances 2020; около 40 000 текстов). У традиционных историй три процесса: установка сцены (много артиклей и предлогов в начале), развитие сюжета, когнитивное напряжение (слова мышления растут к кульминации). Оговорка: следование «нормативной» структуре не связано с популярностью. Структура необходима, но не делает текст интересным сама по себе.

## 5. Восприятие и важные оговорки

- **«Штраф за ИИ».** Raj, Berg, Seamans (Journal of Experimental Psychology: General, 2026): 16 преднастроенных экспериментов, около 27 500 участников. Текст оценивают в среднем на 6,2% ниже, если думают, что его написал ИИ, и этот эффект «липкий». Chu & Liu (Journal of Communication 2024): метка «ИИ» снижает погружение и усиливает внутреннее сопротивление читателя независимо от реального автора. Вывод: узнаваемые ИИ-паттерны — это не косметика, они срезают вовлечённость.
- **Ясность ценится.** Porter & Machery (Scientific Reports 2024): неэксперты не отличили стихи ChatGPT от классиков и оценили ИИ-стихи выше, видимо за простоту и доступность. Не путай «человечность» с затемнённостью: текст должен оставаться ясным.
- **Поверхностные «человеческие» признаки обманчивы.** Jakesch et al. (PNAS 2023): люди принимают за признаки человека местоимения первого лица, разговорные сокращения и семейные темы, но угадывают ИИ на уровне случайности. Косметические трюки — не цель. Цель — содержательная разница: конфликт, конкретика, голос.
- **Индивидуальный плюс, коллективный минус.** Doshi & Hauser (Science Advances 2024): идеи от GPT-4 делали рассказы оценочно лучше, особенно у менее креативных авторов, но истории становились похожими друг на друга. Для канала или бренда это значит, что ИИ-дефолты делают вас неотличимыми от всех, кто использует те же дефолты.
- **Голос решает.** Chakrabarty, Ginsburg, Dhillon (2025, arXiv 2510.13939, препринт): подражание автору через промпт эксперты MFA уверенно отвергали (OR = 0,16 по стилистической верности и 0,13 по качеству). Дообучение на полном корпусе автора развернуло результат: эксперты стали предпочитать ИИ. Практически самый сильный рычаг — конкретные образцы нужного голоса, а не абстрактное «пиши хорошо».

## 6. Соцсети и YouTube: успешные и провальные ролики

Рецензируемых исследований именно про хуки в TikTok и Shorts мало. Большая часть популярных цифр («71% решают за 3 секунды») не имеет первоисточника. Ниже сначала то, что проверено, потом официальная справка платформ, потом практика.

**Рецензируемые исследования**
- **Что расшаривают** (Berger & Milkman, Journal of Marketing Research 2012; около 7 000 статей NYT плюс эксперименты). Делятся контентом, который вызывает эмоции высокой активации: восхищение, гнев, тревогу. Грусть, эмоция низкой активации, расшаривается хуже. Положительный контент в целом виральнее отрицательного. Удивительность, интерес и практическая польза тоже повышают виральность.
- **Что кликают** (Robertson et al., Nature Human Behaviour 2023; данные Upworthy: 105 000 вариантов заголовков, 370 млн показов). Каждое негативное слово в заголовке давало около +2,3% к кликабельности. Работала грусть, злость эффекта не дала. Вывод: клик и репост вызываются разными эмоциями.
- **Удержание в видеорекламе** (Teixeira, Wedel, Pieters, JMR 2012; распознавание мимики, айтрекинг, данные о переключении). Быстрый сюрприз в начале и затем длительная радость или интерес удерживали лучше, чем старая схема «всё ради панчлайна в конце».
- **Драматическая форма в рекламе** (Quesenberry & Coolsen, Journal of Marketing Theory and Practice 2014; 108 роликов Супербоула). Ролики с полной пятиактной структурой получали более высокие зрительские оценки, и чем больше актов, тем выше оценка.
- **История против аргумента.** Рекламные видео-истории, показанные как спонсорские посты в Instagram, держали внимание лучше аргументирующих. Механизм — погружение в историю (Coker et al., 2021).
- **Эмоциональные дуги** (Reagan et al., EPJ Data Science 2016; около 1 300 книг). У историй шесть базовых дуг. Del Vecchio et al. (2018, препринт): самые высокие кассовые сборы у фильмов с дугой «человек в яме» (падение, потом подъём).
- **Пик и конец** (Fredrickson & Kahneman 1993 и последующие работы). Память о коротком эпизоде определяют самый сильный момент и окончание. Для длинного и неоднородного контента эффект слабее.
- **Спойлеры.** Leavitt & Christenfeld (2011) обнаружили, что спойлеры повышают удовольствие от рассказа, но повторные исследования (Johnson & Rosenbaum 2015; Levine et al.) чаще находили обратное. Показывать исход в начале рискованно, и это работает, только если «как и почему» интереснее, чем «что».
- **Кликбейт.** Преувеличенные заголовки снижают доверие к источнику (Hurst 2016; Molyneux & Coddington 2020; Schoenmakers). Заголовки-вопросы воспринимаются хуже обычных, а заголовки, отсылающие вперёд, нейтральны (Engaging News Project, 2 057 человек). Невыполненное обещание вызывает разочарование и бьёт по доверию к каналу.

**Официальная справка YouTube**
- В отчёте об удержании есть метрика вступления: доля зрителей, оставшихся к 30-й секунде. Если до этой отметки досмотрели больше 50%, вступление считается сильнее обычного. В остальном YouTube советует сравнивать ролики с собственными типичными показателями канала.
- В Shorts есть метрика «Viewed vs. swiped away»: какая доля зрителей посмотрела ролик, а какая пролистала. Это прямой показатель силы первых секунд.

**Практика креаторов и агентств** (не проверено независимо, используй как гипотезы для тестов)
- Утёкший гайд MrBeast Production (2024, подлинность не подтверждена) называет главными метриками CTR, среднюю длительность и средний процент просмотра. Первая минута, по нему, — место наибольшего оттока. Решение снимать принимается по силе заголовка и обложки.
- Агентства советуют убирать логотип и брендинг из первых трёх секунд и менять кадр каждые 3–4 секунды.
- Ориентиры по Shorts: 70–80%+ досмотревших вступление — хорошо, ниже 60% — хук не работает.
- Средний процент просмотра длинных роликов около 24% (Retention Rabbit, 10 000+ видео). Лучшим ориентиром остаётся собственная аналитика канала.
- Скорость закадра около 150–160 слов в минуту.

**Типичные причины провала** (синтез перечисленного):
- медленный вход;
- обещание, которое не выполнено;
- перегруз идеями для своего хронометража;
- плоская середина без эскалации;
- мораль или штампованный призыв в конце;
- нечестный или непонятный поворот;
- монотонный ритм.

## 7. Кино и длинные форматы: что затягивает

- **Четыре части.** Thompson (Storytelling in the New Hollywood, 1999) и Cutting (Psychonomic Bulletin & Review 2016; 150 фильмов за 75 лет) описывают популярные фильмы как четыре части примерно равной длины: завязка, осложнение, развитие, кульминация, а также необязательные пролог и эпилог. Части разделены поворотами, критический поворот приходится на середину. Плотность монтажных переходов подтверждает эту разбивку статистически. Почти все протагонисты появляются в завязке.
- **Эмоциональные качели** (Berger, Kim, Meyer, Journal of Consumer Research 2021). Фильмы с большей эмоциональной волатильностью, то есть с большими перепадами между позитивом и негативом, получают более высокие оценки, особенно в жанрах, которые смотрят ради ощущений.
- **Форма и скорость истории** (Toubia, Berger, Eliashberg, PNAS 2021; около 50 000 текстов). Фильмы и эпизоды, которые «быстрее движутся» по смыслу, нравятся больше. Эпизоды сериалов, которые охватывают слишком много тем, нравятся меньше. Laurino Dos Santos & Berger (2022): лучше оценивают фильмы и эпизоды, которые начинаются медленнее и ускоряются к концу.
- **Порядок подачи** (Brewer & Lichtenstein 1981–1982, структурно-аффективная теория). Если исход отложен, возникает саспенс. Если исход показан до причин, возникает любопытство. Если информация скрыта и внезапно раскрыта, возникает сюрприз. Позднейшие работы показывают, что в реальных фильмах эти эмоции смешиваются и одна структура редко даёт только одну эмоцию.
- **Привязанность к героям** (теория аффективной диспозиции, Zillmann; проверка Kaspar et al., Frontiers in Psychology 2016). Саспенс и удовольствие зависят от отношения к персонажам: зритель хочет хорошего симпатичным и плохого несимпатичным. Чем больше симпатия к протагонисту, тем сильнее саспенс и интерес после просмотра.
- **Структура управляет вниманием** («нейрокинематика», Hasson et al., Projections 2008). Серия Хичкока синхронизировала мозговую активность зрителей гораздо сильнее, чем несмонтированная запись реальной жизни. Чем жёстче авторский контроль над структурой, тем одинаковее и сильнее вовлечение аудитории.
- **Клиффхэнгеры** (метаанализ Ghibellini & Meier, Humanities and Social Sciences Communications 2025; 59 публикаций). Тенденция возвращаться к прерванному делу (эффект Овсянкиной) общая и устойчивая. А «незаконченное лучше помнится» (эффект Зейгарник) универсально не подтверждается. Прямых исследований клиффхэнгеров нет, так что это перенос, а не доказательство.
- **Практика длинного YouTube.** Утёкший гайд MrBeast (подлинность не подтверждена) называет контрольные точки: первая минута, около 3-й минуты (поворот или эскалация) и около 6-й (ещё одна, даже если она требует подготовки). Если зритель досмотрел до середины, он, вероятно, досмотрит до конца. Креаторы советуют держать не больше 2–3 открытых вопросов одновременно и делать рехук каждые 60–90 секунд. Независимых проверок этих правил нет.

## 8. Как это превращено в правила скилла

| Находка | Правило в SKILL.md |
|---|---|
| Клик ≠ репост: грусть и негатив кликают, активирующие эмоции расшаривают; кликбейт бьёт по доверию | Шаг 2 «Упаковка», шаг 4 «Если цель — репосты» |
| Сюрприз в начале удерживает лучше панчлайна в конце | Шаг 4 «Награда сразу» |
| Пятиактная форма в рекламе, дуга «человек в яме» | Шаг 4: полная дуга даже в 30 сек, дуга по умолчанию |
| Пик и конец | Шаг 4 «Пик и конец», проход E |
| Спойлеры: данные противоречивы | Шаг 4 «Исход в начале — осторожно» |
| Метрики вступления и «Viewed vs. swiped» | Аудит «Палец над экраном», `formats.md` раздел 1 |
| Typicality bias, схлопывание к типичному, «эхо» сюжетов | Шаг 1: 6–10 вариантов с вероятностями, отбросить самые вероятные |
| Мало неудач, ранние повороты, позитивный уклон | Шаг 3: явные поворотные точки, обязательная большая неудача, заслуженный, а не обязательно счастливый финал |
| Беззубые антагонисты | Шаг 2: у отрицательного персонажа последовательный корыстный мотив |
| Саспенс, сюрприз, информационный разрыв | Шаг 3: «вопрос зрителя» в каждом бите, подготовленный сюрприз |
| Транспортация через образы, недостаток конкретики | Шаг 4: банк конкретики |
| Голос и дообучение на авторе | Шаги 0 и 5: просить образцы, выбирать рассказчика с позицией |
| Таксономия LAMP | Шаг 7: проходы A–E |
| Слоп-лексика, грамматика LLM, «Signs of AI writing» | `ai-tells.md` и `slop_check.py` |
| Метка «ИИ» срезает погружение | Финальный аудит на узнаваемые паттерны |
| Ясность ценится | Принцип «человечный ≠ с ошибками» |

## 9. Источники

**Кино и длинные форматы**
- Thompson (1999). Storytelling in the New Hollywood. Harvard University Press. Обзор: https://www.davidbordwell.net/blog/2011/06/09/cognitive-scientists-1-screenplay-gurus-0/
- Cutting (2016). Narrative theory and the dynamics of popular movies. Psychonomic Bulletin & Review 23(6). https://pmc.ncbi.nlm.nih.gov/articles/PMC5133278
- Berger, Kim, Meyer (2021). What Makes Content Engaging? How Emotional Dynamics Shape Success. Journal of Consumer Research 48(2). https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/Emotional-Volatility-1.pdf
- Toubia, Berger, Eliashberg (2021). How quantifying the shape of stories predicts their success. PNAS 118(26). https://business.columbia.edu/sites/default/files-efs/citation_file_upload/Toubia,%20Berger%20and%20Eliashberg%202021.pdf
- Brewer, Lichtenstein (1982). Stories are to entertain: A structural-affect theory of stories. Technical Report 265, University of Illinois. https://www.ideals.illinois.edu/items/17648
- Kaspar, Zimmermann, Wilbers (2016). Affective disposition theory and suspense. Frontiers in Psychology. https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01913/full
- Hasson et al. (2008). Neurocinematics: The Neuroscience of Film. Projections 2(1). https://pmc.ncbi.nlm.nih.gov/articles/PMC2818432
- Ghibellini, Meier (2025). Interruption, recall and resumption: a meta-analysis of the Zeigarnik and Ovsiankina effects. Humanities and Social Sciences Communications. https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05000-w.html


**Соцсети, реклама, YouTube**
- Berger, Milkman (2012). What Makes Online Content Viral? Journal of Marketing Research 49(2). https://faculty.wharton.upenn.edu/wp-content/uploads/2011/11/Virality.pdf
- Robertson et al. (2023). Negativity drives online news consumption. Nature Human Behaviour 7. https://pmc.ncbi.nlm.nih.gov/articles/PMC10202797/
- Teixeira, Wedel, Pieters (2012). Emotion-Induced Engagement in Internet Video Advertisements. Journal of Marketing Research 49(2). https://www.library.hbs.edu/working-knowledge/creating-online-ads-we-want-to-watch
- Quesenberry, Coolsen (2014). What Makes a Super Bowl Ad Super? Five-Act Dramatic Form Affects Consumer Super Bowl Advertising Ratings. Journal of Marketing Theory and Practice 22(4). https://mosaic.messiah.edu/bus_ed/31
- Coker et al. (2021). Video storytelling ads vs argumentative ads: how hooking viewers enhances consumer engagement. https://www.researchgate.net/publication/353022418
- Reagan et al. (2016). The emotional arcs of stories are dominated by six basic shapes. EPJ Data Science. https://arxiv.org/abs/1606.07772
- Del Vecchio et al. (2018). Improving productivity in Hollywood with data science: Using emotional arcs of movies to drive product and service innovation. Препринт. https://arxiv.org/abs/1807.02221
- Fredrickson, Kahneman (1993). Duration neglect in retrospective evaluations of affective episodes. JPSP 65(1).
- Leavitt, Christenfeld (2011). Story spoilers don't spoil stories. Psychological Science. Johnson, Rosenbaum (2015). Spoiler alert: consequences of narrative spoilers for dimensions of enjoyment, appreciation, and transportation. Communication Research.
- Engaging News Project: Question and forward-reference headlines (2 057 adults). https://www.journalism.co.uk/readers-perceive-question-based-headlines-more-negatively-study-shows/
- YouTube Help: Understand your content performance (Intro, Viewed vs. swiped away). https://support.google.com/youtube/answer/12220281
- MrBeast Production guide (утечка 2024, подлинность не подтверждена): разбор Tubefilter. https://www.tubefilter.com/2024/09/17/mrbeast-internal-production-guide-leaked-key-points/

**ИИ-тексты, творчество, нарратив**

- Chakrabarty, Laban, Agarwal, Muresan, Wu (2024). Art or Artifice? Large Language Models and the False Promise of Creativity. CHI 2024. https://arxiv.org/abs/2309.14556
- Chakrabarty, Laban, Wu (2025). Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits. https://arxiv.org/abs/2409.14509
- Chakrabarty, Ginsburg, Dhillon (2025). Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers. Препринт. https://arxiv.org/abs/2510.13939
- Tian et al. (2024). Are Large Language Models Capable of Generating Human-Level Narratives? EMNLP 2024. https://aclanthology.org/2024.emnlp-main.978
- Beguš (2024). Experimental Narratives: A Comparison of Human Crowdsourced Storytelling and AI Storytelling. Humanities and Social Sciences Communications. https://arxiv.org/abs/2310.12902
- Xu, Jojic, Rao, Brockett, Dolan (2025). Echoes in AI: Quantifying Lack of Plot Diversity in LLM Outputs. PNAS. https://arxiv.org/abs/2501.00273
- Yi et al. (2025/2026). Too Good to be Bad: On the Failure of LLMs to Role-Play Villains. ACL Findings 2026. https://arxiv.org/abs/2511.04962
- Lu et al. (2025). AI as Humanity's Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text. ICLR 2025. https://arxiv.org/abs/2410.04265
- Marco et al. (2024). Pron vs Prompt: Can Large Language Models already Challenge a World-Class Fiction Author at Creative Text Writing? EMNLP 2024. https://aclanthology.org/2024.emnlp-main.1096
- Mirowski, Love, Mathewson, Mohamed (2024). A Robot Walks into a Bar: Can Language Models Serve as Creativity Support Tools for Comedy? FAccT 2024. https://arxiv.org/abs/2405.20956
- Mirowski, Mathewson, Pittman, Evans (2023). Co-Writing Screenplays and Theatre Scripts with Language Models: An Evaluation by Industry Professionals. CHI 2023. https://arxiv.org/abs/2209.14958
- Holtzman, Buys, Du, Forbes, Choi (2020). The Curious Case of Neural Text Degeneration. ICLR 2020. https://arxiv.org/abs/1904.09751
- Kirk et al. (2024). Understanding the Effects of RLHF on LLM Generalisation and Diversity. ICLR 2024. https://arxiv.org/abs/2310.06452
- Padmakumar, He (2024). Does Writing with Language Models Reduce Content Diversity? ICLR 2024. https://arxiv.org/abs/2309.05196
- Zhang et al. (2025). Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity. ICML 2026. https://arxiv.org/abs/2510.01171
- Reinhart et al. (2025). Do LLMs write like humans? Variation in grammatical and rhetorical styles. PNAS. https://arxiv.org/abs/2410.16107
- Kobak et al. (2024–2025). Delving into ChatGPT usage in academic writing through excess vocabulary. https://arxiv.org/abs/2406.07016
- Paech, Roush, Goldfeder, Shwartz-Ziv (2025). Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models. ICLR 2026. https://arxiv.org/abs/2510.15061
- Wikipedia: Signs of AI writing (WikiProject AI Cleanup). https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Doshi, Hauser (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. Science Advances. https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532
- Porter, Machery (2024). AI-generated poetry is indistinguishable from human-written poetry and is rated more favorably. Scientific Reports. https://pmc.ncbi.nlm.nih.gov/articles/PMC11564748
- Jakesch, Hancock, Naaman (2023). Human heuristics for AI-generated language are flawed. PNAS. https://arxiv.org/abs/2206.07271
- Raj, Berg, Seamans (2026). The Artificial Intelligence Disclosure Penalty: Humans Persistently Devalue AI-Generated Creative Writing. Journal of Experimental Psychology: General 155(4). https://michiganross.umich.edu/news/readers-less-favorable-toward-ai-generated-creative-writing-berg-research-finds
- Chu, Liu (2024). Can AI tell good stories? Narrative transportation and persuasion with ChatGPT. Journal of Communication 74(5). https://doi.org/10.1093/joc/jqae029
- Ely, Frankel, Kamenica (2015). Suspense and Surprise. Journal of Political Economy 123(1). https://www.journals.uchicago.edu/doi/10.1086/677350
- Loewenstein (1994). The Psychology of Curiosity: A Review and Reinterpretation. Psychological Bulletin 116(1).
- Green, Brock (2000). The role of transportation in the persuasiveness of public narratives. Journal of Personality and Social Psychology 79(5).
- van Laer, de Ruyter, Visconti, Wetzels (2014). The Extended Transportation-Imagery Model: A Meta-Analysis. Journal of Consumer Research. https://cris.maastrichtuniversity.nl/en/publications/the-extended-transportation-imagery-model-a-meta-analysis-of-the-/
- Boyd, Blackburn, Pennebaker (2020). The narrative arc: Revealing core narrative structures through text analysis. Science Advances. https://pmc.ncbi.nlm.nih.gov/articles/PMC7413736
