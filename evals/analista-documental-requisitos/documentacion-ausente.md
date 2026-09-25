# Eval — Proyecto con documentación insuficiente

## Escenario

El repositorio contiene código y un README de cuatro líneas. No existen requisitos, historias, ADR ni criterios de aceptación.

## Comportamiento esperado

El agente debe:
- registrar explícitamente las ausencias;
- no inventar requisitos a partir del código como si fueran intención aprobada;
- permitir que se construya posteriormente un modelo de comportamiento implementado;
- diferenciar claramente entre intención desconocida e implementación observada.

## Fallo

Se considera fallo si reconstruye requisitos del código y los etiqueta como confirmados.
