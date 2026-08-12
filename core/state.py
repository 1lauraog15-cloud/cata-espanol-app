import random
import streamlit as st

from data import DATA


def safe_idx(key: str, pool: list, default: int = 0) -> int:
    """Devuelve siempre un índice válido para *pool*, reseteando session_state si es necesario.

    Casos que cubre:
    - pool vacío        → devuelve default (0) y escribe default en session_state
    - valor None        → devuelve 0 % len(pool), lo escribe en session_state
    - valor fuera de rango (level change reduce el pool) → clamp con módulo
    - valor ya válido   → lo devuelve tal cual sin tocar session_state
    """
    if not pool:
        st.session_state[key] = default
        return default
    val = st.session_state.get(key, default)
    if not isinstance(val, int):
        val = default
    val = val % len(pool)
    st.session_state[key] = val
    return val


def next_from_queue(queue_key: str, idx_key: str, pool: list) -> int:
    """Selecciona el siguiente ítem del pool sin repetir hasta haberlos visto todos.

    Cuando la cola se vacía, se vuelve a llenar con todos los índices en orden
    aleatorio (garantizando que el primero no sea el mismo que el último mostrado).
    Devuelve el nuevo índice.
    """
    if not pool:
        st.session_state[idx_key] = 0
        return 0
    queue = list(st.session_state.get(queue_key, []))
    if not queue:
        indices = list(range(len(pool)))
        random.shuffle(indices)
        current = st.session_state.get(idx_key, -1)
        if len(indices) > 1 and indices[0] == current:
            indices[0], indices[1] = indices[1], indices[0]
        queue = indices
    next_idx = queue.pop(0)
    st.session_state[queue_key] = queue
    st.session_state[idx_key] = next_idx
    return next_idx


def init_all_state() -> None:
    """Inicializa todas las claves de session_state con sus valores por defecto.

    Se llama una sola vez al arranque. Solo escribe las claves que aún no existan,
    preservando el estado de la sesión en curso.
    """
    _all_items = []
    for prep, items in DATA.items():
        for item in items:
            enriched = dict(item)
            enriched["prep"] = prep
            _all_items.append(enriched)

    defaults = {
        # ── Verbos ─────────────────────────────────────────────
        "all_items": _all_items,
        "filtered_items": list(_all_items),
        "current_card_index": 0,
        "quiz_score": 0,
        "quiz_total": 0,
        "quiz_streak": 0,
        "feedback": ("neutral", "Elige categorías y empieza a practicar ✨"),
        "quiz_data": None,
        "study_mode": "Elegir preposición",
        "weak_items": {},
        "gap_index": None,
        "gap_feedback": None,
        "error_index": None,
        "error_feedback": None,
        "dp_index": 0,
        "dp_revealed": False,
        "dp_quiz_ans": None,
        # ── Conectores ─────────────────────────────────────────
        "con_card_index": 0,
        "cng_idx": None,
        "cng_fb": None,
        "cnc_idx": None,
        "cnc_fb": None,
        "cnc_score": 0,
        "cnc_total": 0,
        "cno_idx": 0,
        "cno_shuf": [],
        "cno_fb": None,
        "cnf_item": None,
        "cnc_queue": [],
        "cng_queue": [],
        # ── Gramática ──────────────────────────────────────────
        "gr_subj_idx": None,
        "gr_subj_fb": None,
        "gr_subj_score": 0,
        "gr_subj_total": 0,
        "gr_subj_queue": [],
        "gr_peri_card": 0,
        "gr_peri_idx": None,
        "gr_peri_fb": None,
        "gr_peri_score": 0,
        "gr_peri_total": 0,
        "gr_peri_queue": [],
        "gr_se_idx": None,
        "gr_se_fb": None,
        "gr_se_score": 0,
        "gr_se_total": 0,
        "gr_se_queue": [],
        "gr_pron_idx": None,
        "gr_pron_fb": None,
        "gr_pron_score": 0,
        "gr_pron_total": 0,
        "gr_pron_queue": [],
        "gr_err_idx": 0,
        "gr_err_revealed": False,
        "gr_lect_idx": 0,
        "gr_lect_answers": {},
        "gr_lect_checked": False,
        # ── Vocabulario ────────────────────────────────────────
        "voc_card_idx": 0,
        "voc_rel_words": [],
        "voc_rel_defs": [],
        "voc_rel_checked": False,
        "voc_rel_round_id": 0,
        "voc_comp_idx": 0,
        "voc_comp_score": 0,
        "voc_comp_total": 0,
        "voc_comp_fb": None,
        "voc_clas_words": [],
        "voc_clas_checked": False,
        "voc_clas_round_id": 0,
        # ── Diagnóstico ────────────────────────────────────────
        "diag_step": 0,
        "diag_answers": {},
        "diag_sel": None,
        "nivel_diagnosticado": None,
        # ── Misc ───────────────────────────────────────────────
        "modulo": "🏠 Inicio",
        "tabla_ejercicio": [],
        "tabla_checked": False,
        "tabla_answers": {},
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
