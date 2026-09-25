# SMOKE-001 — Analista Documental y de Requisitos v0.1

## Fecha

2026-09-25

## Objetivo

Realizar inventario documental de JARVIS SDLC sin analizar código, modificar archivos ni usar web.

## Resultado

**PARCIAL**

## PASS observados

- delegación al agente correcto;
- documentación primero;
- acceso read-only;
- sin investigación web;
- sin requisitos inventados;
- incertidumbres visibles;
- sin permisos innecesarios;
- formato general de handoff presente.

## Fallos observados

### F-001 — Conclusión de ausencia sin cobertura suficiente

El agente afirmó ausencias globales sobre áreas cuyo contenido no había inspeccionado completamente.

Causa probable:
no existía una regla suficientemente explícita que separara "no observado" de "no existe".

### F-002 — Conteos inconsistentes

El informe presentó cifras incompatibles con los elementos enumerados.

Causa probable:
conteo manual/no reconciliado antes de entregar.

### F-003 — Ambigüedad sobre control de versiones

La frase "no hay control central de versiones" mezcló:
- Git;
- versionado documental;
- changelog;
- baseline.

### F-004 — Múltiples siguientes acciones

La sección final contenía tres acciones aunque la especificación pedía una sola.

## Severidad

Media.

## Bloquea v1.0

Sí.

## Bloquea continuar evaluando

No.

## Corrección prevista

- protocolo explícito de alcance de evidencia;
- reglas adicionales de decisión;
- checklist de cierre;
- evals específicos;
- nueva ejecución de SMOKE-001.
