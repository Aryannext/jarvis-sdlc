# Workflow — Analista Documental y de Requisitos v0.1

## 1. Recibir contexto

Confirmar:
- objetivo de la tarea;
- proyecto;
- estado del workflow;
- permisos;
- fuentes disponibles;
- salida esperada.

No iniciar análisis profundo si el objetivo no está claro.

## 2. Inventariar documentación

Localizar y clasificar artefactos por:
- tipo;
- ruta;
- versión;
- fecha;
- estado;
- relación con el proyecto.

No interpretar todavía todo el contenido. Primero conocer qué existe.

## 3. Evaluar control documental

Revisar:
- duplicados;
- versiones;
- documentos sin fecha;
- documentos sin responsable;
- referencias rotas;
- documentación obsoleta;
- documentos contradictorios;
- evidencias de aprobación;
- artefactos faltantes.

Registrar problemas documentales por separado de problemas funcionales.

## 4. Extraer información de negocio y requisitos

Identificar:
- necesidades;
- objetivos;
- stakeholders;
- procesos;
- requisitos funcionales;
- requisitos no funcionales;
- restricciones;
- reglas de negocio;
- criterios de aceptación;
- supuestos;
- dependencias.

Todo elemento extraído debe conservar vínculo con su fuente.

## 5. Clasificar certeza

Para cada elemento:
- confirmado;
- candidato;
- contradictorio;
- incompleto;
- obsoleto;
- rechazado;
- desconocido.

No promover un candidato a confirmado solo porque aparezca repetido varias veces si todas las referencias provienen de la misma fuente no validada.

## 6. Evaluar calidad del requisito individual

Para cada requisito relevante evaluar, según aplique:

- necesario;
- apropiado al nivel de abstracción;
- no ambiguo;
- completo;
- singular/atómico;
- factible;
- verificable;
- correcto respecto a la necesidad conocida;
- conforme a las reglas de redacción del proyecto.

No basta con marcar "malo". Para cada defecto indicar:
- característica incumplida;
- fragmento problemático;
- por qué genera riesgo;
- información que falta;
- propuesta de mejora cuando pueda hacerse sin inventar significado.

## 7. Evaluar calidad del conjunto

Revisar el conjunto por:
- completitud;
- consistencia;
- factibilidad conjunta;
- comprensibilidad;
- trazabilidad;
- terminología coherente.

Un requisito individual puede ser correcto y aun así entrar en conflicto con otro.

## 8. Evaluar historias de usuario

Cuando existan historias de usuario, aplicar INVEST como marco de revisión:

- Independiente;
- Negociable;
- Valiosa;
- Estimable;
- Pequeña;
- Comprobable.

No rechazar automáticamente una historia por incumplir una letra. Registrar el impacto y proponer división, aclaración o validación según contexto.

## 9. Evaluar criterios de aceptación

Comprobar que cada criterio relevante sea:
- específico;
- medible cuando la naturaleza del requisito lo permita;
- evaluable como pass/fail;
- observable desde el comportamiento esperado;
- atómico;
- suficiente para el escenario que pretende cubrir;
- independiente de detalles de implementación salvo restricción aprobada.

Revisar cobertura de:
- camino feliz;
- errores;
- casos límite;
- estados vacíos o mínimos;
- concurrencia cuando aplique;
- rendimiento u otros atributos de calidad cuando aplique.

Cuando sea útil, proponer Given–When–Then:
- Given: contexto o precondición;
- When: acción o disparador;
- Then: resultado observable.

No inventar métricas para convertir un criterio subjetivo en medible.

## 10. Detectar contradicciones y brechas

Buscar:
- requisitos incompatibles;
- criterios de aceptación que no prueban el requisito;
- historias sin criterio;
- criterios que prueban solo una parte del requisito;
- reglas sin fuente;
- documentos más recientes sin evidencia de aprobación;
- procesos as-is y to-be mezclados;
- requisitos expresados como solución sin necesidad identificada;
- requisitos no verificables;
- documentos que mencionan funcionalidades sin requisito asociado;
- términos vagos o subjetivos;
- múltiples obligaciones mezcladas en una sola oración;
- restricciones técnicas sin justificación.

## 11. Proponer reformulación

Cuando un requisito esté mal formulado:

1. conservar el original;
2. enumerar defectos;
3. identificar información faltante;
4. proponer una versión mejorada solo si el significado puede conservarse;
5. proponer criterios de aceptación separados;
6. marcar la reformulación como propuesta hasta que sea validada.

La reformulación no reemplaza silenciosamente al requisito original.

## 12. Elicitar o preparar elicitación

Si faltan datos:
- formular pregunta exacta;
- indicar a quién debería dirigirse;
- explicar por qué importa;
- registrar qué evidencia sería aceptable.

Si no hay stakeholder disponible, marcar el punto como no validado y escalar según la política del Orquestador.

## 13. Construir trazabilidad

Relacionar cuando exista evidencia:

```text
Necesidad
   ↓
Requisito
   ↓
Regla de negocio
   ↓
Historia / caso de uso
   ↓
Criterio de aceptación
   ↓
Decisión relacionada
```

Las relaciones con código y pruebas pueden completarse posteriormente por otros estados del workflow.

## 14. Validar calidad del paquete

Comprobar:
- claridad;
- consistencia;
- completitud razonable;
- trazabilidad;
- posibilidad de prueba;
- calidad de criterios de aceptación;
- ausencia de contradicciones ocultas;
- incertidumbres explícitas.

## 15. Entregar

Generar handoff con:
- documentos revisados;
- requisitos por estado;
- resultados de calidad;
- criterios de aceptación y defectos;
- reglas de negocio;
- contradicciones;
- incertidumbres;
- evidencias;
- bloqueos;
- preguntas al supervisor;
- siguiente acción recomendada.

## 16. Mantener

Cuando cambie un documento:
- detectar impacto;
- actualizar relaciones;
- marcar artefactos potencialmente obsoletos;
- solicitar revisión de requisitos afectados;
- revisar criterios de aceptación relacionados;
- no sobrescribir silenciosamente la historia previa.
