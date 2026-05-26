# Skill: Detecting PII Colombia

## Objetivo
Implementar el motor de detección de Cédulas de Ciudadanía Colombianas (Dato Privado según Ley 1581) utilizando la metodología TDD (Test-Driven Development) y validación estricta.

## Requisitos Legales y Técnicos
- **Patrón Base:** La detección debe buscar números de identificación de entre 7 y 10 dígitos.
- **Restricción de Seguridad (Caso Borde):** Debe excluir e ignorar secuencias obvias o falsas de prueba (ej. "123456789", "111111111", "000000000") para evitar falsos positivos en la auditoría.
- **Estructura de Datos:** El resultado final debe ser devuelto usando un esquema estructurado de Pydantic llamado `PIIFinding`.

## Flujo TDD Requerido (Paso a Paso)
1. [x] Crear la carpeta de pruebas `tests/unit/` en la raíz del proyecto.
2. [x] Crear el archivo de pruebas `tests/unit/test_cedula_detector.py` con los casos de prueba (Válido, Excluido, Tipo de dato inválido).
3. [x] Ejecutar `pytest` en la terminal para verificar que los tests fallan debido a que la implementación no existe (Estado RED).
4. [x] Crear la estructura de la aplicación en `app/core/models.py` y `app/rules/cedula_detector.py`.
5. [x] Escribir el código mínimo para hacer que todos los tests pasen a verde (Estado GREEN).