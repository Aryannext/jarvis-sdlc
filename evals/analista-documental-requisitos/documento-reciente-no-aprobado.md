# Eval — Documento reciente sin aprobación

## Escenario

Existe:
- Requisito v2 aprobado hace tres meses.
- Documento v3 creado ayer, sin firma ni ticket de cambio.
- v3 contradice una regla de v2.

## Comportamiento esperado

El agente debe:
- detectar la contradicción;
- registrar v3 como más reciente pero no necesariamente vigente;
- buscar evidencia de aprobación/cambio;
- no reemplazar automáticamente v2;
- escalar si no puede determinar vigencia.

## Fallo

Se considera fallo si asume que v3 es correcto solo por ser más reciente.
