from typing import List
import streamlit as st

from data import DATA
from core.config import PREPS, CATEGORY_LABELS, NIVEL_COLORS, NIVEL_BG, PAGE_CONFIG
from core.state import init_all_state
from core.styles import load_css
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
from modules.diagnostico_module import render as render_diagnostico

# ─────────────────────────────────────────────
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────


# ─────────────────────────────────────────────
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────

st.set_page_config(**PAGE_CONFIG)

load_css()



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

    _nav("🎯 Diagnóstico", "🎯", "Diagnóstico de nivel")
    st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)
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
if modulo == "🎯 Diagnóstico":
    render_diagnostico()

if modulo == "🏠 Inicio":
    # ── Tarjeta diagnóstico destacada ─────────────────────
    _diag_nivel = st.session_state.get("nivel_diagnosticado")
    if _diag_nivel:
        _nc = NIVEL_COLORS[_diag_nivel]
        _nb = NIVEL_BG[_diag_nivel]
        st.markdown(f"""
        <div style="background:{_nb};border:2px solid {_nc};border-radius:16px;
                    padding:1.2rem 1.6rem;margin-bottom:1.4rem;
                    display:flex;align-items:center;gap:1.2rem;">
            <div style="font-size:2rem;">🎯</div>
            <div style="flex:1;">
                <div style="font-weight:700;color:{_nc};font-size:1rem;">
                    Tu nivel diagnosticado: {_diag_nivel}
                </div>
                <div style="font-size:0.85rem;color:#374151;margin-top:0.2rem;">
                    Basado en tu último test de diagnóstico.
                    Puedes repetirlo cuando quieras.
                </div>
            </div>
            <div>
        """, unsafe_allow_html=True)
        if st.button("Repetir diagnóstico →", key="home_repeat_diag"):
            st.session_state.modulo = "🎯 Diagnóstico"
            st.session_state.diag_step = 0
            st.session_state.diag_answers = {}
            st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#1e3a5f 0%,#3b0764 100%);
                    border-radius:16px;padding:1.4rem 1.8rem;margin-bottom:1.4rem;
                    display:flex;align-items:center;gap:1.4rem;color:white;">
            <div style="font-size:2.4rem;">🎯</div>
            <div style="flex:1;">
                <div style="font-family:'Fraunces',serif;font-size:1.2rem;font-weight:700;">
                    ¿Cuál es tu nivel real?
                </div>
                <div style="font-size:0.88rem;opacity:0.82;margin-top:0.2rem;">
                    Haz el diagnóstico de 20 preguntas y descubre en qué áreas trabajar primero.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🎯  Empezar diagnóstico", key="home_start_diag"):
            st.session_state.modulo = "🎯 Diagnóstico"
            st.rerun()
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
