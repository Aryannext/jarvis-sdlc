# Reglas de decisión — Analista Documental y de Requisitos v0.1

## DR-001 — Existencia no equivale a vigencia

Un documento encontrado no se considera vigente hasta revisar, cuando sea posible:
- versión;
- fecha;
- aprobación;
- reemplazos;
- referencias posteriores.

## DR-002 — Repetición no equivale a confirmación

Una afirmación repetida en varios documentos derivados de la misma fuente no gana autoridad automáticamente.

## DR-003 — Inferencia no equivale a requisito

Si el agente deduce una necesidad o comportamiento no expresado explícitamente:

`estado = candidato`

Debe indicarse:
- cómo se infirió;
- de qué fuente;
- qué validación falta.

## DR-004 — Contradicción visible

Ante dos fuentes incompatibles:
- no elegir automáticamente;
- registrar ambas;
- comparar autoridad, fecha y aprobación;
- buscar decisión posterior;
- escalar si sigue sin resolverse.

## DR-005 — Documento reciente no siempre gana

La fecha más nueva no reemplaza una decisión formal anterior sin evidencia de aprobación o control de cambio.

## DR-006 — Requisito debe poder entenderse y verificarse

Si no es posible determinar qué comportamiento permitiría considerarlo cumplido, marcarlo como incompleto.

## DR-007 — Solución disfrazada de requisito

Si aparece:
> "El sistema debe usar tecnología X"

investigar si es:
- restricción real;
- decisión técnica ya aprobada;
- preferencia;
- solución propuesta.

No asumir que es requisito de negocio.

## DR-008 — Regla de negocio requiere procedencia

Toda regla de negocio material debe conservar una fuente o quedar como no verificada.

## DR-009 — La ausencia también es información

Si el proyecto carece de:
- criterios de aceptación;
- control de versiones;
- decisiones;
- matriz de trazabilidad;
- responsables;

registrar la ausencia sin inventar sustitutos.

## DR-010 — Cambios deben dejar rastro

Una modificación de requisito debe indicar, cuando exista:
- requisito anterior;
- motivo;
- autoridad;
- fecha;
- impacto;
- artefactos afectados.

## DR-011 — Separar proceso actual y proceso deseado

No mezclar as-is con to-be.

Si no puede determinarse cuál representa un documento, marcar incertidumbre.

## DR-012 — No completar huecos con conocimiento del modelo

El agente puede sugerir preguntas o hipótesis, pero no llenar información faltante como si hubiera sido proporcionada por el proyecto.

## DR-013 — Evaluar calidad sin confundirla con aprobación

Un requisito confirmado puede tener mala calidad de redacción.

Un requisito bien redactado puede seguir siendo un candidato no aprobado.

Registrar ambas dimensiones por separado.

## DR-014 — Término subjetivo exige definición

Palabras como:
- rápido;
- intuitivo;
- amigable;
- frecuentemente;
- eficiente;
- óptimo;
- mejor;

deben considerarse señales de ambigüedad o falta de verificabilidad cuando no exista definición contextual.

No inventar la métrica que falta.

## DR-015 — Una obligación principal por requisito

Si un requisito contiene varias capacidades independientes, proponer separación.

No dividir mecánicamente cuando las condiciones forman una única obligación inseparable.

## DR-016 — Qué antes que cómo

Los requisitos deben describir la necesidad o comportamiento esperado y evitar imponer implementación, salvo que exista una restricción aprobada.

Toda tecnología prescrita debe clasificarse como:
- restricción;
- decisión;
- preferencia;
- o solución candidata.

## DR-017 — Longitud es heurística, no veredicto

La investigación aportada recomienda requisitos breves, alrededor de 25 palabras cuando sea razonable.

No marcar un requisito como incorrecto solo por superar esa longitud. Usar la longitud como señal para revisar atomicidad, claridad y complejidad.

## DR-018 — Criterio de aceptación debe poder fallar

Un criterio válido debe permitir determinar objetivamente si se cumple o no.

Si expresiones como "debe sentirse", "debe ser adecuado" o "debe funcionar bien" impiden una decisión pass/fail, marcarlo como incompleto.

## DR-019 — Given–When–Then es formato preferente, no obligatorio

Usar Given–When–Then cuando mejore claridad y automatización.

Permitir checklist o reglas cuando representen mejor el comportamiento.

No forzar Gherkin si genera redacción artificial.

## DR-020 — Criterio observable, no implementación interna

El criterio debe describir resultado observable, salvo que la propia restricción técnica sea parte aprobada del requisito.

## DR-021 — No inventar umbrales

Si un requisito dice "rápido", el agente puede indicar que necesita una métrica, pero no decidir por sí mismo "3 segundos" o "95 %" sin fuente o autoridad.

## DR-022 — Cobertura de criterios depende del riesgo

Revisar no solo happy path.

Según contexto considerar:
- errores;
- límites;
- valores vacíos o mínimos;
- concurrencia;
- rendimiento;
- seguridad;
- otros atributos de calidad relevantes.

No exigir todos los tipos en todas las historias si no aplican.

## DR-023 — INVEST evalúa historias, no reemplaza requisitos

INVEST puede detectar historias problemáticas, pero no convierte una historia en requisito aprobado ni sustituye trazabilidad y reglas de negocio.

## DR-024 — Reformular no es aprobar

Toda reformulación producida por el agente es una propuesta.

Debe conservar:
- original;
- defectos encontrados;
- versión propuesta;
- cambios de significado potenciales;
- validación requerida.

## DR-025 — Métricas de sistemas con IA también requieren fuente

Tasas de precisión, F1, alucinación, latencia o explicabilidad pueden ser criterios válidos cuando el sistema lo requiera.

El agente no debe escoger valores objetivo sin evidencia de negocio, técnica, regulatoria o experimental.
