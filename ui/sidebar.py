"""UI Sidebar — navegación lateral y filtros."""
from typing import List, Tuple

import streamlit as st

from modules.verbos_module import render_sidebar as _render_verbos_filters


def _nav(key: str, icon: str, label: str) -> None:
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


def render_sidebar() -> Tuple[str, List[str], list, list]:
    """Renderiza el sidebar completo y devuelve (modulo, nivel_filter, base_items, weighted_items)."""
    with st.sidebar:
        # ── Branding ─────────────────────────────────────────────
        st.markdown("""
        <div class="brand">
            <div class="brand-name">🇪🇸 EspañolPro</div>
            <div class="brand-tagline">Nivel C1 · C2 · DELE Cervantes</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Nivel ─────────────────────────────────────────────────
        st.markdown('<div class="nav-section" style="padding-top:0.6rem;">NIVEL</div>',
                    unsafe_allow_html=True)
        nivel_filter: List[str] = st.multiselect(
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

        # ── Navegación ────────────────────────────────────────────
        modulo: str = st.session_state.modulo

        _nav("🎯 Diagnóstico",          "🎯", "Diagnóstico de nivel")
        st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)
        _nav("🏠 Inicio",               "🏠", "Inicio")
        st.markdown('<div class="nav-section">LÉXICO</div>', unsafe_allow_html=True)
        _nav("📗 Verbos + Preposición", "📗", "Verbos + Preposición")
        _nav("🔗 Conectores",           "🔗", "Conectores")
        _nav("📝 Vocabulario",          "📝", "Vocabulario temático")
        st.markdown('<div class="nav-section">GRAMÁTICA</div>', unsafe_allow_html=True)
        _nav("🔀 Subjuntivo",           "🔀", "Subjuntivo")
        _nav("⚙️ Perífrasis",           "⚙️", "Perífrasis")
        _nav("🔵🔴 Ser vs Estar",       "🔴", "Ser vs Estar")
        _nav("🔤 Pronombres",           "🔤", "Pronombres")
        st.markdown('<div class="nav-section">PRÁCTICA</div>', unsafe_allow_html=True)
        _nav("🇬🇧 Errores",             "🇬🇧", "Errores")
        _nav("📚 Comprensión lectora",  "📚", "Comprensión lectora")

        # ── Filtros específicos de verbos ─────────────────────────
        base_items, weighted_items = [], []
        if modulo == "📗 Verbos + Preposición":
            base_items, weighted_items = _render_verbos_filters(nivel_filter)

    return modulo, nivel_filter, base_items, weighted_items
