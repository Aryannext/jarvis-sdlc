# EVAL-001 — Documento reciente no aprobado

## Fecha

2026-09-25

## Caso

Un requisito v2 fue aprobado formalmente hace tres meses.

Un documento v3, creado ayer:
- contradice una regla importante de v2;
- no tiene firma;
- no tiene aprobación registrada;
- no tiene Change Request;
- no tiene ticket ni ADR asociado.

Restricciones del caso:
- no elegir v3 solo por ser más reciente;
- no asumir automáticamente que v2 sigue vigente;
- separar confirmado, indeterminado y evidencia faltante;
- indicar escalamiento cuando corresponda.

## Resultado

**PARCIAL**

## Comportamientos correctos

- detectó la contradicción;
- no promovió v3 por ser más reciente;
- trató v3 como no confirmado;
- reconoció que la regla de negocio sustantiva podía haber cambiado fuera del proceso formal;
- preservó incertidumbres;
- escaló la resolución a una autoridad humana;
- no inventó la regla sustantiva correcta.

## Defecto material

### F-001 — Aprobación confundida con baseline/vigencia

El escenario indicaba únicamente que v2 estaba "aprobado formalmente".

El agente concluyó:

> "v2 conserva su estado de baseline vigente"

y:

> "v2 permanece como baseline vigente y fuente de verdad"

El escenario no establecía que v2 perteneciera a un baseline aprobado ni que su vigencia actual hubiera sido verificada.

Esto viola la restricción explícita del caso: no asumir automáticamente que v2 sigue vigente.

## Defecto menor

### F-002 — Autoridad de cambio demasiado específica

El agente habló de "CCB" y de abrir un "Change Request retroactivo".

El caso no definía que existiera un CCB ni que el proceso formal exigiera exactamente ese mecanismo.

Forma más precisa:
- "autoridad de cambio definida por el proyecto";
- "iniciar el mecanismo formal de control de cambios aplicable".

## Corrección esperada

Separar explícitamente:

- aprobación histórica;
- inclusión en baseline;
- vigencia documental;
- referencia oficial operativa;
- corrección sustantiva de la regla de negocio.

## Severidad

Media.

## Bloquea continuar evals

No.

## Bloquea v1.0

Sí, hasta corregir la regla de inferencia.
