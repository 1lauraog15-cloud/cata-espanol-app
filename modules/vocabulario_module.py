"""Módulo Vocabulario temático — UI completa (4 ejercicios)."""
import random
from typing import List

import streamlit as st

from data.vocabulario import VOCABULARIO
from core.config import NIVEL_COLORS


# ── Helpers ───────────────────────────────────────────────────────────────────

def _get_pool(tema_key: str, nivel_filter: List[str]) -> list:
    palabras = VOCABULARIO[tema_key]["palabras"]
    pool = [p for p in palabras if p["nivel"] in nivel_filter]
    return pool or palabras


def _reset_voc_state() -> None:
    st.session_state.voc_card_idx = 0
    st.session_state.voc_rel_words = []
    st.session_state.voc_rel_defs = []
    st.session_state.voc_rel_checked = False
    st.session_state.voc_rel_round_id += 1
    st.session_state.voc_comp_idx = 0
    st.session_state.voc_comp_score = 0
    st.session_state.voc_comp_total = 0
    st.session_state.voc_comp_fb = None
    st.session_state.voc_clas_words = []
    st.session_state.voc_clas_checked = False
    st.session_state.voc_clas_round_id += 1


def _strip_article(palabra: str) -> str:
    for art in ("el ", "la ", "los ", "las ", "un ", "una "):
        if palabra.lower().startswith(art):
            return palabra[len(art):]
    return palabra


def _make_gap(p: dict) -> str:
    GAP = ('<span style="background:#d1fae5;color:#065f46;padding:2px 10px;'
           'border-radius:6px;font-weight:700;">___</span>')
    ejemplo = p["ejemplo"]
    palabra = p["palabra"]
    lower_ej = ejemplo.lower()
    lower_p = palabra.lower()
    pos = lower_ej.find(lower_p)
    if pos >= 0:
        return ejemplo[:pos] + GAP + ejemplo[pos + len(palabra):]
    core = _strip_article(palabra)
    lower_core = core.lower()
    pos = lower_ej.find(lower_core)
    if pos >= 0:
        return ejemplo[:pos] + GAP + ejemplo[pos + len(core):]
    return ejemplo + f' <em style="color:#6b7280;">(completa con: ___)</em>'


def _check_voc_answer(user_ans: str, correct: str) -> bool:
    def norm(s):
        return " ".join(s.lower().strip().split())
    user_n = norm(user_ans)
    if user_n == norm(correct):
        return True
    if user_n == norm(_strip_article(correct)):
        return True
    return False


# ── Tab 1: Tarjetas ──────────────────────────────────────────────────────────

def _tab_tarjetas(pool: list) -> None:
    idx = st.session_state.voc_card_idx % len(pool)
    st.session_state.voc_card_idx = idx
    p = pool[idx]
    nc = NIVEL_COLORS.get(p["nivel"], "#6b7280")

    st.markdown(f"""
    <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:16px;
                padding:1.8rem 2rem;margin-bottom:1rem;text-align:center;">
        <div style="font-family:'Fraunces',serif;font-size:1.8rem;font-weight:700;
                    color:#1e1b4b;margin-bottom:0.8rem;">{p['palabra']}</div>
        <div style="display:flex;justify-content:center;gap:0.5rem;margin-bottom:1rem;">
            <span style="background:#ede9fe;color:#4c1d95;border-radius:999px;
                          padding:0.2rem 0.7rem;font-size:0.8rem;font-weight:600;">{p['categoria']}</span>
            <span style="background:{nc};color:white;border-radius:999px;
                          padding:0.2rem 0.7rem;font-size:0.8rem;font-weight:600;">{p['nivel']}</span>
        </div>
        <div style="font-size:1rem;color:#374151;margin-bottom:0.8rem;">{p['definicion']}</div>
        <div style="font-style:italic;color:#6b7280;font-size:0.93rem;
                    border-top:1px solid #e5e7eb;padding-top:0.8rem;">{p['ejemplo']}</div>
    </div>
    """, unsafe_allow_html=True)

    tc1, tc2, tc3, tc4 = st.columns([2, 2, 2, 3])
    with tc1:
        if st.button("← Anterior", key="voc_card_prev", use_container_width=True):
            st.session_state.voc_card_idx = (idx - 1) % len(pool)
            st.rerun()
    with tc2:
        if st.button("Siguiente →", key="voc_card_next", use_container_width=True):
            st.session_state.voc_card_idx = (idx + 1) % len(pool)
            st.rerun()
    with tc3:
        if st.button("Aleatoria 🎲", key="voc_card_rand", use_container_width=True):
            st.session_state.voc_card_idx = random.randrange(len(pool))
            st.rerun()
    with tc4:
        st.markdown(
            f'<p style="text-align:center;color:#6b7280;padding-top:0.5rem;">'
            f'Palabra {idx + 1} de {len(pool)}</p>',
            unsafe_allow_html=True)


# ── Tab 2: Relacionar ─────────────────────────────────────────────────────────

def _ensure_rel_round(pool: list) -> None:
    current = st.session_state.voc_rel_words
    pool_set = {p["palabra"] for p in pool}
    if not current or not all(w["palabra"] in pool_set for w in current):
        sample = random.sample(pool, min(6, len(pool)))
        defs = [w["definicion"] for w in sample]
        random.shuffle(defs)
        st.session_state.voc_rel_words = sample
        st.session_state.voc_rel_defs = defs
        st.session_state.voc_rel_checked = False
        st.session_state.voc_rel_round_id += 1


def _tab_relacionar(pool: list) -> None:
    _ensure_rel_round(pool)
    words = st.session_state.voc_rel_words
    defs = st.session_state.voc_rel_defs
    rid = st.session_state.voc_rel_round_id

    st.markdown("**Relaciona cada palabra con su definición:**")
    col_w, col_d = st.columns(2)

    user_matches = {}
    for i, w in enumerate(words):
        with col_w:
            st.markdown(
                f'<div style="background:#f0f9ff;border:1px solid #bae6fd;border-radius:10px;'
                f'padding:0.6rem 0.9rem;margin-bottom:0.55rem;font-weight:600;color:#0369a1;">'
                f'{w["palabra"]}</div>',
                unsafe_allow_html=True)
        with col_d:
            sel = st.selectbox(
                label=f"def_{i}",
                options=defs,
                label_visibility="collapsed",
                key=f"voc_rel_{rid}_{i}",
            )
            user_matches[i] = sel

    st.markdown("")
    rb1, rb2 = st.columns(2)
    with rb1:
        if st.button("Comprobar ✓", key="voc_rel_check", use_container_width=True):
            st.session_state.voc_rel_checked = True
            st.rerun()
    with rb2:
        if st.button("Nueva ronda 🔀", key="voc_rel_new", use_container_width=True):
            st.session_state.voc_rel_words = []
            st.session_state.voc_rel_checked = False
            st.rerun()

    if st.session_state.voc_rel_checked:
        score = 0
        for i, w in enumerate(words):
            correct = user_matches.get(i, "") == w["definicion"]
            if correct:
                score += 1
            icon = "✅" if correct else "❌"
            color = "#065f46" if correct else "#991b1b"
            st.markdown(
                f'<div style="font-size:0.88rem;margin:0.3rem 0;color:{color};">'
                f'{icon} <strong>{w["palabra"]}</strong> → {w["definicion"]}</div>',
                unsafe_allow_html=True)
        total = len(words)
        badge_color = "#065f46" if score == total else "#92400e" if score >= total // 2 else "#991b1b"
        st.markdown(
            f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
            f'padding:0.9rem 1.2rem;margin-top:0.8rem;text-align:center;">'
            f'<span style="font-size:1.3rem;font-weight:700;color:{badge_color};">{score}/{total}</span>'
            f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctas</span>'
            f'</div>',
            unsafe_allow_html=True)


# ── Tab 3: Completar frases ───────────────────────────────────────────────────

def _tab_completar(pool: list) -> None:
    idx = st.session_state.voc_comp_idx % len(pool)
    st.session_state.voc_comp_idx = idx
    p = pool[idx]

    st.markdown(
        f'<div style="background:#f9fafb;border:1px solid #e5e7eb;border-radius:14px;'
        f'padding:1.2rem 1.4rem;font-size:1rem;color:#1f2937;line-height:1.8;margin-bottom:0.8rem;">'
        f'{_make_gap(p)}</div>',
        unsafe_allow_html=True)

    user_ans = st.text_input(
        "Escribe la palabra que falta:",
        placeholder="Ej: sostenible / la huella ecológica...",
        key=f"voc_comp_inp_{idx}",
    )

    cc1, cc2 = st.columns(2)
    with cc1:
        if st.button("Comprobar ✓", key="voc_comp_check", use_container_width=True):
            st.session_state.voc_comp_total += 1
            if _check_voc_answer(user_ans, p["palabra"]):
                st.session_state.voc_comp_score += 1
                st.session_state.voc_comp_fb = ("ok",
                    f"✅ Correcto: **{p['palabra']}**\n\n📖 {p['definicion']}")
            else:
                st.session_state.voc_comp_fb = ("bad",
                    f"❌ Correcta: **{p['palabra']}**\n\n📖 {p['definicion']}")
            st.rerun()
    with cc2:
        if st.button("Nueva →", key="voc_comp_next", use_container_width=True):
            st.session_state.voc_comp_idx = (idx + 1) % len(pool)
            st.session_state.voc_comp_fb = None
            st.rerun()

    if st.session_state.voc_comp_fb:
        kind, msg = st.session_state.voc_comp_fb
        css = {"ok": "feedback-ok", "bad": "feedback-bad"}[kind]
        st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

    if st.session_state.voc_comp_total:
        score = st.session_state.voc_comp_score
        total = st.session_state.voc_comp_total
        pct = int(score / total * 100)
        st.progress(score / total)
        st.caption(f"Precisión: {score}/{total} ({pct} %)")
        if st.button("Reiniciar marcador", key="voc_comp_reset"):
            st.session_state.voc_comp_score = 0
            st.session_state.voc_comp_total = 0
            st.session_state.voc_comp_fb = None
            st.rerun()


# ── Tab 4: Clasificar ─────────────────────────────────────────────────────────

def _ensure_clas_round(pool: list) -> None:
    current = st.session_state.voc_clas_words
    pool_set = {p["palabra"] for p in pool}
    if not current or not all(w["palabra"] in pool_set for w in current):
        st.session_state.voc_clas_words = random.sample(pool, min(10, len(pool)))
        st.session_state.voc_clas_checked = False
        st.session_state.voc_clas_round_id += 1


def _tab_clasificar(pool: list) -> None:
    _ensure_clas_round(pool)
    words = st.session_state.voc_clas_words
    rid = st.session_state.voc_clas_round_id
    cats = ["sustantivo", "adjetivo", "verbo"]

    st.markdown("**Clasifica cada palabra según su categoría gramatical:**")
    user_cats = {}
    for i, w in enumerate(words):
        c1, c2 = st.columns([3, 2])
        with c1:
            st.markdown(
                f'<div style="padding:0.5rem 0;font-weight:600;color:#1e1b4b;">'
                f'{w["palabra"]}</div>',
                unsafe_allow_html=True)
        with c2:
            sel = st.selectbox(
                label=f"cat_{i}",
                options=cats,
                label_visibility="collapsed",
                key=f"voc_clas_{rid}_{i}",
            )
            user_cats[i] = sel

    st.markdown("")
    cl1, cl2 = st.columns(2)
    with cl1:
        if st.button("Comprobar ✓", key="voc_clas_check", use_container_width=True):
            st.session_state.voc_clas_checked = True
            st.rerun()
    with cl2:
        if st.button("Nueva ronda 🔀", key="voc_clas_new", use_container_width=True):
            st.session_state.voc_clas_words = []
            st.session_state.voc_clas_checked = False
            st.rerun()

    if st.session_state.voc_clas_checked:
        score = 0
        for i, w in enumerate(words):
            sel = user_cats.get(i, "")
            correct = w["categoria"] == sel
            if correct:
                score += 1
            icon = "✅" if correct else "❌"
            color = "#065f46" if correct else "#991b1b"
            wrong_note = (f' <span style="color:#6b7280;">(pusiste: {sel})</span>'
                          if not correct else "")
            st.markdown(
                f'<div style="font-size:0.88rem;margin:0.3rem 0;color:{color};">'
                f'{icon} <strong>{w["palabra"]}</strong> — {w["categoria"]}{wrong_note}</div>',
                unsafe_allow_html=True)
        total = len(words)
        pct = int(score / total * 100)
        badge_color = "#065f46" if pct >= 80 else "#92400e" if pct >= 50 else "#991b1b"
        st.markdown(
            f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
            f'padding:0.9rem 1.2rem;margin-top:0.8rem;text-align:center;">'
            f'<span style="font-size:1.3rem;font-weight:700;color:{badge_color};">{score}/{total}</span>'
            f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctas</span>'
            f'</div>',
            unsafe_allow_html=True)


# ── Render principal ──────────────────────────────────────────────────────────

def render(nivel_filter: List[str]) -> None:
    st.markdown('<div class="section-title">Vocabulario temático</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Léxico avanzado organizado por temas. Estudia con tarjetas y practica con ejercicios de uso real.</div>', unsafe_allow_html=True)

    tema_options = {k: v["titulo"] for k, v in VOCABULARIO.items()}
    tema_label = st.selectbox("Tema", list(tema_options.values()), key="voc_tema_sel")
    tema_key = next(k for k, v in VOCABULARIO.items() if v["titulo"] == tema_label)

    if st.session_state.get("_voc_prev_tema") != tema_key:
        _reset_voc_state()
        st.session_state["_voc_prev_tema"] = tema_key

    pool = _get_pool(tema_key, nivel_filter)

    desc = VOCABULARIO[tema_key]["descripcion"]
    st.markdown(
        f'<div style="background:#f0f9ff;border:1px solid #bae6fd;border-radius:10px;'
        f'padding:0.6rem 1rem;margin-bottom:1rem;font-size:0.9rem;color:#0369a1;">'
        f'{desc} · <strong>{len(pool)} palabras</strong></div>',
        unsafe_allow_html=True)

    t1, t2, t3, t4 = st.tabs(["📖 Tarjetas", "🔗 Relacionar", "✍️ Completar frases", "🗂️ Clasificar"])
    with t1:
        _tab_tarjetas(pool)
    with t2:
        _tab_relacionar(pool)
    with t3:
        _tab_completar(pool)
    with t4:
        _tab_clasificar(pool)
