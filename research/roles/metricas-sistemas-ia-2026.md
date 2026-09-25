# Investigación base — Métricas para sistemas con IA (2026)

## Origen

Documento normalizado a partir de la investigación aportada por el supervisor.

## Objetivo

Cuando una solución contiene IA, los requisitos deben cubrir no solo funcionalidad clásica sino también calidad de tarea, fidelidad, robustez, fairness, seguridad, operación y comportamiento agentic cuando aplique.

## Categorías aportadas

### Calidad de tarea
- Task Success Rate;
- Accuracy;
- Resolution Rate;
- Precision;
- Recall;
- F1.

### Fidelidad
- Hallucination Rate;
- Groundedness;
- Factual Consistency;
- Relevance.

### Robustez y drift
- Data Drift;
- Concept Drift;
- Prediction Drift;
- PSI;
- KS;
- métricas de robustez.

### Fairness
- Demographic Parity;
- Equalized Odds;
- Disparate Impact;
- métricas de sesgo.

### Seguridad
- Toxicity Rate;
- Jailbreak Resistance;
- Policy Violation Rate;
- Safety Pass Rate.

### Operación
- Latency P50/P95/P99;
- Throughput;
- Error Rate;
- Time to First Token;
- Cost per Task / Workflow.

### Negocio / experiencia
- CSAT;
- Resolution Rate;
- Escalation Rate;
- Reopen Rate;
- Cost per Resolution.

### Agentes
- Tool-call Success Rate;
- Trajectory Quality;
- Plan Stability;
- End-to-End Task Completion;
- Escalation Accuracy.

### RAG
- Retrieval Precision;
- Retrieval Recall;
- Context Relevance;
- Answer Relevance;
- Groundedness.

## Estructura de requisito de métrica

```text
El componente [NOMBRE] deberá mantener [MÉTRICA]
[OPERADOR] [UMBRAL]
medido mediante [MÉTODO]
con frecuencia [FRECUENCIA]
sobre [POBLACIÓN/MUESTRA].
```

Atributos asociados:
- definición exacta de la métrica;
- método;
- dataset/muestra;
- umbral de aceptación;
- umbral de alerta cuando aplique;
- frecuencia;
- responsable;
- acción ante incumplimiento.

## Regla crítica

Los valores objetivo aportados en ejemplos de investigación son ilustrativos.

JARVIS no debe convertirlos en requisitos de un proyecto real sin fuente, autoridad o evidencia contextual.

## Ciclo de vida

1. definición de métricas;
2. dataset/golden set;
3. validación offline;
4. baseline de producción;
5. monitoreo;
6. detección de drift;
7. alertas;
8. Change Request para actualizaciones relevantes;
9. regresión;
10. sign-off;
11. monitoreo continuo.

## Referencias aportadas

La investigación menciona:
- ISO/IEC 25059;
- ISO/IEC 42001;
- NIST;
- EU AI Act;
- trabajos IEEE en desarrollo;
- evaluación humana y LLM-as-judge.

Su aplicabilidad y vigencia deben verificarse por el especialista correspondiente cuando un proyecto real dependa de ellas.
