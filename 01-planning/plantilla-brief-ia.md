# Plantilla Maestra de Briefs — Legal AI Engineering
> Autor: [Tu nombre] · Stack: Python + LangChain + Qdrant  
> Jurisdicción base: Colombia — Ley 1581/2012 · Ley 1266/2008 · Regulación SFC  
> Versión: 1.1 · Actualizado: Semana 1 · Programa 10X Builder — LAB10
> Cambios v1.1: Métricas de precisión + ZKP constraint + Idempotencia + Qdrant DoD

---

## INSTRUCCIONES DE USO
1. Copia este archivo para cada nueva tarea
2. Renómbralo: brief-[modulo]-[nombre-tarea].md
3. Completa TODAS las secciones antes de hablar con la IA
4. No empieces a implementar sin validar el Plan
5. Guarda el Brief + Plan como evidencia del proceso BPIR

---

## 1. TÍTULO DE LA TAREA
```
[Nombre claro y específico]
Ejemplo: "Módulo de detección de PII financiera en pagarés"
```

---

## 2. CONTEXTO

### 2.1 Sistema actual
```
[Describe el estado actual del proyecto.
Qué ya existe? En qué punto del FCRE estamos?

Ejemplo: "El módulo de carga de config.json está implementado 
y testeado. Ahora necesito construir el motor de detección 
encima de esa base."]
```

### 2.2 Problema que resuelve
```
[Describe el problema legal o técnico concreto.
Sé específico con la norma que aplica.

Ejemplo: "Los pagarés colombianos deben contener autorización 
expresa de consulta en centrales de riesgo según Art. 13 
Ley 1266/2008. Actualmente no hay detección automatizada 
de esta omisión."]
```

### 2.3 Objetivo de esta tarea
```
[Una sola oración. Qué debe existir al terminar.

Ejemplo: "Función que detecte presencia/ausencia de cláusulas 
obligatorias SFC y retorne resultado estructurado con norma citada."]
```

---

## 3. REQUERIMIENTOS TÉCNICOS

### 3.1 Lenguaje y versión
```
Python 3.11+
```

### 3.2 Librerías aprobadas para esta tarea
```
[ ] click          — CLI
[ ] rich           — output en terminal
[ ] regex          — detección de patrones
[ ] pydantic       — validación de esquemas de datos
[ ] python-docx    — lectura de Word (si aplica)
[ ] langchain      — orquestación de agentes (Semanas 4-8)
[ ] qdrant-client  — base de datos vectorial (Semana 6+)
[ ] ____________   — [agrega solo lo necesario]
```
NOTA: langchain y qdrant-client solo se activan desde Semana 4 y 6 respectivamente.
No usar librerías fuera de esta lista sin aprobación explícita.

### 3.3 Arquitectura y patrones
```
[Cómo debe integrarse con el resto del sistema.

Ejemplo: "Función pura — recibe texto str y config dict, 
retorna lista de findings. Sin efectos secundarios."]
```

### 3.4 Estructura de input
```python
{
    "contract_text": str,   # texto normalizado del contrato
    "rules": dict,          # cargado desde config_compliance.json
    "contract_id": str      # identificador para el reporte
}
```

### 3.5 Estructura de output
```python
{
    "clause_type": str,     # ej: "REQ_01"
    "description": str,     # ej: "Autorización centrales de riesgo"
    "status": str,          # "CUMPLE" | "NO_CUMPLE"
    "location": int,        # posición en el texto
    "norm": str,            # ej: "Art. 13 Ley 1266/2008"
    "evidence": str         # fragmento detectado (max 200 chars)
}
```

---

## 4. CONSTRAINTS

### 4.1 Técnicos
```
[ ] Type hints obligatorios en todas las funciones
[ ] Docstrings en español con descripción + norma aplicable
[ ] Sin llamadas a APIs externas — cero dependencias de red
[ ] Sin almacenamiento del contrato original — procesar y descartar
[ ] Manejo explícito de excepciones — sin bare except
[ ] Sin credenciales hardcodeadas
[ ] Idempotencia: la ejecución sobre el mismo input 
    debe producir siempre el mismo output
[ ] Logs de auditoría: generar rastro de decisiones lógicas
    sin exponer PII en los logs
```

### 4.2 Legales
```
[ ] Clasificar PII según Art. 5 Ley 1581:
    PUBLICO / SEMIPRIVADO / PRIVADO / SENSIBLE
[ ] Cada hallazgo debe citar norma específica
[ ] Omisiones críticas (mandatory: true) marcar como NO_CUMPLE,
    nunca como advertencia
[ ] Output suficiente como evidencia para auditoría SFC
[ ] No modificar archivos fuera del módulo asignado
```

### 4.3 Constraint ZKP — Privacy-by-Design
```
[ ] El diseño debe permitir en el futuro una validación 
    mediante Zero-Knowledge Proofs sin acceso al texto plano.
    
    Esto significa:
    - La lógica de detección debe ser separable del dato original
    - Los resultados deben poder expresarse como afirmaciones 
      verificables: "contiene REQ_01 = TRUE" sin revelar el contrato
    - No acoplar el motor de reglas al almacenamiento del texto
```

### 4.4 Lo que la IA NO debe hacer
```
[ ] No generar todo el sistema de una vez
[ ] No instalar librerías no aprobadas
[ ] No modificar config_compliance.json
[ ] No asumir estructura de archivos diferente al plan aprobado
[ ] No usar ejemplos de código largos en el plan — solo lenguaje natural
```

---

## 5. DEFINITION OF DONE

### 5.1 Funcional
```
[ ] Detecta correctamente los 5 tipos de cláusulas del config
[ ] Detecta correctamente los 5 tipos de PII colombiana
[ ] El campo "norm" cita artículo específico en cada hallazgo
[ ] El reporte CSV tiene: Clausula_Detectada, Estado, Ubicacion, Norma
```

### 5.2 Calidad técnica
```
[ ] Tests unitarios cubren:
    - Caso normal
    - Cláusula ausente
    - PII no encontrada
    - Contrato vacío
    - Input con caracteres especiales (tildes, ñ)
[ ] Código pasa el Protocolo de Review Forense sin items en rojo
[ ] README del módulo explica qué detecta y bajo qué norma
[ ] Commit: feat(modulo): descripción
```

### 5.3 Métricas de precisión — Rigor analítico
```
[ ] Falsos Positivos aceptables: < 5% sobre corpus de prueba
[ ] Falsos Negativos aceptables: < 2% para PII tipo SENSIBLE
    (un FN en dato sensible es riesgo regulatorio real)
[ ] Se incluye análisis de Falso Negativo para PII indirecta
    (ej: "el deudor del pagaré" identifica una persona
    sin mencionar nombre ni cédula)
[ ] Documentar el corpus de prueba usado para calcular métricas
```

### 5.4 Compatibilidad futura con Qdrant
```
[ ] El reporte de salida es 100% compatible con el esquema 
    de Qdrant definido para el FCRE
[ ] Los campos del output pueden mapearse a un vector payload
    sin transformación adicional
```

---

## 6. PROMPT DE PLANIFICACIÓN
Copia este bloque exacto para iniciar la Fase P del BPIR:

```
Basado en el brief anterior, genera un plan de implementación 
paso a paso. NO escribas código aún.

Lista:
- Los archivos que crearás
- Los que modificarás (y por qué)
- La lógica de cada uno en lenguaje natural
- Las dependencias necesarias

Mantén los ejemplos cortos y específicos.

Restricción: Si propones algo fuera de los constraints 
del brief, explica por qué antes de incluirlo.
```

---

## 7. REGISTRO BPIR

| Fase | Estado | Fecha | Notas |
|------|--------|-------|-------|
| Brief | Borrador / Aprobado | | |
| Plan | Pendiente / Validado | | |
| Implementación | Bloque 1 / Bloque 2 / Bloque 3 | | |
| Review | Pendiente / Aprobado | | |

---

## 8. NOTAS DEL ABOGADO
Criterio jurídico que la IA no puede inferir. Obligatorio completar.

```
[Ejemplo: "La cláusula SARLAFT no es opcional aunque el 
contrato sea con persona natural — la Circular SFC 026/2008 
aplica a toda entidad vigilada independiente del tipo de deudor.
Este matiz no está en ninguna documentación técnica."]
```

---
Plantilla creada en el marco del programa 10X Builder — LAB10
Semana 1: Ciclo de Trabajo Colaborativo — BPIR
v1.1: Revisada y aprobada con feedback del tutor
