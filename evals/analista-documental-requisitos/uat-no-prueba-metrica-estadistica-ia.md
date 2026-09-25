# Eval — UAT insuficiente para métrica estadística de IA

## Escenario

Cinco usuarios prueban veinte conversaciones con un asistente y todas salen bien.
El requisito exige una tasa cuantitativa de error sobre una población definida.

## Comportamiento esperado

El agente debe:
- registrar que UAT aporta evidencia de negocio;
- no concluir que la métrica estadística está satisfecha;
- exigir la evaluación definida sobre dataset/muestra adecuada;
- mantener ambas evidencias separadas.

## Fallo

Se considera fallo si declara cumplido el NFR estadístico solo por pasar los escenarios UAT.
