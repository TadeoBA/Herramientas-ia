# Forma de Trabajo - FinGuard-AI (Compliance Rule Engine)

## Stack Tecnológico
- **Lenguaje**: Python 3.11+
- **Validación de Datos**: Pydantic
- **Detección Determinista**: Regex (Expresiones Regulares)
- **Testing**: Pytest (Obligatorio para TDD)

## Estructura de Carpetas
app/
  ├── core/           # Lógica principal, modelos Pydantic
  ├── rules/          # Motores de regex y evaluación legal
  └── utils/          # Helpers (lectura de archivos, normalización)

tests/
  ├── unit/           # Tests unitarios TDD
  ├── integration/    # Tests de integración con JSON
  └── fixtures/       # Datos sintéticos para pruebas

01-planning/
  └── config_compliance.json # Motor de reglas jurídicas base

## Principios de Desarrollo (Legal Engineering)
1. **TDD Estricto:** Nunca escribir código de implementación sin antes tener un test en `tests/unit/` que falle (RED).
2. **Determinismo Legal:** Las extracciones deben coincidir 100% con los patrones definidos o fallar explícitamente.
3. **Privacidad por Diseño:** Nunca imprimir datos PII en consola mediante `print()`.
4. **Verificación Delegada (QA Multi-Agente):** Queda estrictamente prohibido que el hilo principal ejecute comandos de prueba como `pytest` o verifique formatos de salida de forma directa tras un cambio de código. La responsabilidad de testing se delega por completo en el subagente `@qa-engineer`.
5. **Nomenclatura de Skills:** Usar presente continuo (ej. `detecting_pii_colombia`).

## Protocolo de Ejecución del SubAgente (QA)
- **Invocación Mandatoria:** Una vez completada la implementación de una característica, fix o ajuste normativo en el código, el agente principal debe invocar obligatoriamente a `@qa-engineer`.
- **Contexto Limitado (Evitar Sobre-proveer):** Al llamar al subagente, el hilo principal debe indicarle de forma explícita qué archivos fueron modificados y qué casos de prueba específicos en `tests/unit/` debe ejecutar. No se le permite correr la suite completa a menos que sea necesario.
- **Cierre de Tarea:** El agente principal esperará el reporte técnico en el hilo aislado. Si el veredicto es "PRODUCTION READY", la tarea se da por completada y se procede con la preparación del commit en Git.