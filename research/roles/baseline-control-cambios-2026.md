# Investigación base — Baseline y control de cambios (2026)

## Origen

Documento normalizado a partir de la investigación aportada por el supervisor.

## Baseline

Un baseline es una versión aprobada y congelada de un conjunto de requisitos en un momento determinado.

Debe conservar:
- identificador de versión;
- fecha;
- autoridad de aprobación;
- requisitos incluidos;
- criterios de aceptación;
- prioridad;
- fuente;
- rationale;
- trazabilidad.

Sirve como referencia oficial para diseño, desarrollo, pruebas y aceptación.

## Momento de establecimiento

La investigación aportada propone como momentos frecuentes:
- cierre de análisis/discovery;
- cierre de release o incremento importante;
- después de una validación relevante.

La condición principal es que los requisitos tengan calidad suficiente y exista aprobación válida.

## Control de cambios

Después del baseline, un requisito no debe modificarse informalmente.

Flujo:

1. Change Request;
2. análisis de impacto;
3. evaluación y decisión;
4. implementación del cambio aprobado;
5. actualización de trazabilidad y nueva versión/baseline;
6. comunicación y registro.

## Decisiones posibles

- aprobado;
- aprobado con modificaciones;
- rechazado;
- diferido.

## Análisis de impacto

Debe considerar, según aplique:
- otros requisitos;
- procesos;
- arquitectura;
- diseño;
- código;
- pruebas;
- documentación;
- datos;
- entrenamiento;
- esfuerzo;
- costo;
- plazo;
- riesgos;
- cumplimiento;
- compromisos existentes.

## Predictivo vs ágil

El nivel de formalidad puede cambiar.

Predictivo:
- baseline formal;
- CCB más estructurado.

Ágil:
- baseline por release/incremento;
- cambios más frecuentes;
- control más liviano.

La disciplina de trazabilidad y autoridad sigue siendo necesaria.

## IA

La IA puede:
- detectar artefactos potencialmente impactados;
- proponer análisis;
- comparar versiones;
- preparar reportes;
- actualizar borradores de trazabilidad.

No puede aprobar por sí sola un cambio de negocio ni alterar el baseline oficial sin autoridad.
