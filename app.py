import streamlit as st
import random
import difflib

# --- Set page settings ---
st.set_page_config(page_title="Vocabulary Quiz", layout="centered")

# --- Word dictionary: English to Russian ---
translations = {
    "aftermath": "последствие",
    "also-ran": "проигравший",
    "amenable": "податливый",
    "aptitude": "способность",
    "askew": "криво",
    "aspire": "стремиться",
    "castigate": "жестко критиковать",
    "circa": "примерно",
    "comprise": "включать",
    "dispel": "развеять",
    "divine": "предугадывать",
    "domain": "область",
    "dormant": "спящий",
    "edifice": "сооружение",
    "egalitarian": "эгалитарный",
    "embellish": "приукрашивать",
    "embody": "воплощать",
    "emit": "излучать",
    "endure": "выдерживать",
    "evade": "уклоняться",
    "exhume": "эксгумировать",
    "expunge": "вычеркнуть",
    "facilitate": "облегчать",
    "fathom": "постичь",
    "feign": "притворяться",
    "fickle": "непостоянный",
    "fortuitous": "случайный",
    "husbandry": "земледелие",
    "idiosyncrasy": "особенность",
    "impede": "препятствовать",
    "irascible": "вспыльчивый",
    "legacy": "наследие",
    "lieu": "вместо",
    "loiter": "слоняться",
    "maim": "калечить",
    "muse": "размышлять",
    "nepotism": "кумовство",
    "lithe": "гибкий",
    "mawkish": "слащавый",
    "frank": "откровенный",
    "diatribe": "резкая речь",
    "appease": "умиротворять",
    "camaraderie": "товарищество",
    "paragon": "образец",
    "ebullience": "энтузиазм",
    "sublime": "возвышенный",
    "opaque": "непрозрачный",
    "serene": "безмятежный",
    "batter": "избивать",
    "bevy": "толпа",
    "crony": "приятель",
    "quaff": "пить залпом",
    "quail": "струсить",
    "bandy": "обмениваться (словами)",
    "demise": "кончина",
    "acme": "апогей",
    "crux": "суть",
    "brink": "край",
    "abhor": "ненавидеть",
    "appalling": "ужасающий",
    "raze": "сносить",
    "raucous": "шумный",
    "placate": "успокаивать",
    "penury": "нищета",
    "nefarious": "гнусный",
    "morose": "угрюмый",
    "intimidate": "запугивать",
    "insularity": "замкнутость",
    "innocuous": "безобидный",
    "incongruous": "несоответствующий",
    "impudence": "наглость",
    "gregarious": "общительный",
    "garrulous": "болтливый",
    "emulate": "подражать",
    "zealot": "фанатик",
    "deride": "высмеивать",
    "braggart": "хвастун",
    "affable": "приветливый",
    "adversity": "бедствия",
    "elusive": "неуловимый",
    "stolid": "флегматичный",
    "scrutinize": "тщательно изучать",
    "mogul": "магнат",
    "armament": "вооружение",
    "prattle": "лепетать",
    "booty": "добыча",
    "plethora": "изобилие",
    "exodus": "массовый исход",
    "cascade": "каскад",
    "skullduggery": "жульничество",
    "specter": "призрак",
    "pinguid": "жирный",
    "eloquent": "красноречивый",
    "winnow": "отсеивать",
    "escapade": "шалость",
    "dolt": "простофиля",
    "adherent": "сторонник",
    "waffle": "болтовня",
    "onerous": "обременительный",
    "chide": "бранить",
    "cranny": "щель",
    "hoard": "копить",
    "masticate": "жевать",
    "laudable": "похвальный",
    "tyro": "новичок",
    "vertigo": "головокружение",
    "supplant": "вытеснять",
    "relay": "передавать",
    "adjoining": "прилегающий",
    "dispute": "спор",
    "glacial": "ледяной",
    "fowl": "домашняя птица",
    "prolong": "продлить",
    "gallant": "храбрый",
    "courtesy": "вежливость",
    "lanky": "долговязый",
    "accumulate": "накапливать",
    "scenic": "живописный",
    "meddlesome": "назойливый",
    "rendezvous": "встреча",
    "refuge": "убежище",
    "inquisitive": "любопытный",
    "stout": "крепкий",
    "prosperity": "процветание",
    "reside": "проживать",
    "ample": "обильный",
    "unfurl": "разворачивать",
    "exceptional": "исключительный",
    "mingled": "смешанный",
    "voracious": "прожорливый",
    "obese": "ожиревший",
    "don": "надевать",
    "plucky": "отважный",
    "cupidity": "алчность",
    "curtail": "сокращать",
    "animosity": "враждебность",
    "respite": "передышка",
    "garner": "собирать",
    "annex": "присоединять",
    "arduous": "тяжелый",
    "kindle": "разжигать",
    "capacious": "вместительный",
    "accolade": "похвала",
    "assail": "атаковать",
    "doff": "снять (одежду)",
    "altercation": "ссора",
    "disparage": "принижать",
    "petulant": "раздражительный",
    "deduce": "делать вывод",
    "deft": "ловкий",
    "ostracize": "изгонять",
    "ensemble": "ансамбль",
    "engulf": "поглощать",
    "desiccate": "высушивать",
    "denounce": "осуждать",
    "abstruse": "заумный",
    "wither": "увядать",
    "truncate": "усекать",
    "wane": "убывать",
    "somber": "мрачный",
    "rivet": "заклепка",
    "sundry": "различный",
    "prowess": "мастерство",
    "plight": "тяжелое положение",
    "permeate": "проникать",
    "precarious": "ненадежный",
    "revere": "почитать",
    "forsake": "покидать",
    "curb": "сдерживать",
    "rife": "распространенный",
    "chastise": "наказывать",
    "tantalize": "дразнить",
    "surmise": "догадываться",
    "disperse": "рассеивать",
    "evince": "проявлять",
}

# --- Functions ---
def get_options(correct_word, correct_answer):
    distractors = random.sample([v for k, v in translations.items() if k != correct_word], 3)
    options = distractors + [correct_answer]
    random.shuffle(options)
    return options

def is_similar(user_input, correct_answer):
    ratio = difflib.SequenceMatcher(None, user_input.lower(), correct_answer.lower()).ratio()
    return ratio >= 0.8

# --- Session state ---
if "mastered" not in st.session_state:
    st.session_state.mastered = set()
if "current_word" not in st.session_state:
    st.session_state.current_word, st.session_state.correct_answer = random.choice(list(translations.items()))
    st.session_state.options = get_options(st.session_state.current_word, st.session_state.correct_answer)
    st.session_state.answered = False

# --- Title ---
st.title("📚 Vocabulary Quiz (EN ➜ RU)")

# --- Quiz content ---
st.write(f"**What does '{st.session_state.current_word}' mean?**")

for i, opt in enumerate(st.session_state.options, 1):
    if st.button(f"{i}) {opt}"):
        if opt == st.session_state.correct_answer:
            st.success("✅ Correct!")
            st.session_state.mastered.add(st.session_state.current_word)
        else:
            st.error(f"❌ Wrong! Correct answer: {st.session_state.correct_answer}")
            st.session_state.mastered.clear()
        st.session_state.answered = True

# --- Next question button ---
if st.session_state.answered:
    if len(st.session_state.mastered) == len(translations):
        st.balloons()
        st.success("🎉 You mastered all the words!")
    elif st.button("➡ Next Word"):
        remaining = [w for w in translations if w not in st.session_state.mastered]
        new_word = random.choice(remaining)
        st.session_state.current_word = new_word
        st.session_state.correct_answer = translations[new_word]
        st.session_state.options = get_options(new_word, translations[new_word])
        st.session_state.answered = False
