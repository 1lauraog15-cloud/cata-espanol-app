from typing import List
import streamlit as st

from data import DATA
from core.config import PREPS, CATEGORY_LABELS
from core.state import init_all_state
from modules.verbos_module import render as render_verbos, active_items
from modules.conectores_module import render as render_conectores
from modules.gramatica_module import (
    render_subjuntivo,
    render_perifrasis,
    render_ser_estar,
    render_pronombres,
    render_errores,
    render_lectura,
)

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
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────

init_all_state()

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
        for _rk in ["gr_subj_queue", "gr_peri_queue", "gr_se_queue", "gr_pron_queue"]:
            st.session_state[_rk] = []
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
    render_verbos(nivel_filter, base_items, weighted_items)

if modulo == "🔗 Conectores":
    render_conectores(nivel_filter)


if modulo == "🔀 Subjuntivo":
    render_subjuntivo(nivel_filter)

if modulo == "⚙️ Perífrasis":
    render_perifrasis(nivel_filter)

if modulo == "🔵🔴 Ser vs Estar":
    render_ser_estar(nivel_filter)

if modulo == "🔤 Pronombres":
    render_pronombres(nivel_filter)

if modulo == "🇬🇧 Errores":
    render_errores(nivel_filter)

if modulo == "📚 Comprensión lectora":
    render_lectura(nivel_filter)
