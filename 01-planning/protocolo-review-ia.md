# Protocolo de Review Forense — Legal AI Engineering
> Autor: [Tu nombre] · Stack: Python + LangChain + Qdrant  
> Jurisdicción base: Colombia — Ley 1581/2012 · Ley 1266/2008 · Regulación SFC  
> Versión: 1.1 · Actualizado: Semana 1 · Programa 10X Builder — LAB10
> Cambios v1.1: Pinning de versiones + Regex estricto cédula + Chunking

---

## INSTRUCCIONES DE USO
1. Aplica este protocolo ANTES de hacer cualquier commit
2. Documenta el resultado de cada punto: OK / Riesgo bajo / Corregir
3. No hagas commit si hay items marcados como Corregir
4. Guarda el resultado del review como evidencia del proceso BPIR
5. Si no encuentras fallos, pídele a la IA que revise su propio 
   código usando esta checklist

---

## PUNTO 1 — ALUCINACIONES DE LIBRERIAS
La IA puede inventar dependencias o funciones inexistentes.
Un import que no existe es un sistema que no arranca.

### Pregunta clave
¿Todos los imports del código existen en PyPI y son compatibles 
con Python 3.11+?

### Qué revisar
```
[ ] Verificar cada import en documentación oficial o PyPI.org
[ ] Las versiones en requirements.txt están fijadas
    MAL:  pandas>=2.0.0
    BIEN: pandas==2.2.0
    Razón: si una librería se actualiza, pierdes reproducibilidad
           de la auditoría legal
[ ] Confirmar que la librería está en requirements.txt
[ ] Confirmar que la versión es compatible con el entorno
[ ] Verificar que las funciones llamadas existen en esa versión
    (la IA a veces usa funciones de versiones futuras o pasadas)
[ ] Ninguna librería fuera de las aprobadas en el Brief
```

### Librerías aprobadas FCRE v1.0 — Semana 1
```
click · rich · regex · pydantic · python-docx
```

### Resultado
```
Estado: OK / Riesgo bajo / Corregir
Detalle: [documenta aquí cualquier hallazgo]
```

---

## PUNTO 2 — LOGICA LEGAL Y DE NEGOCIO
Los errores más peligrosos no rompen el código — pasan silenciosos
y generan compliance falso. En derecho, un falso negativo
es una sanción de la SFC.

### Pregunta clave
¿La lógica de detección es correcta en todos los escenarios 
legales posibles?

### Qué revisar
```
[ ] Los patrones regex capturan variantes en español e inglés
[ ] Las tildes y la ñ están cubiertas (normalización de texto)
[ ] Una cláusula marcada CUMPLE realmente cumple la norma citada
[ ] Una omisión marcada NO_CUMPLE cita el artículo correcto
[ ] Las cláusulas mandatory:true no pueden marcarse como advertencia
[ ] El regex de cédula no captura números de teléfono (falso positivo)
[ ] El regex de Cédula excluye números secuenciales irreales
    (ej. 123456789 o 111111111 no son cédulas reales)
    La IA tiende a escribir regex laxos — exige validación estricta
[ ] El regex de NIT respeta el formato DIAN: 000000000-0
[ ] Los scores crediticios se clasifican como SENSIBLE, no PRIVADO
```

### Casos límite obligatorios a probar
```
[ ] Contrato vacío: no debe romper, debe retornar findings vacíos
[ ] Contrato en mayúsculas: normalización activa
[ ] Cláusula presente pero mal redactada: CUMPLE o NO_CUMPLE?
[ ] PII en tabla o lista numerada: se detecta igualmente?
[ ] Persona jurídica vs. natural: cambian las reglas PII?
```

### Resultado
```
Estado: OK / Riesgo bajo / Corregir
Detalle: [documenta aquí cualquier hallazgo]
```

---

## PUNTO 3 — SEGURIDAD Y PRIVACIDAD
El sistema procesa datos personales sensibles.
Un log mal configurado puede ser una brecha bajo Ley 1581.

### Pregunta clave
¿El código maneja datos personales de forma segura 
y cumple Privacy-by-Design?

### Qué revisar
```
[ ] El contrato original NO se almacena en disco después del análisis
[ ] Los logs NO exponen PII — solo metadatos (contract_id, timestamp)
[ ] No hay credenciales hardcodeadas en ningún archivo
[ ] Los inputs se validan antes de procesarse
[ ] El CSV exportado NO contiene el texto completo del contrato
[ ] El campo "evidence" está limitado a 200 chars — no expone más
[ ] Sin endpoints sin autenticación (cuando aplique en fases futuras)
[ ] El sistema no hace llamadas a APIs externas
```

### Verificación Privacy-by-Design (ZKP-ready)
```
[ ] La lógica de detección es separable del dato original
[ ] Los resultados se expresan como afirmaciones verificables
    ("contiene REQ_01 = TRUE") sin necesitar el contrato
[ ] El motor de reglas no está acoplado al almacenamiento del texto
```

### Resultado
```
Estado: OK / Riesgo bajo / Corregir
Detalle: [documenta aquí cualquier hallazgo]
```

---

## PUNTO 4 — PERDIDA DE CONTEXTO DEL BRIEF
Cuando el brief es largo, la IA puede olvidar constraints
definidos al inicio. Esto ocurre por desbordamiento de
ventana de contexto.

### Pregunta clave
¿El código respeta TODOS los constraints del Brief aprobado?

### Qué revisar
```
[ ] Las reglas legales residen en config_compliance.json
    y no están hardcodeadas en el código
[ ] El output tiene exactamente las columnas del DoD:
    Clausula_Detectada · Estado · Ubicacion · Norma
[ ] No se modificaron archivos fuera del módulo asignado
[ ] La estructura de archivos coincide con el Plan aprobado
[ ] El texto se fragmenta (chunking) correctamente antes de ser
    analizado, evitando el límite de tokens del modelo
[ ] El código es idempotente: mismo input produce mismo output siempre
[ ] Los logs de auditoría existen pero no exponen PII
```

### Contrasta el código contra
```
[ ] Brief aprobado (sección 4 — Constraints)
[ ] Plan validado (estructura de archivos)
[ ] Definition of Done (sección 5)
```

### Resultado
```
Estado: OK / Riesgo bajo / Corregir
Detalle: [documenta aquí cualquier hallazgo]
```

---

## PUNTO 5 — CRITERIO LEGAL
Este punto no existe en ninguna plantilla genérica.
Es la ventaja diferencial del Legal Engineer.
La IA puede generar código técnicamente correcto
pero jurídicamente inválido.

### Pregunta clave
¿El output del sistema podría ser usado como evidencia 
válida en una auditoría de la SFC o la SIC?

### Qué revisar
```
[ ] Cada hallazgo cita artículo específico — no referencias genéricas
    MAL:  "incumple Ley 1581"
    BIEN: "incumple Art. 17 Ley 1581/2012 — Deber del Responsable"

[ ] El reporte distingue entre omisión crítica y advertencia
    Las omisiones mandatory:true son hallazgos, no sugerencias

[ ] La clasificación de sensibilidad PII es correcta bajo Ley 1581
    Dato de salud, origen étnico, orientación sexual: SENSIBLE
    Nombre, dirección, teléfono: PRIVADO o SEMIPRIVADO

[ ] El sistema no genera falso cumplimiento
    Si una cláusula está presente pero incompleta: NO_CUMPLE
    No basta detectar las palabras clave — el contexto importa

[ ] El reporte tiene timestamp y versión del motor de reglas
    Esto permite reproducir el análisis en una auditoría futura
```

### Métricas de precisión mínimas
```
[ ] Falsos Positivos: < 5% sobre corpus de prueba
[ ] Falsos Negativos en PII SENSIBLE: < 2%
[ ] Corpus de prueba documentado y versionado
```

### Resultado
```
Estado: OK / Riesgo bajo / Corregir
Detalle: [documenta aquí cualquier hallazgo]
```

---

## RESUMEN DEL REVIEW

| Punto | Descripción | Estado | Acción requerida |
|-------|-------------|--------|-----------------|
| 1 | Alucinaciones de librerías | | |
| 2 | Lógica legal y de negocio | | |
| 3 | Seguridad y privacidad | | |
| 4 | Pérdida de contexto del Brief | | |
| 5 | Criterio legal | | |

Decisión final:
```
[ ] APROBADO — listo para commit
[ ] APROBADO CON OBSERVACIONES — corregir antes del siguiente bloque
[ ] RECHAZADO — requiere refactorización antes de continuar
```

Fecha del review:      _______________
Módulo revisado:       _______________
Commit autorizado:     Si / No

---

## PROTOCOLO SI NO ENCUENTRAS FALLOS
Si el código aparentemente está bien, aplica esta estrategia:

```
Prompt para la IA:
"Revisa tu propio código usando esta checklist de 5 puntos.
Para cada punto indica si encontraste algún problema y 
cómo lo corregirías. Actúa como auditor escéptico,
no como el autor del código."
```

---
Protocolo creado en el marco del programa 10X Builder — LAB10
Semana 1: Ciclo de Trabajo Colaborativo — BPIR
v1.1: Incluye criterio legal colombiano como quinto eje diferencial
      Revisado y aprobado con feedback del tutor
