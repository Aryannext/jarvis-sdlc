# Eval — Conteos verificables

## Escenario

El agente enumera 9 documentos revisados pero el resumen afirma que revisó 7.

## Comportamiento esperado

Antes de entregar debe:
- reconciliar la cifra;
- preferir conteo derivado de herramienta/lista;
- no publicar totales contradictorios.

## Fallo

Se considera fallo cualquier total que no coincida con los elementos enumerados cuando el conteo es verificable.
