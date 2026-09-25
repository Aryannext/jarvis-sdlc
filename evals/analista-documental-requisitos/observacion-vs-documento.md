# Eval — Observación contradice procedimiento

## Escenario

Manual:
> Toda devolución requiere aprobación del supervisor.

Observación:
Tres operadores procesan devoluciones sin aprobación durante una sesión observada.

## Comportamiento esperado

El agente debe:
- registrar discrepancia entre proceso documentado y observado;
- no concluir inmediatamente que el manual está mal;
- investigar si existe excepción, incumplimiento, cambio no documentado o contexto particular;
- mantener ambas evidencias.

## Fallo

Se considera fallo si reemplaza la regla documental por la observación sin investigación.
