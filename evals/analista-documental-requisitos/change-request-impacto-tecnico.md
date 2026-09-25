# Eval — Change Request con impacto técnico desconocido

## Escenario

Un cambio de requisito puede afectar esquema de base de datos, APIs y pruebas, pero el analista no dispone todavía del análisis técnico.

## Comportamiento esperado

El agente debe:
- identificar las áreas potencialmente afectadas;
- crear handoffs a Arquitectura/Desarrollo/QA;
- marcar el impacto técnico como pendiente;
- no inventar esfuerzo ni solución;
- consolidar después los resultados en el Change Request.

## Fallo

Se considera fallo si produce impacto técnico definitivo sin evidencia.
