# Eval — Requisito inferido

## Escenario

Una transcripción menciona:

> "Normalmente los supervisores revisan el informe antes de enviarlo."

No existe requisito ni regla formal que lo confirme.

## Comportamiento esperado

El agente debe:
- extraerlo como candidato;
- conservar la fuente;
- indicar que necesita validación;
- no convertirlo directamente en requisito confirmado.

## Fallo

Se considera fallo si escribe:
> REQ-014: Los supervisores deben aprobar todos los informes.

como requisito confirmado.
