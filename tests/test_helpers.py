import pytest

from core.helpers import normalize


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("  Hola   Mundo ", "hola mundo"),
        ("ABC", "abc"),
        ("", ""),
        ("   ", ""),
        ("a\tb\nc", "a b c"),
        ("Sin  Embargo", "sin embargo"),
    ],
)
def test_normalize_lowercases_and_collapses_whitespace(raw: str, expected: str) -> None:
    assert normalize(raw) == expected


def test_normalize_keeps_accents() -> None:
    assert normalize("  Ahí  Está ") == "ahí está"


def test_normalize_is_idempotent() -> None:
    once = normalize("  Por   Tanto ")
    assert normalize(once) == once
