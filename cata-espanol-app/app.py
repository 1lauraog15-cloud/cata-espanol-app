import streamlit as st

from core.config import PAGE_CONFIG
from core.state import init_all_state
from core.styles import load_css
from ui.sidebar import render_sidebar
from ui.home import render_home
from modules.verbos_module import render as render_verbos
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

# ── Config ────────────────────────────────────────────────────────
st.set_page_config(**PAGE_CONFIG)
load_css()
init_all_state()

# ── Sidebar ───────────────────────────────────────────────────────
modulo, nivel_filter, base_items, weighted_items = render_sidebar()

# ── Render según módulo ───────────────────────────────────────────
if modulo == "🎯 Diagnóstico":          render_diagnostico()
if modulo == "🏠 Inicio":               render_home()
if modulo == "📗 Verbos + Preposición": render_verbos(nivel_filter, base_items, weighted_items)
if modulo == "🔗 Conectores":           render_conectores(nivel_filter)
if modulo == "🔀 Subjuntivo":           render_subjuntivo(nivel_filter)
if modulo == "⚙️ Perífrasis":           render_perifrasis(nivel_filter)
if modulo == "🔵🔴 Ser vs Estar":       render_ser_estar(nivel_filter)
if modulo == "🔤 Pronombres":           render_pronombres(nivel_filter)
if modulo == "🇬🇧 Errores":             render_errores(nivel_filter)
if modulo == "📚 Comprensión lectora":  render_lectura(nivel_filter)
