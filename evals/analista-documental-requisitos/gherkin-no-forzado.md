# Eval — Gherkin no obligatorio

## Entrada

Regla:
> Una contraseña nueva no puede coincidir con ninguna de las últimas 5 contraseñas.

## Comportamiento esperado

El agente puede:
- conservarla como regla verificable;
- acompañarla de escenarios Given–When–Then si aportan valor;
- no considerar el requisito defectuoso solo por no estar escrito originalmente en Gherkin.

## Fallo

Se considera fallo si obliga a convertir toda regla a Gherkin como condición de calidad.
