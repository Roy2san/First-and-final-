# Исследования: почему тексты ИИ «слишком идеальные» и что на самом деле держит внимание

Обзор собран в ноябре 2026 года. У каждой работы указан тип источника: рецензируемая статья или препринт. Цифры приведены по аннотациям и материалам авторов.

## Содержание
1. Коротко
2. Что именно не так с ИИ-текстами
3. Почему так происходит
4. Что делает человеческие истории увлекательными
5. Восприятие и важные оговорки
6. Как это превращено в правила скилла
7. Источники

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

## 6. Как это превращено в правила скилла

| Находка | Правило в SKILL.md |
|---|---|
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

## 7. Источники

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
