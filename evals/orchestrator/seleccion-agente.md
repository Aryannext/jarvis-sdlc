# Eval — Selección mínima de agente

## Entrada

El supervisor solicita:

> Corrige una errata ortográfica en una sección del README. No cambia comportamiento, requisitos ni arquitectura.

## Comportamiento esperado

El Orquestador debe:
- clasificar la tarea como documental;
- no activar QA, Seguridad, Arquitectura ni Análisis de Negocio;
- delegar solo al agente documental cuando exista;
- registrar el cambio de forma mínima.

## Fallo

Se considera fallo si activa varios especialistas sin justificación.
