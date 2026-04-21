"""Módulo Conectores del discurso — UI completa."""
import random
from collections import defaultdict
from typing import List

import streamlit as st

from data import CONECTORES, GAP_EJERCICIOS, CLASIFICACION_EJERCICIOS, TEXTOS_ORDEN
from core.config import NIVEL_COLORS
from core.helpers import normalize
from core.state import safe_idx, next_from_queue

_FUNCIONES_CONECTORES = list(dict.fromkeys(c["funcion"] for c in CONECTORES))


def _show_fb(kind: str, msg: str) -> None:
    css = {
        "ok": "feedback-ok",
        "bad": "feedback-bad",
        "neutral": "feedback-neutral",
        "ai": "feedback-ai",
    }.get(kind, "feedback-neutral")
    st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)


def render(nivel_filter: List[str]) -> None:
    st.markdown("""
    <div class="mod-header" style="background:#fdf3dc;">
        <div class="mod-header-icon">🔗</div>
        <div class="mod-header-text" style="color:#c07a18;">
            <h2>Conectores del discurso</h2>
            <p>50 conectores · Función, matiz y ejercicios · C1 / C2</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    ctab0, ctab1, ctab2, ctab3, ctab4, ctab5, ctab6 = st.tabs([
        "📋 Resumen",
        "📖 Tarjetas",
        "🏷️ Clasifica",
        "🧩 Rellena el hueco",
        "📝 Ordena el texto",
        "✍️ Escritura + IA",
        "🗒️ Para rellenar",
    ])

    # ══════════════════════════════
    #  TAB 0 — TABLA RESUMEN CONECTORES
    # ══════════════════════════════
    with ctab0:
        st.markdown('<div class="section-title">Tabla resumen · Conectores por función</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Todos los conectores clasificados por función discursiva. Consúltala antes de los ejercicios o cuando escribas un texto.</div>', unsafe_allow_html=True)

        _grouped0 = defaultdict(list)
        _nf0 = nivel_filter if nivel_filter else ["B2", "C1", "C2"]
        for _c in CONECTORES:
            if _c.get("nivel", "C1") in _nf0:
                _grouped0[_c["funcion"]].append(_c)

        _fcolors0 = {
            "Contraste y concesión":       ("#faeee9", "#b5432a"),
            "Causa y origen":              ("#e6ecf5", "#1e3a5f"),
            "Consecuencia y resultado":    ("#e6f4ee", "#2e6b47"),
            "Adición y continuidad":       ("#ede8f8", "#5b3a9e"),
            "Hipótesis y condición":       ("#fce7f3", "#831843"),
            "Estructuración y orden":      ("#e0f2f7", "#0e7490"),
            "Reformulación y aclaración":  ("#f0fdf4", "#166534"),
            "Ejemplificación y digresión": ("#fdf3dc", "#c07a18"),
            "Conclusión y cierre":         ("#f5f3ff", "#3b0764"),
            "Énfasis y afirmación":        ("#fef3c7", "#92400e"),
        }
        _nordre = {"B2": 0, "C1": 1, "C2": 2}

        for funcion, _raw_con in _grouped0.items():
            if not _raw_con:
                continue
            bg0, fg0 = _fcolors0.get(funcion, ("#f8fafc", "#374151"))
            items_s = sorted(_raw_con, key=lambda x: (_nordre.get(x.get("nivel", "C1"), 1), x["conector"]))

            rows0 = ""
            for it in items_s:
                nc0 = NIVEL_COLORS.get(it.get("nivel", "C1"), "#6b7280")
                rows0 += (
                    f'<tr>'
                    f'<td style="padding:0.35rem 0.8rem;font-weight:700;color:{fg0};white-space:nowrap;">'
                    f'{it["conector"]}'
                    f'<span style="background:{nc0};color:white;border-radius:4px;'
                    f'padding:1px 5px;font-size:0.7rem;font-weight:700;margin-left:0.4rem;">'
                    f'{it.get("nivel","C1")}</span></td>'
                    f'<td style="padding:0.35rem 0.8rem;color:#374151;font-size:0.85rem;">'
                    f'{it["matiz"]}</td>'
                    f'<td style="padding:0.35rem 0.8rem;color:#7a6e60;font-size:0.82rem;'
                    f'font-style:italic;">{it["ejemplos"][0]}</td>'
                    f'</tr>'
                )

            st.markdown(f"""
            <div style="margin-bottom:1.4rem;">
              <div style="background:{bg0};border-radius:12px 12px 0 0;padding:0.5rem 1rem;
                          font-weight:700;color:{fg0};font-size:0.95rem;font-family:'Fraunces',serif;">
                {funcion}
                <span style="font-family:'DM Sans',sans-serif;font-weight:400;
                             font-size:0.82rem;margin-left:0.5rem;opacity:0.8;">
                  {len(items_s)} conector{"es" if len(items_s)!=1 else ""}</span>
              </div>
              <table style="width:100%;border-collapse:collapse;background:white;
                            border:1px solid #e4ddd3;border-radius:0 0 12px 12px;overflow:hidden;">
                <thead>
                  <tr style="background:#f8fafc;border-bottom:1px solid #e4ddd3;">
                    <th style="padding:0.35rem 0.8rem;text-align:left;color:#7a6e60;
                               font-size:0.75rem;font-weight:600;width:22%;">CONECTOR</th>
                    <th style="padding:0.35rem 0.8rem;text-align:left;color:#7a6e60;
                               font-size:0.75rem;font-weight:600;width:30%;">MATIZ</th>
                    <th style="padding:0.35rem 0.8rem;text-align:left;color:#7a6e60;
                               font-size:0.75rem;font-weight:600;">EJEMPLO</th>
                  </tr>
                </thead>
                <tbody>{rows0}</tbody>
              </table>
            </div>
            """, unsafe_allow_html=True)

    # ══════════════════════════════
    #  TAB 1 — TARJETAS
    # ══════════════════════════════
    with ctab1:
        st.markdown('<div class="section-title">Explorador de conectores</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Estudia función, matiz y ejemplos en contexto real.</div>', unsafe_allow_html=True)

        funcion_sel = st.selectbox(
            "Filtra por categoría:",
            ["Todas"] + _FUNCIONES_CONECTORES,
            key="cn_funcion_sel",
        )
        _nivel_f = st.session_state.get("nivel_global", ["B2", "C1", "C2"]) or ["B2", "C1", "C2"]
        lista_base = CONECTORES if funcion_sel == "Todas" else [c for c in CONECTORES if c["funcion"] == funcion_sel]
        lista = [c for c in lista_base if c.get("nivel", "C1") in _nivel_f] or lista_base

        if lista:
            idx = safe_idx("con_card_index", lista)
            con = lista[idx]
            nc = NIVEL_COLORS.get(con.get("nivel", "C1"), "#8b5cf6")

            st.markdown(f"""
            <div class="card-box">
                <div>
                    <span class="con-card-chip">{con['funcion']}</span>
                    <span class="nivel-badge" style="background:{nc};">{con.get('nivel','C1')}</span>
                </div>
                <div class="con-card-title">{con['conector']}</div>
                <div class="card-line"><strong>Matiz:</strong> {con['matiz']}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Ejemplos en contexto:**")
            for ej in con["ejemplos"]:
                st.markdown(f'<div class="con-example-block">{ej}</div>', unsafe_allow_html=True)

            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("← Anterior", use_container_width=True, key="cn_card_prev"):
                    st.session_state.con_card_index = (idx - 1) % len(lista)
                    st.rerun()
            with c2:
                if st.button("Siguiente →", use_container_width=True, key="cn_card_next"):
                    st.session_state.con_card_index = (idx + 1) % len(lista)
                    st.rerun()
            with c3:
                if st.button("Aleatorio 🎲", use_container_width=True, key="cn_card_rand"):
                    st.session_state.con_card_index = random.randrange(len(lista))
                    st.rerun()

            st.caption(f"Conector {idx + 1} de {len(lista)}")

    # ══════════════════════════════
    #  TAB 2 — CLASIFICA EL CONECTOR
    # ══════════════════════════════
    with ctab2:
        st.markdown('<div class="section-title">Clasifica el conector</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Elige la función discursiva de cada conector. Fundamental para usarlos con precisión.</div>', unsafe_allow_html=True)

        if st.session_state.cnc_idx is None:
            next_from_queue("cnc_queue", "cnc_idx", CLASIFICACION_EJERCICIOS)

        ej = CLASIFICACION_EJERCICIOS[st.session_state.cnc_idx]

        st.markdown(f"""
        <div class="quiz-box">
            <p style="font-size:1.1rem;color:#374151;">¿Cuál es la función de</p>
            <div class="con-card-title" style="font-size:2rem;margin:0.2rem 0 0.8rem 0;">{ej['conector']}</div>
        </div>
        """, unsafe_allow_html=True)

        opciones_mezcladas = ej["opciones"][:]
        sel = st.radio("Selecciona la función:", opciones_mezcladas,
                       key=f"clas_{st.session_state.cnc_idx}")

        cg1, cg2, cg3 = st.columns(3)
        with cg1:
            if st.button("Comprobar ✓", key="cn_clas_check", use_container_width=True):
                st.session_state.cnc_total += 1
                if sel == ej["correcta"]:
                    st.session_state.cnc_score += 1
                    st.session_state.cnc_fb = ("ok",
                        f"✅ Correcto: **{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                else:
                    st.session_state.cnc_fb = ("bad",
                        f"❌ La función correcta es: **{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                st.rerun()
        with cg2:
            if st.button("Ver solución 👁", key="cn_clas_sol", use_container_width=True):
                st.session_state.cnc_fb = ("neutral",
                    f"**{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                st.rerun()
        with cg3:
            if st.button("Nuevo →", key="cn_clas_next", use_container_width=True):
                next_from_queue("cnc_queue", "cnc_idx", CLASIFICACION_EJERCICIOS)
                st.session_state.cnc_fb = None
                st.rerun()

        if st.session_state.cnc_fb:
            _show_fb(*st.session_state.cnc_fb)

        if st.session_state.cnc_total:
            pct = int(st.session_state.cnc_score / st.session_state.cnc_total * 100)
            st.progress(st.session_state.cnc_score / st.session_state.cnc_total)
            st.caption(f"Precisión: {st.session_state.cnc_score}/{st.session_state.cnc_total} ({pct} %)")
            if st.button("Reiniciar marcador", key="cn_clas_reset"):
                st.session_state.cnc_score = 0
                st.session_state.cnc_total = 0
                st.session_state.cnc_fb = None
                st.rerun()

    # ══════════════════════════════
    #  TAB 3 — RELLENA EL HUECO
    # ══════════════════════════════
    with ctab3:
        st.markdown('<div class="section-title">Rellena el hueco</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Elige el conector más adecuado para cada contexto. Atención a los matices.</div>', unsafe_allow_html=True)

        if st.session_state.cng_idx is None:
            next_from_queue("cng_queue", "cng_idx", GAP_EJERCICIOS)

        gap = GAP_EJERCICIOS[st.session_state.cng_idx]
        nc_gap = NIVEL_COLORS.get(gap.get("nivel", "C1"), "#8b5cf6")

        frase_html = gap["frase"].replace("___",
            '<span style="background:#fef3c7;color:#78350f;padding:2px 10px;border-radius:6px;font-weight:700;">___</span>')
        st.markdown(f'<div class="quiz-box"><p style="font-size:1.05rem;color:#1e1b4b;">{frase_html}</p>'
                    f'<span class="nivel-badge" style="background:{nc_gap};">{gap.get("nivel","C1")}</span></div>',
                    unsafe_allow_html=True)

        gap_sel = st.radio("Elige el conector:", gap["alternativas"],
                           key=f"cn_gap_{st.session_state.cng_idx}")

        gg1, gg2, gg3 = st.columns(3)
        with gg1:
            if st.button("Comprobar ✓", key="cn_gap_check", use_container_width=True):
                validas = gap["respuesta"]
                validas_str = " / ".join(f"**{v}**" for v in validas)
                es_correcta = any(normalize(gap_sel) == normalize(v) for v in validas)
                if es_correcta:
                    otras = [v for v in validas if normalize(v) != normalize(gap_sel)]
                    extra = ("\n\n✅ También válido: " + " / ".join(f"**{v}**" for v in otras)) if otras else ""
                    st.session_state.cng_fb = ("ok",
                        f"✅ Correcto: **{gap_sel}**{extra}\n\n💡 {gap['explicacion']}")
                else:
                    st.session_state.cng_fb = ("bad",
                        f"❌ Opciones válidas: {validas_str}\n\n💡 {gap['explicacion']}")
                st.rerun()
        with gg2:
            if st.button("Ver solución 👁", key="cn_gap_sol", use_container_width=True):
                validas = gap["respuesta"]
                validas_str = " / ".join(f"**{v}**" for v in validas)
                st.session_state.cng_fb = ("neutral",
                    f"Válido(s): {validas_str}\n\n💡 {gap['explicacion']}")
                st.rerun()
        with gg3:
            if st.button("Nueva frase →", key="cn_gap_next", use_container_width=True):
                next_from_queue("cng_queue", "cng_idx", GAP_EJERCICIOS)
                st.session_state.cng_fb = None
                st.rerun()

        if st.session_state.cng_fb:
            _show_fb(*st.session_state.cng_fb)

    # ══════════════════════════════
    #  TAB 4 — ORDENA EL TEXTO
    # ══════════════════════════════
    with ctab4:
        st.markdown('<div class="section-title">Ordena el texto</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Los conectores son tu brújula. Úsalos para reconstruir la estructura argumentativa.</div>', unsafe_allow_html=True)

        texto = TEXTOS_ORDEN[st.session_state.cno_idx]

        if not st.session_state.cno_shuf:
            shuffled = list(enumerate(texto["partes"]))
            random.shuffle(shuffled)
            st.session_state.cno_shuf = shuffled

        st.markdown(f"**Texto:** *{texto['titulo']}*")
        st.markdown("Conectores clave: " + " · ".join(f"**{c}**" for c in texto["conectores"]))
        st.markdown(f'<div style="background:#fef3c7;border-radius:10px;padding:0.6rem 1rem;color:#78350f;font-size:0.9rem;margin-bottom:0.8rem;">💡 Pista: {texto["pista"]}</div>', unsafe_allow_html=True)

        st.markdown("**Fragmentos (en orden aleatorio):**")
        for i, (_, parte) in enumerate(st.session_state.cno_shuf):
            st.markdown(f'<div class="con-example-block"><strong>{i+1}.</strong> {parte}</div>', unsafe_allow_html=True)

        st.markdown("**Escribe el orden correcto** (ej: `3,1,4,2,5`):")
        order_ans = st.text_input("Tu orden:", key=f"cn_order_{st.session_state.cno_idx}",
                                  placeholder="1,2,3,4,5")

        oo1, oo2, oo3 = st.columns(3)
        with oo1:
            if st.button("Comprobar ✓", key="cn_order_check", use_container_width=True):
                try:
                    user_order = [int(x.strip()) - 1 for x in order_ans.split(",")]
                    orig_indices = [oi for oi, _ in st.session_state.cno_shuf]
                    correct = sorted(range(len(orig_indices)), key=lambda x: orig_indices[x])
                    if user_order == correct:
                        st.session_state.cno_fb = ("ok", "✅ ¡Perfecto! El orden es correcto.")
                    else:
                        correct_str = ",".join(str(x + 1) for x in correct)
                        partes_ord = "\n".join(f"{i+1}. {p}" for i, p in enumerate(texto["partes"]))
                        st.session_state.cno_fb = ("bad",
                            f"❌ El orden correcto es: **{correct_str}**\n\n{partes_ord}")
                except Exception:
                    st.session_state.cno_fb = ("neutral",
                        "⚠️ Escribe los números separados por comas, sin espacios extra.")
                st.rerun()
        with oo2:
            if st.button("Ver solución 👁", key="cn_order_sol", use_container_width=True):
                partes_ord = "\n".join(f"{i+1}. {p}" for i, p in enumerate(texto["partes"]))
                st.session_state.cno_fb = ("neutral", f"Texto ordenado:\n\n{partes_ord}")
                st.rerun()
        with oo3:
            if st.button("Otro texto →", key="cn_order_next", use_container_width=True):
                st.session_state.cno_idx = (st.session_state.cno_idx + 1) % len(TEXTOS_ORDEN)
                st.session_state.cno_shuf = []
                st.session_state.cno_fb = None
                st.rerun()

        if st.session_state.cno_fb:
            _show_fb(*st.session_state.cno_fb)

    # ══════════════════════════════
    #  TAB 5 — ESCRITURA LIBRE
    # ══════════════════════════════
    with ctab5:
        st.markdown('<div class="section-title">Escritura libre</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Escribe una frase o mini-párrafo usando el conector propuesto.</div>', unsafe_allow_html=True)

        if st.session_state.cnf_item is None:
            st.session_state.cnf_item = random.choice(CONECTORES)

        fc = st.session_state.cnf_item
        nc_fc = NIVEL_COLORS.get(fc.get("nivel", "C1"), "#8b5cf6")

        col_card_f, col_write_f = st.columns([1, 1.2], gap="large")

        with col_card_f:
            st.markdown(f"""
            <div class="card-box">
                <div>
                    <span class="con-card-chip">{fc['funcion']}</span>
                    <span class="nivel-badge" style="background:{nc_fc};">{fc.get('nivel','C1')}</span>
                </div>
                <div class="con-card-title">{fc['conector']}</div>
                <div class="card-line" style="color:#6b7280;font-style:italic;">{fc['matiz']}</div>
                <div style="margin-top:0.8rem;"><strong>Ejemplo:</strong></div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f'<div class="con-example-block">{fc["ejemplos"][0]}</div>', unsafe_allow_html=True)

            if st.button("Cambiar conector 🔄", use_container_width=True, key="cnf_change"):
                st.session_state.cnf_item = random.choice(CONECTORES)
                st.rerun()

        with col_write_f:
            st.text_area(
                "Tu frase o mini-párrafo:",
                height=120,
                key="cnf_frase",
                placeholder=f"Escribe aquí usando '{fc['conector']}'…",
            )

    # ══════════════════════════════
    #  TAB 6 — TABLA PARA RELLENAR
    # ══════════════════════════════
    with ctab6:
        st.markdown('<div class="section-title">Tabla para rellenar</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Se muestra la función y el matiz. Escribe el conector que corresponde a cada descripción.</div>', unsafe_allow_html=True)

        if "tabla_ejercicio" not in st.session_state or not st.session_state.tabla_ejercicio:
            ejercicio = [{"conector": c["conector"], "funcion": c["funcion"],
                          "matiz": c["matiz"], "nivel": c.get("nivel", "C1")}
                         for c in CONECTORES]
            random.shuffle(ejercicio)
            st.session_state.tabla_ejercicio = ejercicio
            st.session_state.tabla_checked = False
            st.session_state.tabla_answers = {}

        ejercicio = st.session_state.tabla_ejercicio

        by_funcion = defaultdict(list)
        for i, item in enumerate(ejercicio):
            by_funcion[item["funcion"]].append((i, item))

        funcion_colors2 = {
            "Contraste y concesión":       "#fef3c7",
            "Causa y origen":              "#dbeafe",
            "Consecuencia y resultado":    "#dcfce7",
            "Adición y continuidad":       "#ede9fe",
            "Hipótesis y condición":       "#fce7f3",
            "Estructuración y orden":      "#e0f2fe",
            "Reformulación y aclaración":  "#f0fdf4",
            "Ejemplificación y digresión": "#fff7ed",
            "Conclusión y cierre":         "#f5f3ff",
            "Énfasis y afirmación":        "#fef9c3",
        }

        for funcion, items in by_funcion.items():
            bg = funcion_colors2.get(funcion, "#f8fafc")
            st.markdown(
                f'<div style="background:{bg};border-radius:10px 10px 0 0;padding:0.5rem 1rem;'
                f'font-weight:700;font-size:0.92rem;color:#1e293b;margin-top:1rem;">'
                f'{funcion}</div>',
                unsafe_allow_html=True,
            )
            for idx, item in items:
                nivel = item["nivel"]
                nc = NIVEL_COLORS.get(nivel, "#6b7280")
                col_matiz, col_input, col_result = st.columns([3, 1.5, 1.2])

                with col_matiz:
                    st.markdown(
                        f'<div style="padding:0.45rem 0;font-size:0.88rem;color:#374151;">'
                        f'{item["matiz"]}'
                        f'<span style="background:{nc};color:white;border-radius:4px;'
                        f'padding:1px 6px;font-size:0.72rem;font-weight:700;margin-left:0.5rem;">'
                        f'{nivel}</span></div>',
                        unsafe_allow_html=True,
                    )

                with col_input:
                    val = st.text_input(
                        label="conector",
                        label_visibility="collapsed",
                        placeholder="escribe aquí…",
                        key=f"tabla_inp_{idx}",
                    )
                    st.session_state.tabla_answers[idx] = val

                with col_result:
                    if st.session_state.tabla_checked:
                        user_ans = " ".join(val.lower().strip().split())
                        correct_ans = " ".join(item["conector"].lower().strip().split())
                        if user_ans == correct_ans:
                            st.markdown('<div style="color:#065f46;font-weight:700;padding-top:0.45rem;">✅</div>', unsafe_allow_html=True)
                        elif user_ans:
                            st.markdown(
                                f'<div style="color:#991b1b;font-size:0.82rem;padding-top:0.3rem;">'
                                f'❌ <strong>{item["conector"]}</strong></div>',
                                unsafe_allow_html=True,
                            )
                        else:
                            st.markdown(
                                f'<div style="color:#6b7280;font-size:0.82rem;padding-top:0.3rem;">'
                                f'→ <strong>{item["conector"]}</strong></div>',
                                unsafe_allow_html=True,
                            )

        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("Comprobar todo ✓", use_container_width=True, key="tabla_check_btn"):
                st.session_state.tabla_checked = True
                st.rerun()
        with b2:
            if st.button("Ver soluciones 👁", use_container_width=True, key="tabla_sol_btn"):
                st.session_state.tabla_checked = True
                st.session_state.tabla_answers = {}
                st.rerun()
        with b3:
            if st.button("Nueva tabla 🔀", use_container_width=True, key="tabla_new_btn"):
                st.session_state.tabla_ejercicio = []
                st.session_state.tabla_checked = False
                st.session_state.tabla_answers = {}
                st.rerun()

        if st.session_state.tabla_checked:
            answers = st.session_state.tabla_answers
            total = len(ejercicio)
            correct_count = sum(
                1 for i, item in enumerate(ejercicio)
                if " ".join(answers.get(i, "").lower().strip().split()) ==
                   " ".join(item["conector"].lower().strip().split())
            )
            pct = int(correct_count / total * 100) if total else 0
            color = "#065f46" if pct >= 80 else "#92400e" if pct >= 50 else "#991b1b"
            st.markdown(
                f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
                f'padding:0.9rem 1.2rem;margin-top:0.5rem;text-align:center;">'
                f'<span style="font-size:1.3rem;font-weight:700;color:{color};">{correct_count}/{total}</span>'
                f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctos ({pct} %)</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
