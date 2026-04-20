"""Módulo Verbos + Preposición — UI completa."""
import random
import textwrap
from typing import Dict, List

import streamlit as st

from data import DATA, DOUBLE_PREP, GAP_EXERCISES, ERROR_EXERCISES
from core.config import PREPS, CATEGORY_LABELS, NIVEL_COLORS
from core.helpers import normalize
from core.state import safe_idx

# ── Mapa verbo → preposiciones válidas ─────────────────────────
_VERB_TO_PREPS: Dict[str, List[str]] = {}
for _prep, _items in DATA.items():
    for _it in _items:
        _VERB_TO_PREPS.setdefault(_it["verbo"], [])
        if _prep not in _VERB_TO_PREPS[_it["verbo"]]:
            _VERB_TO_PREPS[_it["verbo"]].append(_prep)


# ── Helpers ─────────────────────────────────────────────────────

def active_items(selected_preps: List[str]):
    """Devuelve (base, weighted) filtrando por preposiciones seleccionadas."""
    base = [i for i in st.session_state.all_items if i["prep"] in selected_preps]
    weighted = []
    for item in base:
        key = item["expresion"]
        fails = st.session_state.weak_items.get(key, 0)
        weighted.append(item)
        if fails >= 2:
            weighted.append(item)
    return base, weighted


def set_feedback(kind: str, message: str) -> None:
    st.session_state.feedback = (kind, message)


def show_feedback() -> None:
    kind, message = st.session_state.feedback
    css = {
        "ok": "feedback-ok", "bad": "feedback-bad",
        "neutral": "feedback-neutral", "ai": "feedback-ai",
    }.get(kind, "feedback-neutral")
    st.markdown(f'<div class="{css}">{message}</div>', unsafe_allow_html=True)


def register_fail(item: Dict) -> None:
    key = item["expresion"]
    st.session_state.weak_items[key] = st.session_state.weak_items.get(key, 0) + 1


def register_ok(item: Dict) -> None:
    key = item["expresion"]
    if key in st.session_state.weak_items and st.session_state.weak_items[key] > 0:
        st.session_state.weak_items[key] -= 1


def new_quiz_question(items: List[Dict], weighted: List[Dict], mode: str) -> None:
    if not items:
        st.session_state.quiz_data = None
        return

    chosen_mode = mode if mode != "Mixto" else random.choice(
        ["Elegir preposición", "Completar expresión", "Ejemplo correcto"]
    )
    item = random.choice(weighted if weighted else items)

    if chosen_mode == "Elegir preposición":
        options = PREPS[:]
        random.shuffle(options)
        valid_preps = _VERB_TO_PREPS.get(item["verbo"], [item["prep"]])
        nota_multi = (
            f"\n\n💡 Este verbo acepta varias preposiciones: {', '.join(valid_preps)}"
            if len(valid_preps) > 1 else ""
        )
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


def check_answer(user_answer: str) -> None:
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
        )}],
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.anthropic.com/v1/messages",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=aiohttp.ClientTimeout(total=20),
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
        return loop.run_until_complete(get_ai_feedback_async(verbo_expr, frase_usuario))
    except Exception as e:
        return f"Error al obtener feedback: {e}"


# ── Render principal ─────────────────────────────────────────────

def render(nivel_filter: List[str], base_items: List[Dict], weighted_items: List[Dict]) -> None:
    """Renderiza el módulo completo de Verbos + Preposición."""

    st.markdown("""
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

    progress_ratio = (
        st.session_state.quiz_score / st.session_state.quiz_total
        if st.session_state.quiz_total else 0.0
    )
    m1, m2, m3, m4, m5 = st.columns(5)
    for col, val, label in [
        (m1, len(items), "verbos activos"),
        (m2, st.session_state.quiz_score, "aciertos"),
        (m3, st.session_state.quiz_total, "intentos"),
        (m4, st.session_state.quiz_streak, "racha"),
        (m5, f"{int(progress_ratio * 100)}%", "precisión"),
    ]:
        col.markdown(
            f'<div class="metric-card">'
            f'<div class="metric-value">{val}</div>'
            f'<div class="metric-label">{label}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
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
            _items_f = [it for it in _raw_items if it.get("nivel", "B2") in nivel_filter]
            if not _items_f:
                continue
            bg, fg = _prep_colors.get(prep, ("#f8fafc", "#374151"))

            rows = ""
            for it in sorted(_items_f, key=lambda x: x.get("nivel", "B2")):
                nc = _nivel_badge.get(it.get("nivel", "B2"), "#6b7280")
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
                  {len(_items_f)} verbo{"s" if len(_items_f) != 1 else ""}</span>
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
                    display_opts.append(
                        "\n".join(textwrap.wrap(opt, width=54))
                        if quiz["type"] == "Ejemplo correcto" else opt
                    )
                sel = st.radio("Selecciona", display_opts, key=f"r_{quiz['question'][:30]}")
                if quiz["type"] == "Ejemplo correcto":
                    user_answer = dict(zip(display_opts, quiz["options"])).get(sel, sel)
                else:
                    user_answer = sel
            else:
                user_answer = st.text_input(
                    "Tu respuesta", placeholder="Ej: acordarse de",
                    key=f"i_{quiz['question'][:30]}"
                )

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
        gap_ans = st.text_input(
            "Preposición:", placeholder="de / a / con / en / por",
            key=f"gap_{st.session_state.gap_index}"
        )

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
            f'<span style="background:#fee2e2;color:#991b1b;padding:0 4px;border-radius:4px;font-weight:700;">*{err["prep_incorrecta"]}*</span>',
        )

        st.markdown(f'<div class="quiz-box"><p style="font-size:1.05rem;color:#1e1b4b;">{frase_display_err}</p></div>', unsafe_allow_html=True)
        err_ans = st.text_input(
            "Preposición correcta:", placeholder="de / a / con / en / por",
            key=f"err_{st.session_state.error_index}"
        )

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
    #  TAB 5 — DOBLE PREPOSICIÓN
    # ────────────────────────────────
    with tab5:
        st.markdown('<div class="section-title">Verbos con doble preposición</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Estos verbos cambian de significado según la preposición. Adivina cuántas preposiciones acepta cada uno y qué significa cada combinación.</div>', unsafe_allow_html=True)

        dp = DOUBLE_PREP[st.session_state.dp_index]

        st.markdown(f"""
        <div class="card-box" style="text-align:center;padding:2rem 1.5rem;">
            <div class="card-title" style="font-size:2.2rem;margin-bottom:0.5rem;">{dp['verbo']}</div>
            <div style="color:#6b7280;font-size:0.95rem;">
                Este verbo acepta <strong>{len(dp['casos'])}</strong> preposición{"es" if len(dp["casos"]) > 1 else ""}.
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

            st.markdown("---")
            st.markdown("**Mini-quiz:** ¿Con qué preposición se usa en este contexto?")

            caso_quiz = dp["casos"][st.session_state.dp_index % len(dp["casos"])]
            frase_con_hueco = caso_quiz["ejemplo"].replace(f" {caso_quiz['prep']} ", " **___** ", 1)
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
                    st.session_state.dp_quiz_ans = ("neutral", f"**+{caso_quiz['prep']}** → {caso_quiz['significado']}")
                    st.rerun()

            if st.session_state.dp_quiz_ans:
                kind, msg = st.session_state.dp_quiz_ans
                css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
                st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

        st.markdown("")
        nav1, nav2, nav3 = st.columns(3)
        with nav1:
            if st.button("← Anterior", use_container_width=True, key="dp_prev"):
                st.session_state.dp_index = (st.session_state.dp_index - 1) % len(DOUBLE_PREP)
                st.session_state.dp_revealed = False
                st.session_state.dp_quiz_ans = None
                st.rerun()
        with nav2:
            st.markdown(
                f'<p style="text-align:center;color:#6b7280;margin-top:0.6rem;">'
                f'{st.session_state.dp_index + 1} / {len(DOUBLE_PREP)}</p>',
                unsafe_allow_html=True,
            )
        with nav3:
            if st.button("Siguiente →", use_container_width=True, key="dp_next"):
                st.session_state.dp_index = (st.session_state.dp_index + 1) % len(DOUBLE_PREP)
                st.session_state.dp_revealed = False
                st.session_state.dp_quiz_ans = None
                st.rerun()
