# Skill: Executing Browser Compliance

## Objetivo
Automatizar flujos de verificación de cumplimiento en la interfaz web de FinGuard-AI usando agent-browser CLI de forma eficiente y económica mediante encadenamiento de comandos.

## Casos de Uso Estratégicos
- Subir contratos de crédito en PDF al dashboard local para auditoría automatizada.
- Verificar reportes visuales de PII detectada (Cédulas de Ciudadanía - Ley 1581/2012).
- Confirmar el estado de alertas CUMPLE/NO_CUMPLE bajo la normativa de SARLAFT.

## Patrón Recomendado (Evita llamadas LLM redundantes)
1. Abrir el navegador en el entorno local del dashboard (`http://localhost:8000`).
2. Tomar un screenshot (captura de pantalla) como evidencia digital del estado inicial.
3. Cargar el archivo del contrato en el input correspondiente de forma semántica.
4. Ejecutar una espera pasiva de procesamiento (máximo 30 segundos).
5. Tomar un screenshot final del reporte generado para indexarlo como evidencia inmutable.
6. Validar que los hallazgos de privacidad y topes transaccionales aparezcan reflejados en la UI.

## Nota de Arquitectura
Este skill se encuentra en fase de planeación documental y se activará de forma operativa en la Semana 8, una vez que el backend en FastAPI y el frontend del dashboard estén completamente desplegados en el entorno local.