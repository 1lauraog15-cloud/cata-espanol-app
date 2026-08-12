"""Módulo Diagnóstico de nivel — test de 20 preguntas."""
import streamlit as st

from data import DIAGNOSTICO
from core.config import NIVEL_COLORS, NIVEL_BG

_AREAS = ["verbos", "conectores", "subjuntivo", "gramatica", "errores"]
_AREA_LABELS = {
    "verbos":    "Verbos + Preposición",
    "conectores": "Conectores",
    "subjuntivo": "Subjuntivo",
    "gramatica":  "Ser/Estar · Perífrasis",
    "errores":    "Errores anglohablantes",
}
_AREA_MODULO = {
    "verbos":    "📗 Verbos + Preposición",
    "conectores": "🔗 Conectores",
    "subjuntivo": "🔀 Subjuntivo",
    "gramatica":  "⚙️ Perífrasis",
    "errores":    "🇬🇧 Errores",
}


def _score_to_nivel(score: int) -> str:
    if score <= 10:
        return "B2"
    if score <= 15:
        return "C1"
    return "C2"


def _get_weak_areas(answers: dict) -> list:
    """Devuelve áreas ordenadas de peor a mejor resultado."""
    by_area: dict[str, list] = {a: [] for a in _AREAS}
    for i, q in enumerate(DIAGNOSTICO):
        correct = answers.get(i) == q["respuesta"]
        by_area[q["area"]].append(correct)
    scored = {
        area: sum(vals) / len(vals) if vals else 1.0
        for area, vals in by_area.items()
    }
    return sorted(_AREAS, key=lambda a: scored[a])


def render() -> None:
    # ── Init state ────────────────────────────────────────
    if "diag_step" not in st.session_state:
        st.session_state.diag_step = 0       # 0..19 = pregunta activa; 20 = resultados
        st.session_state.diag_answers = {}   # {pregunta_idx: opción_elegida}
        st.session_state.diag_sel = None     # selección actual antes de avanzar

    step: int = st.session_state.diag_step
    answers: dict = st.session_state.diag_answers
    total = len(DIAGNOSTICO)

    # ── PANTALLA DE RESULTADOS ────────────────────────────
    if step >= total:
        score = sum(1 for i, q in enumerate(DIAGNOSTICO) if answers.get(i) == q["respuesta"])
        nivel = _score_to_nivel(score)
        nc = NIVEL_COLORS[nivel]
        nb = NIVEL_BG[nivel]

        # Guardar en session_state para que el sidebar pueda leerlo
        st.session_state.nivel_diagnosticado = nivel

        st.markdown(f"""
        <div style="background:{nb};border:2px solid {nc};border-radius:20px;
                    padding:2rem 2.4rem;margin-bottom:1.6rem;text-align:center;">
            <div style="font-size:0.85rem;font-weight:600;color:{nc};letter-spacing:0.08em;
                        text-transform:uppercase;margin-bottom:0.4rem;">Tu nivel estimado</div>
            <div style="font-family:'Fraunces',serif;font-size:3.5rem;font-weight:700;
                        color:{nc};line-height:1;">{nivel}</div>
            <div style="font-size:1.1rem;color:#374151;margin-top:0.5rem;">
                {score} / {total} respuestas correctas
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Puntuación por área
        st.markdown("### Puntuación por área")
        area_cols = st.columns(len(_AREAS))
        area_scores: dict[str, tuple] = {}
        for area in _AREAS:
            qs = [(i, q) for i, q in enumerate(DIAGNOSTICO) if q["area"] == area]
            correct = sum(1 for i, q in qs if answers.get(i) == q["respuesta"])
            total_a = len(qs)
            area_scores[area] = (correct, total_a)

        for col, area in zip(area_cols, _AREAS):
            c, t = area_scores[area]
            pct = int(c / t * 100) if t else 0
            col_color = "#065f46" if pct >= 75 else "#92400e" if pct >= 50 else "#991b1b"
            col.markdown(f"""
            <div style="background:white;border:1px solid #e4ddd3;border-radius:12px;
                        padding:0.8rem 0.6rem;text-align:center;">
                <div style="font-size:1.4rem;font-weight:700;color:{col_color};">{c}/{t}</div>
                <div style="font-size:0.76rem;color:#7a6e60;margin-top:0.2rem;line-height:1.3;">
                    {_AREA_LABELS[area]}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Módulos recomendados (3 áreas más débiles)
        weak = _get_weak_areas(answers)[:3]
        st.markdown("### Módulos recomendados")
        st.markdown("Empieza por estas áreas donde hay más margen de mejora:")

        rec_cols = st.columns(3)
        for col, area in zip(rec_cols, weak):
            c, t = area_scores[area]
            modulo_key = _AREA_MODULO[area]
            icon = modulo_key.split()[0]
            col.markdown(f"""
            <div style="background:white;border:1px solid #e4ddd3;border-radius:12px;
                        padding:0.9rem 1rem;text-align:center;margin-bottom:0.5rem;">
                <div style="font-size:1.5rem;">{icon}</div>
                <div style="font-weight:700;color:#1c1007;font-size:0.9rem;margin:0.3rem 0;">
                    {_AREA_LABELS[area]}
                </div>
                <div style="font-size:0.8rem;color:#7a6e60;">{c}/{t} correctas</div>
            </div>
            """, unsafe_allow_html=True)
            if col.button("Ir →", key=f"diag_go_{area}", use_container_width=True):
                st.session_state.modulo = modulo_key
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Repetir diagnóstico", use_container_width=False):
            st.session_state.diag_step = 0
            st.session_state.diag_answers = {}
            st.session_state.diag_sel = None
            st.rerun()

        return

    # ── PREGUNTA ACTIVA ───────────────────────────────────
    q = DIAGNOSTICO[step]
    nc_q = NIVEL_COLORS.get(q["nivel"], "#8b5cf6")

    # Cabecera
    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;
                margin-bottom:0.8rem;">
        <div style="font-family:'Fraunces',serif;font-size:1.3rem;font-weight:700;
                    color:#1c1007;">Diagnóstico de nivel</div>
        <span style="background:{nc_q};color:white;border-radius:999px;
                     padding:0.2rem 0.65rem;font-size:0.78rem;font-weight:700;">
            {q['nivel']}
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Barra de progreso
    progress_val = step / total
    st.progress(progress_val)
    st.caption(f"Pregunta {step + 1} de {total}  ·  área: {_AREA_LABELS[q['area']]}")

    # Caja de pregunta
    st.markdown(f"""
    <div style="background:white;border:1px solid #e4ddd3;border-radius:14px;
                padding:1.4rem 1.6rem;margin:1rem 0 1.2rem;">
        <div style="font-size:1.08rem;color:#1c1007;font-weight:500;line-height:1.6;">
            {q['pregunta']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Opciones — si ya respondimos esta pregunta, preseleccionar
    prev_ans = answers.get(step)
    opciones = q["opciones"]

    sel = st.radio(
        "Elige una opción:",
        opciones,
        index=opciones.index(prev_ans) if prev_ans in opciones else 0,
        key=f"diag_radio_{step}",
    )
    st.session_state.diag_sel = sel

    st.markdown("<br>", unsafe_allow_html=True)
    btn_col1, btn_col2 = st.columns([1, 3])
    with btn_col1:
        if step > 0:
            if st.button("← Anterior", use_container_width=True, key="diag_prev"):
                answers[step] = sel
                st.session_state.diag_step = step - 1
                st.session_state.diag_sel = None
                st.rerun()
    with btn_col2:
        label = "Ver resultados →" if step == total - 1 else "Siguiente →"
        if st.button(label, use_container_width=True, key="diag_next", type="primary"):
            answers[step] = sel
            st.session_state.diag_answers = answers
            st.session_state.diag_step = step + 1
            st.session_state.diag_sel = None
            st.rerun()
