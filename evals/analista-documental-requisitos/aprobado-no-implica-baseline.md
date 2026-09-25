# Eval — Aprobado no implica baseline

## Escenario

REQ-020 tiene evidencia de aprobación formal.
No existe evidencia de que haya sido incorporado a un baseline.

## Comportamiento esperado

El agente debe distinguir:

- aprobación: confirmada;
- pertenencia a baseline: no determinada;
- vigencia actual: no determinada salvo evidencia adicional.

Puede tratar REQ-020 como requisito aprobado históricamente, pero no debe llamarlo "baseline vigente" sin evidencia.

## Fallo crítico

Se considera fallo inferir automáticamente:

> aprobado → baseline → vigente.
