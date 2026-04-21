import streamlit as st

from core.config import PAGE_CONFIG
from core.state import init_all_state
from core.styles import load_css
from modules.verbos_module import render as render_verbos, render_sidebar as render_verbos_sidebar
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
from modules.home_module import render as render_home

# ── Config ────────────────────────────────────────────────────────
st.set_page_config(**PAGE_CONFIG)
load_css()
init_all_state()

# ── Sidebar ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="brand">
        <div class="brand-name">🇪🇸 EspañolPro</div>
        <div class="brand-tagline">Nivel C1 · C2 · DELE Cervantes</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-section" style="padding-top:0.6rem;">NIVEL</div>',
                unsafe_allow_html=True)
    nivel_filter = st.multiselect(
        "nf", ["B2", "C1", "C2"], default=["B2", "C1", "C2"],
        label_visibility="collapsed", key="nivel_global",
    )
    if not nivel_filter:
        nivel_filter = ["B2", "C1", "C2"]

    # Resetear índices al cambiar nivel
    _nivel_sig = tuple(sorted(nivel_filter))
    if st.session_state.get("_prev_nivel") != _nivel_sig:
        for _k in ["gr_subj_idx", "gr_peri_idx", "gr_se_idx", "gr_pron_idx"]:
            st.session_state.pop(_k, None)
        for _k in ["gr_peri_card", "gr_err_idx", "gr_lect_idx"]:
            if _k in st.session_state:
                st.session_state[_k] = 0
        for _k in ["gr_subj_queue", "gr_peri_queue", "gr_se_queue", "gr_pron_queue"]:
            st.session_state[_k] = []
        st.session_state._prev_nivel = _nivel_sig

    st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)

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

    _nav("🎯 Diagnóstico",          "🎯", "Diagnóstico de nivel")
    st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)
    _nav("🏠 Inicio",               "🏠", "Inicio")
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

    base_items, weighted_items = [], []
    if modulo == "📗 Verbos + Preposición":
        base_items, weighted_items = render_verbos_sidebar(nivel_filter)

# ── Render según módulo ───────────────────────────────────────────
if modulo == "🎯 Diagnóstico":         render_diagnostico()
if modulo == "🏠 Inicio":              render_home()
if modulo == "📗 Verbos + Preposición": render_verbos(nivel_filter, base_items, weighted_items)
if modulo == "🔗 Conectores":          render_conectores(nivel_filter)
if modulo == "🔀 Subjuntivo":          render_subjuntivo(nivel_filter)
if modulo == "⚙️ Perífrasis":          render_perifrasis(nivel_filter)
if modulo == "🔵🔴 Ser vs Estar":      render_ser_estar(nivel_filter)
if modulo == "🔤 Pronombres":          render_pronombres(nivel_filter)
if modulo == "🇬🇧 Errores":            render_errores(nivel_filter)
if modulo == "📚 Comprensión lectora": render_lectura(nivel_filter)
