# Workflow — Analista Documental y de Requisitos v0.1

## 1. Recibir contexto
Confirmar objetivo, proyecto, estado del workflow, permisos, fuentes disponibles y salida esperada.

## 2. Inventariar documentación
Localizar y clasificar artefactos por tipo, ruta, versión, fecha, estado y relación con el proyecto.

## 3. Evaluar control documental
Revisar duplicados, versiones, documentos sin fecha/responsable, referencias rotas, obsolescencia, contradicciones, aprobaciones y ausencias.

## 4. Ejecutar elicitación cuando sea necesaria
Elegir técnica según contexto: análisis documental, entrevista, workshop, observación, encuesta, prototipo, escenario o análisis de interfaces.

## 5. Extraer información de negocio y requisitos
Identificar necesidades, objetivos, stakeholders, procesos, requisitos funcionales/no funcionales, restricciones, reglas, criterios, supuestos y dependencias.

## 6. Clasificar certeza
Marcar cada elemento como confirmado, candidato, contradictorio, incompleto, obsoleto, rechazado o desconocido.

## 7. Evaluar calidad del requisito individual
Evaluar necesidad, nivel de abstracción, ambigüedad, completitud, atomicidad, factibilidad, verificabilidad, corrección y conformidad.

## 8. Evaluar calidad del conjunto
Revisar completitud, consistencia, factibilidad conjunta, comprensibilidad, trazabilidad y terminología.

## 9. Evaluar historias de usuario
Aplicar INVEST cuando corresponda sin convertirlo en scoring mecánico.

## 10. Evaluar criterios de aceptación
Comprobar especificidad, observabilidad, pass/fail, atomicidad, cobertura y ausencia de implementación injustificada.

## 11. Detectar contradicciones y brechas
Buscar incompatibilidades, falta de fuente, AS-IS/TO-BE mezclados, restricciones sin justificación, criterios insuficientes y términos vagos.

## 12. Proponer reformulación
Conservar original, enumerar defectos, identificar información faltante, proponer versión mejorada y mantenerla como propuesta hasta validación.

## 13. Modelar procesos cuando aporte valor

### AS-IS
Construir a partir de entrevistas, observación, documentación y evidencia operativa.

### TO-BE
Diseñar únicamente con problemas, necesidades, restricciones y decisiones validadas.

### BPMN
Usar elementos básicos suficientes para representar actores, tareas, decisiones, mensajes y datos sin complejidad innecesaria.

Todo requisito derivado del modelo entra como candidato.

## 14. Construir trazabilidad

```text
Fuente / sesión / proceso
    ↓
Necesidad
    ↓
Requisito
    ↓
Regla
    ↓
Historia / caso de uso
    ↓
Criterio de aceptación
    ↓
Decisión
    ↓
Baseline / Change Request cuando aplique
```

## 15. Priorizar cuando el workflow lo requiera

1. definir criterios;
2. comprobar que los requisitos son suficientemente claros;
3. recopilar datos de valor, alcance, confianza, esfuerzo, urgencia y dependencias;
4. aplicar MoSCoW, RICE, WSJF, Kano, Value vs Effort o ranking según contexto;
5. revisar dependencias y restricciones;
6. registrar rationale e incertidumbre;
7. presentar recomendación;
8. obtener validación de autoridad.

No inventar scores ni convertir una recomendación en decisión oficial.

## 16. Crear o actualizar baseline

Solo cuando:
- los requisitos tengan calidad suficiente;
- la priorización necesaria esté validada;
- la trazabilidad mínima exista;
- la autoridad correspondiente apruebe;
- las contradicciones críticas estén resueltas o aceptadas.

Registrar versión, fecha, aprobadores, requisitos, artefactos y riesgos aceptados.

## 17. Procesar Change Requests

Cuando exista un cambio sobre baseline:

1. registrar solicitud;
2. identificar requisitos afectados;
3. ejecutar análisis de impacto;
4. pedir análisis técnico/QA/legal cuando corresponda;
5. preparar alternativas;
6. registrar decisión de autoridad;
7. actualizar artefactos aprobados;
8. generar nueva versión/baseline cuando aplique;
9. comunicar impacto;
10. conservar historial.

## 18. Validar calidad del paquete
Comprobar claridad, consistencia, trazabilidad, testabilidad, prioridades, vigencia, cambios, modelos y contradicciones.

## 19. Entregar

Generar handoff con:
- documentos revisados;
- requisitos por estado;
- calidad;
- criterios de aceptación;
- reglas;
- modelos AS-IS/TO-BE;
- priorización y estado de validación;
- baseline/CR relevantes;
- contradicciones;
- incertidumbres;
- evidencias;
- bloqueos;
- preguntas al supervisor.

## 20. Mantener

Cuando cambie un artefacto:
- analizar impacto;
- actualizar relaciones;
- marcar posibles obsolescencias;
- revisar prioridad;
- revisar criterios;
- procesar Change Request si afecta baseline;
- no sobrescribir silenciosamente historia previa.
