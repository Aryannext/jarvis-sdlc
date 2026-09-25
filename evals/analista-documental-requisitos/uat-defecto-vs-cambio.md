# Eval — UAT: defecto vs cambio

## Escenario

Baseline:
> El sistema muestra el costo de envío antes del pago.

Durante UAT el usuario confirma que eso funciona, pero pide además mostrar una comparación de tres transportistas.

## Comportamiento esperado

El agente debe:
- marcar el requisito vigente como cumplido respecto a ese punto;
- registrar la nueva solicitud como cambio/mejora candidata;
- no etiquetarla como defecto;
- enrutarla a Change Control.

## Fallo

Se considera fallo si declara que la implementación actual es defectuosa solo porque el usuario desea funcionalidad adicional.
