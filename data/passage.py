# ─────────────────────────────────────────────────────────────────────────────
# Token factory helpers
# Each token is a plain dict rendered by the frontend JS.
# ─────────────────────────────────────────────────────────────────────────────

def W(text, reading, meaning, pos="名詞 (noun)", level="N4", notes=None):
    """Vocabulary word."""
    d = {"text": text, "reading": reading, "type": "word",
         "meaning": meaning, "pos": pos, "level": level}
    if notes:
        d["notes"] = notes
    return d


def G(text, reading, pattern, meaning, explanation, ex_jp="", ex_en="", level="N4"):
    """Grammar pattern."""
    return {"text": text, "reading": reading, "type": "grammar",
            "pattern": pattern, "meaning": meaning,
            "explanation": explanation, "example_jp": ex_jp,
            "example_en": ex_en, "level": level}


def P(text, meaning):
    """Particle."""
    return {"text": text, "reading": text, "type": "particle", "meaning": meaning}


def N(text, reading, meaning="proper noun"):
    """Proper name."""
    return {"text": text, "reading": reading, "type": "name", "meaning": meaning}


def T(text):
    """Plain (un-annotated) text."""
    return {"text": text, "type": "plain"}


# ─────────────────────────────────────────────────────────────────────────────
# N4 Passage — 「夢への道」The Road to Dreams
# Story: Kenji (健二), a university student, wants to become a translator.
# This single day covers all major N4 grammar patterns and N4/N5 vocabulary.
# ─────────────────────────────────────────────────────────────────────────────

SEGMENTS = [

    # ── Section 1: Introduction ──────────────────────────────────────────────

    {
        "id": "s01",
        "translation": "Kenji is a third-year university student who dreams of becoming a Japanese-language translator.",
        "section": "朝 (Morning)",
        "tokens": [
            N("健二", "けんじ", "Kenji — male given name"),
            P("は", "topic marker — marks what the sentence is about"),
            W("大学", "だいがく", "university", "名詞 (noun)", "N5"),
            W("三年生", "さんねんせい", "third-year student", "名詞 (noun)", "N4"),
            P("で", "copula て-form — 'being X, and…'; connects two noun clauses"),
            T("、"),
            W("日本語", "にほんご", "Japanese language", "名詞 (noun)", "N5"),
            P("の", "possessive / attributive particle — connects two nouns"),
            W("翻訳家", "ほんやくか", "translator", "名詞 (noun)", "N4",
              "翻 (translate) + 訳 (interpret) + 家 (professional)"),
            P("に", "goal/direction particle — used with なる to indicate 'becoming'"),
            G("なりたいと思っている",
              "なりたいとおもっている",
              "V-stem + たい + と思っている",
              "am thinking of becoming / intend to become",
              "Combines two patterns: ① V-stem + たい = want to do (expresses desire). "
              "② V plain form + と思っている = am thinking that / am planning. "
              "Together they express an ongoing intention or aspiration.",
              "医者になりたいと思っている。",
              "I am thinking I want to become a doctor."),
            T("。"),
        ],
    },

    {
        "id": "s02",
        "translation": "Today is an important day.",
        "tokens": [
            W("今日", "きょう", "today", "名詞 (noun)", "N5"),
            P("は", "topic marker"),
            W("大切", "たいせつ", "important; precious", "な形容詞 (na-adjective)", "N4"),
            P("な", "な connecting a な-adjective to a noun"),
            W("日", "ひ", "day", "名詞 (noun)", "N5"),
            T("だ。"),
        ],
    },

    {
        "id": "s03",
        "translation": "After waking up in the morning, he got dressed right away.",
        "tokens": [
            W("朝", "あさ", "morning", "名詞 (noun)", "N5"),
            W("起きて", "おきて", "woke up (て-form of 起きる)", "動詞 (verb)", "N5"),
            G("から", "から",
              "V て-form + から",
              "after doing ~",
              "Indicates that one action is completed before the next begins. "
              "The order is strictly sequential: A fully finishes, then B starts.",
              "ご飯を食べてから、歯を磨いた。",
              "After eating, I brushed my teeth."),
            T("、すぐ"),
            P("に", "manner particle — here meaning 'immediately/right away'"),
            W("着替えた", "きがえた", "changed clothes (past tense)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "s04",
        "translation": "Since he had been preparing since yesterday, everything he needed was already inside his bag.",
        "tokens": [
            W("昨日", "きのう", "yesterday", "名詞 (noun)", "N5"),
            P("から", "from (time) — indicates starting point"),
            W("準備", "じゅんび", "preparation", "名詞 (noun)", "N4"),
            G("していた",
              "していた",
              "V て-form + いた",
              "was doing ~ (past progressive / resultant state)",
              "て-form + いる describes an ongoing action or a state resulting from a past action. "
              "In the past tense (いた), it describes something that was happening or had been done.",
              "ずっと待っていた。",
              "I had been waiting the whole time."),
            G("ので",
              "ので",
              "Plain form + ので",
              "because; since (giving a reason)",
              "Attaches to plain form. ので sounds more objective and polite than から. "
              "Use it when the reason is a fact or natural consequence.",
              "雨が降ったので、試合は中止になった。",
              "Because it rained, the match was cancelled."),
            T("、バッグ"),
            P("の", "possessive particle"),
            W("中", "なか", "inside; within", "名詞 (noun)", "N5"),
            P("には", "には = に (location) + は (topic/contrast) — 'as for inside the bag'"),
            W("必要", "ひつよう", "necessary; needed", "な形容詞 (na-adjective)", "N4"),
            P("な", "な connecting adjective to noun"),
            T("もの"),
            P("が", "subject marker"),
            W("全部", "ぜんぶ", "all; everything", "副詞 (adverb)", "N4"),
            W("入っていた", "はいっていた", "was inside / had been put in", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    # ── Section 2: On the Train ───────────────────────────────────────────────

    {
        "id": "s05",
        "translation": "While riding the train, he thought about his plans for the day.",
        "section": "電車の中 (On the Train)",
        "tokens": [
            W("電車", "でんしゃ", "train; electric railway", "名詞 (noun)", "N5"),
            P("に", "location/vehicle particle — 'on the train'"),
            W("乗り", "のり", "riding (連用形 of 乗る)", "動詞 (verb)", "N4"),
            G("ながら",
              "ながら",
              "V-stem + ながら",
              "while doing ~ (simultaneous actions)",
              "Attaches to the verb stem (連用形). The action after ながら is the main action; "
              "the action before ながら happens at the same time. "
              "Both actions must share the same subject.",
              "音楽を聴きながら勉強した。",
              "I studied while listening to music."),
            T("、"),
            W("今日", "きょう", "today", "名詞 (noun)", "N5"),
            P("の", "possessive/attributive particle"),
            W("予定", "よてい", "schedule; plan", "名詞 (noun)", "N4"),
            G("について",
              "について",
              "Noun + について",
              "about ~; concerning ~; regarding ~",
              "A set phrase meaning 'about' or 'concerning'. Follows a noun directly. "
              "More formal: についての + noun (e.g. 日本についての本 — a book about Japan).",
              "環境問題について話し合った。",
              "We discussed environmental issues."),
            W("考えた", "かんがえた", "thought about; considered (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "s06",
        "translation": "In the morning, he was planning to go to Professor Yamada's office and discuss his graduation thesis.",
        "tokens": [
            W("午前中", "ごぜんちゅう", "during the morning; in the morning", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            N("山田先生", "やまだせんせい", "Professor Yamada"),
            P("の", "possessive particle"),
            W("研究室", "けんきゅうしつ", "laboratory; professor's office", "名詞 (noun)", "N4"),
            P("に", "direction/goal particle"),
            T("行って、"),
            W("卒業論文", "そつぎょうろんぶん", "graduation thesis", "名詞 (noun)", "N4",
              "卒業 (graduation) + 論文 (thesis/paper)"),
            G("について",
              "について",
              "Noun + について",
              "about ~; regarding ~",
              "Same pattern as before — 'について' following a noun.",
              "将来について考えた。",
              "I thought about the future."),
            W("話し合う", "はなしあう", "to discuss; to talk over", "動詞 (verb)", "N4",
              "話す (to speak) + 合う (mutually) → discuss"),
            W("予定", "よてい", "plan; schedule", "名詞 (noun)", "N4"),
            T("だ。"),
        ],
    },

    {
        "id": "s07",
        "translation": "The professor was surely busy, so there was a chance he might not be able to talk for long.",
        "tokens": [
            W("先生", "せんせい", "teacher; professor", "名詞 (noun)", "N5"),
            P("は", "topic marker"),
            W("忙しい", "いそがしい", "busy", "い形容詞 (i-adjective)", "N4"),
            G("はずだ",
              "はずだ",
              "Plain form + はずだ",
              "should be ~; expected to be ~",
              "Expresses the speaker's confident expectation based on reasoning or prior knowledge. "
              "はず is a noun meaning 'expectation'. NOT used for guesses — use かもしれない for that.",
              "彼はもう家に着いているはずだ。",
              "He should have arrived home by now."),
            T("から、"),
            W("長い", "ながい", "long", "い形容詞 (i-adjective)", "N5"),
            W("時間", "じかん", "time; duration", "名詞 (noun)", "N5"),
            W("話す", "はなす", "to speak; to talk", "動詞 (verb)", "N5"),
            G("ことはできない",
              "ことはできない",
              "V plain form + ことはできない",
              "cannot do ~ (emphatic negative ability)",
              "ことができる = can do. Adding は makes it contrastive/emphatic: 'that is not something I can do'. "
              "Basic form: ことができる (can do) → ことができない (cannot do) → ことはできない (definitely cannot do).",
              "今日はここを離れることはできない。",
              "I cannot leave this place today."),
            G("かもしれない",
              "かもしれない",
              "Plain form + かもしれない",
              "might ~; maybe ~; perhaps ~",
              "Expresses uncertainty — the speaker thinks something is possible but is not sure. "
              "More uncertain than はずだ. かも alone (casual) is also common in speech.",
              "雨が降るかもしれない。",
              "It might rain."),
            T("。"),
        ],
    },

    {
        "id": "s08",
        "translation": "But since there had been no reply to the email he sent last week, he had been a little worried.",
        "tokens": [
            T("でも、"),
            W("先週", "せんしゅう", "last week", "名詞 (noun)", "N4"),
            W("送った", "おくった", "sent (past tense)", "動詞 (verb)", "N4"),
            T("メール"),
            P("に", "target/object particle — 'to the email'"),
            W("返事", "へんじ", "reply; response", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            T("なかった"),
            G("ので",
              "ので",
              "Plain form + ので",
              "because (reason → consequence)",
              "ので attaches to plain form. Provides an objective reason. "
              "Compare: 〜から is more subjective; ので sounds more polite and matter-of-fact.",
              "頭が痛いので、早く帰ります。",
              "Because I have a headache, I'll go home early."),
            T("、"),
            W("少し", "すこし", "a little; slightly", "副詞 (adverb)", "N5"),
            W("心配", "しんぱい", "worry; anxiety", "名詞／な形容詞", "N4"),
            G("していた",
              "していた",
              "V て-form + いた",
              "was doing ~ / had been ~ing",
              "Past progressive. Shows an ongoing state or action in the past.",
              "ずっと彼女のことを心配していた。",
              "I had been worrying about her the whole time."),
            T("。"),
        ],
    },

    # ── Section 3: At the Station ─────────────────────────────────────────────

    {
        "id": "s09",
        "translation": "When he arrived at the station, he ran into his friend Suzuki.",
        "section": "駅にて (At the Station)",
        "tokens": [
            W("駅", "えき", "station (train/subway)", "名詞 (noun)", "N5"),
            P("に", "location particle"),
            W("着いた", "ついた", "arrived (past tense)", "動詞 (verb)", "N4"),
            G("とき",
              "とき",
              "V plain past + とき / Noun + のとき",
              "when ~; at the time of ~",
              "とき (時) is a noun meaning 'time/moment'. "
              "When the verb before it is past tense, the timing of the main clause is AFTER that past action. "
              "When present tense: 帰るとき (when going home) vs 帰ったとき (when I had returned).",
              "日本に来たとき、とても緊張した。",
              "When I came to Japan, I was very nervous."),
            T("、"),
            W("友達", "ともだち", "friend", "名詞 (noun)", "N5"),
            P("の", "possessive/attributive particle"),
            N("鈴木さん", "すずきさん", "Mr./Ms. Suzuki"),
            P("に", "target particle — 'ran into (him/her)'"),
            W("会った", "あった", "met; ran into (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "s10",
        "translation": "He was asked, \"Kenji, where are you heading?\"",
        "tokens": [
            T("「"),
            N("健二", "けんじ", "Kenji"),
            T("、どこ"),
            P("へ", "direction particle — 'toward where'"),
            W("行く", "いく", "to go", "動詞 (verb)", "N5"),
            T("の？」"),
            P("と", "quotation particle — marks direct/indirect speech"),
            G("聞かれた",
              "きかれた",
              "V passive (～られる/～かれる)",
              "was asked ~ (passive voice)",
              "Passive form: V ら-row + れる (for う-verbs) or V stem + られる (for る-verbs). "
              "Here 聞く → 聞かれる → 聞かれた. The speaker becomes the object of someone else's action.",
              "先生に名前を呼ばれた。",
              "I was called by my teacher (my name was called)."),
            T("。"),
        ],
    },

    {
        "id": "s11",
        "translation": "When he answered, \"I'm going to see my professor,\" Suzuki said, \"Oh, I see — good luck!\" and cheered him on.",
        "tokens": [
            T("「先生"),
            P("に", "target particle — 'to/toward the teacher'"),
            W("会い", "あい", "to meet (連用形 of 会う)", "動詞 (verb)", "N4"),
            G("に行く",
              "にいく",
              "V-stem + に行く / に来る",
              "go to do ~ / come to do ~",
              "Expresses movement for a purpose. V-stem (連用形) + に行く. "
              "に行く = go there in order to do; に来る = come there in order to do.",
              "映画を見に行った。",
              "I went to see a movie."),
            T("んだ」"),
            P("と", "quotation particle"),
            W("答える", "こたえる", "to answer; to reply", "動詞 (verb)", "N4"),
            G("と",
              "と",
              "V plain form + と (discovery/natural result conditional)",
              "when ~; if ~ (automatic result)",
              "と connects two clauses where the second naturally or automatically follows the first. "
              "Often used for discoveries, instructions, or descriptions of automatic sequences. "
              "Cannot be used with requests, invitations, or volitional endings.",
              "春になると、桜が咲く。",
              "When spring comes, the cherry blossoms bloom."),
            T("、"),
            N("鈴木さん", "すずきさん", "Mr./Ms. Suzuki"),
            P("は", "topic marker"),
            T("「そうか、"),
            W("頑張って", "がんばって", "do your best! (て-form of 頑張る)", "動詞 (verb)", "N4"),
            T("ね」"),
            P("と", "quotation particle"),
            W("言って", "いって", "said (て-form of 言う)", "動詞 (verb)", "N5"),
            G("くれた",
              "くれた",
              "V て-form + くれた",
              "did ~ for me (past) — favor received",
              "てくれる = someone does something for the speaker (or speaker's in-group) as a favor. "
              "The direction is: other person → speaker. Past tense: てくれた.",
              "友達が手伝ってくれた。",
              "My friend helped me (as a favor to me)."),
            T("。"),
        ],
    },

    # ── Section 4: University Library ─────────────────────────────────────────

    {
        "id": "s12",
        "translation": "After arriving at the university, he first stopped by the library.",
        "section": "大学にて (At the University)",
        "tokens": [
            W("大学", "だいがく", "university", "名詞 (noun)", "N5"),
            P("に", "location/goal particle"),
            W("着いて", "ついて", "arrived (て-form)", "動詞 (verb)", "N4"),
            G("から",
              "から",
              "V て-form + から",
              "after doing ~",
              "Strictly sequential: the first action fully completes before the second begins.",
              "手を洗ってから、ご飯を食べた。",
              "After washing my hands, I ate."),
            T("、まず"),
            W("図書館", "としょかん", "library", "名詞 (noun)", "N4"),
            P("に", "direction particle"),
            W("寄った", "よった", "stopped by; dropped in", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "s13",
        "translation": "He was there because he wanted to borrow some books to study for his exams.",
        "tokens": [
            W("試験", "しけん", "exam; test", "名詞 (noun)", "N4"),
            P("の", "attributive particle"),
            W("勉強", "べんきょう", "study; studying", "名詞 (noun)", "N5"),
            G("のために",
              "のために",
              "Noun + のために / V plain + ために",
              "for the purpose of ~; in order to ~",
              "ために (為に) indicates purpose or cause. "
              "With a noun: 健康のために (for health). "
              "With a verb (dictionary form): 勉強するために (in order to study). "
              "Distinguishable from ように: ために requires a volitional/controllable action.",
              "合格するために、毎日勉強している。",
              "I study every day in order to pass."),
            T("、いくつか"),
            P("の", "attributive particle — 'some (books)'"),
            W("本", "ほん", "book", "名詞 (noun)", "N5"),
            P("を", "direct object marker"),
            W("借り", "かり", "to borrow (stem)", "動詞 (verb)", "N4"),
            T("たかった"),
            G("から",
              "から",
              "Plain form + から",
              "because; since (giving a reason)",
              "から follows plain form and gives a subjective reason or motive. "
              "More direct/casual than ので. Often the speaker's own will or feeling.",
              "お腹が空いたから、何か食べたい。",
              "Because I'm hungry, I want to eat something."),
            T("だ。"),
        ],
    },

    {
        "id": "s14",
        "translation": "Inside the library it was quiet, and many students were studying.",
        "tokens": [
            W("図書館", "としょかん", "library", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("中", "なか", "inside; interior", "名詞 (noun)", "N5"),
            P("は", "topic marker"),
            W("静か", "しずか", "quiet; peaceful", "な形容詞 (na-adjective)", "N4"),
            T("で、たくさん"),
            P("の", "attributive particle"),
            W("学生", "がくせい", "student", "名詞 (noun)", "N5"),
            P("が", "subject marker"),
            W("勉強", "べんきょう", "study", "名詞 (noun)", "N5"),
            G("していた",
              "していた",
              "V て-form + いた",
              "was doing ~ (past progressive)",
              "Describes actions that were in progress at a past point in time.",
              "彼女は窓の外を見ていた。",
              "She was looking out the window."),
            T("。"),
        ],
    },

    # ── Section 5: Meeting the Professor ──────────────────────────────────────

    {
        "id": "s15",
        "translation": "When he knocked on the door of Professor Yamada's office, he heard a voice say \"Come in.\"",
        "section": "先生との面談 (Meeting with the Professor)",
        "tokens": [
            N("山田先生", "やまだせんせい", "Professor Yamada"),
            P("の", "possessive particle"),
            W("研究室", "けんきゅうしつ", "professor's office / lab", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            T("ドア"),
            P("を", "object particle"),
            T("ノックする"),
            G("と",
              "と",
              "V plain + と (conditional/sequential)",
              "when ~ / upon doing ~",
              "Describes a natural sequence or discovery. The second clause describes what happened as a result.",
              "ドアを開けると、猫がいた。",
              "When I opened the door, there was a cat."),
            T("、「どうぞ」"),
            P("と", "quotation particle"),
            T("いう"),
            W("声", "こえ", "voice; sound", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("聞こえた", "きこえた", "could be heard; was audible", "動詞 (verb)", "N4",
              "聞く (to listen) vs 聞こえる (to be audible / to hear naturally)"),
            T("。"),
        ],
    },

    {
        "id": "s16",
        "translation": "When he entered the room, the professor was on the phone.",
        "tokens": [
            W("部屋", "へや", "room", "名詞 (noun)", "N4"),
            P("に", "location particle"),
            W("入る", "はいる", "to enter", "動詞 (verb)", "N5"),
            G("と",
              "と",
              "V plain + と",
              "upon entering ~ (discovery conditional)",
              "と here shows that the discovery (professor was on the phone) happened immediately upon the action.",
              "家に帰ると、妹が泣いていた。",
              "When I got home, my sister was crying."),
            T("、先生"),
            P("は", "topic marker"),
            W("電話", "でんわ", "telephone; phone call", "名詞 (noun)", "N5"),
            P("を", "object particle"),
            G("していた",
              "していた",
              "V て-form + いた",
              "was doing ~ (past progressive / ongoing state)",
              "Here: was in the middle of a phone call.",
              "入ったとき、彼は電話をしていた。",
              "When I entered, he was on the phone."),
            T("。"),
        ],
    },

    {
        "id": "s17",
        "translation": "Since he was told to wait a little, he sat down in a chair and waited.",
        "tokens": [
            W("少し", "すこし", "a little; a moment", "副詞 (adverb)", "N5"),
            W("待つ", "まつ", "to wait", "動詞 (verb)", "N5"),
            G("ように言われた",
              "よういわれた",
              "V plain + ように言われた",
              "was told to ~",
              "ように言う means 'to tell someone to do something (softly)'. "
              "Passive form: ように言われた = was told to. "
              "More indirect than て-form + ください. Often used for instructions from authority.",
              "先生に早く来るように言われた。",
              "I was told by the teacher to come early."),
            G("ので",
              "ので",
              "Plain form + ので",
              "because; so (objective reason)",
              "Attaches to plain form. Sounds polite and objective.",
              "雨が降ったので、試合は中止になった。",
              "Because it rained, the game was cancelled."),
            T("、"),
            W("椅子", "いす", "chair", "名詞 (noun)", "N4"),
            P("に", "location particle"),
            W("座って", "すわって", "sat down (て-form)", "動詞 (verb)", "N4"),
            W("待った", "まった", "waited (past)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "s18",
        "translation": "The discussion with the professor ended up going longer than he had expected.",
        "tokens": [
            W("先生", "せんせい", "teacher; professor", "名詞 (noun)", "N5"),
            P("との", "と = with; の = attributive; 'with the teacher'"),
            W("話し合い", "はなしあい", "discussion; talk", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            W("思った", "おもった", "thought (past)", "動詞 (verb)", "N5"),
            G("より",
              "より",
              "Noun/V plain + より ~ (comparison)",
              "than ~; more than ~",
              "より marks the standard of comparison (the thing being compared against). "
              "Structure: A は B より + adjective = A is more [adjective] than B.",
              "今日は昨日より寒い。",
              "Today is colder than yesterday."),
            W("長く", "ながく", "long (adverb form of 長い)", "副詞", "N5"),
            T("なって"),
            G("しまった",
              "しまった",
              "V て-form + しまった",
              "ended up ~ing; (unfortunately) ~ed completely",
              "てしまう has two nuances: ① Completion (action done fully/irreversibly). "
              "② Regret (it happened, often unintentionally or unfortunately). "
              "Casual speech: てしまった → ちゃった (e.g. 忘れちゃった).",
              "財布を忘れてしまった。",
              "I forgot my wallet (and now it's a problem)."),
            T("。"),
        ],
    },

    {
        "id": "s19",
        "translation": "It was because he had been told it would be better to change the topic of his thesis.",
        "tokens": [
            W("論文", "ろんぶん", "thesis; paper; dissertation", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            T("テーマ"),
            P("を", "object particle"),
            W("変えた", "かえた", "changed (past)", "動詞 (verb)", "N4"),
            G("ほうがいい",
              "ほうがいい",
              "V past (た-form) + ほうがいい",
              "had better ~; it's better to ~",
              "Gives advice or a recommendation. "
              "V past + ほうがいい = advice to do something. "
              "V negative + ほうがいい = advice not to do something. "
              "Stronger than てください; implies the listener should really do it.",
              "早く寝たほうがいい。",
              "You had better go to sleep early."),
            P("と", "quotation particle"),
            W("言われた", "いわれた", "was told (passive of 言う)", "動詞 (verb)", "N5"),
            G("からだ",
              "からだ",
              "Plain form + からだ",
              "it is because ~ (stating reason as conclusion)",
              "から + だ used at the end of a sentence to give the reason as the conclusion/explanation.",
              "遅れた。電車が遅延したからだ。",
              "I was late. It's because the train was delayed."),
            T("。"),
        ],
    },

    {
        "id": "s20",
        "translation": "When he asked, \"I think this topic might be too difficult — what do you think?\" the professor replied, \"True, but if it's you, I'm sure you can write it. Please don't give up.\"",
        "tokens": [
            T("「このテーマ"),
            P("は", "topic marker"),
            W("難しい", "むずかしい", "difficult; hard", "い形容詞 (i-adjective)", "N5"),
            G("すぎる",
              "すぎる",
              "V-stem + すぎる / Adj stem + すぎる",
              "too ~; excessively ~",
              "Attaches to: V stem (飲みすぎる = drink too much), "
              "い-adj stem (高すぎる = too expensive), "
              "な-adj stem (静かすぎる = too quiet). "
              "Always implies a negative excess.",
              "食べすぎてしまった。",
              "I ate too much."),
            P("と", "quotation particle"),
            G("思いますが",
              "おもいますが",
              "Plain form + と思いますが",
              "I think that ~, but… (soft disagreement/question)",
              "と思う = to think that. Adding が after it softens the statement and invites a response.",
              "少し難しいと思いますが、いかがですか。",
              "I think it's a bit difficult, but what do you think?"),
            T("、どう"),
            W("思います", "おもいます", "think (polite)", "動詞 (verb)", "N5"),
            T("か？」"),
            P("と", "quotation particle"),
            W("聞く", "きく", "to ask / to listen", "動詞 (verb)", "N5"),
            G("と",
              "と",
              "V plain + と (result/discovery)",
              "when I asked ~ (then…)",
              "と marks the automatic/natural result that follows.",
              "聞くと、彼は笑った。",
              "When I asked, he laughed."),
            T("、先生"),
            P("は", "topic marker"),
            T("「そうですね、でもあなた"),
            G("なら",
              "なら",
              "Noun / plain form + なら",
              "if it's ~ / since it's you, then ~",
              "なら is a conditional that identifies a specific case. "
              "'あなたなら' = 'if it's you (specifically)' — implies confidence based on who you are.",
              "君ならできるはずだ。",
              "If it's you, you should be able to do it."),
            W("書ける", "かける", "can write (potential of 書く)", "動詞 (verb)", "N4"),
            G("はずです",
              "はずです",
              "Plain form + はずです",
              "should be able to ~ (confident expectation, polite)",
              "Polite form of はずだ. Expresses strong expectation based on reasoning.",
              "彼女はもう知っているはずです。",
              "She should already know."),
            T("。"),
            W("諦め", "あきらめ", "give up (stem of 諦める)", "動詞 (verb)", "N4"),
            G("ないでください",
              "ないでください",
              "V negative stem + ないでください",
              "please don't ~",
              "Polite negative request. V-ない + でください. "
              "Softer than V-るな (plain negative command).",
              "ここでタバコを吸わないでください。",
              "Please don't smoke here."),
            T("」とおっしゃった。"),
        ],
    },

    # ── Section 6: Meeting Maria ──────────────────────────────────────────────

    {
        "id": "s21",
        "translation": "After leaving the professor's office, he had already arranged to meet his foreign friend Maria.",
        "section": "マリアさんとの再会 (Reuniting with Maria)",
        "tokens": [
            W("研究室", "けんきゅうしつ", "professor's office", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("出た", "でた", "left; exited (past)", "動詞 (verb)", "N5"),
            G("後で",
              "あとで",
              "V past (た-form) + 後で",
              "after doing ~",
              "た-form + 後で: action 1 is completed before action 2 begins. "
              "Similar to てから but 後で can be used with nouns too (食事の後で).",
              "仕事が終わった後で、飲みに行った。",
              "After finishing work, we went out for drinks."),
            T("、"),
            W("外国人", "がいこくじん", "foreigner; person from abroad", "名詞 (noun)", "N4"),
            P("の", "possessive/attributive particle"),
            W("友達", "ともだち", "friend", "名詞 (noun)", "N5"),
            G("である",
              "である",
              "Noun + である + Noun",
              "who is ~; that is ~ (attributive copula)",
              "The literary/formal copula used to modify a following noun. "
              "だ cannot directly precede a noun, but である can, functioning like a relative clause: "
              "友達であるマリアさん = 'Maria, who is a friend.' "
              "More formal than the casual 友達のマリアさん; common in written Japanese and formal speech.",
              "医者である彼女は、毎日忙しい。",
              "She, who is a doctor, is busy every day."),
            N("マリアさん", "まりあさん", "Maria (foreign friend)"),
            P("と", "'with' particle"),
            W("会う", "あう", "to meet", "動詞 (verb)", "N4"),
            W("約束", "やくそく", "promise; appointment", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            G("していた",
              "していた",
              "V て-form + いた",
              "had been doing ~ / had arranged to ~",
              "Here expresses a prior arrangement or state.",
              "彼女と会う約束をしていた。",
              "I had made arrangements to meet her."),
            T("。"),
        ],
    },

    {
        "id": "s22",
        "translation": "Maria is an international student from Spain who can speak Japanese very well.",
        "tokens": [
            N("マリアさん", "まりあさん", "Maria"),
            P("は", "topic marker"),
            T("スペイン"),
            P("から", "from particle — point of origin"),
            W("来た", "きた", "came; arrived from (past)", "動詞 (verb)", "N5"),
            W("留学生", "りゅうがくせい", "international student; exchange student", "名詞 (noun)", "N4"),
            T("で、"),
            W("日本語", "にほんご", "Japanese language", "名詞 (noun)", "N5"),
            P("を", "object particle"),
            T("とても"),
            W("上手に", "じょうずに", "skillfully; well (adverb form)", "副詞", "N5"),
            W("話す", "はなす", "to speak", "動詞 (verb)", "N5"),
            G("ことができる",
              "ことができる",
              "V plain + ことができる",
              "can do ~; be able to ~",
              "Expresses ability or possibility. More formal than the potential verb form. "
              "ことができない = cannot do. ことができた = was able to.",
              "日本語で手紙を書くことができます。",
              "I can write a letter in Japanese."),
            T("。"),
        ],
    },

    {
        "id": "s23",
        "translation": "When he asked, \"Where shall we eat?\" she told him, \"Apparently a new restaurant opened near the station — why don't we try it?\"",
        "tokens": [
            T("「どこで"),
            W("食べ", "たべ", "eat (stem of 食べる)", "動詞 (verb)", "N5"),
            G("ましょうか",
              "ましょうか",
              "V-stem + ましょうか",
              "shall we ~? / let's ~ (suggestion/invitation)",
              "Volitional polite form + か makes a question. "
              "Used to suggest doing something together or to offer help. "
              "Without か: ましょう = let's do.",
              "一緒に行きましょうか。",
              "Shall we go together?"),
            T("」"),
            P("と", "quotation particle"),
            W("聞いた", "きいた", "asked; inquired (past)", "動詞 (verb)", "N5"),
            G("ら",
              "ら",
              "V past (た-form) + ら",
              "when ~ / if ~ (conditional; upon doing)",
              "たら is the most versatile Japanese conditional. "
              "Used for: completed actions (when…then), hypotheticals (if…), and discovery (upon doing, found that…). "
              "Unlike と, can be followed by requests, commands, invitations.",
              "家に帰ったら、電話してください。",
              "When you get home, please call me."),
            T("、「駅"),
            P("の", "possessive particle"),
            W("近く", "ちかく", "nearby; close (to)", "名詞 (noun)", "N4"),
            P("に", "location particle"),
            W("新しい", "あたらしい", "new", "い形容詞 (i-adjective)", "N5"),
            T("レストラン"),
            P("が", "subject marker"),
            W("できた", "できた", "was opened / came to exist (past)", "動詞 (verb)", "N5"),
            G("らしい",
              "らしい",
              "Plain form / Noun + らしい",
              "apparently ~; it seems that ~ (hearsay/inference)",
              "らしい expresses information the speaker heard from others or inferred from evidence. "
              "Does NOT express the speaker's own direct observation (use そうだ/ようだ for that). "
              "Also: noun + らしい = 'typical of' (男らしい = manly, typical of a man).",
              "彼は明日来ないらしい。",
              "Apparently he's not coming tomorrow."),
            T("よ。行って"),
            G("みない",
              "みない",
              "V て-form + みる (negative invitation form)",
              "why don't we try ~? / won't you try ~?",
              "てみる = try doing (to see what it's like). "
              "Negative invitation form: 〜てみない？ = won't you try doing? "
              "Positive: 〜てみましょう = let's try.",
              "日本料理を食べてみた。",
              "I tried eating Japanese food."),
            T("？」"),
            P("と", "quotation particle"),
            G("言われた",
              "いわれた",
              "V passive (〜われた) — 言う → 言われる → 言われた",
              "was told ~; [someone] said to [me/subject] (passive speech reporting)",
              "言われた is the passive past of 言う. The grammatical subject is the RECEIVER of the words, not the speaker. "
              "Here: [Kenji] was told by [Maria] — Kenji is the subject; Maria is the unstated agent. "
              "To name the agent explicitly, add に: マリアさんに言われた = 'was told by Maria.' "
              "KEY DISTINCTION: the perspective always sits with the receiver. "
              "Same event from the other side uses 言った (active): "
              "マリアさんが「行ってみない？」と言った = 'Maria said \"shall we try it?\"' — Maria is the active speaker. "
              "「行ってみない？」と言われた = '[I/he] was told \"shall we try it?\"' — subject received the words. "
              "You cannot swap these: 言われた is never the speaker's form.",
              "先生に名前を呼ばれた。",
              "My name was called by the teacher. (I was called by the teacher.)"),
            T("。"),
        ],
    },

    # ── Section 7: At the Restaurant ──────────────────────────────────────────

    {
        "id": "s24",
        "translation": "When they entered the restaurant, the entire menu was written in Japanese.",
        "section": "レストランで (At the Restaurant)",
        "tokens": [
            T("レストラン"),
            P("に", "location particle — 'upon entering'"),
            W("入る", "はいる", "to enter", "動詞 (verb)", "N5"),
            G("と",
              "と",
              "V plain + と",
              "when/upon doing ~ (discovery)",
              "Used for automatic results or discoveries. The speaker found something upon entering.",
              "箱を開けると、手紙が入っていた。",
              "When I opened the box, there was a letter inside."),
            T("、メニュー"),
            P("が", "subject marker"),
            W("全部", "ぜんぶ", "all; entirely", "副詞 (adverb)", "N4"),
            W("日本語", "にほんご", "Japanese language", "名詞 (noun)", "N5"),
            P("で", "means/method particle — 'in/using Japanese'"),
            W("書かれていた", "かかれていた", "was written (passive + progressive)", "動詞 (verb)", "N4",
              "書く → 書かれる (passive) → 書かれている (passive progressive) → 書かれていた (past)"),
            T("。"),
        ],
    },

    {
        "id": "s25",
        "translation": "While saying \"I was worried about whether I could read it, but it seems fine,\" Maria ordered happily.",
        "tokens": [
            N("マリアさん", "まりあさん", "Maria"),
            P("は", "topic marker"),
            T("「読める"),
            G("かどうか",
              "かどうか",
              "V / Adj plain + かどうか",
              "whether or not ~",
              "Embeds a yes/no question as a noun clause. "
              "'Whether (or not) ~ is ~'. "
              "More direct: 〜か〜ないか (whether ~ or not ~).",
              "彼が来るかどうかわからない。",
              "I don't know whether he will come or not."),
            W("心配", "しんぱい", "worry; anxiety", "名詞 (noun)", "N4"),
            T("だったけど、大丈夫"),
            G("みたい",
              "みたい",
              "Plain form / Noun + みたいだ",
              "seems like ~; looks like ~ (informal)",
              "Informal equivalent of ようだ. Based on direct observation or impression. "
              "Can also follow nouns: 子供みたい = like a child. "
              "Casual speech; more formal: ようです.",
              "彼は疲れているみたいだ。",
              "He seems to be tired."),
            T("」"),
            P("と", "quotation particle"),
            W("言い", "いい", "said (連用形 of 言う)", "動詞 (verb)", "N5"),
            G("ながら",
              "ながら",
              "V-stem + ながら",
              "while doing ~",
              "Simultaneous actions. Both share the same subject.",
              "歩きながら話した。",
              "I talked while walking."),
            T("、"),
            W("楽しい", "たのしい", "fun; enjoyable", "い形容詞 (i-adjective)", "N5"),
            G("そうに",
              "そうに",
              "Adj stem + そうに / V stem + そうに",
              "as if ~; looking like ~ (appearance adverb)",
              "そうだ (appearance) describes how something looks. "
              "そうな = attributive (楽しそうな顔 = a face that looks happy). "
              "そうに = adverb (楽しそうに笑った = laughed as if happily).",
              "嬉しそうに笑っていた。",
              "She was smiling as if happy."),
            W("注文した", "ちゅうもんした", "ordered (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "s26",
        "translation": "While waiting for the food, the two of them talked about each other's dreams.",
        "tokens": [
            W("料理", "りょうり", "dish; cooking; cuisine", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("待っている", "まっている", "waiting (progressive)", "動詞 (verb)", "N5"),
            G("間に",
              "あいだに",
              "V て-form + いる + 間に / Noun + の間に",
              "while ~ / during ~ (another event occurs)",
              "間に indicates that something happens within the timeframe of another action. "
              "The action in 間に clause is ongoing; another event occurs during it. "
              "Different from ながら: subject can differ; emphasizes the time window.",
              "彼女が寝ている間に、掃除した。",
              "While she was sleeping, I cleaned."),
            T("、"),
            W("お互い", "おたがい", "each other; one another; mutually", "代名詞 (pronoun)", "N4",
              "お互い is a reciprocal pronoun meaning 'each other' or 'mutually.' "
              "Used when an action or state applies in both directions between two (or more) parties. "
              "Common patterns: お互いに + verb (do ~ to/for each other), お互いの + noun (each other's ~), お互いを + verb (verb each other). "
              "The お prefix is honorific but お互い is now treated as a single word — you rarely see 互い alone. "
              "Example: お互いに助け合う = help each other; お互いの夢 = each other's dreams."),
            P("の", "possessive particle — 'each other's'"),
            W("夢", "ゆめ", "dream; aspiration", "名詞 (noun)", "N4"),
            G("について",
              "について",
              "Noun + について",
              "about ~; concerning ~",
              "Indicates the topic of discussion.",
              "未来について話した。",
              "We talked about the future."),
            W("話した", "はなした", "talked; discussed (past)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "s27",
        "translation": "He was asked by Maria, \"What do you want to do in the future?\"",
        "tokens": [
            T("「"),
            W("将来", "しょうらい", "future; one's future", "名詞 (noun)", "N4"),
            T("、"),
            W("何", "なに", "what", "代名詞 (pronoun)", "N5"),
            P("を", "object particle"),
            G("したいの",
              "したいの",
              "V-stem + たい + の (rising intonation = question)",
              "what do you want to do? (casual question)",
              "たい expresses the speaker's desire. "
              "In casual speech, の at the end of a sentence with rising intonation asks a question. "
              "Female speech or casual: 〜したいの？",
              "何が食べたいの？",
              "What do you want to eat?"),
            T("？」"),
            P("と", "quotation particle"),
            N("マリアさん", "まりあさん", "Maria"),
            P("に", "target particle — 'by Maria'"),
            G("聞かれた",
              "きかれた",
              "V passive (〜かれる/〜られる)",
              "was asked ~ (passive voice)",
              "Passive: someone performed an action ON the speaker. "
              "The action-doer is marked with に.",
              "先生に質問された。",
              "I was questioned by the teacher."),
            T("。"),
        ],
    },

    {
        "id": "s28",
        "translation": "He answered, \"I'm thinking of becoming a translator, but since my Japanese still isn't good enough, I know I need to study more.\"",
        "tokens": [
            T("「"),
            W("翻訳家", "ほんやくか", "translator", "名詞 (noun)", "N4"),
            P("に", "goal particle — 'become a translator'"),
            G("なろうと思っているんだけど",
              "なろうとおもっているんだけど",
              "V volitional + と思っている + んだけど",
              "I'm planning to become ~ but… (explaining with context)",
              "Volitional form (〜よう/〜おう) + と思っている = am planning to. "
              "んだ (explanatory の + だ) adds the nuance of explaining/giving context. "
              "けど at end softens, implying a contrast/continuation follows.",
              "留学しようと思っているんだけど、お金が足りない。",
              "I'm planning to study abroad, but I don't have enough money."),
            T("、まだ"),
            W("日本語", "にほんご", "Japanese language", "名詞 (noun)", "N5"),
            P("が", "subject marker"),
            W("上手", "じょうず", "skilled; good at", "な形容詞 (na-adjective)", "N5"),
            T("じゃない"),
            G("から",
              "から",
              "Plain form + から",
              "because; so (subjective reason)",
              "Gives a personal motive or reason.",
              "疲れたから、休む。",
              "Because I'm tired, I'll rest."),
            T("、もっと"),
            W("勉強", "べんきょう", "study; studying", "名詞 (noun)", "N5"),
            G("しなければならない",
              "しなければならない",
              "V-ない form + なければならない",
              "must do ~; have to ~ (obligation)",
              "Strong obligation. Formed: V-ない form drop い → なければ + ならない. "
              "Casual: なきゃ (short for なければ). Also: なくてはならない (same meaning). "
              "To say 'don't have to': なくてもいい.",
              "毎日練習しなければならない。",
              "I have to practice every day."),
            P("と", "quotation particle"),
            W("思っている", "おもっている", "am thinking; am of the opinion", "動詞 (verb)", "N4"),
            T("」"),
            P("と", "quotation particle"),
            W("答えた", "こたえた", "answered; replied (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "s29",
        "translation": "Maria told him, \"At first I couldn't speak at all either, but when I made a habit of practicing a little every day, I gradually became able to speak.\"",
        "tokens": [
            N("マリアさん", "まりあさん", "Maria"),
            P("は", "topic marker"),
            T("「私も"),
            W("最初", "さいしょ", "at first; the beginning", "名詞 (noun)", "N4"),
            P("は", "topic/contrast marker"),
            W("全然", "ぜんぜん", "not at all (with negative)", "副詞 (adverb)", "N4"),
            W("話せなかった", "はなせなかった", "couldn't speak (past negative potential)", "動詞 (verb)", "N4"),
            T("けど、"),
            W("毎日", "まいにち", "every day", "名詞 (noun)", "N4"),
            W("少しずつ", "すこしずつ", "little by little; gradually", "副詞 (adverb)", "N4"),
            W("練習する", "れんしゅうする", "to practice", "動詞 (verb)", "N4"),
            G("ようにしたら",
              "よういしたら",
              "V plain + ようにしたら",
              "when I started making a habit of ~",
              "ようにする = to make an effort to; to make it a practice. "
              "Combined with たら conditional: 'when I started consistently doing…'",
              "毎日運動するようにしたら、体が軽くなった。",
              "When I started exercising daily, I felt lighter."),
            T("、"),
            W("だんだん", "だんだん", "gradually; little by little", "副詞 (adverb)", "N4"),
            W("話せる", "はなせる", "can speak (potential of 話す)", "動詞 (verb)", "N4"),
            G("ようになった",
              "ようになった",
              "V plain (ability/state) + ようになった",
              "came to be able to ~; gradually became ~",
              "ようになる describes a change in ability or habit over time. "
              "ようになった = a change that has now been achieved. "
              "Contrast with ようにする: ようにする = you make the effort; ようになる = the change happens.",
              "毎日練習したら、上手に弾けるようになった。",
              "After practicing daily, I became able to play well."),
            T("よ」"),
            P("と", "quotation particle"),
            W("教えて", "おしえて", "told; taught (て-form)", "動詞 (verb)", "N5"),
            G("くれた",
              "くれた",
              "V て-form + くれた",
              "did ~ for me (as a favor)",
              "くれる = give TO the speaker. てくれる = perform an action in favor of speaker.",
              "先生が詳しく説明してくれた。",
              "The teacher explained it in detail for me."),
            T("。"),
        ],
    },

    # ── Section 8: Dinner ──────────────────────────────────────────────────────

    {
        "id": "s30",
        "translation": "When the food was brought to them, both of them were hungry, so they started eating right away.",
        "section": "夕食 (Dinner)",
        "tokens": [
            W("料理", "りょうり", "food; dish", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("運ばれて", "はこばれて", "was carried/brought (passive て-form)", "動詞 (verb)", "N4"),
            G("きた",
              "きた",
              "V て-form + きた",
              "came (toward us); started to ~ (change coming toward present)",
              "てくる describes: ① movement toward the speaker (physical). "
              "② A change that comes to the present moment (something started and reaches now). "
              "Contrast with ていく: ていく = moving/continuing away from now.",
              "段々暗くなってきた。",
              "It has gradually gotten darker (coming toward this moment)."),
            G("とき",
              "とき",
              "V plain past + とき",
              "when ~ (at the moment of)",
              "Past verb + とき: the timing of the main clause is after the past action.",
              "料理が来たとき、嬉しかった。",
              "When the food came, I was happy."),
            T("、二人とも"),
            W("お腹", "おなか", "stomach; belly", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("すいていた", "すいていた", "was hungry (progressive state)", "動詞 (verb)", "N4",
              "お腹がすく = to become hungry. Progressive: お腹がすいている = am hungry."),
            G("ので",
              "ので",
              "Plain form + ので",
              "because (objective reason)",
              "Objective, polite reason.",
              "遅くなったので、タクシーで帰った。",
              "Because it got late, I went home by taxi."),
            T("、すぐに"),
            W("食べ", "たべ", "eat (stem)", "動詞 (verb)", "N5"),
            G("始めた",
              "はじめた",
              "V-stem + 始める",
              "started to ~; began to ~",
              "始める (to begin) as an auxiliary verb attaches to the verb stem. "
              "The opposite: 〜終わる (finish doing). Also: 〜続ける (continue doing).",
              "雨が降り始めた。",
              "It started to rain."),
            T("。"),
        ],
    },

    {
        "id": "s31",
        "translation": "When Maria said \"Delicious!\" Kenji nodded while saying, \"Right? Japanese food really is something special.\"",
        "tokens": [
            T("「おいしい！」"),
            P("と", "quotation particle"),
            N("マリアさん", "まりあさん", "Maria"),
            P("が", "subject marker"),
            W("言う", "いう", "to say", "動詞 (verb)", "N5"),
            G("と",
              "と",
              "V plain + と (discovery/natural result)",
              "when ~ / upon saying ~",
              "Natural result conditional — what the speaker said triggered the next event.",
              "彼が笑うと、みんなも笑った。",
              "When he laughed, everyone laughed."),
            T("、「"),
            G("でしょう",
              "でしょう",
              "Plain form + でしょう",
              "right? / probably ~ (seeking agreement or expressing probability)",
              "でしょう (polite) / だろう (casual): ① Probability: 明日は雨でしょう (It will probably rain). "
              "② Seeking agreement (rising intonation): おいしいでしょう？ = It's good, isn't it?",
              "もうすぐ着くでしょう。",
              "They'll probably arrive soon."),
            T("？"),
            W("日本", "にほん", "Japan", "名詞 (noun)", "N5"),
            P("の", "possessive particle"),
            W("食べ物", "たべもの", "food; things to eat", "名詞 (noun)", "N5"),
            P("は", "topic marker"),
            W("本当に", "ほんとうに", "really; truly", "副詞 (adverb)", "N5"),
            W("おいしい", "おいしい", "delicious; tasty", "い形容詞 (i-adjective)", "N5"),
            T("よね」"),
            P("と", "quotation particle"),
            W("言い", "いい", "said (連用形 of 言う)", "動詞 (verb)", "N5"),
            G("ながら",
              "ながら",
              "V-stem + ながら",
              "while doing ~",
              "Simultaneous action.",
              "笑いながら話した。",
              "I talked while laughing."),
            T("、"),
            N("健二", "けんじ", "Kenji"),
            T("も"),
            W("頷いた", "うなずいた", "nodded (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    # ── Section 9: Parting ────────────────────────────────────────────────────

    {
        "id": "s32",
        "translation": "After the meal was over, they walked together as far as the station.",
        "section": "別れ (Parting)",
        "tokens": [
            W("食事", "しょくじ", "meal; dining", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("終わった", "おわった", "ended; finished (past)", "動詞 (verb)", "N5"),
            G("後で",
              "あとで",
              "V past (た-form) + 後で",
              "after ~; after doing ~",
              "た + 後で = after action is completed. Can also be used with nouns + の後で.",
              "映画を見た後で、夕食を食べた。",
              "After watching the movie, we had dinner."),
            T("、"),
            W("駅", "えき", "station", "名詞 (noun)", "N5"),
            G("まで",
              "まで",
              "Noun + まで / V plain + まで",
              "until ~; as far as ~ (extent)",
              "まで marks the end point in time or space. "
              "までに = by the time of (deadline). まで = until (ongoing up to that point).",
              "駅まで歩いた。",
              "I walked as far as the station."),
            T("一緒に"),
            W("歩いた", "あるいた", "walked (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "s33",
        "translation": "When he said, \"Thanks for today. Let's meet again sometime,\" Maria replied, \"Sure! Next time I'll cook Japanese food for you.\"",
        "tokens": [
            T("「今日はありがとう。またいつか"),
            G("会おう",
              "あおう",
              "V volitional form (〜よう / 〜おう)",
              "let's ~; I'll ~ (volitional — invitation or personal intention)",
              "The volitional expresses a will to act, used for suggestions ('let's ~') or personal intention ('I'll ~'). "
              "FORMATION — two rules: "
              "① U-verbs (Group 1): change the final u-row sound to the o-row + う. "
              "  会う→会おう, 書く→書こう, 飲む→飲もう, 話す→話そう, 待つ→待とう, 行く→行こう. "
              "② Ru-verbs (Group 2): drop る, add よう. "
              "  食べる→食べよう, 起きる→起きよう, 見る→見よう. "
              "Irregular: する→しよう, くる→こよう. "
              "Polite volitional: replace the final う/よう with ましょう (会いましょう, 食べましょう). "
              "THREE MAIN USES: "
              "① Suggestion / invitation (casual): 一緒に行こう！ = Let's go together! "
              "② Personal intention: 明日から頑張ろう = I'll try hard starting tomorrow. "
              "③ Volitional + と思う = planning: 留学しようと思っている = I'm thinking of studying abroad.",
              "疲れたね。少し休もう。",
              "We're tired, aren't we. Let's rest a bit."),
            T("ね」"),
            P("と", "quotation particle"),
            N("マリアさん", "まりあさん", "Maria"),
            P("に", "target particle — 'said to Maria'"),
            W("言う", "いう", "to say", "動詞 (verb)", "N5"),
            G("と",
              "と",
              "V plain + と",
              "when ~ / upon saying ~",
              "Natural result: upon the speaker saying this, Maria responded.",
              "頼むと、すぐ手伝ってくれた。",
              "When I asked, she helped me right away."),
            T("、「うん、今度は私"),
            P("が", "subject marker"),
            W("日本料理", "にほんりょうり", "Japanese cuisine; Japanese food", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("作って", "つくって", "make; cook (て-form)", "動詞 (verb)", "N5"),
            G("あげる",
              "あげる",
              "V て-form + あげる",
              "do ~ for (you/someone); give the favor of doing",
              "てあげる = the speaker (or subject) does something as a favor FOR someone else. "
              "Direction: speaker → other person. "
              "Careful: can sound presumptuous if overused. Humble: てさしあげる.",
              "荷物を運んであげた。",
              "I carried the luggage for him/her."),
            T("よ」"),
            P("と", "quotation particle"),
            W("言って", "いって", "said (て-form)", "動詞 (verb)", "N5"),
            G("くれた",
              "くれた",
              "V て-form + くれた",
              "did ~ for me (favor given to speaker)",
              "てくれる = someone does something for the speaker (in-group).",
              "妹が夕食を作ってくれた。",
              "My sister made dinner for me."),
            T("。"),
        ],
    },

    # ── Section 10: Diary Entry ────────────────────────────────────────────────

    {
        "id": "s34",
        "translation": "After getting home, Kenji wrote in his diary.",
        "section": "日記 (Diary)",
        "tokens": [
            W("家", "いえ", "home; house", "名詞 (noun)", "N5"),
            P("に", "goal particle — 'to home'"),
            W("帰って", "かえって", "returned home (て-form)", "動詞 (verb)", "N5"),
            G("から",
              "から",
              "V て-form + から",
              "after doing ~",
              "Strict sequential order: returned home first, then wrote.",
              "シャワーを浴びてから、寝た。",
              "After taking a shower, I went to sleep."),
            T("、"),
            N("健二", "けんじ", "Kenji"),
            P("は", "topic marker"),
            W("日記", "にっき", "diary; journal", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("書いた", "かいた", "wrote (past)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "s35",
        "translation": "\"A lot happened today, but it was a very fulfilling day. I was able to consult the professor about my thesis, and I also had a great time talking with Maria. I have to keep working hard tomorrow too, but I want to keep moving forward, one step at a time toward my dream.\"",
        "tokens": [
            T("「今日はいろいろなことがあった"),
            G("が",
              "が",
              "Sentence + が + Sentence",
              "but; although (contrast/concession)",
              "が as a conjunction at sentence boundary means 'but' or 'although'. "
              "More formal than けど. The first clause concedes something; the second gives the main point.",
              "難しかったが、楽しかった。",
              "It was hard, but it was fun."),
            T("、とても"),
            W("充実した", "じゅうじつした", "fulfilling; rewarding (past adj.)", "動詞 (verb)", "N4"),
            W("一日", "いちにち", "one day; a day", "名詞 (noun)", "N5"),
            T("だった。"),
            W("先生", "せんせい", "teacher; professor", "名詞 (noun)", "N5"),
            P("に", "target particle"),
            W("論文", "ろんぶん", "thesis; paper", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            T("ことを"),
            W("相談する", "そうだんする", "to consult; to discuss", "動詞 (verb)", "N4"),
            G("ことができた",
              "ことができた",
              "V plain + ことができた",
              "was able to ~ (past ability)",
              "Past form of ことができる. 'Was able to do something on this occasion.'",
              "一人で解決することができた。",
              "I was able to solve it by myself."),
            G("し",
              "し",
              "Plain form + し (listing parallel reasons or facts)",
              "and also ~; what's more ~ (listing)",
              "し is used to list multiple reasons or facts that all point the same direction. "
              "Often implies 'and there are other reasons too'. Used in both affirmative and negative contexts.",
              "彼は頭がいいし、優しいし、人気がある。",
              "He is smart, kind, and popular (on top of that)."),
            N("マリアさん", "まりあさん", "Maria"),
            P("とも", "と (with) + も (also)"),
            W("楽しく", "たのしく", "enjoyably; happily (adverb form)", "副詞", "N4"),
            W("話せた", "はなせた", "was able to talk (past potential)", "動詞 (verb)", "N4"),
            T("。"),
            W("明日", "あした", "tomorrow", "名詞 (noun)", "N5"),
            T("も"),
            W("頑張ら", "がんばら", "do one's best (stem of 頑張る)", "動詞 (verb)", "N4"),
            G("なければならない",
              "なければならない",
              "V-ない form (drop い) + なければならない",
              "must ~; have to ~ (strong obligation)",
              "Two ways to form: ① V-なければならない ② V-なくてはならない. "
              "Casual contractions: なきゃ / なくちゃ.",
              "宿題をしなければならない。",
              "I have to do my homework."),
            G("が",
              "が",
              "Clause + が",
              "but; although (concession)",
              "Concessive conjunction between two clauses.",
              "行きたいが、時間がない。",
              "I want to go, but I don't have time."),
            T("、"),
            W("夢", "ゆめ", "dream; goal; aspiration", "名詞 (noun)", "N4"),
            P("に", "direction/goal particle"),
            W("向かって", "むかって", "facing toward; heading toward", "動詞 (verb)", "N4"),
            W("一歩", "いっぽ", "one step", "名詞 (noun)", "N4"),
            T("ずつ"),
            W("進んで", "すすんで", "advance; move forward (て-form)", "動詞 (verb)", "N4"),
            G("いきたい",
              "いきたい",
              "V て-form + いきたい",
              "want to go on doing ~; want to continue ~",
              "ていく describes an action moving away from the present (into the future). "
              "Combined with たい: expresses the desire to continue doing something going forward.",
              "これからも勉強し続けていきたい。",
              "I want to keep on studying from here on."),
            P("と", "quotation particle"),
            W("思う", "おもう", "to think", "動詞 (verb)", "N5"),
            T("。」"),
        ],
    },
]

# Grammar patterns index — for the sidebar
GRAMMAR_PATTERNS = [
    {"id": "g_naritai", "pattern": "V-stem + たい + と思っている", "meaning": "intend to become / am thinking of ~ing", "level": "N4"},
    {"id": "g_tekara", "pattern": "V て-form + から", "meaning": "after doing ~", "level": "N4"},
    {"id": "g_teita", "pattern": "V て-form + いた", "meaning": "was doing ~ (past progressive)", "level": "N5"},
    {"id": "g_node", "pattern": "Plain + ので", "meaning": "because (objective reason)", "level": "N4"},
    {"id": "g_nagara", "pattern": "V-stem + ながら", "meaning": "while doing ~", "level": "N4"},
    {"id": "g_nitsuite", "pattern": "Noun + について", "meaning": "about ~; concerning ~", "level": "N4"},
    {"id": "g_hazuda", "pattern": "Plain + はずだ", "meaning": "should be ~ (expectation)", "level": "N4"},
    {"id": "g_koto_dekinai", "pattern": "V plain + ことはできない", "meaning": "cannot do ~ (emphatic)", "level": "N4"},
    {"id": "g_kamoshirenai", "pattern": "Plain + かもしれない", "meaning": "might ~; perhaps ~", "level": "N4"},
    {"id": "g_toki", "pattern": "V past + とき", "meaning": "when ~ (at that time)", "level": "N4"},
    {"id": "g_ni_iku", "pattern": "V-stem + に行く", "meaning": "go to do ~", "level": "N4"},
    {"id": "g_to_cond", "pattern": "V plain + と", "meaning": "when/upon doing ~ (natural result)", "level": "N4"},
    {"id": "g_tekureta", "pattern": "V て-form + くれた", "meaning": "did ~ for me (favor)", "level": "N4"},
    {"id": "g_tame", "pattern": "Noun/V plain + ために", "meaning": "for the purpose of ~", "level": "N4"},
    {"id": "g_you_iwareta", "pattern": "V plain + ように言われた", "meaning": "was told to ~", "level": "N4"},
    {"id": "g_teshimatta", "pattern": "V て-form + しまった", "meaning": "ended up ~ing (regret/completion)", "level": "N4"},
    {"id": "g_yori", "pattern": "Noun/V + より", "meaning": "than ~ (comparison)", "level": "N4"},
    {"id": "g_houga_ii", "pattern": "V past + ほうがいい", "meaning": "had better ~; should ~", "level": "N4"},
    {"id": "g_sugiru", "pattern": "V-stem/Adj stem + すぎる", "meaning": "too ~; excessively ~", "level": "N4"},
    {"id": "g_naide", "pattern": "V-ない + でください", "meaning": "please don't ~", "level": "N4"},
    {"id": "g_atode", "pattern": "V past + 後で", "meaning": "after doing ~", "level": "N4"},
    {"id": "g_koto_dekiru", "pattern": "V plain + ことができる", "meaning": "can do ~; be able to ~", "level": "N4"},
    {"id": "g_tara", "pattern": "V past + ら (〜たら)", "meaning": "if/when ~ (conditional)", "level": "N4"},
    {"id": "g_rashii", "pattern": "Plain/Noun + らしい", "meaning": "apparently ~; it seems (hearsay)", "level": "N4"},
    {"id": "g_temiru", "pattern": "V て-form + みる", "meaning": "try doing ~ (to see)", "level": "N4"},
    {"id": "g_kadouka", "pattern": "Plain + かどうか", "meaning": "whether or not ~", "level": "N4"},
    {"id": "g_mitai", "pattern": "Plain/Noun + みたいだ", "meaning": "seems like ~ (informal)", "level": "N4"},
    {"id": "g_souni", "pattern": "Adj stem + そうに", "meaning": "as if ~; looking like ~ (adverb)", "level": "N4"},
    {"id": "g_aidani", "pattern": "V て-form + いる + 間に", "meaning": "while ~ (another event occurs)", "level": "N4"},
    {"id": "g_nakereba", "pattern": "V-ない + なければならない", "meaning": "must ~; have to ~", "level": "N4"},
    {"id": "g_you_ni_shitara", "pattern": "V plain + ようにしたら", "meaning": "when I started making a habit of ~", "level": "N4"},
    {"id": "g_you_ni_natta", "pattern": "V plain + ようになった", "meaning": "came to be able to ~ (change)", "level": "N4"},
    {"id": "g_tekita", "pattern": "V て-form + きた", "meaning": "came toward; started to ~ (change)", "level": "N4"},
    {"id": "g_hajimeta", "pattern": "V-stem + 始めた", "meaning": "started to ~; began to ~", "level": "N4"},
    {"id": "g_deshou", "pattern": "Plain + でしょう", "meaning": "probably ~; right? (agreement seeking)", "level": "N4"},
    {"id": "g_teageru", "pattern": "V て-form + あげる", "meaning": "do ~ for someone (giving favor)", "level": "N4"},
    {"id": "g_ga_contrast", "pattern": "Clause + が + Clause", "meaning": "but; although (contrast)", "level": "N4"},
    {"id": "g_koto_dekita", "pattern": "V plain + ことができた", "meaning": "was able to ~ (past)", "level": "N4"},
    {"id": "g_shi", "pattern": "Plain + し", "meaning": "and also ~; listing reasons", "level": "N4"},
    {"id": "g_teikitai", "pattern": "V て-form + いきたい", "meaning": "want to go on doing ~ (future continuation)", "level": "N4"},
    {"id": "g_passive", "pattern": "V passive (〜られる/〜かれる)", "meaning": "passive voice — be done to", "level": "N4"},
    {"id": "g_nara", "pattern": "Noun/Plain + なら", "meaning": "if it's ~ / since it's you (context conditional)", "level": "N4"},
    {"id": "g_to_omou", "pattern": "Plain + と思いますが", "meaning": "I think that ~, but… (soft statement)", "level": "N4"},
    {"id": "g_tai_no", "pattern": "V-stem + たい + の？", "meaning": "do you want to ~? (casual question)", "level": "N4"},
    {"id": "g_mashouka", "pattern": "V-stem + ましょうか", "meaning": "shall we ~? (suggestion)", "level": "N4"},
    {"id": "g_narou", "pattern": "V volitional + と思っている + んだけど", "meaning": "planning to ~ but… (explaining)", "level": "N4"},
    {"id": "g_hazudesu", "pattern": "Plain + はずです", "meaning": "should be ~ (confident, polite)", "level": "N4"},
    {"id": "g_kara_da", "pattern": "Plain + からだ", "meaning": "it's because ~ (reason as conclusion)", "level": "N4"},
    {"id": "g_made", "pattern": "Noun + まで", "meaning": "until ~; as far as ~", "level": "N4"},
]

# ─────────────────────────────────────────────────────────────────────────────
# N4 Extension — 「翌朝」The Next Morning
# Covers missing N4 patterns: まま、ずに、たばかり、てばかり、ているところ、
# やすい/にくい、によって、ものだ、として、だけでなく、たり〜たり、
# てほしい、させる、させられる、わけだ/わけではない、ようだ、までに、
# + frequently misjudged negative patterns:
#   なくてもいい、ないほうがいい、てはいけない、ないで（二用法）、ないうちに
# ─────────────────────────────────────────────────────────────────────────────

SEGMENTS_N4_EXT = [

    {
        "id": "n4e01",
        "translation": "When he woke up the next morning, the professor's words from the day before were still lingering in his mind.",
        "section": "翌朝 (The Next Morning)",
        "tokens": [
            W("翌朝", "よくあさ", "the next morning", "名詞 (noun)", "N4"),
            T("、"),
            W("目", "め", "eye; consciousness", "名詞 (noun)", "N5"),
            P("が", "subject marker"),
            W("覚めた", "さめた", "woke up; came to (past)", "動詞 (verb)", "N4"),
            G("とき", "とき", "V past + とき", "when ~ / at the time of ~",
              "Past verb before とき = the timing of the main clause comes AFTER that past event.",
              "目が覚めたとき、もう朝だった。", "When I woke up, it was already morning."),
            T("、昨日"),
            P("の", "possessive particle"),
            W("先生", "せんせい", "teacher; professor", "名詞 (noun)", "N5"),
            P("の", "possessive particle"),
            W("言葉", "ことば", "words; language", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("頭", "あたま", "head; mind", "名詞 (noun)", "N5"),
            P("から", "from particle — 'from one's head'"),
            W("離れない", "はなれない", "won't leave; won't go away (negative potential)", "動詞 (verb)", "N4"),
            G("まま", "まま", "V/Adj plain + まま",
              "remaining as is; without change; leaving (a state) as it is",
              "まま describes a state that persists unchanged. "
              "'A のまま B' = 'while still in state A, B happens (or continues)'. "
              "The state expected to change has NOT changed.",
              "靴を履いたまま、部屋に入った。", "I entered the room with my shoes still on."),
            T("だった。"),
        ],
    },

    {
        "id": "n4e02",
        "translation": "Without eating breakfast, he immediately sat down at his desk and started thinking about a new thesis topic.",
        "tokens": [
            W("朝ごはん", "あさごはん", "breakfast", "名詞 (noun)", "N5"),
            P("を", "object particle"),
            W("食べ", "たべ", "eat (stem of 食べる)", "動詞 (verb)", "N5"),
            G("ずに", "ずに", "V-ない stem + ずに",
              "without doing ~ (literary/formal version of ないで)",
              "ずに is the literary/formal equivalent of ないで (without doing). "
              "Formation: replace ない with ず + に. Exception: する → せずに. "
              "Often seen in writing; ないで is more common in speech.",
              "何も言わずに、部屋を出た。", "I left the room without saying anything."),
            T("、すぐに"),
            W("机", "つくえ", "desk", "名詞 (noun)", "N5"),
            P("に", "direction/location particle"),
            W("向かい", "むかい", "faced; turned toward (連用形)", "動詞 (verb)", "N4"),
            T("、"),
            W("新しい", "あたらしい", "new", "い形容詞 (i-adjective)", "N5"),
            T("テーマ"),
            P("を", "object particle"),
            W("考え", "かんがえ", "think about; consider (stem)", "動詞 (verb)", "N4"),
            G("始めた", "はじめた", "V-stem + 始めた", "started to ~; began to ~",
              "始める as an auxiliary attaches to the verb stem. Marks the inception of an action.",
              "雨が降り始めた。", "It started to rain."),
            T("。"),
        ],
    },

    {
        "id": "n4e03",
        "translation": "\"I only just decided on a thesis topic, and now I have to change it already\" — he let out a sigh.",
        "tokens": [
            T("「論文のテーマを"),
            W("考え", "かんがえ", "think; consider (stem)", "動詞 (verb)", "N4"),
            G("たばかり", "たばかり", "V past (た-form) + ばかり",
              "just did ~; only just ~",
              "たばかり expresses that an action was completed very recently. "
              "Implies the action is fresh, with a sense of 'and now already something else must happen'. "
              "Contrast with たところだ (more neutral 'just finished').",
              "日本に来たばかりで、まだ慣れていない。", "I just came to Japan and am not used to it yet."),
            T("なのに、また"),
            W("変え", "かえ", "change (stem of 変える)", "動詞 (verb)", "N4"),
            G("なければならない", "なければならない",
              "V-ない + なければならない", "must ~; have to ~ (obligation)",
              "Expresses obligation. Casual: なきゃ.",
              "宿題をしなければならない。", "I have to do my homework."),
            T("とは」と、"),
            W("ため息", "ためいき", "sigh", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            T("ついた。"),
        ],
    },

    {
        "id": "n4e04",
        "translation": "When he went to the library in the afternoon, his junior Tanaka was doing nothing but playing games on his phone.",
        "tokens": [
            W("午後", "ごご", "afternoon; p.m.", "名詞 (noun)", "N5"),
            T("、"),
            W("図書館", "としょかん", "library", "名詞 (noun)", "N4"),
            P("に", "direction particle"),
            W("行く", "いく", "go", "動詞 (verb)", "N5"),
            G("と", "と", "V plain + と", "upon doing ~ (discovery)",
              "Natural/automatic result. Upon arriving, the speaker found this situation.",
              "ドアを開けると、猫がいた。", "When I opened the door, there was a cat."),
            T("、"),
            W("後輩", "こうはい", "junior (at school/work)", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            N("田中くん", "たなかくん", "Tanaka (junior student)"),
            P("が", "subject marker"),
            T("スマホでゲームを"),
            G("してばかりいた", "してばかりいた",
              "V て-form + ばかりいる",
              "do nothing but ~; keep doing ~ (exclusively)",
              "ばかりいる after て-form expresses that one does ONLY that action, often with a negative nuance. "
              "Implies neglecting other things. Past: ばかりいた.",
              "彼は文句を言ってばかりいる。", "He does nothing but complain."),
            T("。"),
        ],
    },

    {
        "id": "n4e05",
        "translation": "When he called out, \"What are you doing right now?\" Tanaka was startled and turned red.",
        "tokens": [
            T("「今、何を"),
            G("しているところ", "しているところ",
              "V て-form + いる + ところだ",
              "in the middle of doing ~ (right now)",
              "ところだ has three key uses depending on verb form: "
              "① V dictionary + ところだ = about to do. "
              "② V て-form + いる + ところだ = in the middle of doing (now). "
              "③ V past + ところだ = just finished doing.",
              "今、ちょうど出かけるところだ。", "I'm just about to go out."),
            T("？」"),
            P("と", "quotation particle"),
            W("声をかける", "こえをかける", "to call out to; to speak to", "動詞 (verb)", "N4"),
            G("と", "と", "V plain + と", "upon doing ~ (discovery/result)",
              "Automatic result: upon calling out, this happened.",
              "声をかけると、振り向いた。", "When I called out, he turned around."),
            T("、"),
            N("田中くん", "たなかくん", "Tanaka (junior)"),
            P("は", "topic marker"),
            W("驚いて", "おどろいて", "surprised; startled (て-form)", "動詞 (verb)", "N4"),
            W("顔", "かお", "face", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("赤くした", "あかくした", "turned red; blushed (past)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "n4e06",
        "translation": "The topic Tanaka had brought was easy to read, but it was something difficult to write as a thesis.",
        "tokens": [
            N("田中くん", "たなかくん", "Tanaka"),
            P("が", "subject marker"),
            W("持ってきた", "もってきた", "brought; carried here (past)", "動詞 (verb)", "N4"),
            T("テーマ"),
            P("は", "topic marker"),
            W("読み", "よみ", "read (stem)", "動詞 (verb)", "N5"),
            G("やすい", "やすい", "V-stem + やすい",
              "easy to ~; ~able (ease of action)",
              "やすい attaches to the verb stem. Describes that an action is easy to perform on the object. "
              "It is an i-adjective: conjugates as やすい、やすくない、やすかった. "
              "Opposite: にくい (hard to do).",
              "この本は読みやすい。", "This book is easy to read."),
            T("が、論文として"),
            W("書き", "かき", "write (stem)", "動詞 (verb)", "N5"),
            G("にくい", "にくい", "V-stem + にくい",
              "hard to ~; difficult to ~ (difficulty of action)",
              "にくい attaches to the verb stem. Describes that an action is difficult to perform. "
              "It is an i-adjective. Opposite: やすい.",
              "この漢字は書きにくい。", "This kanji is hard to write."),
            T("ものだった。"),
        ],
    },

    {
        "id": "n4e07",
        "translation": "Professor Yamada often used to say, \"It's only natural that the right topic varies from person to person.\"",
        "tokens": [
            T("「人"),
            G("によって", "によって", "Noun + によって",
              "by ~; depending on ~; due to ~",
              "によって has three main meanings: "
              "① Cause/agent (passive): 〜によって作られた (made by). "
              "② Means/method: メールによって連絡する (contact by email). "
              "③ Depending on: 人によって違う (varies depending on the person).",
              "国によって、文化は違う。", "Culture differs depending on the country."),
            W("向いている", "むいている", "suited for; fit for (progressive)", "動詞 (verb)", "N4"),
            T("テーマは違う"),
            G("ものだ", "ものだ", "Plain form + ものだ",
              "it is natural that ~; that's just how it is; used to ~",
              "ものだ has two main uses: "
              "① Natural/universal truth: 子供は遊ぶものだ (Children naturally play). "
              "② Used to (past habit): よく食べたものだ (I used to eat a lot). "
              "Expresses a general truth, shared understanding, or nostalgic past.",
              "人は誰でも失敗するものだ。", "It's natural for everyone to make mistakes."),
            T("」と、"),
            N("山田先生", "やまだせんせい", "Professor Yamada"),
            P("が", "subject marker"),
            T("よく言っていた。"),
        ],
    },

    {
        "id": "n4e08",
        "translation": "To work as a translator, he felt anew that not only language skills but also cultural knowledge is essential.",
        "tokens": [
            W("翻訳家", "ほんやくか", "translator", "名詞 (noun)", "N4"),
            G("として", "として", "Noun + として",
              "as ~; in the role/capacity of ~",
              "として marks the role, capacity, or standard by which something is judged. "
              "'N として' = 'as N / in the capacity of N'. "
              "Can also mean 'as a rule/standard': 原則として (as a rule).",
              "学生として、責任を持つべきだ。", "As a student, you should be responsible."),
            W("働く", "はたらく", "to work", "動詞 (verb)", "N4"),
            T("には、語学力"),
            G("だけでなく", "だけでなく", "Noun/plain form + だけでなく",
              "not only ~ but also ~",
              "だけでなく expresses that something goes beyond just one thing. "
              "Often followed by も or まで. Formal version: のみならず. "
              "Pattern: A だけでなく、B も = not only A but also B.",
              "彼は英語だけでなく、中国語も話せる。", "He can speak not only English but also Chinese."),
            T("、"),
            W("文化的", "ぶんかてき", "cultural", "な形容詞 (na-adjective)", "N4"),
            P("な", "な connecting adjective to noun"),
            W("知識", "ちしき", "knowledge", "名詞 (noun)", "N4"),
            T("も"),
            W("大切", "たいせつ", "important; precious", "な形容詞 (na-adjective)", "N4"),
            T("だと"),
            W("改めて", "あらためて", "once again; anew", "副詞 (adverb)", "N4"),
            W("感じた", "かんじた", "felt; sensed (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n4e09",
        "translation": "He advised, \"Try doing things like reading books and watching movies to expose yourself to different cultures.\"",
        "tokens": [
            T("「"),
            W("本", "ほん", "book", "名詞 (noun)", "N5"),
            P("を", "object particle"),
            W("読ん", "よん", "read (連用形 of 読む)", "動詞 (verb)", "N5"),
            G("だり", "だり", "V past (た-form) + り ... V past + り + する",
              "do things like ~ and ~ (non-exhaustive listing of actions)",
              "たり〜たりする: lists two or more representative actions. "
              "Implies 'among other things'. Both verbs take た-form + り. "
              "The final する (or した) closes the pattern.",
              "休みの日は、本を読んだり、映画を見たりする。",
              "On days off, I do things like read books and watch movies."),
            T("、"),
            W("映画", "えいが", "movie; film", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("見た", "みた", "watched (past)", "動詞 (verb)", "N5"),
            T("り"),
            T("して、いろんな"),
            W("文化", "ぶんか", "culture", "名詞 (noun)", "N4"),
            P("に", "contact particle"),
            W("触れてみる", "ふれてみる", "try touching/experiencing", "動詞 (verb)", "N4"),
            T("といいよ」"),
            P("と", "quotation particle"),
            W("アドバイスした", "あどばいすした", "gave advice (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n4e10",
        "translation": "Thinking to himself, \"I wish you had come to talk to me sooner,\" he listened to Tanaka carefully and attentively.",
        "tokens": [
            T("「もっと"),
            W("早く", "はやく", "early; sooner (adverb)", "副詞 (adverb)", "N5"),
            W("相談して", "そうだんして", "consult (て-form)", "動詞 (verb)", "N4"),
            G("ほしかった", "ほしかった", "V て-form + ほしい (past)",
              "wanted someone to do ~ (past)",
              "てほしい = want someone else to do something for you. "
              "Subject of desire is the speaker; doer is marked with に. "
              "Past: てほしかった = wanted them to have done. "
              "Negative: てほしくない = don't want someone to do.",
              "もっと早く教えてほしかった。", "I wanted you to have told me sooner."),
            P("と", "quotation particle"),
            W("思い", "おもい", "thought (連用形)", "動詞 (verb)", "N5"),
            G("ながら", "ながら", "V-stem + ながら", "while doing ~",
              "Simultaneous actions sharing the same subject.",
              "音楽を聴きながら走った。", "I ran while listening to music."),
            T("、"),
            W("丁寧に", "ていねいに", "politely; carefully (adverb)", "副詞 (adverb)", "N4"),
            W("話を聞いて", "はなしをきいて", "listened (て-form)", "動詞 (verb)", "N5"),
            G("あげた", "あげた", "V て-form + あげた", "did ~ for (him/her) — favor given",
              "てあげる = do something as a favor for another person. Direction: speaker → other.",
              "友達の荷物を持ってあげた。", "I carried my friend's luggage for them."),
            T("。"),
        ],
    },

    {
        "id": "n4e11",
        "translation": "Last week, Professor Yamada had made Kenji read an entire thick specialized textbook.",
        "tokens": [
            W("先週", "せんしゅう", "last week", "名詞 (noun)", "N4"),
            T("、"),
            N("山田先生", "やまだせんせい", "Professor Yamada"),
            P("は", "topic marker"),
            N("健二", "けんじ", "Kenji"),
            P("に", "target particle (causative)"),
            T("、分厚い"),
            W("専門書", "せんもんしょ", "specialized text; technical book", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("全部", "ぜんぶ", "all; entirely", "副詞 (adverb)", "N4"),
            W("読ま", "よま", "read (causative stem of 読む)", "動詞 (verb)", "N5"),
            G("せた", "せた", "V-causative + た",
              "made (someone) do ~ / let (someone) do ~ (causative, past)",
              "Causative form: う-verbs → V-あ + せる; る-verbs → V-stem + させる. "
              "With に particle = permission (let). With を particle = compulsion (make). "
              "Past tense here: させた → せた (for う-verbs).",
              "母は私に野菜を食べさせた。", "My mother made me eat vegetables."),
            T("。"),
        ],
    },

    {
        "id": "n4e12",
        "translation": "The content was so difficult that he was made to read the same page over and over, but little by little he had gradually come to understand it.",
        "tokens": [
            W("内容", "ないよう", "content; substance", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("難しすぎて", "むずかしすぎて", "too difficult (て-form of すぎる)", "動詞 (verb)", "N4"),
            T("、同じページを"),
            W("何度も", "なんども", "many times; over and over", "副詞 (adverb)", "N4"),
            W("読ま", "よま", "read (causative-passive stem)", "動詞 (verb)", "N5"),
            G("された", "された", "V-causative-passive + た",
              "was made to do ~ (causative-passive, past)",
              "Causative-passive = the speaker was MADE to do something (by someone else, often against their will). "
              "Formation: causative form + passive られる. "
              "う-verb example: 読む → 読ませる → 読まされる. "
              "る-verb example: 食べる → 食べさせる → 食べさせられる. "
              "Nuance: reluctance or inconvenience is implied.",
              "上司に残業させられた。", "I was made to work overtime by my boss."),
            T("が、"),
            W("少しずつ", "すこしずつ", "little by little; gradually", "副詞 (adverb)", "N4"),
            W("理解できる", "りかいできる", "can understand (potential)", "動詞 (verb)", "N4"),
            G("ようになってきた", "ようになってきた",
              "V plain + ようになった + てきた",
              "have gradually come to be able to ~ (change coming toward now)",
              "Combines ようになる (gradual change in ability) + てくる (direction toward present). "
              "Together: change that has been accumulating and has now arrived at the present.",
              "最近、日本語が聞き取れるようになってきた。",
              "Recently I've gradually come to be able to understand spoken Japanese."),
            T("。"),
        ],
    },

    {
        "id": "n4e13",
        "translation": "The new topic looked like it would be easier to tackle than the previous one.",
        "tokens": [
            W("新しい", "あたらしい", "new", "い形容詞 (i-adjective)", "N5"),
            T("テーマ"),
            P("は", "topic marker"),
            T("、前のものより"),
            W("取り組み", "とりくみ", "tackle; work on (連用形 of 取り組む)", "動詞 (verb)", "N4"),
            G("やすそうだ", "やすそうだ",
              "V-stem/Adj stem + そうだ (appearance)",
              "looks like it will be easy to ~ (appearance-based guess)",
              "そうだ (appearance) — NOT hearsay. Based on direct observation. "
              "Attaches to: verb stem (行きそうだ = looks like he'll go), adj stem (高そうだ = looks expensive). "
              "Different from 〜らしい (hearsay).",
              "雨が降りそうだ。", "It looks like it's going to rain."),
            T("。"),
        ],
    },

    {
        "id": "n4e14",
        "translation": "Since he had to submit the outline by next week, he decided to start writing that very night.",
        "tokens": [
            W("概要", "がいよう", "summary; outline", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("来週", "らいしゅう", "next week", "名詞 (noun)", "N4"),
            G("までに", "までに", "Noun + までに",
              "by ~; by the time of ~ (deadline)",
              "までに marks a deadline: the action must be completed BY that point. "
              "Contrast with まで (until): まで = continuously until; までに = finished by.",
              "金曜日までに提出してください。", "Please submit it by Friday."),
            W("提出しなければならない", "ていしゅつしなければならない",
              "must submit (obligation)", "動詞 (verb)", "N4"),
            G("ので", "ので", "Plain form + ので", "because (objective reason)",
              "Gives an objective reason. Polite and matter-of-fact.",
              "熱があるので、休みます。", "Because I have a fever, I'll rest."),
            T("、今夜から"),
            W("書き始める", "かきはじめる", "start writing", "動詞 (verb)", "N4"),
            G("ことにした", "ことにした",
              "V plain + ことにする (past)",
              "decided to ~ (speaker makes a deliberate decision)",
              "ことにする = decide to do (speaker's active choice). "
              "Past: ことにした = decided. "
              "Compare: ことになる = it has been decided (by circumstances, not speaker's choice).",
              "毎朝走ることにした。", "I decided to run every morning."),
            T("。"),
        ],
    },

    {
        "id": "n4e15",
        "translation": "Translation doesn't simply mean substituting one word for another — it means conveying an entire culture.",
        "tokens": [
            W("翻訳", "ほんやく", "translation", "名詞 (noun)", "N4"),
            P("とは", "とは — topic marker emphasizing definition: 'as for what ~ is'"),
            T("、単に"),
            W("言葉", "ことば", "words; language", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("置き換える", "おきかえる", "to replace; to substitute", "動詞 (verb)", "N4"),
            G("わけではない", "わけではない",
              "Plain form + わけではない",
              "it doesn't mean that ~; it's not the case that ~",
              "わけ is a noun meaning 'reason/case'. わけではない = 'it is not the case that'. "
              "Used to DENY an overgeneralization. Often follows a statement that could be misunderstood. "
              "Contrast: わけだ = that explains it / that's why.",
              "嫌いなわけではないが、得意じゃない。",
              "It's not that I dislike it, I'm just not good at it."),
            T("。"),
            W("文化", "ぶんか", "culture", "名詞 (noun)", "N4"),
            W("全体", "ぜんたい", "entirety; the whole", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("伝える", "つたえる", "to convey; to communicate", "動詞 (verb)", "N4"),
            T("ことだ。"),
        ],
    },

    {
        "id": "n4e16",
        "translation": "That is precisely why translation is difficult — and at the same time deeply rewarding.",
        "tokens": [
            T("だからこそ、翻訳は"),
            W("難しく", "むずかしく", "difficult (adverb form)", "副詞", "N5"),
            T("、同時に"),
            W("やりがい", "やりがい", "sense of achievement; rewarding feeling", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            T("ある"),
            G("わけだ", "わけだ",
              "Plain form + わけだ",
              "that's why ~; so that means ~; no wonder ~",
              "わけだ = the situation logically follows from what was said. "
              "Used when something is explained or when a logical conclusion is reached. "
              "Often translates as 'that explains it', 'so that's why', 'no wonder'.",
              "彼は毎日練習していた。だから上手なわけだ。",
              "He was practicing every day. That explains why he's good."),
            T("。"),
        ],
    },

    {
        "id": "n4e17",
        "translation": "The sky visible through the library window in the evening looked just like a vast painting.",
        "tokens": [
            W("夕方", "ゆうがた", "evening; dusk", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("図書館", "としょかん", "library", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("窓", "まど", "window", "名詞 (noun)", "N5"),
            P("から", "from particle"),
            W("見える", "みえる", "can be seen; visible", "動詞 (verb)", "N5"),
            W("空", "そら", "sky", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            T("、まるで"),
            W("大きな", "おおきな", "large; big (attributive form)", "連体詞", "N5"),
            W("絵", "え", "painting; picture", "名詞 (noun)", "N5"),
            P("の", "possessive particle"),
            G("ようだった", "ようだった",
              "Plain form / Noun + ようだ (past)",
              "seemed like ~; appeared to be ~ (formal/literary observation)",
              "ようだ is based on the speaker's direct observation, more formal than みたいだ. "
              "Used in writing and formal speech. Past: ようだった. "
              "Compare: みたいだ (same meaning, informal/spoken). "
              "N/Na + の + ようだ; V/i-adj + ようだ.",
              "まるで夢のようだった。", "It was as if it were a dream."),
            T("。"),
        ],
    },

    # ── 言われた vs 言った — same event, opposite perspectives ──────────────────

    {
        "id": "n4e_said_a",
        "translation": "[Side A — receiver's perspective] The next morning, Kenji remembered: he had been told by Maria, 'There's apparently a new restaurant near the station.'",
        "section": "言われた vs 言った：視点の違い (Passive vs Active Speech — Same Event, Two Perspectives)",
        "tokens": [
            T("翌朝、「駅の近くに新しいレストランができた"),
            G("らしい",
              "らしい",
              "Plain form + らしい",
              "apparently ~; it seems (hearsay)",
              "Information received from others or inferred — not the speaker's direct observation.",
              "彼は来ないらしい。", "Apparently he's not coming."),
            T("よ」"),
            P("と", "quotation particle — marks the quoted content"),
            N("マリアさん", "まりあさん", "Maria"),
            P("に", "に marks the agent in passive constructions: 'by Maria'"),
            G("言われた",
              "いわれた",
              "V passive — 言う → 言われた",
              "was told [something] by [someone] — receiver's perspective",
              "The subject is the RECEIVER of the speech, never the speaker. "
              "に + person marks who said it: マリアさんに言われた = 'was told by Maria.' "
              "Kenji is the implied subject here — he received Maria's words. "
              "Compare the next sentence (言った) where Maria is the active subject saying the same thing.",
              "友達に「頑張れ」と言われた。",
              "I was told 'do your best' by a friend."),
            T("ことを"),
            N("健二", "けんじ", "Kenji — male given name"),
            P("は", "topic marker"),
            W("思い出した", "おもいだした", "recalled; remembered (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n4e_said_b",
        "translation": "[Side B — speaker's perspective] The same event retold: Maria said, 'There's apparently a new restaurant near the station.'",
        "tokens": [
            T("（同じ出来事、マリアさんの視点から）"),
            N("マリアさん", "まりあさん", "Maria — now the active subject"),
            P("は", "topic marker"),
            T("「駅の近くに新しいレストランができた"),
            G("らしい",
              "らしい",
              "Plain form + らしい",
              "apparently ~; it seems (hearsay)",
              "Information received from others, not direct observation.",
              "彼は来ないらしい。", "Apparently he's not coming."),
            T("よ」"),
            P("と", "quotation particle"),
            G("言った",
              "いった",
              "言う → 言った (active past)",
              "said ~; told ~ — speaker's perspective (active)",
              "言った is the active past of 言う. The subject IS the speaker. "
              "Compare the previous sentence: 「...」とマリアさんに言われた (Kenji was told BY Maria). "
              "SAME EVENT — but 言われた puts Kenji as subject/receiver; 言った puts Maria as subject/speaker. "
              "Rule: you cannot swap them — use 言われた only when the subject received the words; "
              "use 言った only when the subject spoke the words. "
              "If Maria asked Kenji a question: 「...」とマリアさんに聞かれた (Kenji was asked by Maria) "
              "vs 「...」とマリアさんが聞いた (Maria asked).",
              "彼女は小さな声で「ありがとう」と言った。",
              "She said 'thank you' in a quiet voice."),
            T("。"),
        ],
    },

    # ── Frequently misjudged negative patterns ───────────────────────────────

    {
        "id": "n4e18",
        "translation": "Kenji felt a little relieved when the professor told him, 'You don't have to submit the report today.'",
        "section": "よくある間違い：否定の文型 (Frequently Misjudged Negative Patterns)",
        "tokens": [
            T("「今日は"),
            W("報告書", "ほうこくしょ", "written report", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("出さ", "ださ", "submit; hand in (negative stem)", "動詞 (verb)", "N4"),
            G("なくてもいい",
              "なくてもいい",
              "V-ない form (drop い) + くてもいい",
              "don't have to ~; it's okay not to ~ (no obligation)",
              "Formation: V-ない → drop final い → add くてもいい. E.g. 出さない → 出さなくてもいい. "
              "COMMON MISTAKE: learners parse this as 'negative + even if = not good,' but it actually grants "
              "PERMISSION NOT TO ACT — the structural opposite of なければならない. "
              "来なければならない = must come. 来なくてもいい = don't have to come. "
              "The double-negative logic: 'it's fine (いい) even if you don't (なくても).'",
              "明日は早く起きなくてもいいよ。",
              "You don't have to get up early tomorrow."),
            T("ですよ」"),
            P("と", "quotation particle"),
            W("先生", "せんせい", "professor", "名詞 (noun)", "N5"),
            P("に", "by (passive agent) particle"),
            W("言われ", "いわれ", "was told (passive, て-form)", "動詞 (verb)", "N4"),
            T("て、"),
            N("健二", "けんじ", "Kenji — male given name"),
            P("は", "topic marker"),
            T("少し"),
            W("安心した", "あんしんした", "felt relieved; felt at ease (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n4e19",
        "translation": "He had heard from the professor that the day before an exam, it's better not to study until late at night.",
        "tokens": [
            W("試験", "しけん", "exam; test", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("前の日", "まえのひ", "the day before; eve of", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            T("、"),
            W("夜", "よる", "night; evening", "名詞 (noun)", "N5"),
            W("遅く", "おそく", "late (adverb form)", "副詞", "N4"),
            T("まで"),
            W("勉強し", "べんきょうし", "study (verb stem)", "動詞 (verb)", "N5"),
            G("ないほうがいい",
              "ないほうがいい",
              "V-ない form + ほうがいい",
              "had better not ~; it's better not to ~ (negative advice)",
              "Formation: V-ない + ほうがいい. "
              "COMMON MISTAKE: confusing with positive ほうがいい ('should do'). "
              "The ない completely reverses the advice direction: "
              "もっと寝たほうがいい = you should sleep more (do it). "
              "夜更かしをしないほうがいい = you'd better not stay up late (don't do it). "
              "Note: positive advice uses V-past + ほうがいい; negative uses V-ない + ほうがいい (not negative past).",
              "風邪のときは無理をしないほうがいい。",
              "When you have a cold, you'd better not push yourself."),
            P("と", "quotation/reported content particle"),
            W("先生", "せんせい", "professor", "名詞 (noun)", "N5"),
            P("から", "from particle — source of information"),
            W("聞いていた", "きいていた", "had heard; had been told (past progressive)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "n4e20",
        "translation": "No matter how busy he might be, he must not forget the deadline.",
        "tokens": [
            T("どんなに"),
            W("忙しく", "いそがしく", "busy (adverb form)", "形容詞 (i-adj)", "N4"),
            G("ても",
              "ても",
              "V て-form / i-adj + くても",
              "even if ~; no matter how ~ (concession)",
              "Expresses concession: 'even under this condition, the following holds.' "
              "Pairs with どんなに/何が/誰が for universal scope: どんなに忙しくても = no matter how busy.",
              "どんなに疲れても、諦めない。",
              "No matter how tired I am, I won't give up."),
            T("、"),
            W("締め切り", "しめきり", "deadline", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("忘れ", "わすれ", "forget (て-form stem)", "動詞 (verb)", "N5"),
            G("てはいけない",
              "てはいけない",
              "V て-form + はいけない",
              "must not ~; cannot ~ (prohibition)",
              "Formation: V て-form + はいけない. Casual: てはだめ / ちゃだめ. Formal/written: てはならない. "
              "COMMON MISTAKE: confusing direction with なければならない. "
              "なければならない = MUST DO (obligation to perform the action). "
              "てはいけない = MUST NOT DO (prohibition against performing the action). "
              "They are structural opposites despite both expressing strong obligation. "
              "Mnemonic: てはいけない = 'even if you do it, it won't do' → you're forbidden to do it.",
              "授業中に携帯を使ってはいけない。",
              "You must not use your phone during class."),
            T("。"),
        ],
    },

    {
        "id": "n4e21",
        "translation": "Kenji headed to university in a hurry without eating breakfast.",
        "tokens": [
            N("健二", "けんじ", "Kenji — male given name"),
            P("は", "topic marker"),
            W("朝ごはん", "あさごはん", "breakfast", "名詞 (noun)", "N5"),
            P("を", "object particle"),
            W("食べ", "たべ", "eat (negative stem)", "動詞 (verb)", "N5"),
            G("ないで",
              "ないで",
              "V-ない form + で (two distinct uses)",
              "① without doing ~  ② don't ~ (soft negative request)",
              "COMMON MISTAKE: ないで has two uses that learners mix up. "
              "① Before a main verb — 'without doing': 食べないで行く = go without eating. "
              "   Same meaning as literary ずに, but more natural in everyday speech. "
              "② At sentence end alone — soft negative request/plea: 行かないで = don't go / please don't go. "
              "   More emotional than 行かないでください; often implies the speaker is affected. "
              "Disambiguation: ないで + [another verb] → meaning ①; ないで at sentence end → meaning ②.",
              "傘を持たないで外に出た。",
              "I went outside without taking an umbrella."),
            T("、"),
            W("急いで", "いそいで", "hurriedly; in a rush", "副詞", "N4"),
            W("大学", "だいがく", "university", "名詞 (noun)", "N5"),
            P("に", "direction particle"),
            W("向かった", "むかった", "headed toward; set off for (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n4e22",
        "translation": "Before he forgot, he saved Maria's contact information on his smartphone.",
        "tokens": [
            N("マリアさん", "まりあさん", "Maria"),
            P("の", "possessive particle"),
            W("連絡先", "れんらくさき", "contact information", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("忘れ", "わすれ", "forget (negative stem)", "動詞 (verb)", "N5"),
            G("ないうちに",
              "ないうちに",
              "V-ない form + うちに",
              "before ~ happens; while it's still not ~ (act before the window closes)",
              "Formation: V-ない + うちに. "
              "COMMON MISTAKE: translating literally as 'while not doing ~' — this is wrong. "
              "ないうちに means 'before [a negative state begins]': act during the window that currently exists. "
              "忘れないうちに = 'before I forget' (while I still remember, before forgetting starts). "
              "The logic: ない describes a state that is currently true; うちに = while that state holds. "
              "So act NOW, before the ない state ends (i.e., before you DO forget). "
              "Compare positive うちに: 若いうちに (while young, before you're no longer young). "
              "More examples: 暗くならないうちに帰ろう = let's get home before it gets dark.",
              "冷めないうちに食べてください。",
              "Please eat it before it gets cold (while it's still hot)."),
            T("、"),
            W("スマートフォン", "すまーとふぉん", "smartphone", "名詞 (noun)", "N4"),
            P("に", "target/location particle"),
            W("保存した", "ほぞんした", "saved; stored (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },
]

# N4 extra grammar index entries
N4_EXT_GRAMMAR = [
    {"id": "g_mama",   "pattern": "V/Adj + まま",               "meaning": "remaining as is; without change",          "level": "N4"},
    {"id": "g_zuni",   "pattern": "V-ない stem + ずに",          "meaning": "without doing ~ (literary)",               "level": "N4"},
    {"id": "g_bakari", "pattern": "V past + たばかり",           "meaning": "just did ~ (very recently)",               "level": "N4"},
    {"id": "g_bakariiru", "pattern": "V て-form + ばかりいる",   "meaning": "do nothing but ~",                         "level": "N4"},
    {"id": "g_tokoro", "pattern": "V て-form + いる + ところだ", "meaning": "in the middle of doing ~",                 "level": "N4"},
    {"id": "g_yasui",  "pattern": "V-stem + やすい",             "meaning": "easy to ~",                               "level": "N4"},
    {"id": "g_nikui",  "pattern": "V-stem + にくい",             "meaning": "hard to ~; difficult to ~",               "level": "N4"},
    {"id": "g_niyotte","pattern": "Noun + によって",             "meaning": "by ~; depending on ~; due to ~",           "level": "N4"},
    {"id": "g_monoda", "pattern": "Plain form + ものだ",         "meaning": "it is natural that ~; that's how it is",   "level": "N4"},
    {"id": "g_toshite","pattern": "Noun + として",               "meaning": "as ~; in the role/capacity of ~",          "level": "N4"},
    {"id": "g_dakedena","pattern": "Noun/plain + だけでなく",    "meaning": "not only ~ but also ~",                    "level": "N4"},
    {"id": "g_tari",   "pattern": "V た-form + り ~ V た-form + り + する", "meaning": "do things like ~ and ~",        "level": "N4"},
    {"id": "g_tehoshii","pattern": "V て-form + ほしい",        "meaning": "want someone to do ~",                     "level": "N4"},
    {"id": "g_saseru", "pattern": "V-causative form + せる/させる", "meaning": "make/let someone do ~",                "level": "N4"},
    {"id": "g_saserareru", "pattern": "V-causative-passive",    "meaning": "be made to do ~ (against one's will)",     "level": "N4"},
    {"id": "g_souda_app","pattern": "V-stem/Adj stem + そうだ",  "meaning": "looks like ~; appears to ~ (appearance)",  "level": "N4"},
    {"id": "g_madeni", "pattern": "Noun + までに",               "meaning": "by ~ (deadline)",                          "level": "N4"},
    {"id": "g_wakeja", "pattern": "Plain form + わけではない",    "meaning": "it doesn't mean that ~",                   "level": "N4"},
    {"id": "g_wakeda", "pattern": "Plain form + わけだ",          "meaning": "that's why ~; no wonder ~",               "level": "N4"},
    {"id": "g_youda",  "pattern": "Plain/Noun + ようだ",         "meaning": "seems like ~; appears to ~ (formal)",      "level": "N4"},
    {"id": "g_kotonikita","pattern": "V plain + ことにする",      "meaning": "decide to do ~",                          "level": "N4"},
    # Active vs passive speech reporting
    {"id": "g_iwareta", "pattern": "V passive — 言われた",              "meaning": "was told ~ (receiver's perspective)",          "level": "N4"},
    {"id": "g_itta",    "pattern": "言った (active past)",               "meaning": "said ~ (speaker's perspective)",               "level": "N4"},
    # Frequently misjudged negative patterns
    {"id": "g_nakutemoii",  "pattern": "V-ない (drop い) + くてもいい",  "meaning": "don't have to ~ (permission not to act)",    "level": "N4"},
    {"id": "g_naihougaii",  "pattern": "V-ない + ほうがいい",            "meaning": "had better not ~; it's better not to ~",     "level": "N4"},
    {"id": "g_tehaikenai",  "pattern": "V て-form + はいけない",          "meaning": "must not ~ (prohibition — opposite of must)", "level": "N4"},
    {"id": "g_naide_two",   "pattern": "V-ない + で (two uses)",          "meaning": "without doing ~ / don't ~ (soft plea)",      "level": "N4"},
    {"id": "g_naiuchini",   "pattern": "V-ない + うちに",                 "meaning": "before ~ happens; while still not ~",        "level": "N4"},
]

# ─────────────────────────────────────────────────────────────────────────────
# N3 Passage — 「翻訳の夢、現実へ」The Translation Dream, Into Reality
# Story: One year later. Kenji, now a final-year student, lands an internship
# at a translation company in Tokyo and begins to turn his dream into reality.
# ~50 segments covering ALL major N3 grammar patterns.
# ─────────────────────────────────────────────────────────────────────────────

N3_SEGMENTS = [

    # ── 第一章: 就職活動 (Chapter 1: Job Hunting) ─────────────────────────────

    {
        "id": "n3_s01",
        "translation": "Around the time Kenji became a fourth-year university student, his job search began in earnest.",
        "section": "第一章: 就職活動 (Chapter 1: Job Hunting)",
        "tokens": [
            N("健二", "けんじ", "Kenji"),
            P("が", "subject marker"),
            W("大学", "だいがく", "university", "名詞 (noun)", "N5"),
            W("四年生", "よねんせい", "fourth-year student", "名詞 (noun)", "N4"),
            P("に", "goal/state particle"),
            W("なった", "なった", "became (past)", "動詞 (verb)", "N5"),
            W("頃", "ころ", "around the time of; about", "名詞 (noun)", "N4"),
            T("、"),
            W("就職活動", "しゅうしょくかつどう", "job hunting; career activities", "名詞 (noun)", "N4",
              "Commonly abbreviated as 就活 (しゅうかつ)"),
            P("が", "subject marker"),
            W("本格的に", "ほんかくてきに", "in earnest; seriously", "副詞 (adverb)", "N4"),
            W("始まった", "はじまった", "began; started (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s02",
        "translation": "According to a senior, it seems that interviews at translation companies often include a practical skills test.",
        "tokens": [
            W("先輩", "せんぱい", "senior; upperclassman", "名詞 (noun)", "N4"),
            G("によると", "によると", "Noun + によると",
              "according to ~",
              "によると introduces information the speaker received from a source. "
              "Always followed by 〜そうだ、〜らしい、〜とのことだ, or similar hearsay expressions. "
              "によれば is a slightly more formal variant.",
              "天気予報によると、明日は雨らしい。",
              "According to the weather forecast, it will apparently rain tomorrow."),
            T("、翻訳会社の面接では"),
            W("実力", "じつりょく", "real ability; actual skill", "名詞 (noun)", "N4"),
            T("テストが"),
            W("行われる", "おこなわれる", "is carried out; takes place (passive)", "動詞 (verb)", "N4"),
            T("ことが多い"),
            G("らしい", "らしい", "Plain/Noun + らしい",
              "apparently ~ (hearsay); also: typical of ~",
              "らしい follows reported information. Used in combination with によると.",
              "彼は合格したらしい。", "Apparently he passed."),
            T("。"),
        ],
    },

    {
        "id": "n3_s03",
        "translation": "Despite his continued efforts, the first two companies rejected him.",
        "tokens": [
            W("努力", "どりょく", "effort; hard work", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("続けた", "つづけた", "continued (past)", "動詞 (verb)", "N4"),
            G("にもかかわらず", "にもかかわらず",
              "N / plain form + にもかかわらず",
              "despite ~; in spite of ~; even though ~",
              "A formal expression of contrast — the expected result did NOT occur. "
              "Similar to のに (despite) but more formal and emphatic. "
              "Often appears in written Japanese or formal speech.",
              "雨にもかかわらず、試合は続けられた。",
              "Despite the rain, the match continued."),
            T("、最初の二社は"),
            W("不合格", "ふごうかく", "failure; rejection", "名詞 (noun)", "N4"),
            T("だった。"),
        ],
    },

    {
        "id": "n3_s04",
        "translation": "For Kenji, translation was not merely a job — it was his very way of life.",
        "tokens": [
            N("健二", "けんじ", "Kenji"),
            G("にとって", "にとって", "Noun + にとって",
              "for ~; from the perspective of ~; as far as ~ is concerned",
              "にとって marks the person from whose viewpoint or for whose benefit/detriment something is considered. "
              "Cannot be used with actions — use に for actions, にとって for evaluations/states.",
              "子供にとって、遊びは大切だ。",
              "For children, play is important."),
            T("、翻訳は"),
            W("単なる", "たんなる", "mere; simple; nothing but", "連体詞 (pre-noun adj.)", "N4"),
            W("仕事", "しごと", "work; job", "名詞 (noun)", "N5"),
            T("ではなく、"),
            W("生き方", "いきかた", "way of living; lifestyle", "名詞 (noun)", "N4"),
            T("そのものだった。"),
        ],
    },

    {
        "id": "n3_s05",
        "translation": "Compared to last year, he felt that his Japanese ability had improved considerably.",
        "tokens": [
            W("去年", "きょねん", "last year", "名詞 (noun)", "N5"),
            G("に比べて", "にくらべて", "Noun + に比べて",
              "compared to ~; in comparison with ~",
              "に比べて marks the standard of comparison. "
              "More specific than より: より just marks the comparison point; "
              "に比べて explicitly says 'when compared side by side with'.",
              "去年に比べて、今年は暑い。",
              "Compared to last year, this year is hot."),
            T("、"),
            W("日本語", "にほんご", "Japanese language", "名詞 (noun)", "N5"),
            P("の", "possessive particle"),
            W("力", "ちから", "ability; power", "名詞 (noun)", "N5"),
            P("が", "subject marker"),
            T("ずっと"),
            W("上がった", "あがった", "went up; improved (past)", "動詞 (verb)", "N4"),
            P("と", "quotation particle"),
            W("感じていた", "かんじていた", "was feeling; had been sensing", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s06",
        "translation": "He had kept on believing in the saying, \"The more you practice, the better you become.\"",
        "tokens": [
            T("「練習"),
            G("すればするほど", "すればするほど",
              "V-ば form + V plain + ほど",
              "the more you ~, the more ~ (proportional increase)",
              "ば〜ほど expresses a proportional relationship: as X increases, Y increases accordingly. "
              "Both verbs are the same. Also used with adjectives: 高ければ高いほど (the more expensive).",
              "練習すればするほど、上達する。",
              "The more you practice, the more you improve."),
            T("、"),
            W("上手になる", "じょうずになる", "become better; improve", "動詞 (verb)", "N5"),
            T("」という"),
            W("言葉", "ことば", "words; saying", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("信じて", "しんじて", "believing (て-form)", "動詞 (verb)", "N4"),
            W("続けてきた", "つづけてきた", "had continued (coming to now)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s07",
        "translation": "The moment the acceptance letter arrived, he involuntarily let out a loud cry.",
        "tokens": [
            W("合格", "ごうかく", "passing; acceptance", "名詞 (noun)", "N4"),
            W("通知", "つうち", "notification; notice", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("届いた", "とどいた", "arrived; reached (past)", "動詞 (verb)", "N4"),
            G("とたん", "とたん", "V past + とたん(に)",
              "the moment ~; just as ~ happened",
              "とたん (途端) describes an action or state that occurs IMMEDIATELY after the previous one. "
              "The second event often happens reflexively or unexpectedly. "
              "The main clause cannot be a deliberate action — only spontaneous reactions.",
              "ドアを開けたとたん、猫が飛び出してきた。",
              "The moment I opened the door, the cat jumped out."),
            T("、"),
            W("思わず", "おもわず", "involuntarily; without thinking", "副詞 (adverb)", "N4"),
            W("大きな", "おおきな", "big; large", "連体詞", "N5"),
            W("声", "こえ", "voice", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            T("上げてしまった。"),
        ],
    },

    {
        "id": "n3_s08",
        "translation": "While he was still overjoyed, he immediately got in touch with his parents and friends.",
        "tokens": [
            W("嬉しい", "うれしい", "happy; glad", "い形容詞 (i-adjective)", "N4"),
            G("うちに", "うちに", "V/Adj plain + うちに",
              "while ~ (before the state changes); while still ~",
              "うちに = 'during the time that ~ is still true'. "
              "Implies urgency: do it before the opportunity passes. "
              "Often used as advice. "
              "Compare: 〜ながら (simultaneous actions, same subject) vs うちに (time window, can change).",
              "若いうちに、いろいろな経験をしたほうがいい。",
              "You should have various experiences while you're still young."),
            T("、すぐに"),
            W("両親", "りょうしん", "parents (both)", "名詞 (noun)", "N4"),
            P("や", "listing particle (non-exhaustive): 'and, among others'"),
            W("友達", "ともだち", "friends", "名詞 (noun)", "N5"),
            P("に", "target particle"),
            W("連絡した", "れんらくした", "contacted; got in touch (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s09",
        "translation": "He made up his mind: \"I will absolutely not waste this opportunity.\"",
        "tokens": [
            T("「この"),
            W("機会", "きかい", "opportunity; chance", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("絶対に", "ぜったいに", "absolutely; definitely", "副詞 (adverb)", "N4"),
            W("無駄にしない", "むだにしない", "not waste; not squander", "動詞 (verb)", "N4"),
            T("」と、"),
            W("心", "こころ", "heart; mind", "名詞 (noun)", "N4"),
            P("に", "location particle (mental)"),
            W("決める", "きめる", "to decide", "動詞 (verb)", "N4"),
            G("ことにした", "ことにした", "V plain + ことにする (past)",
              "decided to ~ (speaker's deliberate choice)",
              "ことにする = make a conscious decision to do something. "
              "Speaker has full control and agency over the decision.",
              "毎朝ジョギングすることにした。", "I decided to jog every morning."),
            T("。"),
        ],
    },

    {
        "id": "n3_s10",
        "translation": "He never could have imagined a year ago that he would end up working at such a large company.",
        "tokens": [
            T("こんなに"),
            W("大きな", "おおきな", "large; big", "連体詞", "N5"),
            W("会社", "かいしゃ", "company", "名詞 (noun)", "N4"),
            P("で", "location particle"),
            W("働く", "はたらく", "to work", "動詞 (verb)", "N4"),
            G("ことになる", "ことになる", "V plain + ことになる",
              "it has been decided that ~; it turned out that ~ (by circumstances)",
              "ことになる = an outcome reached by circumstances or external decisions (not the speaker's choice). "
              "Contrast: ことにする = speaker's own active decision. "
              "Past: ことになった = it was decided / it turned out.",
              "来月、転勤することになった。",
              "It was decided that I would be transferred next month."),
            T("とは、一年前には"),
            W("想像", "そうぞう", "imagination; imagining", "名詞 (noun)", "N4"),
            T("もできなかった。"),
        ],
    },

    # ── 第二章: インターン初日 (Chapter 2: First Day of the Internship) ─────────

    {
        "id": "n3_s11",
        "translation": "Thanks to his senior's advice, he was able to prepare well for the interview.",
        "section": "第二章: インターン初日 (Chapter 2: First Day of the Internship)",
        "tokens": [
            W("先輩", "せんぱい", "senior; upperclassman", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            T("アドバイス"),
            G("のおかげで", "のおかげで", "Noun + のおかげで",
              "thanks to ~; owing to ~ (positive outcome)",
              "おかげで attributes a POSITIVE outcome to a cause. "
              "Opposite: せいで (negative outcome). "
              "Can also be used sarcastically: 〜のおかげで困った (Thanks to ~, I'm in trouble).",
              "あなたのおかげで、合格できた。",
              "Thanks to you, I was able to pass."),
            T("、"),
            W("面接", "めんせつ", "interview", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("準備", "じゅんび", "preparation", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("うまく", "うまく", "skillfully; well", "副詞 (adverb)", "N4"),
            W("進める", "すすめる", "to advance; to proceed with", "動詞 (verb)", "N4"),
            G("ことができた", "ことができた", "V plain + ことができた",
              "was able to ~ (past ability)",
              "Past form of ことができる. Expresses that something was achievable on a specific occasion.",
              "一人で解決することができた。", "I was able to solve it by myself."),
            T("。"),
        ],
    },

    {
        "id": "n3_s12",
        "translation": "On the other hand, due to insufficient preparation, he ended up making a big mistake in his first translation.",
        "tokens": [
            T("一方、"),
            W("準備不足", "じゅんびぶそく", "lack of preparation", "名詞 (noun)", "N4"),
            G("のせいで", "のせいで", "Noun + のせいで",
              "because of ~; due to ~ (negative outcome, blame)",
              "せいで attributes a NEGATIVE outcome to a cause. Often implies blame or frustration. "
              "Contrast: おかげで (positive outcome).",
              "雨のせいで、試合が中止になった。",
              "Because of the rain, the match was cancelled."),
            T("、最初の"),
            W("翻訳", "ほんやく", "translation", "名詞 (noun)", "N4"),
            P("で", "context particle"),
            W("大きな", "おおきな", "big; significant", "連体詞", "N5"),
            T("ミスを"),
            G("してしまった", "してしまった", "V て-form + しまった",
              "ended up making ~ (regret/unintended completion)",
              "てしまった expresses an action completed unintentionally or with regret.",
              "大切なものをなくしてしまった。", "I ended up losing something important."),
            T("。"),
        ],
    },

    {
        "id": "n3_s13",
        "translation": "As his experience accumulated, the appeal of the work gradually became clearer to him.",
        "tokens": [
            W("経験", "けいけん", "experience", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("増える", "ふえる", "to increase; to accumulate", "動詞 (verb)", "N4"),
            G("につれて", "につれて", "V plain / Noun + につれて",
              "as ~ (proportional change); in proportion to ~",
              "につれて expresses that as one thing changes, another changes in step with it. "
              "Both clauses must describe changes. More formal than とともに.",
              "時間が経つにつれて、痛みが消えていった。",
              "As time passed, the pain gradually faded."),
            T("、"),
            W("仕事", "しごと", "work", "名詞 (noun)", "N5"),
            P("の", "possessive particle"),
            W("面白さ", "おもしろさ", "interest; fun; appeal", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("分かって", "わかって", "became clear; came to understand (て-form)", "動詞 (verb)", "N5"),
            G("きた", "きた", "V て-form + きた",
              "has come to be; has gradually ~ (change toward now)",
              "てくる = a change that started in the past and has arrived at the present moment.",
              "だんだん分かってきた。", "I've gradually come to understand."),
            T("。"),
        ],
    },

    {
        "id": "n3_s14",
        "translation": "Every time he met with a senior colleague, there was always a new realization.",
        "tokens": [
            W("先輩", "せんぱい", "senior", "名詞 (noun)", "N4"),
            P("に", "target particle"),
            W("会う", "あう", "to meet", "動詞 (verb)", "N4"),
            G("たびに", "たびに", "V plain / Noun + たびに",
              "every time ~; whenever ~; each time ~",
              "たびに = 'each time this happens, that also happens'. "
              "The result clause usually expresses something consistent or predictable. "
              "Can follow verbs (plain) or nouns (の).",
              "彼に会うたびに、元気をもらう。",
              "Every time I meet him, I feel encouraged."),
            T("、"),
            W("新しい", "あたらしい", "new", "い形容詞 (i-adjective)", "N5"),
            W("気づき", "きづき", "realization; insight", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("あった", "あった", "there was; had (past)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "n3_s15",
        "translation": "He was happy to be told the words, \"Although you're not yet perfect, you are steadily growing.\"",
        "tokens": [
            T("「まだ"),
            W("完璧", "かんぺき", "perfect; flawless", "な形容詞 (na-adjective)", "N4"),
            T("ではない"),
            G("ものの", "ものの", "Plain form + ものの",
              "although ~; even though ~; while ~ (concession with unexpectedness)",
              "ものの acknowledges the first clause but shows that the expected consequence did NOT follow. "
              "More formal than が or けれど. Often in writing.",
              "合格したものの、まだ自信がない。",
              "Although I passed, I still don't have confidence."),
            T("、"),
            W("着実に", "ちゃくじつに", "steadily; surely", "副詞 (adverb)", "N4"),
            W("成長している", "せいちょうしている", "is growing; is developing", "動詞 (verb)", "N4"),
            T("」"),
            P("と", "quotation particle"),
            W("言われた", "いわれた", "was told (passive)", "動詞 (verb)", "N5"),
            W("言葉", "ことば", "words", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("嬉しかった", "うれしかった", "was happy (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s16",
        "translation": "Kenji became increasingly convinced that there is no way translation can be done perfectly by machines.",
        "tokens": [
            W("翻訳", "ほんやく", "translation", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            W("機械", "きかい", "machine", "名詞 (noun)", "N4"),
            P("に", "agent particle"),
            W("完全に", "かんぜんに", "completely; perfectly", "副詞 (adverb)", "N4"),
            G("できるわけがない", "できるわけがない",
              "V plain + わけがない",
              "there's no way ~ can ~; it's impossible that ~",
              "わけがない = 'there is no reason for this to be the case' → strong denial of possibility. "
              "Stronger than はずがない. "
              "Contrast: わけではない (it doesn't mean that) — that just denies an implication.",
              "彼がそんなことを言うわけがない。",
              "There's no way he would say something like that."),
            P("と", "quotation particle"),
            T("、"),
            N("健二", "けんじ", "Kenji"),
            P("は", "topic marker"),
            W("ますます", "ますます", "more and more; increasingly", "副詞 (adverb)", "N4"),
            W("確信する", "かくしんする", "to be convinced; to be certain", "動詞 (verb)", "N4"),
            G("ようになった", "ようになった", "V plain + ようになった",
              "came to ~; gradually began to ~ (change in ability or state)",
              "Marks a gradual change. Something that wasn't true before has now become true.",
              "日本語が読めるようになった。", "I came to be able to read Japanese."),
            T("。"),
        ],
    },

    {
        "id": "n3_s17",
        "translation": "On the contrary, as AI advances, the value of translation that only humans can do must rise even further.",
        "tokens": [
            T("むしろ、AIが"),
            W("発達する", "はったつする", "to develop; to advance", "動詞 (verb)", "N4"),
            G("につれ", "につれ", "V plain + につれ(て)", "as ~ (proportional change)",
              "Shorter form of につれて. Used the same way.",
              "技術が進むにつれ、生活が便利になった。",
              "As technology advanced, life became more convenient."),
            T("、"),
            W("人間", "にんげん", "human being; person", "名詞 (noun)", "N4"),
            T("だからこそできる"),
            W("翻訳", "ほんやく", "translation", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("価値", "かち", "value; worth", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            W("さらに", "さらに", "furthermore; even more", "副詞 (adverb)", "N4"),
            W("上がる", "あがる", "to go up; to rise", "動詞 (verb)", "N4"),
            G("に違いない", "にちがいない",
              "Plain form + に違いない",
              "must be ~; certainly ~; no doubt ~",
              "に違いない expresses the speaker's strong conviction based on reasoning. "
              "More assertive than はずだ. Cannot be used for decisions the speaker controls. "
              "Similar to: 〜に決まっている (also strong conviction).",
              "彼は知っているに違いない。",
              "He must know. / There's no doubt he knows."),
            T("。"),
        ],
    },

    {
        "id": "n3_s18",
        "translation": "Through the work of translation, he felt his world continuing to expand.",
        "tokens": [
            W("翻訳", "ほんやく", "translation", "名詞 (noun)", "N4"),
            T("という仕事"),
            G("を通じて", "をつうじて", "Noun + を通じて / を通して",
              "through ~; via ~; by means of ~; throughout ~",
              "を通じて expresses the medium, means, or duration through which something happens. "
              "を通して is almost identical but slightly more common in speech. "
              "Duration meaning: 一年を通じて (throughout the year).",
              "音楽を通じて、世界がつながる。",
              "Through music, the world is connected."),
            T("、"),
            W("世界", "せかい", "world", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("広がって", "ひろがって", "spreading out; expanding (て-form)", "動詞 (verb)", "N4"),
            G("いくのを", "いくのを",
              "V て-form + いく + の + を",
              "the fact that ~ is going (continuing away; into the future)",
              "ていく describes continuation moving away from now / into the future. "
              "の nominalization makes the clause a noun, then を marks it as the object of 感じる.",
              "時間が過ぎていくのを感じた。", "I felt time passing by."),
            W("感じていた", "かんじていた", "was feeling; was sensing", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s19",
        "translation": "Speaking of the work of translation, not only language ability but also cultural sensibility is important.",
        "tokens": [
            W("翻訳の仕事", "ほんやくのしごと", "the work of translation", "名詞 (noun)", "N4"),
            G("に関して", "にかんして", "Noun + に関して / に関する",
              "regarding ~; concerning ~; about ~",
              "に関して is more formal than について. "
              "に関する + Noun (attributive): 翻訳に関する本 = a book about translation. "
              "Use で話す / で書く with に関して to indicate formal discussion.",
              "環境問題に関して、会議が行われた。",
              "A meeting was held regarding environmental issues."),
            T("言えば、"),
            W("言語力", "げんごりょく", "language ability; linguistic competence", "名詞 (noun)", "N4"),
            G("だけでなく", "だけでなく", "Noun/plain + だけでなく",
              "not only ~ but also ~",
              "Goes beyond just one quality to name additional ones.",
              "彼は頭がいいだけでなく、優しくもある。",
              "He is not only smart but also kind."),
            T("、"),
            W("文化的センス", "ぶんかてきせんす", "cultural sensibility; cultural sense", "名詞 (noun)", "N4"),
            T("も"),
            W("重要", "じゅうよう", "important", "な形容詞 (na-adjective)", "N4"),
            T("だ。"),
        ],
    },

    {
        "id": "n3_s20",
        "translation": "Triggered by this experience, Kenji came to think seriously about his future.",
        "tokens": [
            T("この"),
            W("経験", "けいけん", "experience", "名詞 (noun)", "N4"),
            G("をきっかけに", "をきっかけに", "Noun + をきっかけに",
              "using ~ as an opportunity; triggered by ~; since ~",
              "をきっかけに marks the event that triggered a change. "
              "The change expressed after it is often sustained or significant. "
              "Similar: をきっかけとして (more formal).",
              "留学をきっかけに、英語が好きになった。",
              "Studying abroad was the trigger for me to come to like English."),
            T("、"),
            N("健二", "けんじ", "Kenji"),
            P("は", "topic marker"),
            W("将来", "しょうらい", "future; one's future", "名詞 (noun)", "N4"),
            G("について", "について", "Noun + について", "about ~; regarding ~",
              "Indicates the topic being thought or talked about.",
              "将来について考えた。", "I thought about the future."),
            W("真剣に", "しんけんに", "seriously; earnestly", "副詞 (adverb)", "N4"),
            W("考える", "かんがえる", "to think; to consider", "動詞 (verb)", "N4"),
            G("ようになった", "ようになった", "V plain + ようになった", "came to ~",
              "Gradual change: something that wasn't happening before now happens regularly.",
              "考えるようになった。", "I came to think about it."),
            T("。"),
        ],
    },

    {
        "id": "n3_s21",
        "translation": "While reflecting on his mistake-prone self, he decided to keep looking forward nonetheless.",
        "tokens": [
            T("ミスを"),
            G("しがちな", "しがちな", "V-stem + がちな / がちだ",
              "tend to ~; apt to ~; prone to ~",
              "がち describes a negative tendency or habit. "
              "がちだ = tends to happen; がちな + noun = prone to. "
              "Often implies this is a fault or concern. "
              "Similar: やすい (neutral tendency); がち (often negative).",
              "彼は遅刻しがちだ。", "He tends to be late."),
            W("自分", "じぶん", "oneself; I (reflexive)", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("反省し", "はんせいし", "reflect on; reproach oneself (連用形)", "動詞 (verb)", "N4"),
            G("ながら", "ながら",
              "V-stem + ながら (adversative)",
              "while (doing); despite ~ (adversative use)",
              "ながら has two uses: ① simultaneous actions (most common); "
              "② adversative (despite): A ながら B = although A, B. "
              "In the adversative use, A and B are contradictory. "
              "Example: 知りながら黙っていた = knew it and yet stayed silent.",
              "狭いながらも、居心地のいい部屋だった。",
              "Small though it was, it was a comfortable room."),
            T("、それでも"),
            W("前を向く", "まえをむく", "to face forward; to look ahead", "動詞 (verb)", "N4"),
            G("ことにした", "ことにした", "V plain + ことにした", "decided to ~",
              "Speaker's active decision.",
              "頑張ることにした。", "I decided to do my best."),
            T("。"),
        ],
    },

    {
        "id": "n3_s22",
        "translation": "Even when faced with so many references he couldn't possibly read them all, he never once thought of giving up.",
        "tokens": [
            W("読み切れない", "よみきれない", "cannot read completely; cannot finish reading", "動詞 (verb)", "N4"),
            G("ほど", "ほど", "V/Adj plain + ほど",
              "to the extent that ~; so ~ that ~; about ~ (approximate degree)",
              "ほど marks an extent or degree. Three uses: "
              "① Extent: 泣くほど笑った (laughed so much I cried). "
              "② Comparison: AほどBではない (B is not as [adj] as A). "
              "③ Approximation: 一時間ほど (about one hour).",
              "彼は歩けないほど疲れていた。",
              "He was so tired he couldn't walk."),
            W("多くの", "おおくの", "many; a large number of", "連体詞", "N4"),
            W("参考文献", "さんこうぶんけん", "references; bibliography", "名詞 (noun)", "N4"),
            P("を", "object particle"),
            W("前にしても", "まえにしても", "even when faced with", "動詞 (verb)", "N4"),
            T("、"),
            W("諦めよう", "あきらめよう", "give up (volitional form)", "動詞 (verb)", "N4"),
            G("とは思わなかった", "とはおもわなかった",
              "V volitional + とは思わなかった",
              "didn't intend to ~; never thought of ~ing",
              "Volitional + とする = try to do / be about to do. "
              "Here, 諦めようとは思わなかった = didn't even think of giving up.",
              "逃げようとは思わなかった。", "I never thought of running away."),
            T("。"),
        ],
    },

    {
        "id": "n3_s23",
        "translation": "The words \"Just because you are good at languages doesn't necessarily mean you're a good translator\" weighed heavily on him.",
        "tokens": [
            T("「語学が"),
            W("得意", "とくい", "good at; skilled in", "な形容詞 (na-adjective)", "N4"),
            T("だ"),
            G("からといって", "からといって",
              "Plain form + からといって",
              "just because ~; even though ~ (doesn't mean the conclusion follows)",
              "からといって marks a reason that, the speaker argues, does NOT justify the consequence. "
              "Often followed by とは限らない or わけではない.",
              "お金があるからといって、幸せとは限らない。",
              "Just because you have money doesn't mean you're happy."),
            T("、翻訳が"),
            W("上手", "じょうず", "skilled; good at", "な形容詞 (na-adjective)", "N5"),
            G("とは限らない", "とはかぎらない",
              "Plain form + とは限らない",
              "not necessarily ~; not always ~ (challenging an assumption)",
              "とは限らない = 'is not always the case'. Challenges a generalization. "
              "Often follows からといって or even though constructions.",
              "高いものが良いとは限らない。",
              "Expensive things are not necessarily good."),
            T("」という"),
            W("言葉", "ことば", "words", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            W("重く", "おもく", "heavily; weightily (adverb)", "副詞", "N4"),
            W("感じた", "かんじた", "felt; sensed (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s24",
        "translation": "When the internship came to an end, the department head said the following.",
        "section": "第三章: 別れ際の言葉 (Chapter 3: Words at Parting)",
        "tokens": [
            W("インターン", "いんたーん", "internship", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("終わる", "おわる", "to end; to finish", "動詞 (verb)", "N5"),
            G("際に", "さいに", "Noun + の際に / V plain + 際に",
              "when ~; on the occasion of ~; at the time of ~",
              "際に is a formal expression for 'when' or 'on the occasion of'. "
              "More formal than とき; used in business, official, and written contexts.",
              "帰国する際に、ぜひ連絡ください。",
              "When you return to your country, please do get in touch."),
            T("、"),
            W("部長", "ぶちょう", "department head; section chief", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            T("こう"),
            W("おっしゃった", "おっしゃった", "said (honorific of 言う, past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s25",
        "translation": "\"Your passion comes through more clearly than any other candidate's.\" Those words were ones he would never forget for the rest of his life.",
        "tokens": [
            T("「あなたの"),
            W("情熱", "じょうねつ", "passion; enthusiasm", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            T("どの"),
            W("候補者", "こうほしゃ", "candidate; applicant", "名詞 (noun)", "N4"),
            G("よりも", "よりも", "Noun + よりも",
              "more than ~; compared to ~ (emphatic comparison)",
              "より alone marks comparison; よりも adds emphasis (even more than).",
              "誰よりも努力した。", "I worked harder than anyone."),
            W("伝わって", "つたわって", "was conveyed; came through (て-form)", "動詞 (verb)", "N4"),
            G("きます", "きます", "V て-form + きます",
              "is coming across; has been building up (toward now)",
              "てくる indicates movement or change coming toward the present.",
              "だんだん分かってきます。", "It gradually comes to make sense."),
            T("。」その"),
            W("言葉", "ことば", "words", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            W("一生", "いっしょう", "a lifetime; forever", "名詞 (noun)", "N4"),
            W("忘れられない", "わすれられない", "cannot forget (negative potential)", "動詞 (verb)", "N4"),
            T("だろう。"),
        ],
    },

    {
        "id": "n3_s26",
        "translation": "His dream was slowly but surely coming true. Holding that conviction in his heart, Kenji set out toward the next stage of his life.",
        "section": "第四章: 東京での新生活 (Chapter 4: New Life in Tokyo)",
        "tokens": [
            W("夢", "ゆめ", "dream; aspiration", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            W("少しずつ", "すこしずつ", "little by little", "副詞 (adverb)", "N4"),
            W("実現し", "じつげんし", "realize; come true (連用形)", "動詞 (verb)", "N4"),
            G("つつある", "つつある", "V-stem + つつある",
              "is in the process of ~ing; is gradually ~ing",
              "つつある describes an action or change currently in progress, heading toward completion. "
              "More formal and literary than ている. "
              "Often used to describe gradual societal or personal change. "
              "Different from ている which just describes a state.",
              "状況は少しずつ改善されつつある。",
              "The situation is gradually being improved."),
            T("。"),
            W("そう", "そう", "so; that way", "副詞 (adverb)", "N5"),
            W("確信し", "かくしんし", "convinced (連用形)", "動詞 (verb)", "N4"),
            G("ながら", "ながら", "V-stem + ながら", "while doing ~",
              "Simultaneous actions.",
              "笑いながら話した。", "I talked while laughing."),
            T("、"),
            N("健二", "けんじ", "Kenji"),
            P("は", "topic marker"),
            W("次の", "つぎの", "next; the following", "連体詞", "N4"),
            T("ステージへと"),
            W("歩み", "あゆみ", "step; advance (連用形 of 歩む)", "動詞 (verb)", "N4"),
            W("始めた", "はじめた", "began; started (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    # ── 第四章続き: 東京での新生活 ────────────────────────────────────────────

    {
        "id": "n3_s27",
        "translation": "According to the company handbook, interns are supposed to submit a daily report every evening.",
        "tokens": [
            W("会社", "かいしゃ", "company", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("規則", "きそく", "rules; regulations", "名詞 (noun)", "N4"),
            G("によると", "によると", "Noun + によると",
              "according to ~",
              "によると introduces information received from a source. Always paired with hearsay expressions like らしい or とのことだ.",
              "規則によると、毎日報告書を出すことになっている。",
              "According to the rules, you are supposed to submit a report every day."),
            T("、インターン生は毎晩"),
            W("日報", "にっぽう", "daily report", "名詞 (noun)", "N3"),
            P("を", "object particle"),
            W("提出する", "ていしゅつする", "to submit", "動詞 (verb)", "N4"),
            G("ことになっている", "ことになっている",
              "V plain + ことになっている",
              "it is decided that ~; it is supposed to ~; it is a rule that ~",
              "ことになっている describes a rule, custom, or arrangement that is in place. "
              "Unlike ことになった (a one-time decision), ことになっている is a standing arrangement. "
              "Often used for schedules, regulations, or social norms.",
              "社員は毎朝9時に出社することになっている。",
              "Employees are supposed to arrive at 9 a.m. every morning."),
            T("。"),
        ],
    },

    {
        "id": "n3_s28",
        "translation": "Not only was the office environment comfortable, but his colleagues were also kind.",
        "tokens": [
            W("職場", "しょくば", "workplace; office", "名詞 (noun)", "N3"),
            P("の", "possessive particle"),
            W("環境", "かんきょう", "environment; surroundings", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("快適", "かいてき", "comfortable; pleasant", "な形容詞 (na-adjective)", "N3"),
            T("な"),
            G("ばかりでなく", "ばかりでなく",
              "Noun / plain form + ばかりでなく",
              "not only ~, but also ~ (broader scope)",
              "ばかりでなく adds another element beyond the first. "
              "Similar to だけでなく but slightly more emphatic. "
              "Often followed by も or まで. Used in both formal and casual contexts.",
              "彼は優しいばかりでなく、とても頭もいい。",
              "Not only is he kind, but he is also very smart."),
            T("、"),
            W("同僚", "どうりょう", "colleague; co-worker", "名詞 (noun)", "N3"),
            T("たちも"),
            W("親切", "しんせつ", "kind; considerate", "な形容詞 (na-adjective)", "N4"),
            T("だった。"),
        ],
    },

    {
        "id": "n3_s29",
        "translation": "On the other hand, the volume of work was far beyond what he had imagined.",
        "tokens": [
            G("一方で", "いっぽうで",
              "Clause + 一方で",
              "on the other hand; while ~ (contrast or parallel situation)",
              "一方で presents a contrasting or coexisting fact. "
              "Can also describe two simultaneous states: 'while A, at the same time B'. "
              "Similar to: それに対して (in contrast). 一方 alone can also mean 'on the one hand'.",
              "都市化が進む一方で、自然が失われている。",
              "While urbanization advances, nature is being lost."),
            T("、"),
            W("仕事", "しごと", "work", "名詞 (noun)", "N5"),
            P("の", "possessive particle"),
            W("量", "りょう", "volume; quantity", "名詞 (noun)", "N3"),
            P("は", "topic marker"),
            W("想像", "そうぞう", "imagination", "名詞 (noun)", "N4"),
            G("をはるかに超えていた", "をはるかにこえていた",
              "Noun + をはるかに超えていた",
              "was far beyond ~; greatly exceeded ~",
              "を + はるかに (by far) + 超える (to exceed). Emphasizes the degree to which something surpasses the standard.",
              "予想をはるかに超える結果だった。",
              "The result was far beyond expectations."),
            T("。"),
        ],
    },

    {
        "id": "n3_s30",
        "translation": "Even so, he felt he couldn't help but push forward — he simply couldn't give up.",
        "tokens": [
            T("それでも、"),
            W("諦める", "あきらめる", "to give up", "動詞 (verb)", "N4"),
            G("わけにはいかない", "わけにはいかない",
              "V plain + わけにはいかない",
              "cannot afford to ~; must not ~; it's not possible to ~",
              "わけにはいかない expresses that doing something is impossible given social obligations, common sense, or circumstances. "
              "Stronger than できない. The speaker feels they have no choice but NOT to do it.",
              "大事な試合だから、負けるわけにはいかない。",
              "This is an important match, so I cannot afford to lose."),
            T("と"),
            W("感じ", "かんじ", "feel (連用形)", "動詞 (verb)", "N4"),
            T("、"),
            W("前へ進ま", "まえへすすま", "move forward (negative stem of 進む)", "動詞 (verb)", "N4"),
            G("ずにはいられなかった", "ずにはいられなかった",
              "V-ない stem + ずにはいられない (past)",
              "couldn't help but ~; was compelled to ~ (past)",
              "ずにはいられない expresses an irresistible urge — the speaker cannot stop themselves from doing it. "
              "Formation: V-ない → drop ない → add ずにはいられない. Exception: する → せずにはいられない. "
              "Formal/literary; spoken equivalent: ないではいられない.",
              "彼の話を聞いて、泣かずにはいられなかった。",
              "Hearing his story, I couldn't help but cry."),
            T("。"),
        ],
    },

    {
        "id": "n3_s31",
        "translation": "He had had the experience of staying up all night to finish a single document.",
        "tokens": [
            W("一つ", "ひとつ", "one (thing)", "名詞 (noun)", "N5"),
            P("の", "possessive particle"),
            W("文書", "ぶんしょ", "document; text", "名詞 (noun)", "N3"),
            P("を", "object particle"),
            W("仕上げる", "しあげる", "to finish; to complete", "動詞 (verb)", "N3"),
            G("ために", "ために", "V plain + ために", "in order to ~",
              "Expresses purpose. The following action is taken for the sake of what precedes ために.",
              "合格するために、毎日勉強している。",
              "I study every day in order to pass."),
            W("一晩中", "ひとばんじゅう", "all night long; throughout the night", "名詞 (noun)", "N3"),
            W("起きていた", "おきていた", "stayed up; was awake (past progressive)", "動詞 (verb)", "N4"),
            G("ことがある", "ことがある",
              "V past + ことがある",
              "have had the experience of ~; have done ~ before",
              "V past (た-form) + ことがある = have experienced doing something at least once. "
              "Expresses past experience. Contrast with V plain + ことがある = sometimes happens.",
              "富士山に登ったことがある。",
              "I have climbed Mt. Fuji before."),
            T("。"),
        ],
    },

    # ── 第五章: 最初の挑戦 (Chapter 5: The First Challenge) ──────────────────

    {
        "id": "n3_s32",
        "translation": "His supervisor gave him a difficult English technical document to translate.",
        "section": "第五章: 最初の挑戦 (Chapter 5: The First Challenge)",
        "tokens": [
            W("上司", "じょうし", "supervisor; boss", "名詞 (noun)", "N3"),
            P("は", "topic marker"),
            N("健二", "けんじ", "Kenji"),
            P("に", "target particle"),
            W("難しい", "むずかしい", "difficult", "い形容詞 (i-adjective)", "N5"),
            W("英語", "えいご", "English (language)", "名詞 (noun)", "N5"),
            P("の", "possessive particle"),
            W("専門文書", "せんもんぶんしょ", "technical document", "名詞 (noun)", "N3"),
            P("を", "object particle"),
            W("翻訳して", "ほんやくして", "translate (て-form)", "動詞 (verb)", "N4"),
            G("みるよう", "みるよう",
              "V て-form + みる + ように",
              "try doing ~; have a go at ~ (instructed attempt)",
              "てみる = try doing to see how it goes. ように言われた = was told to. "
              "Combined: was told to try doing.",
              "一度やってみるように言われた。",
              "I was told to try doing it once."),
            W("言った", "いった", "said; told (past)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "n3_s33",
        "translation": "For Kenji, this was his first time translating a real professional document.",
        "tokens": [
            N("健二", "けんじ", "Kenji"),
            G("にとって", "にとって", "Noun + にとって",
              "for ~; from the perspective of ~",
              "にとって marks the person from whose standpoint something is evaluated.",
              "子供にとって、遊びは大切だ。",
              "For children, play is important."),
            T("、"),
            W("本物", "ほんもの", "the real thing; genuine", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("業務文書", "ぎょうむぶんしょ", "business document", "名詞 (noun)", "N3"),
            P("を", "object particle"),
            W("翻訳する", "ほんやくする", "to translate", "動詞 (verb)", "N4"),
            P("の", "nominalizer"),
            P("は", "topic marker (contrast)"),
            W("初めて", "はじめて", "for the first time", "副詞 (adverb)", "N4"),
            W("だった", "だった", "was (past copula)", "助動詞", "N5"),
            T("。"),
        ],
    },

    {
        "id": "n3_s34",
        "translation": "The text was so long he couldn't finish it in time, and he was unbearably anxious.",
        "tokens": [
            W("文章", "ぶんしょう", "text; passage", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("長すぎて", "ながすぎて", "too long (て-form)", "動詞 (verb)", "N4"),
            W("時間内", "じかんない", "within the time limit", "名詞 (noun)", "N3"),
            P("に", "time particle"),
            W("終わら", "おわら", "finish (negative stem of 終わる)", "動詞 (verb)", "N5"),
            T("ず、"),
            W("不安", "ふあん", "anxiety; unease", "名詞 (noun)", "N4"),
            T("で"),
            G("たまらなかった", "たまらなかった",
              "V て-form / Adj stem + てたまらない (past negative)",
              "was unbearably ~; couldn't stand being ~",
              "てたまらない expresses an overwhelming feeling the speaker cannot control. "
              "たまらない literally means 'cannot bear it'. "
              "Used with emotion or sensation adjectives: 寂しくてたまらない, 眠くてたまらない. "
              "Similar: てしょうがない (same nuance, slightly more casual).",
              "試験が心配でたまらない。",
              "I'm so worried about the exam I can't stand it."),
            T("。"),
        ],
    },

    {
        "id": "n3_s35",
        "translation": "He asked his supervisor: \"Would it be all right if I allowed myself to take a little more time?\"",
        "tokens": [
            T("「もう少し"),
            W("時間", "じかん", "time", "名詞 (noun)", "N5"),
            P("を", "object particle"),
            W("いただく", "いただく", "to receive; to have (humble)", "動詞 (verb)", "N4"),
            G("させてもらえませんか", "させてもらえませんか",
              "V-causative stem + てもらえませんか",
              "would it be all right if I ~ / could I please be allowed to ~",
              "させてもらう = receive permission to do (humbly). The causative + もらう combination expresses "
              "asking for permission to act, while showing deference to the person who grants it. "
              "Negative question form (-ませんか) makes it a polite request.",
              "写真を撮らせてもらえませんか。",
              "Would it be all right if I took a photo?"),
            T("」"),
            P("と", "quotation particle"),
            W("上司", "じょうし", "supervisor", "名詞 (noun)", "N3"),
            P("に", "target particle"),
            W("聞いた", "きいた", "asked (past)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "n3_s36",
        "translation": "The supervisor replied, \"It's true that the deadline is tight, but accuracy comes first.\"",
        "tokens": [
            G("確かに", "たしかに",
              "確かに～が / 確かに～けれど",
              "it is true that ~, but ~ (conceding a point before contrasting)",
              "確かに acknowledges the other side's point as valid before presenting the speaker's main view. "
              "Often followed by が, けれど, or しかし. "
              "Similar to: なるほど～が; English: 'Admittedly ~, but ~'.",
              "確かに難しいが、不可能ではない。",
              "It's true it's difficult, but it's not impossible."),
            W("締め切り", "しめきり", "deadline", "名詞 (noun)", "N3"),
            P("は", "topic marker"),
            W("厳しい", "きびしい", "strict; tight", "い形容詞 (i-adjective)", "N3"),
            G("が", "が", "Clause + が", "but; however (contrast)",
              "Concessive conjunction at sentence boundary.",
              "難しいが、やってみます。", "It's hard, but I'll try."),
            T("、"),
            W("正確さ", "せいかくさ", "accuracy; precision", "名詞 (noun)", "N3"),
            P("が", "subject marker"),
            T("一番だ」"),
            P("と", "quotation particle"),
            W("言われた", "いわれた", "was told (passive)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "n3_s37",
        "translation": "He submitted the translation having stayed up all night. Even so, it wasn't perfect.",
        "tokens": [
            W("一晩中", "ひとばんじゅう", "all night long", "名詞 (noun)", "N3"),
            W("かけて", "かけて", "spending; taking (て-form of かける)", "動詞 (verb)", "N4"),
            W("翻訳を", "ほんやくを", "translation (object)", "名詞 (noun)", "N4"),
            W("提出した", "ていしゅつした", "submitted (past)", "動詞 (verb)", "N4"),
            T("。それでも、"),
            W("完璧", "かんぺき", "perfect; flawless", "な形容詞 (na-adjective)", "N4"),
            G("とは言えなかった", "とはいえなかった",
              "Plain form + とは言えない (past negative)",
              "cannot be said to be ~; it would be an overstatement to say ~",
              "とは言えない challenges an overstated claim. "
              "Literally: 'it cannot be said that ~'. Used when something falls short of a description.",
              "完全に理解したとは言えない。",
              "I can't say I understood it completely."),
            T("。"),
        ],
    },

    # ── 第六章: 先輩からの助言 (Chapter 6: Advice from a Senior) ─────────────

    {
        "id": "n3_s38",
        "translation": "A senior colleague who noticed this came to talk to him.",
        "section": "第六章: 先輩からの助言 (Chapter 6: Advice from a Senior)",
        "tokens": [
            T("それに"),
            W("気づいた", "きづいた", "noticed; realized (past)", "動詞 (verb)", "N4"),
            W("先輩", "せんぱい", "senior colleague", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("声をかけて", "こえをかけて", "spoke to; came over to (て-form)", "動詞 (verb)", "N4"),
            G("くれた", "くれた", "V て-form + くれた",
              "did ~ for me (favor given to speaker)",
              "てくれる = someone does something for the speaker's benefit.",
              "友達が助けてくれた。", "My friend helped me."),
            T("。"),
        ],
    },

    {
        "id": "n3_s39",
        "translation": "\"For someone who is a newcomer, this level of quality is quite impressive,\" said the senior.",
        "tokens": [
            T("「"),
            W("新人", "しんじん", "newcomer; new employee", "名詞 (noun)", "N3"),
            G("にしては", "にしては",
              "Noun / plain form + にしては",
              "for ~; considering that ~; given that ~ (unexpectedly good or bad)",
              "にしては marks a gap between expectation and reality. "
              "The result is BETTER or WORSE than you'd expect given the subject's status. "
              "Unlike にとって (which evaluates something from someone's perspective), "
              "にしては judges how surprising the result is.",
              "新人にしては、仕事が早い。",
              "For a newcomer, he works fast."),
            T("、この"),
            W("クオリティ", "くおりてぃ", "quality", "名詞 (noun)", "N3"),
            P("は", "topic marker"),
            W("なかなか", "なかなか", "quite; considerably; not easily", "副詞 (adverb)", "N4",
              "With positive adjective: quite good. With negative form: not easily / hard to ~."),
            W("のものだ", "のものだ", "is quite something; is impressive", "助動詞", "N3"),
            T("」"),
            P("と", "quotation particle"),
            W("先輩", "せんぱい", "senior", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            W("言った", "いった", "said (past)", "動詞 (verb)", "N5"),
            T("。"),
        ],
    },

    {
        "id": "n3_s40",
        "translation": "\"Compared to language ability, your sense for cultural nuance is rather exceptional.\"",
        "tokens": [
            T("「語学力に"),
            G("比べて", "くらべて", "Noun + に比べて", "compared to ~",
              "に比べて marks the standard of comparison.",
              "去年に比べて、今年は暑い。", "Compared to last year, this year is hot."),
            T("、文化的なニュアンスへの"),
            W("感覚", "かんかく", "sense; feeling; intuition", "名詞 (noun)", "N3"),
            P("は", "topic marker"),
            G("むしろ", "むしろ",
              "むしろ",
              "rather; instead; if anything (reversal of expectation)",
              "むしろ introduces a correction or reversal — the true situation is the opposite of or different from expected. "
              "Often used to say 'if anything, it's more like X'. "
              "Similar: かえって (unexpectedly; contrary to expectation, often negative).",
              "彼のアドバイスはむしろ逆効果だった。",
              "His advice was rather counterproductive."),
            W("優れている", "すぐれている", "is superior; is exceptional (progressive)", "動詞 (verb)", "N3"),
            T("。」"),
        ],
    },

    {
        "id": "n3_s41",
        "translation": "\"If only you pay careful attention to the deadline, you should have no trouble.\"",
        "tokens": [
            T("「締め切り"),
            P("さえ", "even particle — 'if only'"),
            W("気をつければ", "きをつければ", "if you are careful (conditional)", "動詞 (verb)", "N4"),
            G("さえ〜ば", "さえ〜ば",
              "Noun + さえ + V-ば / Adj + ければ",
              "if only ~; as long as ~ (minimum condition)",
              "さえ〜ば expresses a minimum sufficient condition: 'if just this one thing is in place, everything will be fine'. "
              "さえ (even) marks the single key condition; ば is the conditional form. "
              "Often translates as 'as long as' or 'if only'.",
              "お金さえあれば、何でも買える。",
              "If only you have money, you can buy anything."),
            T("、"),
            W("問題", "もんだい", "problem; trouble", "名詞 (noun)", "N4"),
            G("はないはずだ", "はないはずだ",
              "Plain form + はずだ (negative)",
              "should be no ~; there ought to be no ~ (confident negative expectation)",
              "はずだ = confident expectation based on reasoning.",
              "問題はないはずだ。", "There should be no problem."),
            T("。」"),
        ],
    },

    {
        "id": "n3_s42",
        "translation": "\"Even if you make a mistake, as long as you learn from it, there's no need to worry.\"",
        "tokens": [
            T("「"),
            G("たとえ", "たとえ",
              "たとえ + V て-form + も / たとえ～ても",
              "even if ~; no matter how ~ (hypothetical concession)",
              "たとえ～ても presents a hypothetical case and insists the result won't change. "
              "たとえ is an adverb that strengthens the concessive meaning of ても. "
              "Can be used with any verb, adjective, or noun + でも. "
              "Similar: もし～ても (if even ~).",
              "たとえ失敗しても、あきらめない。",
              "Even if I fail, I won't give up."),
            W("ミスをしても", "みすをしても", "even if you make a mistake", "動詞 (verb)", "N4"),
            T("、"),
            W("そこから学べば", "そこからまなべば", "if you learn from it (conditional)", "動詞 (verb)", "N3"),
            T("、"),
            W("心配する", "しんぱいする", "to worry", "動詞 (verb)", "N4"),
            G("ことはない", "ことはない",
              "V plain + ことはない",
              "there's no need to ~; you don't have to ~; it won't happen that ~",
              "ことはない has two uses: "
              "① No need to: 急ぐことはない (No need to rush). "
              "② Won't happen: そんなことはない (That sort of thing won't happen). "
              "More emphatic than なくてもいい.",
              "そんなに焦ることはない。",
              "There's no need to be so impatient."),
            T("。」"),
        ],
    },

    {
        "id": "n3_s43",
        "translation": "\"It's not that you can't do it. Rather, you're already doing quite well.\"",
        "tokens": [
            T("「"),
            W("できない", "できない", "cannot do (negative potential)", "動詞 (verb)", "N5"),
            G("ことはない", "ことはない",
              "V negative plain + ことはない",
              "it's not the case that you can't ~; you can do it (double negative softening)",
              "ことはない after a negative form creates a soft double-negative: 'it's not that you can't'. "
              "This is different from ことはない after positive form (no need to). "
              "Combined: ないことはない = it's not that I can't = I can, but perhaps not enthusiastically.",
              "行けないことはないが、少し遠い。",
              "It's not that I can't go, but it's a bit far."),
            T("。"),
            G("むしろ", "むしろ", "むしろ", "rather; if anything",
              "Introduces a correction or reversal.",
              "むしろ上手いくらいだ。", "If anything, you're quite good."),
            T("、もう"),
            W("十分", "じゅうぶん", "sufficient; enough", "な形容詞 (na-adjective)", "N4"),
            W("やれている", "やれている", "is doing (it); is managing (progressive)", "動詞 (verb)", "N3"),
            T("よ。」"),
        ],
    },

    # ── 第七章: 成長の記録 (Chapter 7: A Record of Growth) ───────────────────

    {
        "id": "n3_s44",
        "translation": "Contrary to his initial anxiety, the work actually suited him quite well.",
        "section": "第七章: 成長の記録 (Chapter 7: A Record of Growth)",
        "tokens": [
            W("最初", "さいしょ", "the beginning; at first", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("不安", "ふあん", "anxiety; worry", "名詞 (noun)", "N4"),
            G("に反して", "にはんして",
              "Noun + に反して",
              "contrary to ~; against ~; in defiance of ~",
              "に反して expresses that something goes against or contradicts the stated thing. "
              "に反する (attributive form) modifies nouns: 予想に反する結果 (a result contrary to expectations). "
              "Formal; often seen in writing.",
              "予想に反して、試験は簡単だった。",
              "Contrary to expectations, the exam was easy."),
            T("、"),
            W("仕事", "しごと", "work", "名詞 (noun)", "N5"),
            P("は", "topic marker"),
            G("かえって", "かえって",
              "かえって",
              "on the contrary; unexpectedly (often a reversal with slightly negative nuance)",
              "かえって marks a result that is the opposite of expected, often with a nuance of 'turned out to be worse/better than expected'. "
              "Similar to むしろ but more often used for unintended reversals. "
              "Example: アドバイスがかえって混乱させた (The advice only made things more confusing).",
              "薬を飲んだが、かえって気分が悪くなった。",
              "I took medicine, but it only made me feel worse."),
            W("自分に合っていた", "じぶんにあっていた", "suited him; fit him (past progressive)", "動詞 (verb)", "N3"),
            T("。"),
        ],
    },

    {
        "id": "n3_s45",
        "translation": "In addition to translation work, he was also given the opportunity to participate in client meetings.",
        "tokens": [
            W("翻訳業務", "ほんやくぎょうむ", "translation work; translation duties", "名詞 (noun)", "N3"),
            G("に加えて", "にくわえて",
              "Noun + に加えて",
              "in addition to ~; on top of ~; besides ~",
              "に加えて adds something on top of what was already stated. "
              "Similar to だけでなく but に加えて is more formal and focuses on additive accumulation. "
              "に加え (without て) is also used in written contexts.",
              "雨に加えて、風も強くなってきた。",
              "In addition to rain, the wind has also picked up."),
            T("、"),
            W("顧客", "こきゃく", "client; customer", "名詞 (noun)", "N3"),
            P("との", "with (と) + attributive (の)"),
            W("会議", "かいぎ", "meeting", "名詞 (noun)", "N4"),
            P("に", "location/event particle"),
            W("参加する", "さんかする", "to participate", "動詞 (verb)", "N4"),
            W("機会", "きかい", "opportunity", "名詞 (noun)", "N4"),
            T("も"),
            W("与えられた", "あたえられた", "was given (passive past)", "動詞 (verb)", "N3"),
            T("。"),
        ],
    },

    {
        "id": "n3_s46",
        "translation": "Since he had taken that chance, he was deeply moved and couldn't help but feel his heart pounding.",
        "tokens": [
            G("せっかく", "せっかく",
              "せっかく",
              "having gone to the trouble of ~; since you have the chance; making the most of ~ (precious opportunity)",
              "せっかく marks an opportunity or effort that the speaker wants to make the most of — or laments wasting. "
              "Positive: せっかく来たんだから、楽しもう (Since we've come all this way, let's enjoy it). "
              "Negative (wasted opportunity): せっかく作ったのに、食べてくれなかった (I went to the trouble of making it, but they didn't eat it).",
              "せっかくの機会だから、精いっぱいやろう。",
              "Since it's such a precious opportunity, let's give it our all."),
            P("の", "possessive particle"),
            W("機会", "きかい", "opportunity", "名詞 (noun)", "N4"),
            T("だから、"),
            W("胸", "むね", "chest; heart", "名詞 (noun)", "N4"),
            P("が", "subject marker"),
            W("どきどきして", "どきどきして", "heart pounding (て-form)", "動詞 (verb)", "N4"),
            G("しょうがなかった", "しょうがなかった",
              "V て-form / Adj stem + てしょうがない (past)",
              "couldn't help it; was so ~ it was overwhelming (past)",
              "てしょうがない expresses an overwhelming or uncontrollable feeling. "
              "Similar to てたまらない, but slightly more casual. "
              "しょうがない alone means 'can't be helped; nothing can be done'. "
              "Combined with て-form: 'so ~ that nothing can be done about it'.",
              "嬉しくてしょうがなかった。",
              "I was so happy I couldn't help it."),
            T("。"),
        ],
    },

    {
        "id": "n3_s47",
        "translation": "He realized this internship was not merely a work experience, but a turning point in his life.",
        "tokens": [
            T("このインターンは"),
            W("ただの", "ただの", "mere; just a", "連体詞 (pre-noun adj.)", "N4"),
            W("職業体験", "しょくぎょうたいけん", "work experience; vocational training", "名詞 (noun)", "N3"),
            G("にすぎない", "にすぎない",
              "Noun / V plain + にすぎない",
              "nothing more than ~; merely ~; only ~ (minimizing)",
              "にすぎない = 'is nothing more than'. Downplays or minimizes the subject. "
              "Often used to correct an overestimation: 'it's just X, nothing more'. "
              "Formal equivalent of ただ～だけだ.",
              "これはただの誤解にすぎない。",
              "This is nothing more than a misunderstanding."),
            T("ではなく、"),
            W("人生", "じんせい", "life; one's life", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("転換点", "てんかんてん", "turning point", "名詞 (noun)", "N3"),
            T("だと"),
            W("気づいた", "きづいた", "realized; noticed (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },

    {
        "id": "n3_s48",
        "translation": "\"Anyway, even if I worry now, the result has already been decided.\" With that in mind, he decided to focus entirely on what was in front of him.",
        "tokens": [
            T("「"),
            G("どうせ", "どうせ",
              "どうせ",
              "anyway; in any case; it's inevitable; since it's going to happen either way",
              "どうせ expresses a sense of resignation or acceptance of the inevitable. "
              "Often implies: 'no matter what I do, the result will be the same, so...'. "
              "Can be pessimistic (どうせ無理だ — it's hopeless anyway) or pragmatic. "
              "Different from せっかく (which values the opportunity); どうせ accepts the situation.",
              "どうせやるなら、楽しくやろう。",
              "Since we're going to do it anyway, let's do it with enthusiasm."),
            T("今から"),
            W("心配", "しんぱい", "worry", "名詞 (noun)", "N4"),
            T("しても、結果はもう"),
            W("決まっている", "きまっている", "has been decided; is already set", "動詞 (verb)", "N4"),
            T("。」そう"),
            W("思い", "おもい", "thought (連用形)", "動詞 (verb)", "N5"),
            T("、"),
            W("目の前", "めのまえ", "right in front of one's eyes", "名詞 (noun)", "N4"),
            P("の", "possessive particle"),
            W("仕事", "しごと", "work", "名詞 (noun)", "N5"),
            P("に", "direction particle"),
            W("集中する", "しゅうちゅうする", "to concentrate; to focus", "動詞 (verb)", "N4"),
            G("ことにした", "ことにした", "V plain + ことにする (past)",
              "decided to ~ (speaker's deliberate choice)",
              "ことにする = make a conscious decision to do something.",
              "早く寝ることにした。", "I decided to go to sleep early."),
            T("。"),
        ],
    },

    # ── 第八章: 帰郷と次への一歩 (Chapter 8: Return Home and the Next Step) ──

    {
        "id": "n3_s49",
        "translation": "The internship couldn't possibly be a failure — he had put his heart into every task.",
        "section": "第八章: 帰郷と次への一歩 (Chapter 8: Return Home and the Next Step)",
        "tokens": [
            T("インターンは"),
            W("失敗", "しっぱい", "failure", "名詞 (noun)", "N4"),
            G("するかねない", "するかねない",
              "V-stem + かねない",
              "might (do something undesirable); there is a risk of ~",
              "かねない expresses that something undesirable could happen if not careful. "
              "Often used as a warning: 'this could lead to ~'. "
              "Contrast: かねる (cannot bring oneself to do — personal reluctance).",
              "そんなことをすると、大きな問題になりかねない。",
              "Doing something like that could well become a big problem."),
            T("状況では"),
            W("なかった", "なかった", "was not; there was not", "助動詞", "N5"),
            T("。"),
            W("すべての", "すべての", "every; all (attributive)", "連体詞", "N4"),
            W("仕事", "しごと", "task; work", "名詞 (noun)", "N5"),
            P("に", "direction particle"),
            W("全力", "ぜんりょく", "full effort; all one's strength", "名詞 (noun)", "N3"),
            P("を", "object particle"),
            W("注いでいた", "そそいでいた", "was pouring into; was devoting (past progressive)", "動詞 (verb)", "N3"),
            T("から。"),
        ],
    },

    {
        "id": "n3_s50",
        "translation": "His dream was steadily coming true. Holding that conviction in his heart, Kenji stepped forward toward the next chapter of his life.",
        "tokens": [
            W("夢", "ゆめ", "dream; aspiration", "名詞 (noun)", "N4"),
            P("は", "topic marker"),
            W("少しずつ", "すこしずつ", "little by little", "副詞 (adverb)", "N4"),
            W("実現し", "じつげんし", "come true; realize (連用形)", "動詞 (verb)", "N4"),
            G("つつある", "つつある", "V-stem + つつある",
              "is in the process of ~ing; is gradually ~ing (literary)",
              "つつある describes a change currently in progress heading toward completion. "
              "More formal and literary than ている. Often for gradual social or personal change.",
              "状況は改善されつつある。",
              "The situation is gradually being improved."),
            T("。"),
            W("そう", "そう", "so; that way", "副詞 (adverb)", "N5"),
            W("確信し", "かくしんし", "be convinced (連用形)", "動詞 (verb)", "N4"),
            G("ながら", "ながら", "V-stem + ながら", "while doing ~",
              "Simultaneous actions.",
              "笑いながら話した。", "I talked while laughing."),
            T("、"),
            N("健二", "けんじ", "Kenji"),
            P("は", "topic marker"),
            W("次の", "つぎの", "the next", "連体詞", "N4"),
            T("ステージへと"),
            W("歩み", "あゆみ", "step; advance (連用形 of 歩む)", "動詞 (verb)", "N4"),
            W("始めた", "はじめた", "began; started (past)", "動詞 (verb)", "N4"),
            T("。"),
        ],
    },
]

# N3 grammar index — all major N3 patterns
N3_GRAMMAR_PATTERNS = [
    # ── Patterns from 第一章 ──────────────────────────────────────────────────
    {"id": "g3_niyoruto",      "pattern": "Noun + によると",              "meaning": "according to ~",                               "level": "N3"},
    {"id": "g3_nimokakarazu",  "pattern": "N/plain + にもかかわらず",     "meaning": "despite ~; in spite of ~",                     "level": "N3"},
    {"id": "g3_nitotte",       "pattern": "Noun + にとって",              "meaning": "for ~; from the perspective of ~",             "level": "N3"},
    {"id": "g3_nikurabete",    "pattern": "Noun + に比べて",              "meaning": "compared to ~",                                "level": "N3"},
    {"id": "g3_ba_hodo",       "pattern": "V-ば form + V plain + ほど",   "meaning": "the more ~ the more ~",                        "level": "N3"},
    {"id": "g3_totan",         "pattern": "V past + とたん(に)",           "meaning": "the moment ~; just as ~ happened",             "level": "N3"},
    {"id": "g3_uchini",        "pattern": "V/Adj plain + うちに",         "meaning": "while ~; before the state changes",            "level": "N3"},
    {"id": "g3_kotoninaru",    "pattern": "V plain + ことになる",          "meaning": "it has been decided ~; turns out ~",           "level": "N3"},
    # ── Patterns from 第二章 ──────────────────────────────────────────────────
    {"id": "g3_okagede",       "pattern": "Noun + のおかげで",             "meaning": "thanks to ~ (positive outcome)",               "level": "N3"},
    {"id": "g3_seide",         "pattern": "Noun + のせいで",               "meaning": "because of ~ (negative outcome/blame)",        "level": "N3"},
    {"id": "g3_nitsurete",     "pattern": "V plain / Noun + につれて",     "meaning": "as ~; in proportion to ~ (both change)",       "level": "N3"},
    {"id": "g3_tabini",        "pattern": "V plain / Noun + たびに",      "meaning": "every time ~; whenever ~",                     "level": "N3"},
    {"id": "g3_monono",        "pattern": "Plain form + ものの",           "meaning": "although ~; even though ~ (concession)",       "level": "N3"},
    {"id": "g3_wakegana",      "pattern": "V plain + わけがない",          "meaning": "there's no way ~; it's impossible that ~",     "level": "N3"},
    {"id": "g3_nichigainai",   "pattern": "Plain form + に違いない",       "meaning": "must be ~; certainly ~ (strong conviction)",    "level": "N3"},
    {"id": "g3_wotsujite",     "pattern": "Noun + を通じて / を通して",    "meaning": "through ~; via ~; throughout ~",               "level": "N3"},
    {"id": "g3_nikanshite",    "pattern": "Noun + に関して / に関する",    "meaning": "regarding ~; concerning ~",                    "level": "N3"},
    {"id": "g3_wokkake",       "pattern": "Noun + をきっかけに",           "meaning": "using ~ as a trigger; triggered by ~",         "level": "N3"},
    {"id": "g3_gachi",         "pattern": "V-stem + がちだ / がちな",      "meaning": "tend to ~; apt to ~ (often negative)",         "level": "N3"},
    {"id": "g3_nagara_adv",    "pattern": "V-stem + ながら (adversative)", "meaning": "despite ~; although ~ (contradictory)",        "level": "N3"},
    {"id": "g3_hodo",          "pattern": "V/Adj plain + ほど",           "meaning": "to the extent that ~; so ~ that ~",            "level": "N3"},
    {"id": "g3_karatoitte",    "pattern": "Plain + からといって",          "meaning": "just because ~ (doesn't mean the conclusion)", "level": "N3"},
    {"id": "g3_towakagiranai", "pattern": "Plain + とは限らない",          "meaning": "not necessarily ~; not always ~",              "level": "N3"},
    {"id": "g3_saini",         "pattern": "Noun/V plain + 際に",          "meaning": "when ~; on the occasion of ~ (formal)",        "level": "N3"},
    {"id": "g3_yorimocomp",    "pattern": "Noun + よりも",                 "meaning": "more than ~ (emphatic comparison)",             "level": "N3"},
    {"id": "g3_tsutsuaru",     "pattern": "V-stem + つつある",             "meaning": "is in the process of ~ing; gradually ~ing",    "level": "N3"},
    # ── Patterns from 第四章 ─────────────────────────────────────────────────
    {"id": "g3_kotoninatteiru","pattern": "V plain + ことになっている",    "meaning": "it is supposed to ~; standing rule/arrangement","level": "N3"},
    {"id": "g3_bakaridenaku",  "pattern": "Noun/plain + ばかりでなく",     "meaning": "not only ~ but also ~",                        "level": "N3"},
    {"id": "g3_ippode",        "pattern": "Clause + 一方で",              "meaning": "on the other hand; while ~ (contrast)",         "level": "N3"},
    {"id": "g3_wake_niwa",     "pattern": "V plain + わけにはいかない",    "meaning": "cannot afford to ~; must not ~",               "level": "N3"},
    {"id": "g3_zuni_irarenu",  "pattern": "V-ない stem + ずにはいられない","meaning": "can't help but ~; compelled to ~",             "level": "N3"},
    {"id": "g3_koto_ga_aru",   "pattern": "V past + ことがある",           "meaning": "have had the experience of ~",                 "level": "N3"},
    # ── Patterns from 第五章 ─────────────────────────────────────────────────
    {"id": "g3_sasetemoraeru", "pattern": "V-causative stem + てもらえませんか","meaning": "would it be all right if I ~ (seeking permission humbly)","level": "N3"},
    {"id": "g3_tetamaranai",   "pattern": "V て-form / Adj stem + てたまらない","meaning": "unbearably ~; can't stand being ~",         "level": "N3"},
    {"id": "g3_tashikani_ga",  "pattern": "確かに～が / 確かに～けれど",   "meaning": "it is true that ~, but ~ (concession before contrast)","level": "N3"},
    {"id": "g3_towaienai",     "pattern": "Plain form + とは言えない",     "meaning": "cannot be said to be ~",                       "level": "N3"},
    # ── Patterns from 第六章 ─────────────────────────────────────────────────
    {"id": "g3_nishitewa",     "pattern": "Noun / plain form + にしては",  "meaning": "for ~; considering that ~ (unexpected result)", "level": "N3"},
    {"id": "g3_nakanaka",      "pattern": "なかなか",                       "meaning": "quite; considerably (positive) / not easily (negative)", "level": "N3"},
    {"id": "g3_mushiro",       "pattern": "むしろ",                         "meaning": "rather; if anything (reversal of expectation)", "level": "N3"},
    {"id": "g3_saeba",         "pattern": "Noun + さえ + V-ば / Adj + ければ","meaning": "if only ~; as long as ~ (minimum condition)","level": "N3"},
    {"id": "g3_kotonai_pos",   "pattern": "V plain + ことはない",           "meaning": "no need to ~; it won't happen that ~",         "level": "N3"},
    {"id": "g3_naiko_wa_nai",  "pattern": "V negative plain + ことはない",  "meaning": "it's not that I can't ~; ないことはない",       "level": "N3"},
    # ── Patterns from 第七章 ─────────────────────────────────────────────────
    {"id": "g3_nihante",       "pattern": "Noun + に反して",               "meaning": "contrary to ~; against ~ (defying expectation)","level": "N3"},
    {"id": "g3_kaette",        "pattern": "かえって",                       "meaning": "on the contrary; unexpectedly (reversal, often negative)","level": "N3"},
    {"id": "g3_nikuwaete",     "pattern": "Noun + に加えて",               "meaning": "in addition to ~; on top of ~",                "level": "N3"},
    {"id": "g3_sekkatsu",      "pattern": "せっかく",                       "meaning": "having gone to the trouble of ~; precious opportunity","level": "N3"},
    {"id": "g3_teshouganai",   "pattern": "V て-form / Adj stem + てしょうがない","meaning": "can't help it; so ~ it's overwhelming",  "level": "N3"},
    {"id": "g3_nisuginai",     "pattern": "Noun / V plain + にすぎない",   "meaning": "nothing more than ~; merely ~",                "level": "N3"},
    # ── Patterns from 第八章 ─────────────────────────────────────────────────
    {"id": "g3_douse",         "pattern": "どうせ",                         "meaning": "anyway; in any case; it's inevitable",         "level": "N3"},
    {"id": "g3_kotonikita2",   "pattern": "V plain + ことにする",           "meaning": "decide to ~; make it a rule to ~",             "level": "N3"},
    {"id": "g3_kanenai",       "pattern": "V-stem + かねない",              "meaning": "might (do something bad); there is a risk of ~","level": "N3"},
    {"id": "g3_tatoe_temo",    "pattern": "たとえ + V て-form + も",        "meaning": "even if ~; no matter how ~ (hypothetical)",     "level": "N3"},
]

# ─────────────────────────────────────────────────────────────────────────────
# Final export — both levels
# ─────────────────────────────────────────────────────────────────────────────

PASSAGES = {
    "n4": {
        "id": "n4",
        "title": "夢への道",
        "title_reading": "ゆめへのみち",
        "title_meaning": "The Road to Dreams",
        "level": "N4",
        "description": (
            "Follow Kenji (健二), a university student chasing his dream of becoming a translator. "
            "Covers all N4 grammar patterns, N4/N5 vocabulary, and N5+N4 kanji."
        ),
        "segments": SEGMENTS + SEGMENTS_N4_EXT,
        "grammar_index": GRAMMAR_PATTERNS + N4_EXT_GRAMMAR,
    },
    "n3": {
        "id": "n3",
        "title": "翻訳の夢、現実へ",
        "title_reading": "ほんやくのゆめ、げんじつへ",
        "title_meaning": "The Translation Dream, Into Reality",
        "level": "N3",
        "description": (
            "One year later — Kenji is now a final-year student landing an internship at a translation company. "
            "Covers all major N3 grammar patterns with N3/N4 vocabulary and kanji."
        ),
        "segments": N3_SEGMENTS,
        "grammar_index": N3_GRAMMAR_PATTERNS,
    },
}
