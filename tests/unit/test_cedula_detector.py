"""Tests unitarios TDD — detector de cédula colombiana (Ley 1581/2012)."""

import pytest

from app.core.models import PIIFinding
from app.rules.cedula_detector import detect_cedulas


class TestCedulaDetector:
    def test_detecta_cedula_valida(self):
        texto = "El titular identificado con cédula 1234567890 solicita el crédito."
        hallazgos = detect_cedulas(texto)

        assert len(hallazgos) == 1
        assert hallazgos[0].value == "1234567890"

    def test_rechaza_secuencia_irreal(self):
        texto = "Dato de prueba 123456789 no debe generar hallazgo."
        hallazgos = detect_cedulas(texto)

        assert hallazgos == []

    def test_rechaza_secuencia_repetida(self):
        texto = "Secuencia falsa 111111111 en el documento."
        hallazgos = detect_cedulas(texto)

        assert hallazgos == []

    def test_output_tiene_campos_requeridos(self):
        texto = "CC 1234567890"
        hallazgos = detect_cedulas(texto)

        assert len(hallazgos) == 1
        hallazgo = hallazgos[0]
        assert isinstance(hallazgo, PIIFinding)

        campos_requeridos = {"type", "value", "sensitivity", "norm"}
        assert campos_requeridos.issubset(set(PIIFinding.model_fields.keys()))

        assert hallazgo.type == "CEDULA"
        assert hallazgo.value == "1234567890"
        assert hallazgo.sensitivity == "PRIVADO"
        assert hallazgo.norm == "Art. 5 Ley 1581/2012 — Dato privado"
