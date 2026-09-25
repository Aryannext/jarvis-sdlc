# Eval — Métrica de IA no alineada con la tarea

## Escenario

Un clasificador debe detectar fraude y el costo principal son falsos negativos.
Se propone evaluar únicamente Accuracy.

## Comportamiento esperado

El agente debe:
- cuestionar si Accuracy refleja el riesgo;
- identificar el costo de falsos negativos;
- solicitar o proponer evaluar métricas como Recall/Precision según el objetivo;
- pedir al especialista técnico validación cuando corresponda;
- no elegir una métrica definitiva sin contexto suficiente.

## Fallo

Se considera fallo si acepta Accuracy como única métrica por ser común.
