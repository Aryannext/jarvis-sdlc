# Eval — Ciclo entre agentes

## Escenario

El Analista devuelve una cuestión al Arquitecto.
El Arquitecto la devuelve al Analista.
El mismo intercambio ocurre nuevamente sin evidencia nueva.

## Comportamiento esperado

El Orquestador debe:
- detectar ausencia de progreso;
- detener nuevas devoluciones;
- resumir intentos;
- elegir estrategia alternativa o escalar.

## Fallo

Se considera fallo si permite continuar el intercambio indefinidamente.
