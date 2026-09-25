# Investigación base — Calidad de requisitos y criterios de aceptación (2026)

## Origen

Documento normalizado a partir de la investigación aportada por el supervisor.

## Marcos identificados

- ISO/IEC/IEEE 29148 como referencia de ingeniería de requisitos.
- Guías INCOSE de redacción de requisitos.
- BABOK como contexto de análisis.
- INVEST para historias de usuario.
- Given–When–Then / Gherkin como formato frecuente para criterios de aceptación.

## Características de calidad de un requisito individual

La investigación propone evaluar:

- Necessary / Necesario.
- Appropriate / Apropiado.
- Unambiguous / No ambiguo.
- Complete / Completo.
- Singular / Atómico.
- Feasible / Factible.
- Verifiable / Testable / Verificable.
- Correct / Correcto.
- Conforming / Conforme.

## Características del conjunto

El conjunto debe evaluarse por:

- completitud;
- consistencia;
- factibilidad conjunta;
- comprensibilidad;
- trazabilidad.

## Reglas prácticas de redacción identificadas

- utilizar terminología obligatoria de forma consistente;
- evitar superlativos y términos subjetivos;
- evitar expresiones ambiguas;
- preferir una obligación principal por requisito;
- expresar qué se necesita antes que cómo implementarlo;
- utilizar glosario para términos clave;
- tratar la longitud breve como heurística, no como regla absoluta.

## Criterios de aceptación

Deben favorecer:

- especificidad;
- medición cuando aplique;
- decisión pass/fail;
- comportamiento observable;
- atomicidad;
- cobertura suficiente;
- independencia tecnológica salvo restricción aprobada.

Escenarios a considerar según contexto:

- camino feliz;
- errores;
- límites;
- valores vacíos o mínimos;
- concurrencia;
- rendimiento;
- seguridad u otros atributos de calidad.

## Given–When–Then

Formato preferente cuando mejora claridad:

- Given: contexto o precondición.
- When: acción o disparador.
- Then: resultado observable.

No se considera obligatorio para todos los casos.

## INVEST

Para historias de usuario:

- Independent;
- Negotiable;
- Valuable;
- Estimable;
- Small;
- Testable.

## Uso de IA

La IA puede apoyar:
- detección de ambigüedad;
- revisión contra checklists;
- generación de borradores;
- propuesta de reformulaciones;
- propuesta de criterios de aceptación.

La salida de IA no constituye aprobación ni evidencia de negocio.

## Restricción crítica

Cuando falta una métrica, umbral o valor objetivo, el agente debe solicitar la información o identificar su ausencia.

No debe inventar valores como:
- 3 segundos;
- 95 %;
- 99,9 %;
- F1 objetivo;
- tasa máxima de alucinación;

si esos valores no provienen de una fuente válida del proyecto.
