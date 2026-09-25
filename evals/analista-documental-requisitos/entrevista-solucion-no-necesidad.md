# Eval — Stakeholder propone solución

## Entrada

Stakeholder:
> Necesitamos poner un chatbot en la página principal.

## Comportamiento esperado

El agente debe:
- tratar "chatbot" inicialmente como solución propuesta;
- investigar qué problema se pretende resolver;
- preguntar por usuarios, tareas, dolor y resultado esperado;
- no generar automáticamente un requisito de chatbot.

## Fallo

Se considera fallo si convierte la frase directamente en:
> REQ-001: El sistema deberá incluir un chatbot.
