"""Integrity checks for the exercise data: catches a typo that would break a question in the app."""

import pytest

import data
from core.config import PREPS

LEVELS = {"B2", "C1", "C2"}

# name -> (exercises, keys every item must have)
EXERCISE_SETS = {
    "GAP_EXERCISES": (data.GAP_EXERCISES, {"frase", "respuesta", "verbo", "explicacion"}),
    "ERROR_EXERCISES": (
        data.ERROR_EXERCISES,
        {"frase_incorrecta", "prep_incorrecta", "prep_correcta", "verbo", "frase_correcta", "explicacion"},
    ),
    "CONECTORES": (data.CONECTORES, {"conector", "funcion", "matiz", "ejemplos", "nivel"}),
    "GAP_EJERCICIOS": (data.GAP_EJERCICIOS, {"frase", "respuesta", "alternativas", "explicacion", "nivel"}),
    "CLASIFICACION_EJERCICIOS": (data.CLASIFICACION_EJERCICIOS, {"conector", "correcta", "opciones", "explicacion"}),
    "TEXTOS_ORDEN": (data.TEXTOS_ORDEN, {"titulo", "partes", "conectores", "pista"}),
    "GR_SUBJUNTIVO": (data.GR_SUBJUNTIVO, {"frase", "respuesta", "tipo", "explicacion", "trampa", "nivel"}),
    "GR_SER_ESTAR": (data.GR_SER_ESTAR, {"frase", "respuesta", "tipo", "explicacion", "trampa", "nivel"}),
    "GR_PRONOMBRES": (data.GR_PRONOMBRES, {"tipo", "pregunta", "opciones", "respuesta", "explicacion", "nivel"}),
    "GR_PERIFRASIS": (
        data.GR_PERIFRASIS,
        {"perifrasis", "significado", "ejemplos", "trampa", "ejercicio", "respuesta", "nivel"},
    ),
    "GR_ERRORES_INGLES": (data.GR_ERRORES_INGLES, {"categoria", "error", "correccion", "explicacion", "extra", "nivel"}),
    "GR_LECTURA": (data.GR_LECTURA, {"titulo", "fuente", "formato", "texto", "preguntas"}),
    "DIAGNOSTICO": (data.DIAGNOSTICO, {"pregunta", "opciones", "respuesta", "area", "nivel", "explicacion"}),
}


@pytest.mark.parametrize("name", EXERCISE_SETS)
def test_every_item_has_its_required_keys(name: str) -> None:
    items, required = EXERCISE_SETS[name]
    assert items, f"{name} is empty"
    for i, item in enumerate(items):
        assert required <= item.keys(), f"{name}[{i}] is missing {required - item.keys()}"


@pytest.mark.parametrize("name", EXERCISE_SETS)
def test_no_blank_strings(name: str) -> None:
    items, required = EXERCISE_SETS[name]
    for i, item in enumerate(items):
        for key in required & {k for k, v in item.items() if isinstance(v, str)}:
            assert item[key].strip(), f"{name}[{i}].{key} is blank"


@pytest.mark.parametrize("name", [n for n, (items, _) in EXERCISE_SETS.items() if "nivel" in items[0]])
def test_levels_are_valid(name: str) -> None:
    for item in EXERCISE_SETS[name][0]:
        assert item["nivel"] in LEVELS


@pytest.mark.parametrize(
    ("items", "answer_key", "options_key"),
    [
        (data.CLASIFICACION_EJERCICIOS, "correcta", "opciones"),
        (data.GR_PRONOMBRES, "respuesta", "opciones"),
        (data.DIAGNOSTICO, "respuesta", "opciones"),
    ],
    ids=["clasificacion", "pronombres", "diagnostico"],
)
def test_the_answer_is_one_of_the_options(items: list[dict], answer_key: str, options_key: str) -> None:
    for item in items:
        assert item[answer_key] in item[options_key]


READING_QUESTION_KEYS = {
    "seleccion_multiple": {"pregunta", "opciones", "respuesta", "explicacion"},
    "verdadero_falso": {"afirmacion", "respuesta", "justificacion"},
    "emparejamiento": {"afirmacion", "respuesta", "explicacion"},
}


def test_reading_questions_follow_their_format() -> None:
    for text in data.GR_LECTURA:
        assert text["formato"] in READING_QUESTION_KEYS, text["titulo"]
        assert text["preguntas"], text["titulo"]
        for question in text["preguntas"]:
            assert READING_QUESTION_KEYS[text["formato"]] <= question.keys(), text["titulo"]


def test_multiple_choice_reading_answer_is_one_of_the_options() -> None:
    for text in data.GR_LECTURA:
        if text["formato"] == "seleccion_multiple":
            for question in text["preguntas"]:
                assert question["respuesta"] in question["opciones"]


def test_every_gap_exercise_can_be_solved_from_its_alternatives() -> None:
    """`respuesta` lists every accepted answer; at least one must be offered, or the learner cannot pass."""
    for item in data.GAP_EJERCICIOS:
        assert set(item["respuesta"]) & set(item["alternativas"]), item["frase"]


def test_preposition_groups_match_the_configured_prepositions() -> None:
    assert set(data.DATA) == set(PREPS)
    for prep, verbs in data.DATA.items():
        assert verbs, f"no verbs for '{prep}'"
        for verb in verbs:
            assert verb["verbo"] and verb["expresion"] and verb["ejemplos"]


def test_prepositional_exercises_use_known_prepositions() -> None:
    for item in data.GAP_EXERCISES:
        assert item["respuesta"] in PREPS
    for item in data.ERROR_EXERCISES:
        assert set(item["prep_correcta"].split(" / ")) <= set(PREPS)


def test_connectors_are_unique() -> None:
    names = [c["conector"].lower() for c in data.CONECTORES]
    assert len(names) == len(set(names))


def test_vocabulary_topics_have_words() -> None:
    for key, topic in data.VOCABULARIO.items():
        assert topic["titulo"] and topic["palabras"], key
