"""UI Home — pantalla de inicio."""
import streamlit as st

from core.config import NIVEL_COLORS, NIVEL_BG

_MODULE_CARDS = [
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


def render_home() -> None:
    # ── Tarjeta diagnóstico ───────────────────────────────────────
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

    # ── Hero ──────────────────────────────────────────────────────
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

    # ── Module cards grid ─────────────────────────────────────────
    rows = [_MODULE_CARDS[:4], _MODULE_CARDS[4:]]
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
                if st.button("Ir →", key=f"home_go_{key}", use_container_width=True):
                    st.session_state.modulo = key
                    st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
