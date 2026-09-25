# Investigación base — BPMN y modelado de procesos (2026)

## Origen

Documento normalizado a partir de la investigación aportada por el supervisor.

## Propósito

El modelado de procesos permite comprender:
- quién hace qué;
- en qué orden;
- qué decisiones existen;
- qué excepciones aparecen;
- qué datos se usan;
- dónde hay esperas, riesgos o retrabajo.

## AS-IS y TO-BE

### AS-IS

Representa cómo funciona realmente el proceso actual.

Debe basarse en:
- entrevistas;
- observación;
- documentación;
- evidencia operativa.

No debe confundirse con el procedimiento "oficial" si la práctica real es distinta.

### TO-BE

Representa el proceso futuro propuesto.

Debe:
- responder a problemas detectados;
- incorporar mejoras validadas;
- mantener restricciones y reglas;
- servir como fuente de requisitos candidatos.

## Elementos básicos BPMN 2.0 aportados

- evento de inicio;
- evento de fin;
- tarea;
- compuerta exclusiva XOR;
- compuerta paralela AND;
- compuerta inclusiva OR;
- pool;
- lane;
- flujo de secuencia;
- flujo de mensaje;
- objeto de datos.

## Buenas prácticas

- un proceso principal por diagrama; usar subprocesos si crece demasiado;
- nombrar actividades con verbo + sustantivo;
- asegurar que cada camino tenga salida válida;
- hacer claras las condiciones de compuertas;
- usar lanes para roles, no personas;
- evitar complejidad gráfica innecesaria;
- documentar reglas de negocio relacionadas;
- validar el modelo con dueños del proceso.

## Derivación de requisitos

Un modelo puede revelar candidatos a:
- requisitos funcionales;
- reglas de negocio;
- requisitos de datos;
- requisitos no funcionales;
- criterios de aceptación.

La derivación automática no equivale a aprobación.

Todo requisito derivado debe conservar el elemento BPMN de origen y pasar por el flujo normal de calidad y validación.
