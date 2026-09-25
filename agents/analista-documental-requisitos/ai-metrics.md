# Protocolo de métricas para sistemas con IA v0.1

## Objetivo

Convertir calidad de IA en requisitos verificables, medibles y trazables sin usar métricas de moda ni umbrales inventados.

## 1. Clasificar el tipo de componente

Determinar si el sistema incluye:
- clasificación/predicción;
- LLM/generación;
- RAG;
- agente;
- recomendador;
- combinación.

No todas las métricas aplican a todos los sistemas.

## 2. Partir del objetivo de negocio

Antes de elegir una métrica preguntar:

- ¿qué tarea debe resolver?
- ¿qué fallo importa?
- ¿qué daño produce un falso positivo/falso negativo?
- ¿cuándo debe escalar a humano?
- ¿qué atributo de confianza importa?

## 3. Categorías disponibles

### Calidad de tarea
Task Success, Accuracy, Precision, Recall, F1, Resolution Rate.

### Fidelidad
Hallucination Rate, Groundedness, Factual Consistency, Relevance.

### Robustez
Data Drift, Concept Drift, Prediction Drift y medidas relacionadas.

### Fairness
Métricas de diferencia entre grupos cuando sean legítimas y aplicables.

### Seguridad
Toxicity, Policy Violation, jailbreak/safety evaluation.

### Operación
Latency, TTFT, Throughput, Error Rate, Cost.

### Negocio / experiencia
CSAT, Escalation, Reopen, Cost per Resolution.

### Agentes
Task Completion, Tool-call Success, Escalation Accuracy, Trajectory/Plan Stability.

### RAG
Retrieval Precision/Recall, Context Relevance, Answer Relevance, Groundedness.

## 4. Definir la métrica

Todo requisito de métrica debe especificar:

- nombre;
- definición operacional;
- fórmula/protocolo;
- población/dataset;
- método de evaluación;
- frecuencia;
- umbral de aceptación;
- umbral de alerta cuando aplique;
- responsable;
- acción ante incumplimiento;
- fuente del umbral.

## 5. Plantilla

```yaml
id: SOL-NFR-AI-000
componente: ""
categoria: ""
metrica: ""
definicion: ""
operador: ""
umbral: ""
fuente_umbral: ""
metodo_medicion: ""
dataset_muestra: ""
frecuencia: ""
responsable: ""
umbral_alerta: ""
accion_incumplimiento: ""
traza_a: []
```

## 6. Evaluación offline

Antes de producción, cuando aplique:
- definir golden set;
- versionar dataset;
- medir baseline;
- revisar segmentos;
- ejecutar regresión.

## 7. Monitoreo en producción

Definir qué métricas:
- son online;
- requieren muestreo;
- requieren evaluación humana;
- pueden usar LLM-as-judge;
- necesitan revisión periódica.

## 8. Drift

Registrar:
- señal;
- método;
- frecuencia;
- umbral;
- respuesta.

No declarar drift únicamente por una variación sin criterio previamente definido.

## 9. Trade-offs

Registrar relaciones como:
- calidad vs latencia;
- calidad vs costo;
- seguridad vs cobertura;
- autonomía vs escalamiento;
- precisión vs recall.

El agente no optimiza una métrica ignorando las demás sin una prioridad explícita.

## 10. Actualizaciones de modelo/agente

Cambios significativos en:
- modelo;
- prompt;
- herramientas;
- retrieval;
- política;
- dataset;

pueden requerir Change Request, nuevo baseline de métricas y regresión según riesgo.

## 11. UAT

UAT puede incluir escenarios de IA orientados al negocio, pero no sustituye una evaluación estadística cuando la métrica requiere un dataset suficientemente grande.

## Regla crítica

Los umbrales de ejemplos o benchmarks externos son referencias, no requisitos del proyecto.

JARVIS no los adopta sin justificación y aprobación.
