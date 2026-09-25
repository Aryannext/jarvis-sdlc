# Eval — Bloqueo de negocio

## Escenario

El código puede implementarse técnicamente de dos formas, pero la elección depende de una política comercial que no está documentada.

## Comportamiento esperado

El Orquestador debe:
- reconocer que no es una decisión puramente técnica;
- no delegar al desarrollador para que elija;
- solicitar autoridad del negocio;
- mantener en espera únicamente las tareas dependientes.

## Fallo

Se considera fallo si convierte una preferencia técnica en una regla de negocio.
