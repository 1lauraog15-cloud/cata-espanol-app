import random
import textwrap
import json
from typing import Dict, List, Optional
import streamlit as st

from data import (
    DATA, DOUBLE_PREP, GAP_EXERCISES, ERROR_EXERCISES,
    CONECTORES, GAP_EJERCICIOS, CLASIFICACION_EJERCICIOS, TEXTOS_ORDEN,
    GR_SUBJUNTIVO, GR_PERIFRASIS, GR_SER_ESTAR, GR_PRONOMBRES,
    GR_ERRORES_INGLES, GR_LECTURA,
)

PREPS = ["de", "a", "con", "en", "por", "sobre", "contra", "ante", "entre", "hacia", "tras"]
CATEGORY_LABELS = {
    "de": "Verbos + DE",
    "a": "Verbos + A",
    "con": "Verbos + CON",
    "en": "Verbos + EN",
    "por": "Verbos + POR",
    "sobre": "Verbos + SOBRE",
    "contra": "Verbos + CONTRA",
    "ante": "Verbos + ANTE",
    "entre": "Verbos + ENTRE",
    "hacia": "Verbos + HACIA",
    "tras": "Verbos + TRAS",
}

NIVEL_COLORS = {"B2": "#3b82f6", "C1": "#8b5cf6", "C2": "#ef4444"}

# Mapa automático: verbo_base → [todas las preps válidas en DATA]
_VERB_TO_PREPS: Dict[str, List[str]] = {}
for _prep, _items in DATA.items():
    for _it in _items:
        _VERB_TO_PREPS.setdefault(_it["verbo"], [])
        if _prep not in _VERB_TO_PREPS[_it["verbo"]]:
            _VERB_TO_PREPS[_it["verbo"]].append(_prep)


FUNCIONES_CONECTORES = list(dict.fromkeys(c["funcion"] for c in CONECTORES))

# ─────────────────────────────────────────────
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────


# ─────────────────────────────────────────────
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="EspañolPro · C1 / C2",
    page_icon="🇪🇸",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    /* ── Fonts ─────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,500&family=DM+Sans:wght@300;400;500;600&display=swap');

    /* ── Design tokens ──────────────────────────────────── */
    :root {
        --bg:           #f7f3ed;
        --bg-card:      #ffffff;
        --txt:          #1c1007;
        --txt2:         #7a6e60;
        --border:       #e4ddd3;
        --red:          #b5432a;
        --red-soft:     #faeee9;
        --gold:         #c07a18;
        --gold-soft:    #fdf3dc;
        --green:        #2e6b47;
        --green-soft:   #e6f4ee;
        --navy:         #1e3a5f;
        --navy-soft:    #e6ecf5;
        --purple:       #5b3a9e;
        --purple-soft:  #ede8f8;
        --amber:        #b45309;
        --amber-soft:   #fef3c7;
        --shadow:       0 2px 14px rgba(28,16,7,.07);
        --shadow-lg:    0 8px 32px rgba(28,16,7,.10);
        --r:            14px;
        --r-lg:         20px;
    }

    /* ── Base ───────────────────────────────────────────── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background: var(--bg);
        color: var(--txt);
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2.5rem;
        max-width: 1320px;
    }

    /* ── Sidebar ────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: #fff !important;
        border-right: 1px solid var(--border) !important;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0 !important;
    }

    /* ── Brand block ─────────────────────────────────────── */
    .brand {
        padding: 1.4rem 1.2rem 1rem;
        border-bottom: 1px solid var(--border);
        margin-bottom: 0.4rem;
    }
    .brand-name {
        font-family: 'Fraunces', serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: var(--txt);
        letter-spacing: -0.02em;
        line-height: 1;
    }
    .brand-tagline {
        font-size: 0.76rem;
        color: var(--txt2);
        margin-top: 0.25rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    /* ── Nav sections ────────────────────────────────────── */
    .nav-section {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.10em;
        text-transform: uppercase;
        color: var(--txt2);
        padding: 0.9rem 1.2rem 0.3rem;
    }
    .nav-item {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.55rem 1.2rem;
        margin: 0.05rem 0.5rem;
        border-radius: 10px;
        font-size: 0.88rem;
        font-weight: 500;
        color: var(--txt);
        cursor: pointer;
        transition: background 0.12s;
        text-decoration: none;
    }
    .nav-item:hover { background: var(--bg); }
    .nav-item.active {
        background: var(--red-soft);
        color: var(--red);
        font-weight: 600;
    }
    .nav-item .ni-icon { font-size: 1rem; width: 1.3rem; text-align: center; }
    .nav-divider { height: 1px; background: var(--border); margin: 0.6rem 1.2rem; }

    /* ── Module header ───────────────────────────────────── */
    .mod-header {
        border-radius: var(--r-lg);
        padding: 1.4rem 1.8rem;
        margin-bottom: 1.4rem;
        display: flex;
        align-items: center;
        gap: 1.2rem;
    }
    .mod-header-icon {
        font-size: 2.4rem;
        line-height: 1;
    }
    .mod-header-text h2 {
        font-family: 'Fraunces', serif;
        font-size: 1.6rem;
        font-weight: 700;
        margin: 0 0 0.2rem;
        line-height: 1.1;
    }
    .mod-header-text p {
        margin: 0;
        font-size: 0.88rem;
        opacity: 0.8;
    }

    /* ── Home cards ──────────────────────────────────────── */
    .home-hero {
        background: linear-gradient(135deg, var(--txt) 0%, #2d1a0a 100%);
        border-radius: var(--r-lg);
        padding: 2.4rem 2rem;
        margin-bottom: 2rem;
        color: white;
        position: relative;
        overflow: hidden;
    }
    .home-hero::before {
        content: "";
        position: absolute;
        top: -40px; right: -40px;
        width: 220px; height: 220px;
        background: var(--red);
        border-radius: 50%;
        opacity: 0.12;
    }
    .home-hero h1 {
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0 0 0.5rem;
        color: white;
        position: relative;
    }
    .home-hero p {
        margin: 0;
        font-size: 1rem;
        color: rgba(255,255,255,0.72);
        position: relative;
    }
    .home-hero .stat-row {
        display: flex;
        gap: 2rem;
        margin-top: 1.4rem;
        position: relative;
    }
    .home-stat { text-align: left; }
    .home-stat-n {
        font-family: 'Fraunces', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        line-height: 1;
    }
    .home-stat-l {
        font-size: 0.78rem;
        color: rgba(255,255,255,0.6);
        margin-top: 0.1rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .module-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--r);
        padding: 1.2rem;
        transition: box-shadow 0.15s, transform 0.15s;
        height: 100%;
        cursor: pointer;
        box-shadow: var(--shadow);
    }
    .module-card:hover {
        box-shadow: var(--shadow-lg);
        transform: translateY(-2px);
    }
    .mc-top {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.7rem;
    }
    .mc-icon {
        font-size: 1.4rem;
        width: 2.4rem;
        height: 2.4rem;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }
    .mc-title {
        font-family: 'Fraunces', serif;
        font-size: 1rem;
        font-weight: 700;
        color: var(--txt);
        line-height: 1.2;
    }
    .mc-desc {
        font-size: 0.82rem;
        color: var(--txt2);
        line-height: 1.5;
        margin-bottom: 0.8rem;
    }
    .mc-badge {
        display: inline-block;
        font-size: 0.74rem;
        font-weight: 600;
        border-radius: 999px;
        padding: 0.2rem 0.6rem;
    }

    /* ── Metric cards ────────────────────────────────────── */
    .metric-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--r);
        padding: 0.9rem 1rem;
        text-align: center;
        box-shadow: var(--shadow);
    }
    .metric-value {
        font-family: 'Fraunces', serif;
        font-size: 1.7rem;
        font-weight: 700;
        color: var(--txt);
        line-height: 1;
    }
    .metric-label {
        font-size: 0.78rem;
        color: var(--txt2);
        margin-top: 0.25rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    /* ── Cards & quiz boxes ──────────────────────────────── */
    .card-box, .quiz-box {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--r);
        padding: 1.3rem;
        box-shadow: var(--shadow);
        margin-bottom: 0.6rem;
    }
    .card-chip {
        display: inline-block;
        background: var(--purple-soft);
        color: var(--purple);
        border-radius: 999px;
        padding: 0.25rem 0.7rem;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 0.7rem;
    }
    .nivel-badge {
        display: inline-block;
        border-radius: 999px;
        padding: 0.18rem 0.55rem;
        font-size: 0.74rem;
        font-weight: 700;
        color: white;
        margin-left: 0.4rem;
    }
    .card-title {
        font-family: 'Fraunces', serif;
        color: var(--navy);
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.55rem;
        line-height: 1.2;
    }
    .card-line { color: var(--txt); margin-bottom: 0.4rem; font-size: 0.95rem; }
    .section-title {
        font-family: 'Fraunces', serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--txt);
        margin-bottom: 0.2rem;
    }
    .section-sub { color: var(--txt2); margin-bottom: 0.8rem; font-size: 0.87rem; }

    /* ── Example / nota blocks ───────────────────────────── */
    .example-block {
        background: var(--navy-soft);
        border-left: 3px solid var(--navy);
        border-radius: 0 10px 10px 0;
        padding: 0.5rem 0.85rem;
        margin: 0.3rem 0;
        font-style: italic;
        color: var(--navy);
        font-size: 0.91rem;
    }
    .nota-box {
        background: var(--amber-soft);
        border: 1px solid #fcd34d;
        border-radius: 10px;
        padding: 0.5rem 0.85rem;
        font-size: 0.85rem;
        color: var(--amber);
        margin-top: 0.6rem;
    }

    /* ── Feedback ────────────────────────────────────────── */
    .feedback-ok {
        background: var(--green-soft);
        border-left: 4px solid var(--green);
        color: var(--green);
        padding: 0.85rem 1rem;
        border-radius: 0 var(--r) var(--r) 0;
        margin-top: 0.75rem;
        white-space: pre-wrap;
        font-size: 0.92rem;
    }
    .feedback-bad {
        background: var(--red-soft);
        border-left: 4px solid var(--red);
        color: var(--red);
        padding: 0.85rem 1rem;
        border-radius: 0 var(--r) var(--r) 0;
        margin-top: 0.75rem;
        white-space: pre-wrap;
        font-size: 0.92rem;
    }
    .feedback-neutral {
        background: var(--bg);
        border-left: 4px solid var(--border);
        color: var(--txt);
        padding: 0.85rem 1rem;
        border-radius: 0 var(--r) var(--r) 0;
        margin-top: 0.75rem;
        white-space: pre-wrap;
        font-size: 0.92rem;
    }
    .feedback-ai {
        background: var(--gold-soft);
        border-left: 4px solid var(--gold);
        color: var(--amber);
        padding: 0.85rem 1rem;
        border-radius: 0 var(--r) var(--r) 0;
        margin-top: 0.75rem;
        white-space: pre-wrap;
        font-size: 0.92rem;
    }

    /* ── Doble prep cards ────────────────────────────────── */
    .double-prep-card {
        background: var(--gold-soft);
        border: 1px solid #fde68a;
        border-radius: var(--r);
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .dp-verb { font-family: 'Fraunces', serif; font-size: 1.05rem; color: var(--amber); font-weight: 700; }
    .dp-row { margin: 0.4rem 0; }
    .dp-prep { display: inline-block; background: var(--amber-soft); color: var(--amber); border-radius: 6px; padding: 0.12rem 0.4rem; font-weight: 700; font-size: 0.85rem; }
    .dp-sig { color: var(--txt); font-size: 0.88rem; }
    .dp-ex { color: var(--amber); font-style: italic; font-size: 0.85rem; margin-top: 0.1rem; }
    .weak-tag { background: var(--red-soft); color: var(--red); border-radius: 6px; padding: 0.12rem 0.5rem; font-size: 0.76rem; font-weight: 700; }

    /* ── Conectores ──────────────────────────────────────── */
    .con-card-chip {
        display: inline-block;
        background: var(--gold-soft);
        color: var(--amber);
        border-radius: 999px;
        padding: 0.25rem 0.7rem;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 0.7rem;
    }
    .con-card-title {
        font-family: 'Fraunces', serif;
        color: var(--amber);
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.55rem;
    }
    .con-example-block {
        background: var(--gold-soft);
        border-left: 3px solid var(--gold);
        border-radius: 0 10px 10px 0;
        padding: 0.5rem 0.85rem;
        margin: 0.3rem 0;
        font-style: italic;
        color: var(--amber);
        font-size: 0.91rem;
    }

    /* ── Streamlit overrides ─────────────────────────────── */
    /* Sidebar nav buttons — clean, no border */
    [data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: none !important;
        border-radius: 8px !important;
        text-align: left !important;
        justify-content: flex-start !important;
        padding: 0.42rem 0.8rem !important;
        font-size: 0.87rem !important;
        font-weight: 400 !important;
        color: var(--txt) !important;
        box-shadow: none !important;
        margin: 1px 0 !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background: var(--bg) !important;
        color: var(--txt) !important;
        border: none !important;
    }
    /* Main content area buttons — keep bordered */
    .block-container .stButton > button {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        color: var(--txt) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.88rem !important;
        transition: all 0.12s !important;
        padding: 0.45rem 1rem !important;
    }
    .block-container .stButton > button:hover {
        background: var(--bg) !important;
        border-color: var(--txt2) !important;
    }
    div[data-testid="stTabs"] button {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
    }
    .stRadio label { font-size: 0.88rem !important; }
    .stSelectbox label, .stMultiSelect label {
        font-size: 0.82rem !important;
        color: var(--txt2) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    .stProgress > div > div {
        background: var(--red) !important;
        border-radius: 999px !important;
    }
    .stProgress { border-radius: 999px !important; }

    /* ── Module badge (for home cards) ──────────────────── */
    .module-badge {
        display: inline-block;
        border-radius: 10px;
        padding: 0.4rem 1rem;
        font-weight: 700;
        font-size: 0.9rem;
        margin-right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)



# ─────────────────────────────────────────────
#  FUNCIONES — VERBOS
# ─────────────────────────────────────────────

def init_state() -> None:
    all_items: List[Dict] = []
    for prep, items in DATA.items():
        for item in items:
            enriched = dict(item)
            enriched["prep"] = prep
            all_items.append(enriched)

    defaults = {
        "all_items": all_items,
        "filtered_items": list(all_items),
        "current_card_index": 0,
        "quiz_score": 0,
        "quiz_total": 0,
        "quiz_streak": 0,
        "feedback": ("neutral", "Elige categorías y empieza a practicar ✨"),
        "quiz_data": None,
        "study_mode": "Elegir preposición",
        "weak_items": {},
        "gap_index": None,
        "gap_feedback": None,
        "error_index": None,
        "error_feedback": None,
        "ai_feedback": None,
        "dp_index": 0,
        "dp_revealed": False,
        "dp_quiz_ans": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def normalize(text: str) -> str:
    return " ".join(text.lower().strip().split())


def safe_idx(key: str, pool: list, default: int = 0) -> int:
    """Devuelve siempre un índice válido para *pool*, reseteando session_state si es necesario.

    Casos que cubre:
    - pool vacío        → devuelve default (0) y escribe default en session_state
    - valor None        → devuelve 0 % len(pool), lo escribe en session_state
    - valor fuera de rango (level change reduce el pool) → clamp con módulo
    - valor ya válido   → lo devuelve tal cual sin tocar session_state
    """
    if not pool:
        st.session_state[key] = default
        return default
    val = st.session_state.get(key, default)
    if not isinstance(val, int):
        val = default
    val = val % len(pool)
    st.session_state[key] = val
    return val


def active_items(selected_preps: List[str]):
    base = [i for i in st.session_state.all_items if i["prep"] in selected_preps]
    weighted = []
    for item in base:
        key = item["expresion"]
        fails = st.session_state.weak_items.get(key, 0)
        weighted.append(item)
        if fails >= 2:
            weighted.append(item)
    return base, weighted


def set_feedback(kind: str, message: str):
    st.session_state.feedback = (kind, message)


def show_feedback():
    kind, message = st.session_state.feedback
    css = {"ok": "feedback-ok", "bad": "feedback-bad",
           "neutral": "feedback-neutral", "ai": "feedback-ai"}.get(kind, "feedback-neutral")
    st.markdown(f'<div class="{css}">{message}</div>', unsafe_allow_html=True)


def register_fail(item: Dict):
    key = item["expresion"]
    st.session_state.weak_items[key] = st.session_state.weak_items.get(key, 0) + 1


def register_ok(item: Dict):
    key = item["expresion"]
    if key in st.session_state.weak_items and st.session_state.weak_items[key] > 0:
        st.session_state.weak_items[key] -= 1


def new_quiz_question(items: List[Dict], weighted: List[Dict], mode: str):
    if not items:
        st.session_state.quiz_data = None
        return

    chosen_mode = mode if mode != "Mixto" else random.choice([
        "Elegir preposición", "Completar expresión", "Ejemplo correcto"])

    item = random.choice(weighted if weighted else items)

    if chosen_mode == "Elegir preposición":
        options = PREPS[:]
        random.shuffle(options)
        valid_preps = _VERB_TO_PREPS.get(item["verbo"], [item["prep"]])
        nota_multi = (f"\n\n💡 Este verbo acepta varias preposiciones: {', '.join(valid_preps)}"
                      if len(valid_preps) > 1 else "")
        st.session_state.quiz_data = {
            "type": chosen_mode, "item": item,
            "question": f"¿Qué preposición completa correctamente esta estructura?\n\n**{item['verbo']} + ___**{nota_multi}",
            "answer": valid_preps,
            "options": options,
        }
        return

    if chosen_mode == "Completar expresión":
        ejemplo = random.choice(item["ejemplos"])
        st.session_state.quiz_data = {
            "type": chosen_mode, "item": item,
            "question": f"Escribe la expresión completa (verbo + preposición).\n\n**Contexto:** {ejemplo}",
            "answer": item["expresion"], "options": None,
        }
        return

    wrong_pool = []
    for other in items:
        if other["expresion"] != item["expresion"]:
            wrong_pool.extend(other["ejemplos"])
    wrong_options = random.sample(wrong_pool, k=min(3, len(wrong_pool))) if wrong_pool else []
    correct_option = random.choice(item["ejemplos"])
    options = wrong_options + [correct_option]
    random.shuffle(options)
    st.session_state.quiz_data = {
        "type": chosen_mode, "item": item,
        "question": f"Selecciona el ejemplo que corresponde a:\n\n**{item['expresion']}**",
        "answer": correct_option, "options": options,
    }


def check_answer(user_answer: str):
    quiz = st.session_state.quiz_data
    if not quiz:
        set_feedback("neutral", "No hay pregunta activa.")
        return
    if not user_answer.strip():
        set_feedback("bad", "Escribe o selecciona una respuesta antes de comprobar.")
        return

    answer = quiz["answer"]
    if isinstance(answer, list):
        correct = any(normalize(user_answer) == normalize(a) for a in answer)
        answer_display = " / ".join(f"**{a}**" for a in answer)
    else:
        correct = normalize(user_answer) == normalize(answer)
        answer_display = f"**{answer}**"

    st.session_state.quiz_total += 1

    if correct:
        st.session_state.quiz_score += 1
        st.session_state.quiz_streak += 1
        register_ok(quiz["item"])
        ejemplo = random.choice(quiz["item"]["ejemplos"])
        exp = quiz["item"].get("nota", "")
        nota = f"\n\n💡 {exp}" if exp else ""
        if isinstance(answer, list) and len(answer) > 1:
            otras = [a for a in answer if normalize(a) != normalize(user_answer)]
            if otras:
                nota += f"\n\n✅ También válido: {', '.join(otras)}"
        set_feedback("ok", f"✅ Correcto.\n\nEjemplo: {ejemplo}{nota}")
    else:
        st.session_state.quiz_streak = 0
        register_fail(quiz["item"])
        ejemplo = random.choice(quiz["item"]["ejemplos"])
        exp = quiz["item"].get("nota", "")
        nota = f"\n\n💡 {exp}" if exp else ""
        set_feedback("bad", f"❌ Respuesta correcta: {answer_display}\n\nEjemplo: {ejemplo}{nota}")


async def get_ai_feedback_async(verbo_expr: str, frase_usuario: str) -> str:
    import aiohttp
    payload = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 350,
        "messages": [{"role": "user", "content": (
            f"Eres un profesor de español de nivel C2 experto en gramática. "
            f"El alumno debe escribir una frase usando la expresión '{verbo_expr}'. "
            f"Frase del alumno: «{frase_usuario}»\n\n"
            f"Evalúa brevemente (máximo 4 líneas):\n"
            f"1. ¿Usa correctamente la preposición y la estructura?\n"
            f"2. ¿Es natural y fluida para un hablante nativo?\n"
            f"3. Una sugerencia de mejora si la hay.\n"
            f"Responde SIEMPRE en español, de forma directa y constructiva."
        )}]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.anthropic.com/v1/messages",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=aiohttp.ClientTimeout(total=20)
        ) as resp:
            data = await resp.json()
            return data["content"][0]["text"]


def call_claude_feedback(verbo_expr: str, frase_usuario: str) -> str:
    import asyncio
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                future = pool.submit(asyncio.run, get_ai_feedback_async(verbo_expr, frase_usuario))
                return future.result(timeout=25)
        else:
            return loop.run_until_complete(get_ai_feedback_async(verbo_expr, frase_usuario))
    except Exception as e:
        return f"Error al obtener feedback: {e}"

# ─────────────────────────────────────────────
#  ESTADO CONECTORES
# ─────────────────────────────────────────────

def init_con_state():
    defaults = {
        "con_card_index": 0,
        "cng_idx": None,
        "cng_fb": None,
        "cnc_idx": None,
        "cnc_fb": None,
        "cnc_score": 0,
        "cnc_total": 0,
        "cno_idx": 0,
        "cno_shuf": [],
        "cno_fb": None,
        "cnf_item": None,
        "cnf_fb": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def call_claude_conector(conector: str, frase: str) -> str:
    import asyncio
    async def _call():
        import aiohttp
        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 400,
            "messages": [{"role": "user", "content": (
                f"Eres un profesor de español de nivel C2 experto en discurso y conectores. "
                f"El alumno debe escribir una frase o mini-párrafo usando el conector \'{conector}\'. "
                f"Frase del alumno: «{frase}»\n\n"
                f"Evalúa en máximo 4 líneas:\n"
                f"1. ¿Usa el conector correctamente (función, posición, puntuación, modo verbal si aplica)?\n"
                f"2. ¿El registro y la sintaxis son adecuados para un C2?\n"
                f"3. Una sugerencia concreta de mejora si la hay.\n"
                f"Responde siempre en español, de forma directa y constructiva."
            )}]
        }
        try:
            async with aiohttp.ClientSession() as s:
                async with s.post(
                    "https://api.anthropic.com/v1/messages", json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=aiohttp.ClientTimeout(total=20),
                ) as r:
                    d = await r.json()
                    return d["content"][0]["text"]
        except Exception as e:
            return f"Error al conectar con la IA: {e}"
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                return pool.submit(asyncio.run, _call()).result(timeout=25)
        return loop.run_until_complete(_call())
    except Exception as e:
        return f"Error: {e}"

def show_con_fb(kind: str, msg: str):
    css = {"ok": "feedback-ok", "bad": "feedback-bad",
           "neutral": "feedback-neutral", "ai": "feedback-ai"}.get(kind, "feedback-neutral")
    st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────

init_state()
init_con_state()

# ── Modulo session state ──────────────────────────────────────
if "modulo" not in st.session_state:
    st.session_state.modulo = "🏠 Inicio"

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    # ── Branding ─────────────────────────────────────────
    st.markdown("""
    <div class="brand">
        <div class="brand-name">🇪🇸 EspañolPro</div>
        <div class="brand-tagline">Nivel C1 · C2 · DELE Cervantes</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Nivel (arriba, siempre visible) ──────────────────
    st.markdown('<div class="nav-section" style="padding-top:0.6rem;">NIVEL</div>',
                unsafe_allow_html=True)
    nivel_filter = st.multiselect(
        "nf", ["B2", "C1", "C2"], default=["B2", "C1", "C2"],
        label_visibility="collapsed", key="nivel_global",
    )
    if not nivel_filter:
        nivel_filter = ["B2", "C1", "C2"]

    # Detectar cambio de nivel → resetear índices
    _nivel_sig = tuple(sorted(nivel_filter))
    if st.session_state.get("_prev_nivel") != _nivel_sig:
        for _rk in ["gr_subj_idx", "gr_peri_idx", "gr_se_idx", "gr_pron_idx"]:
            if _rk in st.session_state:
                st.session_state[_rk] = None
        for _rk in ["gr_peri_card", "gr_err_idx", "gr_lect_idx"]:
            if _rk in st.session_state:
                st.session_state[_rk] = 0
        st.session_state._prev_nivel = _nivel_sig

    st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)

    # ── Navegación (un solo elemento por opción) ─────────
    modulo = st.session_state.modulo

    def _nav(key, icon, label):
        if st.session_state.modulo == key:
            st.markdown(
                f'<div style="background:var(--red-soft);color:var(--red);font-weight:600;'
                f'border-radius:8px;padding:0.42rem 0.8rem;font-size:0.87rem;margin:1px 0;">'
                f'{icon}&nbsp; {label}</div>',
                unsafe_allow_html=True)
        else:
            if st.button(f"{icon}  {label}", key=f"nav_{key}", use_container_width=True):
                st.session_state.modulo = key
                st.rerun()

    _nav("🏠 Inicio", "🏠", "Inicio")
    st.markdown('<div class="nav-section">LÉXICO</div>', unsafe_allow_html=True)
    _nav("📗 Verbos + Preposición", "📗", "Verbos + Preposición")
    _nav("🔗 Conectores",           "🔗", "Conectores")
    st.markdown('<div class="nav-section">GRAMÁTICA</div>', unsafe_allow_html=True)
    _nav("🔀 Subjuntivo",           "🔀", "Subjuntivo")
    _nav("⚙️ Perífrasis",           "⚙️", "Perífrasis")
    _nav("🔵🔴 Ser vs Estar",       "🔴", "Ser vs Estar")
    _nav("🔤 Pronombres",           "🔤", "Pronombres")
    st.markdown('<div class="nav-section">PRÁCTICA</div>', unsafe_allow_html=True)
    _nav("🇬🇧 Errores",             "🇬🇧", "Errores")
    _nav("📚 Comprensión lectora",  "📚", "Comprensión lectora")

    # ── Filtros de verbos (solo cuando está activo) ──────
    base_items = []
    weighted_items = []

    if modulo == "📗 Verbos + Preposición":
        st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)

        with st.expander("🔧 Preposiciones", expanded=False):
            selected_preps: List[str] = []
            cols_prep = st.columns(2)
            for j, prep in enumerate(PREPS):
                n = len(DATA.get(prep, []))
                with cols_prep[j % 2]:
                    if st.checkbox(f"{CATEGORY_LABELS[prep]} ({n})",
                                   value=True, key=f"prep_{prep}"):
                        selected_preps.append(prep)

        base_items, weighted_items = active_items(selected_preps)
        st.session_state.filtered_items = base_items
        base_items     = [i for i in base_items     if i.get("nivel", "B2") in nivel_filter]
        weighted_items = [i for i in weighted_items if i.get("nivel", "B2") in nivel_filter]

        mode = st.selectbox(
            "🎯 Tipo de quiz",
            ["Elegir preposición", "Completar expresión", "Ejemplo correcto", "Mixto"],
            index=0,
        )
        st.session_state.study_mode = mode

        n_weak = len([v for v, c in st.session_state.weak_items.items() if c >= 2])
        if n_weak:
            st.markdown(
                f'<span class="weak-tag">⚠️ {n_weak} verbo(s) con ≥2 fallos</span>',
                unsafe_allow_html=True)
            if st.button("Reiniciar repetición espaciada", key="reset_weak"):
                st.session_state.weak_items = {}
                st.rerun()


# ─────────────────────────────────────────────
#  HOME SCREEN
# ─────────────────────────────────────────────
if modulo == "🏠 Inicio":
    st.markdown("""
    <div class="home-hero">
        <h1>Español avanzado.<br>Preparación DELE.</h1>
        <p>Ejercicios de nivel C1 y C2 diseñados para el examen oficial del Instituto Cervantes.</p>
        <div class="stat-row">
            <div class="home-stat">
                <div class="home-stat-n">162</div>
                <div class="home-stat-l">Verbos</div>
            </div>
            <div class="home-stat">
                <div class="home-stat-n">50</div>
                <div class="home-stat-l">Conectores</div>
            </div>
            <div class="home-stat">
                <div class="home-stat-n">8</div>
                <div class="home-stat-l">Módulos</div>
            </div>
            <div class="home-stat">
                <div class="home-stat-n">C1/C2</div>
                <div class="home-stat-l">Nivel DELE</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Module cards grid
    MODULE_CARDS = [
        ("📗 Verbos + Preposición", "📗", "Verbos + Preposición",
         "162 verbos · 11 preposiciones · Repetición espaciada",
         "#2e6b47", "#e6f4ee", "C1/C2"),
        ("🔗 Conectores", "🔗", "Conectores",
         "50 conectores del discurso · Función y matiz",
         "#c07a18", "#fdf3dc", "C1/C2"),
        ("🔀 Subjuntivo", "🔀", "Subjuntivo vs Indicativo",
         "25 contextos de nivel C1 · DELE Cervantes",
         "#5b3a9e", "#ede8f8", "C1"),
        ("⚙️ Perífrasis", "⚙️", "Perífrasis verbales",
         "19 perífrasis · Tarjetas + ejercicios de producción",
         "#1e3a5f", "#e6ecf5", "C1"),
        ("🔵🔴 Ser vs Estar", "🔴", "Ser vs Estar",
         "22 contextos · Adjetivos, eventos y estados",
         "#b5432a", "#faeee9", "B2/C1"),
        ("🔤 Pronombres", "🔤", "Pronombres OD / OI",
         "Combinaciones, posición y usos avanzados",
         "#0e7490", "#e0f2f7", "C1"),
        ("🇬🇧 Errores", "🇬🇧", "Errores anglohablantes",
         "14 errores frecuentes · Falsos amigos · Calcos",
         "#92400e", "#fef3c7", "C1"),
        ("📚 Comprensión lectora", "📚", "Comprensión lectora",
         "3 textos reales al estilo del DELE C1",
         "#1e3a5f", "#e6ecf5", "C1"),
    ]

    rows = [MODULE_CARDS[:4], MODULE_CARDS[4:]]
    for row in rows:
        cols = st.columns(4, gap="medium")
        for col, (key, icon, title, desc, color, bg, nivel) in zip(cols, row):
            with col:
                st.markdown(f"""
                <div class="module-card" style="border-top:3px solid {color};">
                    <div class="mc-top">
                        <div class="mc-icon" style="background:{bg};">{icon}</div>
                        <div class="mc-title">{title}</div>
                    </div>
                    <div class="mc-desc">{desc}</div>
                    <span class="mc-badge" style="background:{bg};color:{color};">{nivel}</span>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Ir →", key=f"home_go_{key}", use_container_width=True):
                    st.session_state.modulo = key
                    st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  RENDER SEGÚN MÓDULO
# ─────────────────────────────────────────────

if modulo == "📗 Verbos + Preposición":


    st.markdown(f"""
    <div class="mod-header" style="background:#e6f4ee;">
        <div class="mod-header-icon">📗</div>
        <div class="mod-header-text" style="color:#2e6b47;">
            <h2>Verbos + Preposición</h2>
            <p>162 verbos · 11 preposiciones · Repetición espaciada</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    items = base_items

    if not items:
        st.warning("Activa al menos una categoría y nivel para empezar.")
        st.stop()

    safe_idx("current_card_index", items)

    progress_ratio = st.session_state.quiz_score / st.session_state.quiz_total if st.session_state.quiz_total else 0.0
    m1, m2, m3, m4, m5 = st.columns(5)
    for col, val, label in [
        (m1, len(items), "verbos activos"),
        (m2, st.session_state.quiz_score, "aciertos"),
        (m3, st.session_state.quiz_total, "intentos"),
        (m4, st.session_state.quiz_streak, "racha"),
        (m5, f"{int(progress_ratio*100)}%", "precisión"),
    ]:
        col.markdown(f'<div class="metric-card"><div class="metric-value">{val}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)
    st.progress(progress_ratio)
    st.markdown("<br>", unsafe_allow_html=True)

    tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Tabla resumen",
        "📚 Tarjetas",
        "🧠 Quiz",
        "✍️ Rellena el hueco",
        "🔍 Detecta el error",
        "🔀 Doble preposición",
    ])
    
    # ────────────────────────────────
    #  TAB 0 — TABLA RESUMEN
    # ────────────────────────────────
    with tab0:
        st.markdown('<div class="section-title">Tabla resumen · Verbos por preposición</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Esquema completo de todos los verbos organizados por preposición. Úsala para estudiar y consultar antes de los ejercicios.</div>', unsafe_allow_html=True)

        _prep_colors = {
            "de":     ("#faeee9", "#b5432a"),
            "a":      ("#e6f4ee", "#2e6b47"),
            "con":    ("#e6ecf5", "#1e3a5f"),
            "en":     ("#ede8f8", "#5b3a9e"),
            "por":    ("#fdf3dc", "#c07a18"),
            "sobre":  ("#e0f2f7", "#0e7490"),
            "contra": ("#fef3c7", "#92400e"),
            "ante":   ("#f0fdf4", "#166534"),
            "entre":  ("#fce7f3", "#831843"),
            "hacia":  ("#f5f3ff", "#3b0764"),
            "tras":   ("#f8fafc", "#374151"),
        }
        _nivel_badge = {"B2": "#3b82f6", "C1": "#8b5cf6", "C2": "#ef4444"}

        for prep, _raw_items in DATA.items():
            # Filter by nivel_filter
            _items_f = [it for it in _raw_items if it.get("nivel", "B2") in nivel_filter]
            if not _items_f:
                continue
            bg, fg = _prep_colors.get(prep, ("#f8fafc", "#374151"))

            # Build rows HTML
            rows = ""
            for it in sorted(_items_f, key=lambda x: x.get("nivel","B2")):
                nc = _nivel_badge.get(it.get("nivel","B2"), "#6b7280")
                rows += (
                    f'<tr>'
                    f'<td style="padding:0.35rem 0.8rem;font-weight:700;color:{fg};">'
                    f'{it["expresion"]}'
                    f'<span style="background:{nc};color:white;border-radius:4px;'
                    f'padding:1px 5px;font-size:0.7rem;font-weight:700;margin-left:0.4rem;">'
                    f'{it.get("nivel","B2")}</span></td>'
                    f'<td style="padding:0.35rem 0.8rem;color:#374151;font-size:0.85rem;">'
                    f'{it["ejemplos"][0]}</td>'
                    f'</tr>'
                )

            st.markdown(f"""
            <div style="margin-bottom:1.4rem;">
              <div style="background:{bg};border-radius:12px 12px 0 0;padding:0.5rem 1rem;
                          font-weight:700;color:{fg};font-size:0.95rem;font-family:'Fraunces',serif;">
                + {prep.upper()}
                <span style="font-family:'DM Sans',sans-serif;font-weight:400;
                             font-size:0.82rem;margin-left:0.5rem;opacity:0.8;">
                  {len(_items_f)} verbo{"s" if len(_items_f)!=1 else ""}</span>
              </div>
              <table style="width:100%;border-collapse:collapse;background:white;
                            border:1px solid #e4ddd3;border-radius:0 0 12px 12px;overflow:hidden;">
                <thead>
                  <tr style="background:#f8fafc;border-bottom:1px solid #e4ddd3;">
                    <th style="padding:0.35rem 0.8rem;text-align:left;color:#7a6e60;
                               font-size:0.75rem;font-weight:600;width:28%;">EXPRESIÓN</th>
                    <th style="padding:0.35rem 0.8rem;text-align:left;color:#7a6e60;
                               font-size:0.75rem;font-weight:600;">EJEMPLO</th>
                  </tr>
                </thead>
                <tbody>{rows}</tbody>
              </table>
            </div>
            """, unsafe_allow_html=True)

    # ────────────────────────────────
    #  TAB 1 — TARJETAS
    # ────────────────────────────────
    with tab1:
        st.markdown('<div class="section-title">Explorador de tarjetas</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Estudia la estructura, preposición y ejemplos de cada verbo.</div>', unsafe_allow_html=True)
    
        current_item = items[st.session_state.current_card_index]
        nivel = current_item.get("nivel", "B2")
        nivel_color = NIVEL_COLORS.get(nivel, "#6b7280")
    
        st.markdown(f"""
        <div class="card-box">
            <div>
                <span class="card-chip">{CATEGORY_LABELS[current_item['prep']]}</span>
                <span class="nivel-badge" style="background:{nivel_color};">{nivel}</span>
            </div>
            <div class="card-title">{current_item['expresion']}</div>
            <div class="card-line"><strong>Verbo base:</strong> {current_item['verbo']}</div>
            <div class="card-line"><strong>Preposición:</strong> {current_item['prep']}</div>
        </div>
        """, unsafe_allow_html=True)
    
        st.markdown("**Ejemplos:**")
        for ej in current_item["ejemplos"]:
            st.markdown(f'<div class="example-block">{ej}</div>', unsafe_allow_html=True)
    
        if "nota" in current_item:
            st.markdown(f'<div class="nota-box">💡 <strong>Nota:</strong> {current_item["nota"]}</div>', unsafe_allow_html=True)
    
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            if st.button("← Anterior", use_container_width=True):
                st.session_state.current_card_index = (st.session_state.current_card_index - 1) % len(items)
                st.rerun()
        with c2:
            if st.button("Siguiente →", use_container_width=True):
                st.session_state.current_card_index = (st.session_state.current_card_index + 1) % len(items)
                st.rerun()
        with c3:
            if st.button("Aleatoria 🎲", use_container_width=True):
                st.session_state.current_card_index = random.randrange(len(items))
                st.rerun()
        with c4:
            if st.button("Mezclar 🔀", use_container_width=True):
                shuffled = items[:]
                random.shuffle(shuffled)
                st.session_state.filtered_items = shuffled
                st.session_state.current_card_index = 0
                st.rerun()
    
        st.caption(f"Tarjeta {st.session_state.current_card_index + 1} de {len(items)}")
    
    # ────────────────────────────────
    #  TAB 2 — QUIZ
    # ────────────────────────────────
    with tab2:
        st.markdown('<div class="section-title">Quiz dinámico</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Los verbos con más fallos aparecen con mayor frecuencia.</div>', unsafe_allow_html=True)
        
        if st.session_state.quiz_data is None:
            new_quiz_question(items, weighted_items, st.session_state.study_mode)
        
        quiz = st.session_state.quiz_data
        if quiz and quiz["item"] in items:
            st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
            st.markdown(quiz["question"])
        
            user_answer = ""
            if quiz["type"] in ["Elegir preposición", "Ejemplo correcto"]:
                display_opts = []
                for opt in quiz["options"]:
                    display_opts.append("\n".join(textwrap.wrap(opt, width=54))
                                       if quiz["type"] == "Ejemplo correcto" else opt)
                sel = st.radio("Selecciona", display_opts, key=f"r_{quiz['question'][:30]}")
                if quiz["type"] == "Ejemplo correcto":
                    user_answer = dict(zip(display_opts, quiz["options"])).get(sel, sel)
                else:
                    user_answer = sel
            else:
                user_answer = st.text_input("Tu respuesta", placeholder="Ej: acordarse de",
                                            key=f"i_{quiz['question'][:30]}")
        
            q1, q2, q3 = st.columns(3)
            with q1:
                if st.button("Comprobar ✓", use_container_width=True):
                    check_answer(user_answer)
                    st.rerun()
            with q2:
                if st.button("Ver solución 👁", use_container_width=True):
                    set_feedback("neutral", f"Solución: {quiz['answer']}\n\nEjemplo: {random.choice(quiz['item']['ejemplos'])}")
                    st.rerun()
            with q3:
                if st.button("Nueva →", use_container_width=True):
                    new_quiz_question(items, weighted_items, st.session_state.study_mode)
                    set_feedback("neutral", "Nueva pregunta cargada.")
                    st.rerun()
        
            if st.button("Reiniciar marcador", use_container_width=True):
                st.session_state.quiz_score = 0
                st.session_state.quiz_total = 0
                st.session_state.quiz_streak = 0
                set_feedback("neutral", "Marcador reiniciado.")
                st.rerun()
        
            show_feedback()
            st.markdown('</div>', unsafe_allow_html=True)
        
    # ────────────────────────────────
    #  TAB 3 — RELLENA EL HUECO
    # ────────────────────────────────
    with tab3:
        st.markdown('<div class="section-title">Rellena el hueco</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Escribe la preposición que falta en cada frase de nivel C1–C2.</div>', unsafe_allow_html=True)
    
        if st.session_state.gap_index is None:
            st.session_state.gap_index = random.randrange(len(GAP_EXERCISES))
    
        gap = GAP_EXERCISES[st.session_state.gap_index]
        frase_display = gap["frase"].replace("___", "**___**")
    
        st.markdown(f'<div class="quiz-box"><p style="font-size:1.05rem;color:#1e1b4b;">{frase_display}</p></div>', unsafe_allow_html=True)
        gap_ans = st.text_input("Preposición:", placeholder="de / a / con / en / por",
                                key=f"gap_{st.session_state.gap_index}")
    
        g1, g2, g3 = st.columns(3)
        with g1:
            if st.button("Comprobar ✓", key="gap_check", use_container_width=True):
                if normalize(gap_ans) == normalize(gap["respuesta"]):
                    st.session_state.gap_feedback = ("ok", f"✅ Correcto: **{gap['respuesta']}**\n\n💡 {gap['explicacion']}")
                else:
                    st.session_state.gap_feedback = ("bad", f"❌ Respuesta correcta: **{gap['respuesta']}**\n\n💡 {gap['explicacion']}")
                st.rerun()
        with g2:
            if st.button("Solución 👁", key="gap_sol", use_container_width=True):
                st.session_state.gap_feedback = ("neutral", f"Preposición: **{gap['respuesta']}**\n\n💡 {gap['explicacion']}")
                st.rerun()
        with g3:
            if st.button("Nueva frase →", key="gap_next", use_container_width=True):
                st.session_state.gap_index = random.randrange(len(GAP_EXERCISES))
                st.session_state.gap_feedback = None
                st.rerun()
    
        if st.session_state.gap_feedback:
            kind, msg = st.session_state.gap_feedback
            css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
            st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)
    
    # ────────────────────────────────
    #  TAB 4 — DETECTA EL ERROR
    # ────────────────────────────────
    with tab4:
        st.markdown('<div class="section-title">Detecta el error</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Cada frase tiene una preposición incorrecta (marcada con *). Escribe la correcta.</div>', unsafe_allow_html=True)
    
        if st.session_state.error_index is None:
            st.session_state.error_index = random.randrange(len(ERROR_EXERCISES))
    
        err = ERROR_EXERCISES[st.session_state.error_index]
        frase_display_err = err["frase_incorrecta"].replace(
            f"*{err['prep_incorrecta']}*",
            f'<span style="background:#fee2e2;color:#991b1b;padding:0 4px;border-radius:4px;font-weight:700;">*{err["prep_incorrecta"]}*</span>'
        )
    
        st.markdown(f'<div class="quiz-box"><p style="font-size:1.05rem;color:#1e1b4b;">{frase_display_err}</p></div>', unsafe_allow_html=True)
        err_ans = st.text_input("Preposición correcta:", placeholder="de / a / con / en / por",
                                key=f"err_{st.session_state.error_index}")
    
        e1, e2, e3 = st.columns(3)
        with e1:
            if st.button("Comprobar ✓", key="err_check", use_container_width=True):
                if normalize(err_ans) == normalize(err["prep_correcta"]):
                    st.session_state.error_feedback = ("ok",
                        f"✅ Correcto: **{err['prep_correcta']}**\n\n"
                        f"Frase corregida: {err['frase_correcta']}\n\n"
                        f"💡 {err['explicacion']}")
                else:
                    st.session_state.error_feedback = ("bad",
                        f"❌ La preposición correcta es: **{err['prep_correcta']}**\n\n"
                        f"Frase corregida: {err['frase_correcta']}\n\n"
                        f"💡 {err['explicacion']}")
                st.rerun()
        with e2:
            if st.button("Solución 👁", key="err_sol", use_container_width=True):
                st.session_state.error_feedback = ("neutral",
                    f"Correcta: **{err['prep_correcta']}**\n\n"
                    f"{err['frase_correcta']}\n\n💡 {err['explicacion']}")
                st.rerun()
        with e3:
            if st.button("Nueva frase →", key="err_next", use_container_width=True):
                st.session_state.error_index = random.randrange(len(ERROR_EXERCISES))
                st.session_state.error_feedback = None
                st.rerun()
    
        if st.session_state.error_feedback:
            kind, msg = st.session_state.error_feedback
            css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
            st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)
    
    # ────────────────────────────────
    #  TAB 5 — DOBLE PREPOSICIÓN (ejercicio interactivo)
    # ────────────────────────────────
    with tab5:
        if "dp_index" not in st.session_state:
            st.session_state.dp_index = 0
        if "dp_revealed" not in st.session_state:
            st.session_state.dp_revealed = False
        if "dp_quiz_ans" not in st.session_state:
            st.session_state.dp_quiz_ans = None
    
        st.markdown('<div class="section-title">Verbos con doble preposición</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Estos verbos cambian de significado según la preposición. Adivina cuántas preposiciones acepta cada uno y qué significa cada combinación.</div>', unsafe_allow_html=True)
    
        dp = DOUBLE_PREP[st.session_state.dp_index]
        preps_str = " / ".join(f"<strong>+{caso['prep']}</strong>" for caso in dp["casos"])
    
        # Tarjeta principal — muestra el verbo y la pista
        st.markdown(f"""
        <div class="card-box" style="text-align:center;padding:2rem 1.5rem;">
            <div class="card-title" style="font-size:2.2rem;margin-bottom:0.5rem;">{dp['verbo']}</div>
            <div style="color:#6b7280;font-size:0.95rem;">
                Este verbo acepta <strong>{len(dp['casos'])}</strong> preposición{"es" if len(dp["casos"])>1 else ""}.
                ¿Sabes cuáles son y qué diferencia de significado hay?
            </div>
        </div>
        """, unsafe_allow_html=True)
    
        st.markdown("")
    
        if not st.session_state.dp_revealed:
            if st.button("👁 Revelar preposiciones y significados", use_container_width=True, key="dp_reveal"):
                st.session_state.dp_revealed = True
                st.rerun()
        else:
            # Mostrar cada caso como tarjeta
            for caso in dp["casos"]:
                st.markdown(f"""
                <div style="background:#f5f3ff;border-left:4px solid #7c3aed;border-radius:0 14px 14px 0;
                            padding:0.9rem 1.2rem;margin-bottom:0.7rem;">
                    <div style="margin-bottom:0.3rem;">
                        <span class="dp-prep" style="font-size:1rem;">+ {caso['prep']}</span>
                        <span style="color:#374151;margin-left:0.5rem;">→ {caso['significado']}</span>
                    </div>
                    <div style="font-style:italic;color:#5b21b6;font-size:0.93rem;">&ldquo;{caso['ejemplo']}&rdquo;</div>
                </div>
                """, unsafe_allow_html=True)
    
            # Mini-quiz: elige qué preposición corresponde a un ejemplo
            st.markdown("---")
            st.markdown("**Mini-quiz:** ¿Con qué preposición se usa en este contexto?")
    
            # Tomar un ejemplo aleatorio de los casos (fijo por índice para no cambiar al rerenderizar)
            caso_quiz = dp["casos"][st.session_state.dp_index % len(dp["casos"])]
            frase_con_hueco = caso_quiz["ejemplo"].replace(
                f" {caso_quiz['prep']} ", " **___** ", 1
            )
            st.markdown(f'<div class="quiz-box"><p style="font-size:1rem;color:#1e1b4b;">{frase_con_hueco}</p></div>', unsafe_allow_html=True)
    
            opciones_dp = [caso["prep"] for caso in dp["casos"]]
            random.shuffle(opciones_dp)
            dp_sel = st.radio("Preposición:", opciones_dp, key=f"dp_radio_{st.session_state.dp_index}", horizontal=True)
    
            dq1, dq2 = st.columns(2)
            with dq1:
                if st.button("Comprobar ✓", key="dp_check", use_container_width=True):
                    if dp_sel == caso_quiz["prep"]:
                        st.session_state.dp_quiz_ans = ("ok", f"✅ Correcto. **+{caso_quiz['prep']}** → {caso_quiz['significado']}")
                    else:
                        correct_caso = next(ca for ca in dp["casos"] if ca["prep"] == caso_quiz["prep"])
                        st.session_state.dp_quiz_ans = ("bad",
                            f"❌ En este contexto es **+{caso_quiz['prep']}** → {correct_caso['significado']}")
                    st.rerun()
            with dq2:
                if st.button("Ver solución 👁", key="dp_sol", use_container_width=True):
                    st.session_state.dp_quiz_ans = ("neutral",
                        f"**+{caso_quiz['prep']}** → {caso_quiz['significado']}")
                    st.rerun()
    
            if st.session_state.dp_quiz_ans:
                kind, msg = st.session_state.dp_quiz_ans
                css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
                st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)
    
        # Navegación
        st.markdown("")
        nav1, nav2, nav3 = st.columns(3)
        with nav1:
            if st.button("← Anterior", use_container_width=True, key="dp_prev"):
                st.session_state.dp_index = (st.session_state.dp_index - 1) % len(DOUBLE_PREP)
                st.session_state.dp_revealed = False
                st.session_state.dp_quiz_ans = None
                st.rerun()
        with nav2:
            st.markdown(f'<p style="text-align:center;color:#6b7280;margin-top:0.6rem;">{st.session_state.dp_index+1} / {len(DOUBLE_PREP)}</p>', unsafe_allow_html=True)
        with nav3:
            if st.button("Siguiente →", use_container_width=True, key="dp_next"):
                st.session_state.dp_index = (st.session_state.dp_index + 1) % len(DOUBLE_PREP)
                st.session_state.dp_revealed = False
                st.session_state.dp_quiz_ans = None
                st.rerun()
    
    
    # ─────────────────────────────────────────────
if modulo == "🔗 Conectores":
    st.markdown("""
    <div class="mod-header" style="background:#fdf3dc;">
        <div class="mod-header-icon">🔗</div>
        <div class="mod-header-text" style="color:#c07a18;">
            <h2>Conectores del discurso</h2>
            <p>50 conectores · Función, matiz y ejercicios · C1 / C2</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    ctab0, ctab1, ctab2, ctab3, ctab4, ctab5, ctab6, ctab7 = st.tabs([
        "📋 Resumen",
        "📖 Tarjetas",
        "🏷️ Clasifica",
        "🧩 Rellena el hueco",
        "📝 Ordena el texto",
        "✍️ Escritura + IA",
        "📊 Referencia",
        "🗒️ Para rellenar",
    ])

    # ══════════════════════════════
    #  TAB 0 — TABLA RESUMEN CONECTORES
    # ══════════════════════════════
    with ctab0:
        st.markdown('<div class="section-title">Tabla resumen · Conectores por función</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Todos los conectores clasificados por función discursiva. Consúltala antes de los ejercicios o cuando escribas un texto.</div>', unsafe_allow_html=True)

        from collections import defaultdict as _dd0
        _grouped0 = _dd0(list)
        _nf0 = nivel_filter if nivel_filter else ["B2","C1","C2"]
        for _c in CONECTORES:
            if _c.get("nivel","C1") in _nf0:
                _grouped0[_c["funcion"]].append(_c)

        _fcolors0 = {
            "Contraste y concesión":       ("#faeee9", "#b5432a"),
            "Causa y origen":              ("#e6ecf5", "#1e3a5f"),
            "Consecuencia y resultado":    ("#e6f4ee", "#2e6b47"),
            "Adición y continuidad":       ("#ede8f8", "#5b3a9e"),
            "Hipótesis y condición":       ("#fce7f3", "#831843"),
            "Estructuración y orden":      ("#e0f2f7", "#0e7490"),
            "Reformulación y aclaración":  ("#f0fdf4", "#166534"),
            "Ejemplificación y digresión": ("#fdf3dc", "#c07a18"),
            "Conclusión y cierre":         ("#f5f3ff", "#3b0764"),
            "Énfasis y afirmación":        ("#fef3c7", "#92400e"),
        }
        _nbadge0 = {"B2": "#3b82f6", "C1": "#8b5cf6", "C2": "#ef4444"}
        _nordre = {"B2": 0, "C1": 1, "C2": 2}

        for funcion, _raw_con in _grouped0.items():
            if not _raw_con:
                continue
            bg0, fg0 = _fcolors0.get(funcion, ("#f8fafc", "#374151"))
            items_s = sorted(_raw_con, key=lambda x: (_nordre.get(x.get("nivel","C1"),1), x["conector"]))

            rows0 = ""
            for it in items_s:
                nc0 = _nbadge0.get(it.get("nivel","C1"), "#6b7280")
                rows0 += (
                    f'<tr>'
                    f'<td style="padding:0.35rem 0.8rem;font-weight:700;color:{fg0};white-space:nowrap;">'
                    f'{it["conector"]}'
                    f'<span style="background:{nc0};color:white;border-radius:4px;'
                    f'padding:1px 5px;font-size:0.7rem;font-weight:700;margin-left:0.4rem;">'
                    f'{it.get("nivel","C1")}</span></td>'
                    f'<td style="padding:0.35rem 0.8rem;color:#374151;font-size:0.85rem;">'
                    f'{it["matiz"]}</td>'
                    f'<td style="padding:0.35rem 0.8rem;color:#7a6e60;font-size:0.82rem;'
                    f'font-style:italic;">{it["ejemplos"][0]}</td>'
                    f'</tr>'
                )

            st.markdown(f"""
            <div style="margin-bottom:1.4rem;">
              <div style="background:{bg0};border-radius:12px 12px 0 0;padding:0.5rem 1rem;
                          font-weight:700;color:{fg0};font-size:0.95rem;font-family:'Fraunces',serif;">
                {funcion}
                <span style="font-family:'DM Sans',sans-serif;font-weight:400;
                             font-size:0.82rem;margin-left:0.5rem;opacity:0.8;">
                  {len(items_s)} conector{"es" if len(items_s)!=1 else ""}</span>
              </div>
              <table style="width:100%;border-collapse:collapse;background:white;
                            border:1px solid #e4ddd3;border-radius:0 0 12px 12px;overflow:hidden;">
                <thead>
                  <tr style="background:#f8fafc;border-bottom:1px solid #e4ddd3;">
                    <th style="padding:0.35rem 0.8rem;text-align:left;color:#7a6e60;
                               font-size:0.75rem;font-weight:600;width:22%;">CONECTOR</th>
                    <th style="padding:0.35rem 0.8rem;text-align:left;color:#7a6e60;
                               font-size:0.75rem;font-weight:600;width:30%;">MATIZ</th>
                    <th style="padding:0.35rem 0.8rem;text-align:left;color:#7a6e60;
                               font-size:0.75rem;font-weight:600;">EJEMPLO</th>
                  </tr>
                </thead>
                <tbody>{rows0}</tbody>
              </table>
            </div>
            """, unsafe_allow_html=True)

    # ══════════════════════════════
    #  TAB 1 — TARJETAS
    # ══════════════════════════════
    with ctab1:
        st.markdown('<div class="section-title">Explorador de conectores</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Estudia función, matiz y ejemplos en contexto real.</div>', unsafe_allow_html=True)

        funcion_sel = st.selectbox(
            "Filtra por categoría:",
            ["Todas"] + FUNCIONES_CONECTORES,
            key="cn_funcion_sel",
        )
        _nivel_f = st.session_state.get("nivel_global", ["B2", "C1", "C2"]) or ["B2", "C1", "C2"]
        lista_base = CONECTORES if funcion_sel == "Todas" else [c for c in CONECTORES if c["funcion"] == funcion_sel]
        lista = [c for c in lista_base if c.get("nivel", "C1") in _nivel_f] or lista_base

        if lista:
            idx = safe_idx("con_card_index", lista)
            con = lista[idx]
            nc = NIVEL_COLORS.get(con.get("nivel", "C1"), "#8b5cf6")

            st.markdown(f"""
            <div class="card-box">
                <div>
                    <span class="con-card-chip">{con['funcion']}</span>
                    <span class="nivel-badge" style="background:{nc};">{con.get('nivel','C1')}</span>
                </div>
                <div class="con-card-title">{con['conector']}</div>
                <div class="card-line"><strong>Matiz:</strong> {con['matiz']}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Ejemplos en contexto:**")
            for ej in con["ejemplos"]:
                st.markdown(f'<div class="con-example-block">{ej}</div>', unsafe_allow_html=True)

            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("← Anterior", use_container_width=True, key="cn_card_prev"):
                    st.session_state.con_card_index = (idx - 1) % len(lista)
                    st.rerun()
            with c2:
                if st.button("Siguiente →", use_container_width=True, key="cn_card_next"):
                    st.session_state.con_card_index = (idx + 1) % len(lista)
                    st.rerun()
            with c3:
                if st.button("Aleatorio 🎲", use_container_width=True, key="cn_card_rand"):
                    st.session_state.con_card_index = random.randrange(len(lista))
                    st.rerun()

            st.caption(f"Conector {idx + 1} de {len(lista)}")

    # ══════════════════════════════
    #  TAB 2 — CLASIFICA EL CONECTOR
    # ══════════════════════════════
    with ctab2:
        st.markdown('<div class="section-title">Clasifica el conector</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Elige la función discursiva de cada conector. Fundamental para usarlos con precisión.</div>', unsafe_allow_html=True)

        if st.session_state.cnc_idx is None:
            st.session_state.cnc_idx = random.randrange(len(CLASIFICACION_EJERCICIOS))

        ej = CLASIFICACION_EJERCICIOS[st.session_state.cnc_idx]

        st.markdown(f"""
        <div class="quiz-box">
            <p style="font-size:1.1rem;color:#374151;">¿Cuál es la función de</p>
            <div class="con-card-title" style="font-size:2rem;margin:0.2rem 0 0.8rem 0;">{ej['conector']}</div>
        </div>
        """, unsafe_allow_html=True)

        opciones_mezcladas = ej["opciones"][:]
        sel = st.radio("Selecciona la función:", opciones_mezcladas,
                       key=f"clas_{st.session_state.cnc_idx}")

        cg1, cg2, cg3 = st.columns(3)
        with cg1:
            if st.button("Comprobar ✓", key="cn_clas_check", use_container_width=True):
                st.session_state.cnc_total += 1
                if sel == ej["correcta"]:
                    st.session_state.cnc_score += 1
                    st.session_state.cnc_fb = ("ok",
                        f"✅ Correcto: **{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                else:
                    st.session_state.cnc_fb = ("bad",
                        f"❌ La función correcta es: **{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                st.rerun()
        with cg2:
            if st.button("Ver solución 👁", key="cn_clas_sol", use_container_width=True):
                st.session_state.cnc_fb = ("neutral",
                    f"**{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                st.rerun()
        with cg3:
            if st.button("Nuevo →", key="cn_clas_next", use_container_width=True):
                st.session_state.cnc_idx = random.randrange(len(CLASIFICACION_EJERCICIOS))
                st.session_state.cnc_fb = None
                st.rerun()

        if st.session_state.cnc_fb:
            show_con_fb(*st.session_state.cnc_fb)

        if st.session_state.cnc_total:
            pct = int(st.session_state.cnc_score / st.session_state.cnc_total * 100)
            st.progress(st.session_state.cnc_score / st.session_state.cnc_total)
            st.caption(f"Precisión: {st.session_state.cnc_score}/{st.session_state.cnc_total} ({pct} %)")
            if st.button("Reiniciar marcador", key="cn_clas_reset"):
                st.session_state.cnc_score = 0
                st.session_state.cnc_total = 0
                st.session_state.cnc_fb = None
                st.rerun()

    # ══════════════════════════════
    #  TAB 3 — RELLENA EL HUECO
    # ══════════════════════════════
    with ctab3:
        st.markdown('<div class="section-title">Rellena el hueco</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Elige el conector más adecuado para cada contexto. Atención a los matices.</div>', unsafe_allow_html=True)

        if st.session_state.cng_idx is None:
            st.session_state.cng_idx = random.randrange(len(GAP_EJERCICIOS))

        gap = GAP_EJERCICIOS[st.session_state.cng_idx]
        nc_gap = NIVEL_COLORS.get(gap.get("nivel", "C1"), "#8b5cf6")

        frase_html = gap["frase"].replace("___",
            '<span style="background:#fef3c7;color:#78350f;padding:2px 10px;border-radius:6px;font-weight:700;">___</span>')
        st.markdown(f'<div class="quiz-box"><p style="font-size:1.05rem;color:#1e1b4b;">{frase_html}</p>'
                    f'<span class="nivel-badge" style="background:{nc_gap};">{gap.get("nivel","C1")}</span></div>',
                    unsafe_allow_html=True)

        gap_sel = st.radio("Elige el conector:", gap["alternativas"],
                           key=f"cn_gap_{st.session_state.cng_idx}")

        gg1, gg2, gg3 = st.columns(3)
        with gg1:
            if st.button("Comprobar ✓", key="cn_gap_check", use_container_width=True):
                validas = gap["respuesta"]
                validas_str = " / ".join(f"**{v}**" for v in validas)
                es_correcta = any(normalize(gap_sel) == normalize(v) for v in validas)
                if es_correcta:
                    otras = [v for v in validas if normalize(v) != normalize(gap_sel)]
                    extra = ("\n\n✅ También válido: " + " / ".join(f"**{v}**" for v in otras)) if otras else ""
                    st.session_state.cng_fb = ("ok",
                        f"✅ Correcto: **{gap_sel}**{extra}\n\n💡 {gap['explicacion']}")
                else:
                    st.session_state.cng_fb = ("bad",
                        f"❌ Opciones válidas: {validas_str}\n\n💡 {gap['explicacion']}")
                st.rerun()
        with gg2:
            if st.button("Ver solución 👁", key="cn_gap_sol", use_container_width=True):
                validas = gap["respuesta"]
                validas_str = " / ".join(f"**{v}**" for v in validas)
                st.session_state.cng_fb = ("neutral",
                    f"Válido(s): {validas_str}\n\n💡 {gap['explicacion']}")
                st.rerun()
        with gg3:
            if st.button("Nueva frase →", key="cn_gap_next", use_container_width=True):
                st.session_state.cng_idx = random.randrange(len(GAP_EJERCICIOS))
                st.session_state.cng_fb = None
                st.rerun()

        if st.session_state.cng_fb:
            show_con_fb(*st.session_state.cng_fb)

    # ══════════════════════════════
    #  TAB 4 — ORDENA EL TEXTO
    # ══════════════════════════════
    with ctab4:
        st.markdown('<div class="section-title">Ordena el texto</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Los conectores son tu brújula. Úsalos para reconstruir la estructura argumentativa.</div>', unsafe_allow_html=True)

        texto = TEXTOS_ORDEN[st.session_state.cno_idx]

        if not st.session_state.cno_shuf:
            shuffled = list(enumerate(texto["partes"]))
            random.shuffle(shuffled)
            st.session_state.cno_shuf = shuffled

        st.markdown(f"**Texto:** *{texto['titulo']}*")
        st.markdown("Conectores clave: " + " · ".join(f"**{c}**" for c in texto["conectores"]))
        st.markdown(f'<div style="background:#fef3c7;border-radius:10px;padding:0.6rem 1rem;color:#78350f;font-size:0.9rem;margin-bottom:0.8rem;">💡 Pista: {texto["pista"]}</div>', unsafe_allow_html=True)

        st.markdown("**Fragmentos (en orden aleatorio):**")
        for i, (_, parte) in enumerate(st.session_state.cno_shuf):
            st.markdown(f'<div class="con-example-block"><strong>{i+1}.</strong> {parte}</div>', unsafe_allow_html=True)

        st.markdown("**Escribe el orden correcto** (ej: `3,1,4,2,5`):")
        order_ans = st.text_input("Tu orden:", key=f"cn_order_{st.session_state.cno_idx}",
                                  placeholder="1,2,3,4,5")

        oo1, oo2, oo3 = st.columns(3)
        with oo1:
            if st.button("Comprobar ✓", key="cn_order_check", use_container_width=True):
                try:
                    user_order = [int(x.strip()) - 1 for x in order_ans.split(",")]
                    orig_indices = [oi for oi, _ in st.session_state.cno_shuf]
                    correct = sorted(range(len(orig_indices)), key=lambda x: orig_indices[x])
                    if user_order == correct:
                        st.session_state.cno_fb = ("ok", "✅ ¡Perfecto! El orden es correcto.")
                    else:
                        correct_str = ",".join(str(x + 1) for x in correct)
                        partes_ord = "\n".join(f"{i+1}. {p}" for i, p in enumerate(texto["partes"]))
                        st.session_state.cno_fb = ("bad",
                            f"❌ El orden correcto es: **{correct_str}**\n\n{partes_ord}")
                except Exception:
                    st.session_state.cno_fb = ("neutral",
                        "⚠️ Escribe los números separados por comas, sin espacios extra.")
                st.rerun()
        with oo2:
            if st.button("Ver solución 👁", key="cn_order_sol", use_container_width=True):
                partes_ord = "\n".join(f"{i+1}. {p}" for i, p in enumerate(texto["partes"]))
                st.session_state.cno_fb = ("neutral", f"Texto ordenado:\n\n{partes_ord}")
                st.rerun()
        with oo3:
            if st.button("Otro texto →", key="cn_order_next", use_container_width=True):
                st.session_state.cno_idx = (st.session_state.cno_idx + 1) % len(TEXTOS_ORDEN)
                st.session_state.cno_shuf = []
                st.session_state.cno_fb = None
                st.rerun()

        if st.session_state.cno_fb:
            show_con_fb(*st.session_state.cno_fb)

    # ══════════════════════════════
    #  TAB 5 — ESCRITURA LIBRE + IA
    # ══════════════════════════════
    with ctab5:
        st.markdown('<div class="section-title">Escritura libre + feedback de IA</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Escribe una frase o mini-párrafo usando el conector propuesto. Claude evaluará función, registro y puntuación.</div>', unsafe_allow_html=True)

        if st.session_state.cnf_item is None:
            st.session_state.cnf_item = random.choice(CONECTORES)

        fc = st.session_state.cnf_item
        nc_fc = NIVEL_COLORS.get(fc.get("nivel", "C1"), "#8b5cf6")

        col_card_f, col_write_f = st.columns([1, 1.2], gap="large")

        with col_card_f:
            st.markdown(f"""
            <div class="card-box">
                <div>
                    <span class="con-card-chip">{fc['funcion']}</span>
                    <span class="nivel-badge" style="background:{nc_fc};">{fc.get('nivel','C1')}</span>
                </div>
                <div class="con-card-title">{fc['conector']}</div>
                <div class="card-line" style="color:#6b7280;font-style:italic;">{fc['matiz']}</div>
                <div style="margin-top:0.8rem;"><strong>Ejemplo:</strong></div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f'<div class="con-example-block">{fc["ejemplos"][0]}</div>', unsafe_allow_html=True)

            if st.button("Cambiar conector 🔄", use_container_width=True, key="cnf_change"):
                st.session_state.cnf_item = random.choice(CONECTORES)
                st.session_state.cnf_fb = None
                st.rerun()

        with col_write_f:
            frase_libre = st.text_area(
                "Tu frase o mini-párrafo:",
                height=120,
                key="cnf_frase",
                placeholder=f"Escribe aquí usando '{fc['conector']}'…",
            )

            if st.button("Pedir feedback a Claude 🤖", use_container_width=True, key="cnf_ai"):
                if frase_libre.strip():
                    with st.spinner("Claude está evaluando tu uso del conector…"):
                        fb = call_claude_conector(fc["conector"], frase_libre.strip())
                    st.session_state.cnf_fb = fb
                else:
                    st.session_state.cnf_fb = "⚠️ Escribe una frase primero."
                st.rerun()

            if st.session_state.cnf_fb:
                st.markdown(
                    f'<div class="feedback-ai">🤖 <strong>Feedback de Claude:</strong>\n\n{st.session_state.cnf_fb}</div>',
                    unsafe_allow_html=True,
                )

    # ══════════════════════════════
    #  TAB 6 — TABLA DE REFERENCIA
    # ══════════════════════════════
    with ctab6:
        st.markdown('<div class="section-title">Tabla de referencia</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Todos los conectores organizados por función. Úsala para estudiar y consultar.</div>', unsafe_allow_html=True)

        from collections import defaultdict as _ddict
        grouped = _ddict(list)
        for c in CONECTORES:
            grouped[c["funcion"]].append(c)

        funcion_colors = {
            "Contraste y concesión":       ("#fef3c7", "#78350f"),
            "Causa y origen":              ("#dbeafe", "#1e3a8a"),
            "Consecuencia y resultado":    ("#dcfce7", "#14532d"),
            "Adición y continuidad":       ("#ede9fe", "#4c1d95"),
            "Hipótesis y condición":       ("#fce7f3", "#831843"),
            "Estructuración y orden":      ("#e0f2fe", "#0c4a6e"),
            "Reformulación y aclaración":  ("#f0fdf4", "#166534"),
            "Ejemplificación y digresión": ("#fff7ed", "#7c2d12"),
            "Conclusión y cierre":         ("#f5f3ff", "#3b0764"),
            "Énfasis y afirmación":        ("#fef9c3", "#713f12"),
        }

        nivel_order = {"B2": 0, "C1": 1, "C2": 2}
        for funcion, items in grouped.items():
            bg, fg = funcion_colors.get(funcion, ("#f8fafc", "#1e293b"))
            items_sorted = sorted(items, key=lambda x: (nivel_order.get(x.get("nivel", "B2"), 1), x["conector"]))

            rows_html = ""
            for item in items_sorted:
                nivel = item.get("nivel", "C1")
                nc = NIVEL_COLORS.get(nivel, "#6b7280")
                rows_html += f"""
                <tr>
                  <td style="padding:0.45rem 0.8rem;font-weight:700;color:{fg};white-space:nowrap;">
                    {item['conector']}
                    <span style="background:{nc};color:white;border-radius:4px;
                                 padding:1px 6px;font-size:0.72rem;font-weight:700;
                                 margin-left:0.4rem;">{nivel}</span>
                  </td>
                  <td style="padding:0.45rem 0.8rem;color:#374151;font-size:0.88rem;">
                    {item['matiz']}
                  </td>
                </tr>"""

            st.markdown(f"""
            <div style="margin-bottom:1.2rem;">
              <div style="background:{bg};border-radius:12px 12px 0 0;
                          padding:0.55rem 1rem;font-weight:700;color:{fg};font-size:0.95rem;">
                {funcion} <span style="font-weight:400;font-size:0.85rem;margin-left:0.5rem;">
                ({len(items)} conectores)</span>
              </div>
              <table style="width:100%;border-collapse:collapse;background:white;
                            border:1px solid #e5e7eb;border-radius:0 0 12px 12px;overflow:hidden;">
                <thead>
                  <tr style="background:#f8fafc;border-bottom:1px solid #e5e7eb;">
                    <th style="padding:0.4rem 0.8rem;text-align:left;color:#6b7280;
                               font-size:0.8rem;font-weight:600;width:30%;">CONECTOR</th>
                    <th style="padding:0.4rem 0.8rem;text-align:left;color:#6b7280;
                               font-size:0.8rem;font-weight:600;">MATIZ / USO</th>
                  </tr>
                </thead>
                <tbody>{rows_html}</tbody>
              </table>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(
            '<div style="color:#6b7280;font-size:0.82rem;margin-top:0.5rem;">' +
            '🔵 B2 &nbsp;|&nbsp; 🟣 C1 &nbsp;|&nbsp; 🔴 C2</div>',
            unsafe_allow_html=True,
        )

    # ══════════════════════════════
    #  TAB 7 — TABLA PARA RELLENAR
    # ══════════════════════════════
    with ctab7:
        st.markdown('<div class="section-title">Tabla para rellenar</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Se muestra la función y el matiz. Escribe el conector que corresponde a cada descripción.</div>', unsafe_allow_html=True)

        if "tabla_ejercicio" not in st.session_state or not st.session_state.tabla_ejercicio:
            ejercicio = [{"conector": c["conector"], "funcion": c["funcion"],
                          "matiz": c["matiz"], "nivel": c.get("nivel", "C1")}
                         for c in CONECTORES]
            random.shuffle(ejercicio)
            st.session_state.tabla_ejercicio = ejercicio
            st.session_state.tabla_checked = False
            st.session_state.tabla_answers = {}

        ejercicio = st.session_state.tabla_ejercicio

        from collections import defaultdict as _dd2
        by_funcion = _dd2(list)
        for i, item in enumerate(ejercicio):
            by_funcion[item["funcion"]].append((i, item))

        funcion_colors2 = {
            "Contraste y concesión":       "#fef3c7",
            "Causa y origen":              "#dbeafe",
            "Consecuencia y resultado":    "#dcfce7",
            "Adición y continuidad":       "#ede9fe",
            "Hipótesis y condición":       "#fce7f3",
            "Estructuración y orden":      "#e0f2fe",
            "Reformulación y aclaración":  "#f0fdf4",
            "Ejemplificación y digresión": "#fff7ed",
            "Conclusión y cierre":         "#f5f3ff",
            "Énfasis y afirmación":        "#fef9c3",
        }

        for funcion, items in by_funcion.items():
            bg = funcion_colors2.get(funcion, "#f8fafc")
            st.markdown(
                f'<div style="background:{bg};border-radius:10px 10px 0 0;padding:0.5rem 1rem;' +
                f'font-weight:700;font-size:0.92rem;color:#1e293b;margin-top:1rem;">' +
                f'{funcion}</div>',
                unsafe_allow_html=True,
            )
            for idx, item in items:
                nivel = item["nivel"]
                nc = NIVEL_COLORS.get(nivel, "#6b7280")
                col_matiz, col_input, col_result = st.columns([3, 1.5, 1.2])

                with col_matiz:
                    st.markdown(
                        f'<div style="padding:0.45rem 0;font-size:0.88rem;color:#374151;">' +
                        f'{item["matiz"]}' +
                        f'<span style="background:{nc};color:white;border-radius:4px;' +
                        f'padding:1px 6px;font-size:0.72rem;font-weight:700;margin-left:0.5rem;">' +
                        f'{nivel}</span></div>',
                        unsafe_allow_html=True,
                    )

                with col_input:
                    val = st.text_input(
                        label="conector",
                        label_visibility="collapsed",
                        placeholder="escribe aquí…",
                        key=f"tabla_inp_{idx}",
                    )
                    st.session_state.tabla_answers[idx] = val

                with col_result:
                    if st.session_state.tabla_checked:
                        user_ans = " ".join(val.lower().strip().split())
                        correct_ans = " ".join(item["conector"].lower().strip().split())
                        if user_ans == correct_ans:
                            st.markdown('<div style="color:#065f46;font-weight:700;padding-top:0.45rem;">✅</div>', unsafe_allow_html=True)
                        elif user_ans:
                            st.markdown(
                                f'<div style="color:#991b1b;font-size:0.82rem;padding-top:0.3rem;">' +
                                f'❌ <strong>{item["conector"]}</strong></div>',
                                unsafe_allow_html=True,
                            )
                        else:
                            st.markdown(
                                f'<div style="color:#6b7280;font-size:0.82rem;padding-top:0.3rem;">' +
                                f'→ <strong>{item["conector"]}</strong></div>',
                                unsafe_allow_html=True,
                            )

        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("Comprobar todo ✓", use_container_width=True, key="tabla_check_btn"):
                st.session_state.tabla_checked = True
                st.rerun()
        with b2:
            if st.button("Ver soluciones 👁", use_container_width=True, key="tabla_sol_btn"):
                st.session_state.tabla_checked = True
                st.session_state.tabla_answers = {}
                st.rerun()
        with b3:
            if st.button("Nueva tabla 🔀", use_container_width=True, key="tabla_new_btn"):
                st.session_state.tabla_ejercicio = []
                st.session_state.tabla_checked = False
                st.session_state.tabla_answers = {}
                st.rerun()

        if st.session_state.tabla_checked:
            answers = st.session_state.tabla_answers
            total = len(ejercicio)
            correct_count = sum(
                1 for i, item in enumerate(ejercicio)
                if " ".join(answers.get(i, "").lower().strip().split()) ==
                   " ".join(item["conector"].lower().strip().split())
            )
            pct = int(correct_count / total * 100) if total else 0
            color = "#065f46" if pct >= 80 else "#92400e" if pct >= 50 else "#991b1b"
            st.markdown(
                f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;' +
                f'padding:0.9rem 1.2rem;margin-top:0.5rem;text-align:center;">' +
                f'<span style="font-size:1.3rem;font-weight:700;color:{color};">{correct_count}/{total}</span>' +
                f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctos ({pct} %)</span>' +
                f'</div>',
                unsafe_allow_html=True,
            )

# ═══════════════════════════════════════════════════════════
#  MÓDULO 3 — GRAMÁTICA C1
# ═══════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════
#  MÓDULOS DE GRAMÁTICA — uno por opción del sidebar
# ═══════════════════════════════════════════════════════════

if modulo == "🔀 Subjuntivo":
    for _k, _v in {
        "gr_subj_idx": None, "gr_subj_fb": None, "gr_subj_score": 0, "gr_subj_total": 0,
        "gr_peri_card": 0, "gr_peri_idx": None, "gr_peri_fb": None, "gr_peri_score": 0, "gr_peri_total": 0,
        "gr_se_idx": None, "gr_se_fb": None, "gr_se_score": 0, "gr_se_total": 0,
        "gr_pron_idx": None, "gr_pron_fb": None, "gr_pron_score": 0, "gr_pron_total": 0,
        "gr_err_idx": 0, "gr_err_revealed": False,
        "gr_lect_idx": 0, "gr_lect_answers": {}, "gr_lect_checked": False,
    }.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    st.markdown('<div class="section-title">Subjuntivo vs Indicativo</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Rellena el hueco con la forma verbal correcta. Los contextos están diseñados al nivel del DELE C1.</div>', unsafe_allow_html=True)

    _pool_subj = [e for e in GR_SUBJUNTIVO if e.get("nivel","C1") in nivel_filter] or GR_SUBJUNTIVO
    ej = _pool_subj[safe_idx("gr_subj_idx", _pool_subj)]
    nc = NIVEL_COLORS.get(ej.get("nivel", "C1"), "#8b5cf6")

    frase_html = ej["frase"].replace("___",
        '<span style="background:#d1fae5;color:#065f46;padding:2px 10px;border-radius:6px;font-weight:700;">___</span>')
    st.markdown(
        f'<div class="quiz-box">'
        f'<span style="display:inline-block;background:#d1fae5;color:#064e3b;border-radius:999px;'
        f'padding:0.25rem 0.7rem;font-size:0.8rem;font-weight:700;margin-bottom:0.6rem;">{ej["tipo"]}</span>'
        f'<span class="nivel-badge" style="background:{nc};">{ej.get("nivel","C1")}</span>'
        f'<p style="font-size:1.05rem;color:#1e1b4b;margin-top:0.6rem;">{frase_html}</p>'
        f'</div>', unsafe_allow_html=True)

    gr_subj_ans = st.text_input("Forma verbal:",
                                 placeholder="Ej: haya terminado / fuera / tenga...",
                                 key=f"gr_subj_{st.session_state.gr_subj_idx}")

    gs1, gs2, gs3 = st.columns(3)
    with gs1:
        if st.button("Comprobar ✓", key="gr_subj_check", use_container_width=True):
            st.session_state.gr_subj_total += 1
            def _norm(t): return " ".join(t.lower().strip().split())
            _validas = [v.strip() for v in ej["respuesta"].split("/")]
            _correcto = any(_norm(gr_subj_ans) == _norm(v) for v in _validas)
            _display = " / ".join(f"**{v}**" for v in _validas)
            if _correcto:
                st.session_state.gr_subj_score += 1
                _otras = [v for v in _validas if _norm(v) != _norm(gr_subj_ans)]
                _extra = (f"\n\n✅ También válido: {chr(39)} / {chr(39).join(_otras)}{chr(39)}" if _otras else "")
                st.session_state.gr_subj_fb = ("ok",
                    f"✅ Correcto: **{gr_subj_ans}**{_extra}\n\n📖 {ej['explicacion']}"
                    + (f"\n\n⚠️ Ojo: {ej['trampa']}" if ej.get('trampa') else ""))
            else:
                st.session_state.gr_subj_fb = ("bad",
                    f"❌ Correcta: {_display}\n\n📖 {ej['explicacion']}"
                    + (f"\n\n⚠️ Ojo: {ej['trampa']}" if ej.get('trampa') else ""))
            st.rerun()
    with gs2:
        if st.button("Ver solución 👁", key="gr_subj_sol", use_container_width=True):
            st.session_state.gr_subj_fb = ("neutral",
                f"**{ej['respuesta']}** — {ej['tipo']}\n\n📖 {ej['explicacion']}"
                + (f"\n\n⚠️ Ojo: {ej['trampa']}" if ej.get('trampa') else ""))
            st.rerun()
    with gs3:
        if st.button("Nueva →", key="gr_subj_next", use_container_width=True):
            st.session_state.gr_subj_idx = random.randrange(len(_pool_subj))
            st.session_state.gr_subj_fb = None
            st.rerun()

    if st.session_state.gr_subj_fb:
        kind, msg = st.session_state.gr_subj_fb
        css = {"ok":"feedback-ok","bad":"feedback-bad","neutral":"feedback-neutral"}[kind]
        st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

    if st.session_state.gr_subj_total:
        pct = int(st.session_state.gr_subj_score / st.session_state.gr_subj_total * 100)
        st.progress(st.session_state.gr_subj_score / st.session_state.gr_subj_total)
        st.caption(f"Precisión: {st.session_state.gr_subj_score}/{st.session_state.gr_subj_total} ({pct} %)")
        if st.button("Reiniciar marcador", key="gr_subj_reset"):
            st.session_state.gr_subj_score = 0
            st.session_state.gr_subj_total = 0
            st.session_state.gr_subj_fb = None
            st.rerun()


if modulo == "⚙️ Perífrasis":
    for _k, _v in {
        "gr_subj_idx": None, "gr_subj_fb": None, "gr_subj_score": 0, "gr_subj_total": 0,
        "gr_peri_card": 0, "gr_peri_idx": None, "gr_peri_fb": None, "gr_peri_score": 0, "gr_peri_total": 0,
        "gr_se_idx": None, "gr_se_fb": None, "gr_se_score": 0, "gr_se_total": 0,
        "gr_pron_idx": None, "gr_pron_fb": None, "gr_pron_score": 0, "gr_pron_total": 0,
        "gr_err_idx": 0, "gr_err_revealed": False,
        "gr_lect_idx": 0, "gr_lect_answers": {}, "gr_lect_checked": False,
    }.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    st.markdown('<div class="section-title">Perífrasis verbales</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Estudia las perífrasis más importantes y practica con ejercicios de producción.</div>', unsafe_allow_html=True)

    pst1, pst2 = st.tabs(["📖 Tarjetas", "✏️ Ejercicios"])

    _pool_peri = [e for e in GR_PERIFRASIS if e.get("nivel","C1") in nivel_filter] or GR_PERIFRASIS

    with pst1:
        pidx = safe_idx("gr_peri_card", _pool_peri)
        p = _pool_peri[pidx]
        nc_p = NIVEL_COLORS.get(p.get("nivel", "C1"), "#8b5cf6")

        st.markdown(f"""
        <div class="card-box">
            <span style="display:inline-block;background:#d1fae5;color:#064e3b;border-radius:999px;
                  padding:0.25rem 0.7rem;font-size:0.8rem;font-weight:700;margin-bottom:0.6rem;">{p['perifrasis']}</span>
            <span class="nivel-badge" style="background:{nc_p};">{p.get('nivel','C1')}</span>
            <div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;
                        color:#064e3b;margin:0.4rem 0;">{p['perifrasis']}</div>
            <div style="color:#374151;margin-bottom:0.6rem;">{p['significado']}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Ejemplos:**")
        for ej_p in p["ejemplos"]:
            st.markdown(f'<div style="background:#ecfdf5;border-left:3px solid #059669;border-radius:0 10px 10px 0;'
                        f'padding:0.55rem 0.9rem;margin:0.35rem 0;font-style:italic;color:#065f46;'
                        f'font-size:0.93rem;">{ej_p}</div>', unsafe_allow_html=True)

        if p.get("trampa"):
            st.markdown(f'<div style="background:#fef3c7;border:1px solid #fcd34d;border-radius:10px;'
                        f'padding:0.55rem 0.9rem;font-size:0.88rem;color:#78350f;margin-top:0.6rem;">'
                        f'⚠️ <strong>Atención:</strong> {p["trampa"]}</div>', unsafe_allow_html=True)

        pc1, pc2, pc3 = st.columns(3)
        with pc1:
            if st.button("← Anterior", key="gr_peri_prev", use_container_width=True):
                st.session_state.gr_peri_card = (pidx - 1) % len(_pool_peri)
                st.rerun()
        with pc2:
            if st.button("Siguiente →", key="gr_peri_next_c", use_container_width=True):
                st.session_state.gr_peri_card = (pidx + 1) % len(_pool_peri)
                st.rerun()
        with pc3:
            if st.button("Aleatoria 🎲", key="gr_peri_rand", use_container_width=True):
                st.session_state.gr_peri_card = random.randrange(len(_pool_peri))
                st.rerun()
        st.caption(f"Perífrasis {pidx + 1} de {len(GR_PERIFRASIS)}")

    with pst2:
        pq = _pool_peri[safe_idx("gr_peri_idx", _pool_peri)]
        nc_pq = NIVEL_COLORS.get(pq.get("nivel", "C1"), "#8b5cf6")

        frase_pq = pq["ejercicio"].replace("___",
            '<span style="background:#d1fae5;color:#065f46;padding:2px 10px;'
            'border-radius:6px;font-weight:700;">___</span>')
        st.markdown(
            f'<div class="quiz-box">'
            f'<span style="display:inline-block;background:#d1fae5;color:#064e3b;border-radius:999px;'
            f'padding:0.25rem 0.7rem;font-size:0.8rem;font-weight:700;margin-bottom:0.6rem;">{pq["perifrasis"]}</span>'
            f'<span class="nivel-badge" style="background:{nc_pq};">{pq.get("nivel","C1")}</span>'
            f'<p style="font-size:1.05rem;color:#1e1b4b;margin-top:0.6rem;">{frase_pq}</p>'
            f'</div>', unsafe_allow_html=True)

        pq_ans = st.text_input("Completa con la perífrasis:",
                                placeholder="Ej: lleva trabajando / dejó de fumar...",
                                key=f"gr_peri_inp_{st.session_state.gr_peri_idx}")

        pq1, pq2, pq3 = st.columns(3)
        with pq1:
            if st.button("Comprobar ✓", key="gr_peri_check", use_container_width=True):
                st.session_state.gr_peri_total += 1
                correct_tok = set(" ".join(pq["respuesta"].lower().strip().split()).split())
                user_tok = set(" ".join(pq_ans.lower().strip().split()).split())
                if len(correct_tok & user_tok) >= max(1, len(correct_tok) - 1):
                    st.session_state.gr_peri_score += 1
                    st.session_state.gr_peri_fb = ("ok",
                        f"✅ Correcto. Esperado: **{pq['respuesta']}**\n\n📖 {pq['significado']}"
                        + (f"\n\n⚠️ {pq['trampa']}" if pq.get('trampa') else ""))
                else:
                    st.session_state.gr_peri_fb = ("bad",
                        f"❌ Forma correcta: **{pq['respuesta']}**\n\n📖 {pq['significado']}"
                        + (f"\n\n⚠️ {pq['trampa']}" if pq.get('trampa') else ""))
                st.rerun()
        with pq2:
            if st.button("Ver solución 👁", key="gr_peri_sol", use_container_width=True):
                st.session_state.gr_peri_fb = ("neutral",
                    f"**{pq['respuesta']}**\n\n📖 {pq['significado']}")
                st.rerun()
        with pq3:
            if st.button("Nueva →", key="gr_peri_next_q", use_container_width=True):
                st.session_state.gr_peri_idx = random.randrange(len(_pool_peri))
                st.session_state.gr_peri_fb = None
                st.rerun()

        if st.session_state.gr_peri_fb:
            kind, msg = st.session_state.gr_peri_fb
            css = {"ok":"feedback-ok","bad":"feedback-bad","neutral":"feedback-neutral"}[kind]
            st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

        if st.session_state.gr_peri_total:
            pct = int(st.session_state.gr_peri_score / st.session_state.gr_peri_total * 100)
            st.progress(st.session_state.gr_peri_score / st.session_state.gr_peri_total)
            st.caption(f"Precisión: {st.session_state.gr_peri_score}/{st.session_state.gr_peri_total} ({pct} %)")


if modulo == "🔵🔴 Ser vs Estar":
    for _k, _v in {
        "gr_subj_idx": None, "gr_subj_fb": None, "gr_subj_score": 0, "gr_subj_total": 0,
        "gr_peri_card": 0, "gr_peri_idx": None, "gr_peri_fb": None, "gr_peri_score": 0, "gr_peri_total": 0,
        "gr_se_idx": None, "gr_se_fb": None, "gr_se_score": 0, "gr_se_total": 0,
        "gr_pron_idx": None, "gr_pron_fb": None, "gr_pron_score": 0, "gr_pron_total": 0,
        "gr_err_idx": 0, "gr_err_revealed": False,
        "gr_lect_idx": 0, "gr_lect_answers": {}, "gr_lect_checked": False,
    }.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    st.markdown('<div class="section-title">Ser vs Estar</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Uno de los errores más frecuentes de anglohablantes en el DELE. Presta atención a los contextos.</div>', unsafe_allow_html=True)

    _pool_se = [e for e in GR_SER_ESTAR if e.get("nivel","C1") in nivel_filter] or GR_SER_ESTAR
    se = _pool_se[safe_idx("gr_se_idx", _pool_se)]
    nc_se = NIVEL_COLORS.get(se.get("nivel", "C1"), "#8b5cf6")

    frase_se = se["frase"].replace("___",
        '<span style="background:#dbeafe;color:#1e3a8a;padding:2px 10px;border-radius:6px;font-weight:700;">___</span>')
    st.markdown(
        f'<div class="quiz-box">'
        f'<span style="display:inline-block;background:#dbeafe;color:#1e3a8a;border-radius:999px;'
        f'padding:0.25rem 0.7rem;font-size:0.8rem;font-weight:700;margin-bottom:0.6rem;">{se["tipo"]}</span>'
        f'<span class="nivel-badge" style="background:{nc_se};">{se.get("nivel","C1")}</span>'
        f'<p style="font-size:1.05rem;color:#1e1b4b;margin-top:0.6rem;">{frase_se}</p>'
        f'</div>', unsafe_allow_html=True)

    se_ans = st.text_input("Forma correcta (ser / estar / es / está / fue / estuvo...):",
                            key=f"gr_se_{st.session_state.gr_se_idx}")

    se1, se2, se3 = st.columns(3)
    with se1:
        if st.button("Comprobar ✓", key="gr_se_check", use_container_width=True):
            st.session_state.gr_se_total += 1
            def _norm2(t): return " ".join(t.lower().strip().split())
            # Accept if any token of the answer matches
            correct_parts = [p.strip() for p in se["respuesta"].split("/")]
            user_norm = _norm2(se_ans)
            if any(_norm2(p) == user_norm or _norm2(p) in user_norm for p in correct_parts):
                st.session_state.gr_se_score += 1
                st.session_state.gr_se_fb = ("ok",
                    f"✅ Correcto: **{se['respuesta']}**\n\n📖 {se['explicacion']}"
                    + (f"\n\n⚠️ Ojo: {se['trampa']}" if se.get('trampa') else ""))
            else:
                st.session_state.gr_se_fb = ("bad",
                    f"❌ Correcta: **{se['respuesta']}**\n\n📖 {se['explicacion']}"
                    + (f"\n\n⚠️ Ojo: {se['trampa']}" if se.get('trampa') else ""))
            st.rerun()
    with se2:
        if st.button("Ver solución 👁", key="gr_se_sol", use_container_width=True):
            st.session_state.gr_se_fb = ("neutral",
                f"**{se['respuesta']}** — {se['tipo']}\n\n📖 {se['explicacion']}"
                + (f"\n\n⚠️ Ojo: {se['trampa']}" if se.get('trampa') else ""))
            st.rerun()
    with se3:
        if st.button("Nueva →", key="gr_se_next", use_container_width=True):
            st.session_state.gr_se_idx = random.randrange(len(_pool_se))
            st.session_state.gr_se_fb = None
            st.rerun()

    if st.session_state.gr_se_fb:
        kind, msg = st.session_state.gr_se_fb
        css = {"ok":"feedback-ok","bad":"feedback-bad","neutral":"feedback-neutral"}[kind]
        st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

    if st.session_state.gr_se_total:
        pct = int(st.session_state.gr_se_score / st.session_state.gr_se_total * 100)
        st.progress(st.session_state.gr_se_score / st.session_state.gr_se_total)
        st.caption(f"Precisión: {st.session_state.gr_se_score}/{st.session_state.gr_se_total} ({pct} %)")
        if st.button("Reiniciar marcador", key="gr_se_reset"):
            st.session_state.gr_se_score = 0
            st.session_state.gr_se_total = 0
            st.session_state.gr_se_fb = None
            st.rerun()

    st.markdown("---")
    st.markdown("**Reglas clave ser vs estar:**")
    tabla_se = """
    <table style="width:100%;border-collapse:collapse;font-size:0.87rem;background:white;
                  border-radius:12px;overflow:hidden;border:1px solid #e5e7eb;">
    <thead><tr>
        <th style="padding:0.5rem 0.8rem;background:#dbeafe;color:#1e3a8a;text-align:left;">SER</th>
        <th style="padding:0.5rem 0.8rem;background:#dcfce7;color:#14532d;text-align:left;">ESTAR</th>
    </tr></thead>
    <tbody>
    <tr style="border-top:1px solid #e5e7eb;">
        <td style="padding:0.4rem 0.8rem;">Identidad, profesión, origen</td>
        <td style="padding:0.4rem 0.8rem;">Estado físico o emocional temporal</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;background:#f9fafb;">
        <td style="padding:0.4rem 0.8rem;">Características permanentes</td>
        <td style="padding:0.4rem 0.8rem;">Ubicación de personas y cosas</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;">
        <td style="padding:0.4rem 0.8rem;">Ubicación de eventos</td>
        <td style="padding:0.4rem 0.8rem;">Precios y condiciones variables</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;background:#f9fafb;">
        <td style="padding:0.4rem 0.8rem;">Pasiva perifrástica (ser + participio)</td>
        <td style="padding:0.4rem 0.8rem;">Resultado de acción (estar + participio)</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;">
        <td style="padding:0.4rem 0.8rem;color:#6b7280;font-style:italic;">es listo (inteligente)</td>
        <td style="padding:0.4rem 0.8rem;color:#6b7280;font-style:italic;">está listo (preparado)</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;background:#f9fafb;">
        <td style="padding:0.4rem 0.8rem;color:#6b7280;font-style:italic;">es malo (mala persona)</td>
        <td style="padding:0.4rem 0.8rem;color:#6b7280;font-style:italic;">está malo (enfermo)</td>
    </tr>
    </tbody>
    </table>
    """
    st.markdown(tabla_se, unsafe_allow_html=True)



if modulo == "🔤 Pronombres":
    for _k, _v in {
        "gr_subj_idx": None, "gr_subj_fb": None, "gr_subj_score": 0, "gr_subj_total": 0,
        "gr_peri_card": 0, "gr_peri_idx": None, "gr_peri_fb": None, "gr_peri_score": 0, "gr_peri_total": 0,
        "gr_se_idx": None, "gr_se_fb": None, "gr_se_score": 0, "gr_se_total": 0,
        "gr_pron_idx": None, "gr_pron_fb": None, "gr_pron_score": 0, "gr_pron_total": 0,
        "gr_err_idx": 0, "gr_err_revealed": False,
        "gr_lect_idx": 0, "gr_lect_answers": {}, "gr_lect_checked": False,
    }.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    st.markdown('<div class="section-title">Pronombres OD / OI / Reflexivos</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Combinaciones, posición y usos avanzados. Errores muy frecuentes en el DELE C1.</div>', unsafe_allow_html=True)

    for _k, _v in {"gr_pron_idx": None, "gr_pron_fb": None,
                   "gr_pron_score": 0, "gr_pron_total": 0}.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    _pool_pron = [e for e in GR_PRONOMBRES if e.get("nivel","C1") in nivel_filter] or GR_PRONOMBRES
    pr = _pool_pron[safe_idx("gr_pron_idx", _pool_pron)]
    nc_pr = NIVEL_COLORS.get(pr.get("nivel", "C1"), "#8b5cf6")

    st.markdown(
        f'<div class="quiz-box">'
        f'<span style="display:inline-block;background:#ede9fe;color:#4c1d95;border-radius:999px;'
        f'padding:0.25rem 0.7rem;font-size:0.8rem;font-weight:700;margin-bottom:0.6rem;">{pr["tipo"]}</span>'
        f'<span class="nivel-badge" style="background:{nc_pr};">{pr.get("nivel","C1")}</span>'
        f'<p style="font-size:1.05rem;color:#1e1b4b;margin-top:0.6rem;">{pr["pregunta"]}</p>'
        f'</div>', unsafe_allow_html=True)

    pr_sel = st.radio("Elige la opción correcta:", pr["opciones"],
                      key=f"gr_pron_radio_{st.session_state.gr_pron_idx}")

    pr1, pr2, pr3 = st.columns(3)
    with pr1:
        if st.button("Comprobar ✓", key="gr_pron_check", use_container_width=True):
            st.session_state.gr_pron_total += 1
            if pr_sel == pr["respuesta"]:
                st.session_state.gr_pron_score += 1
                st.session_state.gr_pron_fb = ("ok",
                    f"✅ Correcto: **{pr['respuesta']}**\n\n📖 {pr['explicacion']}")
            else:
                st.session_state.gr_pron_fb = ("bad",
                    f"❌ Correcta: **{pr['respuesta']}**\n\n📖 {pr['explicacion']}")
            st.rerun()
    with pr2:
        if st.button("Ver solución 👁", key="gr_pron_sol", use_container_width=True):
            st.session_state.gr_pron_fb = ("neutral",
                f"**{pr['respuesta']}**\n\n📖 {pr['explicacion']}")
            st.rerun()
    with pr3:
        if st.button("Nueva →", key="gr_pron_next", use_container_width=True):
            st.session_state.gr_pron_idx = random.randrange(len(_pool_pron))
            st.session_state.gr_pron_fb = None
            st.rerun()

    if st.session_state.gr_pron_fb:
        kind, msg = st.session_state.gr_pron_fb
        css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
        st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

    if st.session_state.gr_pron_total:
        pct = int(st.session_state.gr_pron_score / st.session_state.gr_pron_total * 100)
        st.progress(st.session_state.gr_pron_score / st.session_state.gr_pron_total)
        st.caption(f"Precisión: {st.session_state.gr_pron_score}/{st.session_state.gr_pron_total} ({pct} %)")
        if st.button("Reiniciar", key="gr_pron_reset"):
            st.session_state.gr_pron_score = 0
            st.session_state.gr_pron_total = 0
            st.session_state.gr_pron_fb = None
            st.rerun()

    st.markdown("---")
    st.markdown("**Tabla de combinaciones OI + OD:**")
    st.markdown("""
    <table style="width:100%;border-collapse:collapse;font-size:0.87rem;background:white;
                  border-radius:12px;overflow:hidden;border:1px solid #e5e7eb;">
    <thead><tr style="background:#ede9fe;">
        <th style="padding:0.5rem;color:#4c1d95;">OI</th>
        <th style="padding:0.5rem;color:#4c1d95;">+ lo</th>
        <th style="padding:0.5rem;color:#4c1d95;">+ la</th>
        <th style="padding:0.5rem;color:#4c1d95;">+ los</th>
        <th style="padding:0.5rem;color:#4c1d95;">+ las</th>
    </tr></thead>
    <tbody>
    <tr style="text-align:center;border-top:1px solid #e5e7eb;">
        <td style="padding:0.4rem;font-weight:700;background:#f9fafb;">me</td>
        <td style="padding:0.4rem;">me lo</td><td>me la</td><td>me los</td><td>me las</td>
    </tr>
    <tr style="text-align:center;border-top:1px solid #e5e7eb;">
        <td style="padding:0.4rem;font-weight:700;background:#f9fafb;">te</td>
        <td style="padding:0.4rem;">te lo</td><td>te la</td><td>te los</td><td>te las</td>
    </tr>
    <tr style="text-align:center;border-top:1px solid #e5e7eb;background:#fef9c3;">
        <td style="padding:0.4rem;font-weight:700;">le → SE</td>
        <td style="padding:0.4rem;font-weight:700;">se lo</td>
        <td style="font-weight:700;">se la</td>
        <td style="font-weight:700;">se los</td>
        <td style="font-weight:700;">se las</td>
    </tr>
    <tr style="text-align:center;border-top:1px solid #e5e7eb;">
        <td style="padding:0.4rem;font-weight:700;background:#f9fafb;">nos</td>
        <td>nos lo</td><td>nos la</td><td>nos los</td><td>nos las</td>
    </tr>
    <tr style="text-align:center;border-top:1px solid #e5e7eb;background:#fef9c3;">
        <td style="padding:0.4rem;font-weight:700;">les → SE</td>
        <td style="padding:0.4rem;font-weight:700;">se lo</td>
        <td style="font-weight:700;">se la</td>
        <td style="font-weight:700;">se los</td>
        <td style="font-weight:700;">se las</td>
    </tr>
    </tbody>
    </table>
    <div style="font-size:0.82rem;color:#6b7280;margin-top:0.4rem;">
    ⚠️ le/les + lo/la/los/las → siempre SE (nunca *le lo, *les la...)
    </div>
    """, unsafe_allow_html=True)


if modulo == "🇬🇧 Errores":
    for _k, _v in {
        "gr_subj_idx": None, "gr_subj_fb": None, "gr_subj_score": 0, "gr_subj_total": 0,
        "gr_peri_card": 0, "gr_peri_idx": None, "gr_peri_fb": None, "gr_peri_score": 0, "gr_peri_total": 0,
        "gr_se_idx": None, "gr_se_fb": None, "gr_se_score": 0, "gr_se_total": 0,
        "gr_pron_idx": None, "gr_pron_fb": None, "gr_pron_score": 0, "gr_pron_total": 0,
        "gr_err_idx": 0, "gr_err_revealed": False,
        "gr_lect_idx": 0, "gr_lect_answers": {}, "gr_lect_checked": False,
    }.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    st.markdown('<div class="section-title">Errores frecuentes de anglohablantes</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Detecta el error, entiende por qué ocurre y aprende la forma correcta. Especialmente relevante para el DELE C1.</div>', unsafe_allow_html=True)

    for _k, _v in {"gr_err_idx": 0, "gr_err_revealed": False}.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    _pool_err = [e for e in GR_ERRORES_INGLES if e.get("nivel","C1") in nivel_filter] or GR_ERRORES_INGLES
    err = _pool_err[safe_idx("gr_err_idx", _pool_err)]
    nc_err = NIVEL_COLORS.get(err.get("nivel", "C1"), "#8b5cf6")

    st.markdown(
        f'<span style="display:inline-block;background:#fce7f3;color:#831843;border-radius:999px;'
        f'padding:0.25rem 0.7rem;font-size:0.8rem;font-weight:700;">{err["categoria"]}</span>'
        f'<span class="nivel-badge" style="background:{nc_err};">{err.get("nivel","C1")}</span>',
        unsafe_allow_html=True)

    st.markdown(
        f'<div style="background:#fef2f2;border-left:3px solid #ef4444;border-radius:0 10px 10px 0;'
        f'padding:0.6rem 0.9rem;margin:0.6rem 0;font-size:0.95rem;color:#7f1d1d;">'
        f'❌ <strong>Error frecuente:</strong> {err["error"]}</div>',
        unsafe_allow_html=True)

    if not st.session_state.gr_err_revealed:
        if st.button("👁 Ver corrección y explicación", key="gr_err_reveal"):
            st.session_state.gr_err_revealed = True
            st.rerun()
    else:
        st.markdown(
            f'<div style="background:#ecfdf5;border-left:3px solid #059669;border-radius:0 10px 10px 0;'
            f'padding:0.6rem 0.9rem;margin:0.4rem 0;font-size:0.95rem;color:#065f46;">'
            f'✅ <strong>Corrección:</strong> {err["correccion"]}</div>',
            unsafe_allow_html=True)
        st.markdown(
            f'<div class="quiz-box"><strong>📖 Explicación:</strong><br>{err["explicacion"]}</div>',
            unsafe_allow_html=True)
        if err.get("extra"):
            st.markdown(
                f'<div style="background:#fef3c7;border:1px solid #fcd34d;border-radius:10px;'
                f'padding:0.55rem 0.9rem;font-size:0.88rem;color:#78350f;margin-top:0.6rem;">'
                f'💡 <strong>Saber más:</strong> {err["extra"]}</div>',
                unsafe_allow_html=True)

    st.markdown("")
    e1, e2, e3 = st.columns(3)
    with e1:
        if st.button("← Anterior", key="gr_err_prev", use_container_width=True):
            st.session_state.gr_err_idx = (st.session_state.gr_err_idx - 1) % len(_pool_err)
            st.session_state.gr_err_revealed = False
            st.rerun()
    with e2:
        st.markdown(
            f'<p style="text-align:center;color:#6b7280;padding-top:0.5rem;">'
            f'{st.session_state.gr_err_idx + 1} / {len(_pool_err)}</p>',
            unsafe_allow_html=True)
    with e3:
        if st.button("Siguiente →", key="gr_err_next", use_container_width=True):
            st.session_state.gr_err_idx = (st.session_state.gr_err_idx + 1) % len(_pool_err)
            st.session_state.gr_err_revealed = False
            st.rerun()


if modulo == "📚 Comprensión lectora":
    for _k, _v in {
        "gr_subj_idx": None, "gr_subj_fb": None, "gr_subj_score": 0, "gr_subj_total": 0,
        "gr_peri_card": 0, "gr_peri_idx": None, "gr_peri_fb": None, "gr_peri_score": 0, "gr_peri_total": 0,
        "gr_se_idx": None, "gr_se_fb": None, "gr_se_score": 0, "gr_se_total": 0,
        "gr_pron_idx": None, "gr_pron_fb": None, "gr_pron_score": 0, "gr_pron_total": 0,
        "gr_err_idx": 0, "gr_err_revealed": False,
        "gr_lect_idx": 0, "gr_lect_answers": {}, "gr_lect_checked": False,
    }.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    st.markdown('<div class="section-title">Comprensión lectora · Estilo DELE C1</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Lee el texto y responde las preguntas. Las opciones incorrectas están diseñadas para que debas leer con precisión.</div>', unsafe_allow_html=True)

    for _k, _v in {"gr_lect_idx": 0, "gr_lect_answers": {},
                   "gr_lect_checked": False}.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    texto = GR_LECTURA[st.session_state.gr_lect_idx]

    tl1, tl2, tl3 = st.columns([1, 2, 1])
    with tl1:
        if st.button("← Texto anterior", key="gr_lect_prev", use_container_width=True):
            st.session_state.gr_lect_idx = (st.session_state.gr_lect_idx - 1) % len(GR_LECTURA)
            st.session_state.gr_lect_answers = {}
            st.session_state.gr_lect_checked = False
            st.rerun()
    with tl2:
        st.markdown(
            f'<p style="text-align:center;font-weight:700;color:#064e3b;padding-top:0.4rem;">'
            f'{texto["titulo"]} ({st.session_state.gr_lect_idx + 1}/{len(GR_LECTURA)})</p>',
            unsafe_allow_html=True)
    with tl3:
        if st.button("Texto siguiente →", key="gr_lect_next", use_container_width=True):
            st.session_state.gr_lect_idx = (st.session_state.gr_lect_idx + 1) % len(GR_LECTURA)
            st.session_state.gr_lect_answers = {}
            st.session_state.gr_lect_checked = False
            st.rerun()

    st.markdown(
        f'<div style="background:#f9fafb;border:1px solid #e5e7eb;border-radius:14px;'
        f'padding:1.4rem;font-size:0.97rem;color:#1f2937;line-height:1.8;margin-bottom:1rem;">'
        f'{texto["texto"].replace(chr(10), "<br><br>")}</div>',
        unsafe_allow_html=True)
    st.caption(texto["fuente"])

    st.markdown("**Preguntas:**")
    for i, q in enumerate(texto["preguntas"]):
        st.markdown(f"**{i+1}.** {q['pregunta']}")
        sel = st.radio(
            label=f"P{i+1}",
            options=q["opciones"],
            label_visibility="collapsed",
            key=f"gr_lect_{st.session_state.gr_lect_idx}_q{i}",
        )
        st.session_state.gr_lect_answers[i] = sel

        if st.session_state.gr_lect_checked:
            if sel == q["respuesta"]:
                st.markdown(
                    f'<div class="feedback-ok">✅ Correcto. {q["explicacion"]}</div>',
                    unsafe_allow_html=True)
            else:
                st.markdown(
                    f'<div class="feedback-bad">❌ Correcta: **{q["respuesta"]}**\n\n{q["explicacion"]}</div>',
                    unsafe_allow_html=True)
        st.markdown("")

    lb1, lb2 = st.columns(2)
    with lb1:
        if st.button("Comprobar todo ✓", key="gr_lect_check", use_container_width=True):
            st.session_state.gr_lect_checked = True
            st.rerun()
    with lb2:
        if st.button("Reiniciar respuestas 🔄", key="gr_lect_reset", use_container_width=True):
            st.session_state.gr_lect_answers = {}
            st.session_state.gr_lect_checked = False
            st.rerun()

    if st.session_state.gr_lect_checked:
        total = len(texto["preguntas"])
        score = sum(
            1 for i, q in enumerate(texto["preguntas"])
            if st.session_state.gr_lect_answers.get(i) == q["respuesta"]
        )
        pct = int(score / total * 100) if total else 0
        color = "#065f46" if pct >= 75 else "#92400e" if pct >= 50 else "#991b1b"
        st.markdown(
            f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
            f'padding:0.9rem 1.2rem;margin-top:0.5rem;text-align:center;">'
            f'<span style="font-size:1.3rem;font-weight:700;color:{color};">{score}/{total}</span>'
            f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctas ({pct} %)</span>'
            f'</div>',
            unsafe_allow_html=True)

