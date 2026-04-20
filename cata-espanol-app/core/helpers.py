def normalize(text: str) -> str:
    """Normaliza texto para comparaciones: minúsculas, sin espacios extra."""
    return " ".join(text.lower().strip().split())
