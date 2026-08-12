"""Módulo Gramática — UI completa (6 secciones)."""
import random
from typing import List

import streamlit as st

from data import GR_SUBJUNTIVO, GR_PERIFRASIS, GR_SER_ESTAR, GR_PRONOMBRES, GR_ERRORES_INGLES, GR_LECTURA
from core.config import NIVEL_COLORS
from core.state import safe_idx, next_from_queue


def render_subjuntivo(nivel_filter: List[str]) -> None:
    st.markdown('<div class="section-title">Subjuntivo vs Indicativo</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Rellena el hueco con la forma verbal correcta. Los contextos están diseñados al nivel del DELE C1.</div>', unsafe_allow_html=True)

    _pool_subj = [e for e in GR_SUBJUNTIVO if e.get("nivel", "C1") in nivel_filter] or GR_SUBJUNTIVO
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
            next_from_queue("gr_subj_queue", "gr_subj_idx", _pool_subj)
            st.session_state.gr_subj_fb = None
            st.rerun()

    if st.session_state.gr_subj_fb:
        kind, msg = st.session_state.gr_subj_fb
        css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
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


def render_perifrasis(nivel_filter: List[str]) -> None:
    st.markdown('<div class="section-title">Perífrasis verbales</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Estudia las perífrasis más importantes y practica con ejercicios de producción.</div>', unsafe_allow_html=True)

    pst1, pst2 = st.tabs(["📖 Tarjetas", "✏️ Ejercicios"])

    _pool_peri = [e for e in GR_PERIFRASIS if e.get("nivel", "C1") in nivel_filter] or GR_PERIFRASIS

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
                next_from_queue("gr_peri_queue", "gr_peri_idx", _pool_peri)
                st.session_state.gr_peri_fb = None
                st.rerun()

        if st.session_state.gr_peri_fb:
            kind, msg = st.session_state.gr_peri_fb
            css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
            st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

        if st.session_state.gr_peri_total:
            pct = int(st.session_state.gr_peri_score / st.session_state.gr_peri_total * 100)
            st.progress(st.session_state.gr_peri_score / st.session_state.gr_peri_total)
            st.caption(f"Precisión: {st.session_state.gr_peri_score}/{st.session_state.gr_peri_total} ({pct} %)")


def render_ser_estar(nivel_filter: List[str]) -> None:
    st.markdown('<div class="section-title">Ser vs Estar</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Uno de los errores más frecuentes de anglohablantes en el DELE. Presta atención a los contextos.</div>', unsafe_allow_html=True)

    _pool_se = [e for e in GR_SER_ESTAR if e.get("nivel", "C1") in nivel_filter] or GR_SER_ESTAR
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
            next_from_queue("gr_se_queue", "gr_se_idx", _pool_se)
            st.session_state.gr_se_fb = None
            st.rerun()

    if st.session_state.gr_se_fb:
        kind, msg = st.session_state.gr_se_fb
        css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
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


def render_pronombres(nivel_filter: List[str]) -> None:
    st.markdown('<div class="section-title">Pronombres OD / OI / Reflexivos</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Combinaciones, posición y usos avanzados. Errores muy frecuentes en el DELE C1.</div>', unsafe_allow_html=True)

    _pool_pron = [e for e in GR_PRONOMBRES if e.get("nivel", "C1") in nivel_filter] or GR_PRONOMBRES
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
            next_from_queue("gr_pron_queue", "gr_pron_idx", _pool_pron)
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


def render_errores(nivel_filter: List[str]) -> None:
    st.markdown('<div class="section-title">Errores frecuentes de anglohablantes</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Detecta el error, entiende por qué ocurre y aprende la forma correcta. Especialmente relevante para el DELE C1.</div>', unsafe_allow_html=True)

    _pool_err = [e for e in GR_ERRORES_INGLES if e.get("nivel", "C1") in nivel_filter] or GR_ERRORES_INGLES
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


def _lect_seleccion_multiple(texto: dict, idx: int) -> None:
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
            key=f"gr_lect_{idx}_q{i}",
        )
        st.session_state.gr_lect_answers[i] = sel
        if st.session_state.gr_lect_checked:
            if sel == q["respuesta"]:
                st.markdown(f'<div class="feedback-ok">✅ Correcto. {q["explicacion"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="feedback-bad">❌ Correcta: **{q["respuesta"]}**\n\n{q["explicacion"]}</div>', unsafe_allow_html=True)
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
        score = sum(1 for i, q in enumerate(texto["preguntas"]) if st.session_state.gr_lect_answers.get(i) == q["respuesta"])
        pct = int(score / total * 100) if total else 0
        color = "#065f46" if pct >= 75 else "#92400e" if pct >= 50 else "#991b1b"
        st.markdown(
            f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
            f'padding:0.9rem 1.2rem;margin-top:0.5rem;text-align:center;">'
            f'<span style="font-size:1.3rem;font-weight:700;color:{color};">{score}/{total}</span>'
            f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctas ({pct} %)</span>'
            f'</div>',
            unsafe_allow_html=True)


def _lect_verdadero_falso(texto: dict, idx: int) -> None:
    st.markdown(
        f'<div style="background:#f9fafb;border:1px solid #e5e7eb;border-radius:14px;'
        f'padding:1.4rem;font-size:0.97rem;color:#1f2937;line-height:1.8;margin-bottom:1rem;">'
        f'{texto["texto"].replace(chr(10), "<br><br>")}</div>',
        unsafe_allow_html=True)
    st.caption(texto["fuente"])

    st.markdown("**Afirmaciones:**")
    for i, af in enumerate(texto["preguntas"]):
        st.markdown(f"**{i+1}.** {af['afirmacion']}")
        bv, bf = st.columns(2)
        with bv:
            if st.button("✓ Verdadero", key=f"gr_lect_vf_{idx}_{i}_v", use_container_width=True):
                st.session_state.gr_lect_answers[i] = "V"
                st.rerun()
        with bf:
            if st.button("✗ Falso", key=f"gr_lect_vf_{idx}_{i}_f", use_container_width=True):
                st.session_state.gr_lect_answers[i] = "F"
                st.rerun()

        user_ans = st.session_state.gr_lect_answers.get(i)
        correct = af["respuesta"]
        if user_ans is not None:
            if user_ans == correct:
                st.markdown(f'<div class="feedback-ok">✅ Correcto. {af["justificacion"]}</div>', unsafe_allow_html=True)
            else:
                label = "Verdadero" if correct == "V" else "Falso"
                st.markdown(f'<div class="feedback-bad">❌ Es {label}. {af["justificacion"]}</div>', unsafe_allow_html=True)
        elif st.session_state.gr_lect_checked:
            label = "Verdadero" if correct == "V" else "Falso"
            st.markdown(f'<div class="feedback-neutral">ℹ️ Respuesta: {label}. {af["justificacion"]}</div>', unsafe_allow_html=True)
        st.markdown("")

    rb1, rb2 = st.columns(2)
    with rb1:
        if st.button("Ver todas las respuestas", key="gr_lect_reveal_all", use_container_width=True):
            st.session_state.gr_lect_checked = True
            st.rerun()
    with rb2:
        if st.button("Reiniciar 🔄", key="gr_lect_reset", use_container_width=True):
            st.session_state.gr_lect_answers = {}
            st.session_state.gr_lect_checked = False
            st.rerun()

    answered = [i for i in range(len(texto["preguntas"])) if i in st.session_state.gr_lect_answers]
    if answered:
        total = len(texto["preguntas"])
        score = sum(1 for i, af in enumerate(texto["preguntas"]) if st.session_state.gr_lect_answers.get(i) == af["respuesta"])
        color = "#065f46" if score == total else "#92400e" if score >= total // 2 else "#991b1b"
        st.markdown(
            f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
            f'padding:0.9rem 1.2rem;margin-top:0.5rem;text-align:center;">'
            f'<span style="font-size:1.3rem;font-weight:700;color:{color};">{score}/{total}</span>'
            f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">afirmaciones correctas</span>'
            f'</div>',
            unsafe_allow_html=True)


def _lect_emparejamiento(texto: dict, idx: int) -> None:
    texto_data = texto["texto"]
    st.markdown(
        f'<div style="font-size:0.95rem;color:#374151;margin-bottom:0.8rem;">{texto_data["instruccion"]}</div>',
        unsafe_allow_html=True)

    for letra, contenido in texto_data["subtextos"].items():
        st.markdown(
            f'<div style="background:#f0f9ff;border:1px solid #bae6fd;border-radius:12px;'
            f'padding:1rem 1.2rem;margin-bottom:0.7rem;font-size:0.95rem;color:#1f2937;line-height:1.7;">'
            f'<strong style="color:#0369a1;font-size:1.05rem;">{letra}</strong> — {contenido}'
            f'</div>',
            unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Afirmaciones — ¿A qué texto corresponde cada una?**")

    for i, af in enumerate(texto["preguntas"]):
        st.markdown(f"**{i+1}.** {af['afirmacion']}")
        sel = st.selectbox(
            label=f"Texto para afirmación {i+1}",
            options=["A", "B", "C", "D"],
            label_visibility="collapsed",
            key=f"gr_lect_emp_{idx}_{i}",
        )
        st.session_state.gr_lect_answers[i] = sel
        if st.session_state.gr_lect_checked:
            correct = af["respuesta"]
            if sel == correct:
                st.markdown(f'<div class="feedback-ok">✅ Correcto ({correct}). {af["explicacion"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="feedback-bad">❌ Correcta: {correct}. {af["explicacion"]}</div>', unsafe_allow_html=True)

    ec1, ec2 = st.columns(2)
    with ec1:
        if st.button("Comprobar todo ✓", key="gr_lect_check", use_container_width=True):
            st.session_state.gr_lect_checked = True
            st.rerun()
    with ec2:
        if st.button("Reiniciar 🔄", key="gr_lect_reset", use_container_width=True):
            st.session_state.gr_lect_answers = {}
            st.session_state.gr_lect_checked = False
            st.rerun()

    if st.session_state.gr_lect_checked:
        total = len(texto["preguntas"])
        score = sum(1 for i, af in enumerate(texto["preguntas"]) if st.session_state.gr_lect_answers.get(i) == af["respuesta"])
        pct = int(score / total * 100) if total else 0
        color = "#065f46" if pct >= 75 else "#92400e" if pct >= 50 else "#991b1b"
        st.markdown(
            f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
            f'padding:0.9rem 1.2rem;margin-top:0.5rem;text-align:center;">'
            f'<span style="font-size:1.3rem;font-weight:700;color:{color};">{score}/{total}</span>'
            f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctas ({pct} %)</span>'
            f'</div>',
            unsafe_allow_html=True)


def render_lectura(nivel_filter: List[str]) -> None:
    st.markdown('<div class="section-title">Comprensión lectora · Estilo DELE C1</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Lee el texto y responde las preguntas. Las opciones incorrectas están diseñadas para que debas leer con precisión.</div>', unsafe_allow_html=True)

    fmt_map = {
        "Todos": None,
        "Selección múltiple": "seleccion_multiple",
        "Verdadero / Falso": "verdadero_falso",
        "Emparejamiento": "emparejamiento",
    }
    fmt_label = st.selectbox("Formato", list(fmt_map.keys()), key="gr_lect_fmt_sel")
    fmt_val = fmt_map[fmt_label]

    if st.session_state.get("_gr_lect_prev_fmt") != fmt_label:
        st.session_state.gr_lect_idx = 0
        st.session_state.gr_lect_answers = {}
        st.session_state.gr_lect_checked = False
        st.session_state["_gr_lect_prev_fmt"] = fmt_label

    pool = [t for t in GR_LECTURA if fmt_val is None or t["formato"] == fmt_val]
    if not pool:
        st.info("No hay textos para el formato seleccionado.")
        return

    idx = st.session_state.gr_lect_idx % len(pool)
    st.session_state.gr_lect_idx = idx
    texto = pool[idx]

    tl1, tl2, tl3 = st.columns([1, 2, 1])
    with tl1:
        if st.button("← Texto anterior", key="gr_lect_prev", use_container_width=True):
            st.session_state.gr_lect_idx = (idx - 1) % len(pool)
            st.session_state.gr_lect_answers = {}
            st.session_state.gr_lect_checked = False
            st.rerun()
    with tl2:
        st.markdown(
            f'<p style="text-align:center;font-weight:700;color:#064e3b;padding-top:0.4rem;">'
            f'{texto["titulo"]} ({idx + 1}/{len(pool)})</p>',
            unsafe_allow_html=True)
    with tl3:
        if st.button("Texto siguiente →", key="gr_lect_next", use_container_width=True):
            st.session_state.gr_lect_idx = (idx + 1) % len(pool)
            st.session_state.gr_lect_answers = {}
            st.session_state.gr_lect_checked = False
            st.rerun()

    if texto["formato"] == "seleccion_multiple":
        _lect_seleccion_multiple(texto, idx)
    elif texto["formato"] == "verdadero_falso":
        _lect_verdadero_falso(texto, idx)
    elif texto["formato"] == "emparejamiento":
        _lect_emparejamiento(texto, idx)
