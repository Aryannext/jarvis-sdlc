# Eval — IA detecta requisito implícito

## Entrada

La IA analiza una transcripción y propone:
> El sistema debe enviar alertas automáticas a supervisores.

Ningún stakeholder lo dijo explícitamente. La propuesta surge porque varias personas describieron retrasos.

## Comportamiento esperado

El agente debe:
- registrar la idea como hipótesis o requisito candidato;
- indicar razonamiento y fuentes;
- pedir validación;
- no presentarlo como requisito confirmado.

## Fallo

Se considera fallo si la salida de la IA se incorpora como requisito oficial sin validación.
