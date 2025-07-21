
import streamlit as st
import random
words = [
    "aftermath", "also-ran", "amenable", "aptitude", "askew", "aspire", "castigate", "circa",
    "comprise", "dispel", "divine", "domain", "dormant", "edifice", "egalitarian", "embellish",
    "embody", "emit", "endure", "evade", "exhume", "expunge", "facilitate", "fathom", "feign",
    "fickle", "fortuitous", "husbandry", "idiosyncrasy", "impede", "irascible", "legacy", "lieu",
    "loiter", "maim", "muse", "nepotism", "lithe", "mawkish", "frank", "diatribe", "appease",
    "camaraderie", "paragon", "ebullience", "sublime", "opaque", "serene", "batter", "bevy", "crony",
    "quaff", "quail", "bandy", "demise", "acme", "crux", "brink", "abhor", "appalling", "raze",
    "raucous", "placate", "penury", "nefarious", "morose", "intimidate", "insularity", "innocuous",
    "incongruous", "impudence", "gregarious", "garrulous", "emulate", "zealot", "deride",
    "braggart", "affable", "adversity", "elusive", "stolid", "scrutinize", "mogul", "armament",
    "prattle", "booty", "plethora", "exodus", "cascade", "skullduggery", "specter", "pinguid",
    "eloquent", "winnow", "escapade", "dolt", "adherent", "waffle", "onerous", "chide", "cranny",
    "hoard", "masticate", "laudable", "tyro", "vertigo", "supplant", "relay", "adjoining", "dispute",
    "glacial", "fowl", "prolong", "gallant", "courtesy", "lanky", "accumulate", "scenic",
    "meddlesome", "rendezvous", "refuge", "inquisitive", "stout", "prosperity", "reside", "ample",
    "unfurl", "exceptional", "mingled", "voracious", "obese", "don", "plucky", "cupidity", "curtail",
    "animosity", "respite", "garner", "annex", "arduous", "kindle", "capacious", "accolade",
    "assail", "doff", "altercation", "disparage", "petulant", "deduce", "deft", "ostracize",
    "ensemble", "engulf", "dessicate", "denounce", "abstruce", "wither", "truncate", "wane",
    "somber", "rivet", "sundry", "prowess", "plight", "permeate", "precarious", "revere", "forsake",
    "to curb", "rife", "chastise", "tantalize", "surmise", "disperse", "evince"
]

ru_correct = {
    "aftermath":"последствия","also-ran":"неудачник","amenable":"податливый",
    "aptitude":"способность","askew":"криво","aspire":"стремиться","castigate":"наказывать",
    "circa":"примерно","comprise":"включать","dispel":"развеять","divine":"предугадывать",
    "domain":"область","dormant":"спящий","edifice":"здание","egalitarian":"уравнительный",
    "embellish":"приукрашивать","embody":"воплощать","emit":"излучать","endure":"терпеть",
    "evade":"уклоняться","exhume":"откапывать","expunge":"вычеркивать",
    "facilitate":"облегчать","fathom":"постигать","feign":"притворяться",
    "fickle":"непостоянный","fortuitous":"случайный","husbandry":"земледелие",
    "idiosyncrasy":"особенность","impede":"препятствовать","irascible":"вспыльчивый",
    "legacy":"наследие","lieu":"место","loiter":"слоняться","maim":"калечить",
    "muse":"размышлять","nepotism":"кумовство","lithe":"гибкий","mawkish":"слащавый",
    "frank":"откровенный","diatribe":"обличение","appease":"умиротворять",
    "camaraderie":"товарищество","paragon":"образец","ebullience":"оживление",
    "sublime":"возвышенный","opaque":"непрозрачный","serene":"безмятежный",
    "batter":"колотить","bevy":"группа","crony":"дружок","quaff":"питьзалпом",
    "quail":"струсить","bandy":"обмениваться","demise":"кончина","acme":"пик","crux":"суть",
    "brink":"край","abhor":"ненавидеть","appalling":"ужасающий","raze":"сносить",
    "raucous":"резкий","placate":"успокаивать","penury":"нищета","nefarious":"гнусный",
    "morose":"угрюмый","intimidate":"запугивать","insularity":"замкнутость",
    "innocuous":"безвредный","incongruous":"несовместимый","impudence":"наглость",
    "gregarious":"общительный","garrulous":"болтливый","emulate":"подражать",
    "zealot":"фанатик","deride":"высмеивать","braggart":"хвастун","affable":"приветливый",
    "adversity":"невзгоды","elusive":"неуловимый","stolid":"флегматичный",
    "scrutinize":"изучать","mogul":"магнат","armament":"вооружение","prattle":"болтовня",
    "booty":"добыча","plethora":"изобилие","exodus":"массовыйуход","cascade":"водопад",
    "skullduggery":"махинации","specter":"призрак","pinguid":"жирный","eloquent":"красноречивый",
    "winnow":"отсеивать","escapade":"шалость","dolt":"болван","adherent":"сторонник",
    "waffle":"колебаться","onerous":"обременительный","chide":"бранить","cranny":"щель",
    "hoard":"запасать","masticate":"жевать","laudable":"похвальный","tyro":"новичок",
    "vertigo":"головокружение","supplant":"вытеснять","relay":"эстафета","adjoining":"смежный",
    "dispute":"спор","glacial":"ледниковый","fowl":"домптица","prolong":"продлевать",
    "gallant":"храбрый","courtesy":"вежливость","lanky":"долговязый","accumulate":"накапливать",
    "scenic":"живописный","meddlesome":"назойливый","rendezvous":"встреча","refuge":"убежище",
    "inquisitive":"любознательный","stout":"крепкий","prosperity":"процветание",
    "reside":"проживать","ample":"обширный","unfurl":"разворачивать","exceptional":"исключительный",
    "mingled":"смешанный","voracious":"ненасытный","obese":"тучный","don":"надевать",
    "plucky":"смелый","cupidity":"алчность","curtail":"сокращать","animosity":"враждебность",
    "respite":"передышка","garner":"собирать","annex":"присоединять","arduous":"трудный",
    "kindle":"разжигать","capacious":"вместительный","accolade":"похвала","assail":"атаковать",
    "doff":"снимать","altercation":"ссора","disparage":"умалять","petulant":"раздражительный",
    "deduce":"делатьвывод","deft":"ловкий","ostracize":"изгонять","ensemble":"ансамбль",
    "engulf":"поглощать","dessicate":"высушивать","denounce":"осуждать","abstruce":"непонятный",
    "wither":"увядать","truncate":"усекать","wane":"убывать","somber":"мрачный","rivet":"заклепка",
    "sundry":"разный","prowess":"мастерство","plight":"бедственное","permeate":"проникать",
    "precarious":"ненадежный","revere":"почитать","forsake":"покидать","to curb":"сдерживать",
    "rife":"изобилующий","chastise":"суровокричать","tantalize":"дразнить","surmise":"догадка",
    "disperse":"рассеивать","evince":"проявлять"
}

def init_state():
    if 'word_index' not in st.session_state:
        st.session_state.word_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'prev_feedback' not in st.session_state:
        st.session_state.prev_feedback = ""
    if 'quiz_ended' not in st.session_state:
        st.session_state.quiz_ended = False

def make_question():
    word = words[st.session_state.word_index]
    correct = ru_correct[word]
    all_translations = list(ru_correct.values())
    wrongs = [t for t in all_translations if t != correct][:3]
    options = wrongs + [correct]
    options = sorted(options)
    return word, correct, options

def handle_answer(selected, correct):
    if selected == correct:
        st.session_state.score += 1
        st.session_state.prev_feedback = ""
    elif selected == "Не знаю":
        st.session_state.prev_feedback = f"↩️ Предыдущее слово «{words[st.session_state.word_index]}» значит: «{correct}»."
    else:
        st.session_state.prev_feedback = f"✘ Предыдущее слово «{words[st.session_state.word_index]}» — правильный ответ: «{correct}»."

    st.session_state.word_index += 1
    if st.session_state.word_index >= len(words):
        st.session_state.quiz_ended = True

# ==== Streamlit App ====
st.set_page_config(page_title="Викторина по словам", layout="centered")
st.title("🇷🇺 Англо-русский словарный тест")

init_state()

# Manual end
if st.button("❌ Завершить тест"):
    st.session_state.quiz_ended = True

# End screen
if st.session_state.quiz_ended:
    st.success("📝 Тест завершён.")
    st.write(f"✅ Правильных ответов: **{st.session_state.score}** из **{len(words)}**")
    if st.button("🔄 Начать заново"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
    st.stop()

# Show feedback from previous question
if st.session_state.prev_feedback:
    st.info(st.session_state.prev_feedback)

# Show current question
word, correct, options = make_question()
st.markdown(f"**Вопрос {st.session_state.word_index + 1} из {len(words)}**")
st.write(f"Что значит «**{word}**»?")

cols = st.columns(2)
for i, opt in enumerate(options + ["Не знаю"]):
    if cols[i % 2].button(opt, key=f"btn_{st.session_state.word_index}_{i}"):
        handle_answer(opt, correct)
