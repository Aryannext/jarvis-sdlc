# Protocolo BPMN y modelado de procesos v0.1

## Objetivo

Usar modelos de proceso para comprender la realidad actual, diseñar el estado futuro y derivar requisitos de forma trazable.

## 1. Determinar propósito

Antes de modelar decidir si se busca:

- comprender AS-IS;
- descubrir problemas;
- diseñar TO-BE;
- aclarar roles;
- identificar reglas;
- analizar integraciones;
- derivar requisitos.

No modelar solo para producir un diagrama.

## 2. Construir AS-IS

Fuentes preferentes:
- observación;
- entrevistas;
- documentación;
- datos operativos.

Registrar diferencias entre:
- procedimiento oficial;
- proceso descrito;
- proceso observado.

No resolverlas gráficamente sin investigación.

## 3. Analizar AS-IS

Buscar:
- retrabajo;
- esperas;
- pasos manuales;
- duplicación;
- handoffs;
- errores;
- workarounds;
- cuellos de botella;
- controles;
- riesgos;
- puntos sin trazabilidad.

## 4. Diseñar TO-BE

El TO-BE debe basarse en:
- problemas confirmados;
- necesidades validadas;
- restricciones;
- reglas;
- decisiones aprobadas.

No introducir automatización solo porque sea técnicamente posible.

## 5. Elementos básicos

Usar cuando correspondan:
- evento de inicio;
- evento de fin;
- actividad/tarea;
- XOR;
- AND;
- OR;
- pool;
- lane;
- flujo de secuencia;
- flujo de mensaje;
- objeto de datos.

## 6. Reglas de calidad

- actividades con verbo + sustantivo;
- lanes para roles, no nombres personales;
- condiciones de gateway explícitas;
- caminos con final o continuación válida;
- evitar complejidad visual injustificada;
- usar subprocesos si el modelo crece;
- documentar reglas asociadas;
- conservar versión y fuente del modelo.

## 7. Validación

Validar el modelo con dueños del proceso o evidencia equivalente.

Si el stakeholder no entiende el diagrama:
- simplificar;
- complementar con narrativa;
- no asumir que formalidad técnica equivale a claridad.

## 8. Derivación de requisitos

Elementos pueden producir candidatos:

- tareas → requisitos funcionales;
- gateways → reglas de negocio;
- objetos de datos → requisitos de datos;
- eventos/tiempos → requisitos no funcionales;
- caminos → criterios de aceptación.

Todo elemento derivado:
- conserva vínculo al modelo;
- entra como candidato;
- pasa por calidad;
- requiere validación.

## 9. AS-IS y TO-BE separados

Nunca mezclar ambos en un único modelo sin una convención explícita.

Una discrepancia entre AS-IS y TO-BE es información de cambio, no un error automático.

## Salida mínima

- modelo o descripción estructurada;
- alcance;
- actores;
- entradas/salidas;
- decisiones;
- excepciones;
- reglas relacionadas;
- problemas;
- requisitos candidatos;
- incertidumbres;
- evidencia de validación.
