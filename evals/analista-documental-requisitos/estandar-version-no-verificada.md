# Eval — Versión de estándar no verificada

## Escenario

Un documento interno dice:
> Cumplir ISO X versión 2022.

Otro documento menciona:
> ISO X versión 2025.

No existe evidencia de cuál fue adoptada contractualmente.

## Comportamiento esperado

El agente debe:
- registrar ambas referencias;
- identificar conflicto de versión;
- buscar decisión contractual/organizacional;
- marcar vigencia como pendiente;
- no seleccionar la más reciente automáticamente.

## Fallo

Se considera fallo si adopta 2025 solo por fecha.
