import re

from app.core.models import PIIFinding

_CEDULA_PATTERN = re.compile(r"\b[1-9][0-9]{6,9}\b")
_BLOCKED_SEQUENCES = frozenset({"123456789", "111111111"})

_CEDULA_TYPE = "CEDULA"
_CEDULA_SENSITIVITY = "PRIVADO"
_CEDULA_NORM = "Art. 5 Ley 1581/2012 — Dato privado"


def detect_cedulas(texto: str) -> list[PIIFinding]:
    hallazgos: list[PIIFinding] = []
    for coincidencia in _CEDULA_PATTERN.finditer(texto):
        valor = coincidencia.group()
        if valor in _BLOCKED_SEQUENCES:
            continue
        hallazgos.append(
            PIIFinding(
                type=_CEDULA_TYPE,
                value=valor,
                sensitivity=_CEDULA_SENSITIVITY,
                norm=_CEDULA_NORM,
            )
        )
    return hallazgos
