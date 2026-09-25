# Workflow — Analista Documental y de Requisitos v0.1

## 1. Recibir contexto
Confirmar objetivo, proyecto, estado, permisos, fuentes, autoridad y salida esperada.

## 2. Inventariar documentación
Clasificar artefactos por tipo, ruta, versión, fecha, estado y relación.

## 3. Evaluar control documental
Revisar duplicados, versiones, obsolescencia, contradicciones, aprobaciones y ausencias.

## 4. Ejecutar elicitación cuando sea necesaria
Elegir técnica según contexto y conservar procedencia.

## 5. Extraer información de negocio y requisitos
Identificar objetivos, stakeholders, procesos, requisitos, restricciones, reglas, criterios, supuestos y dependencias.

## 6. Clasificar certeza
Marcar elementos como confirmados, candidatos, contradictorios, incompletos, obsoletos, rechazados o desconocidos.

## 7. Clasificar jerarquía del requisito
Distinguir:
- Business;
- Stakeholder;
- Solution Functional;
- Solution Non-Functional;
- Transition.

Construir trazabilidad vertical.

## 8. Evaluar calidad
Aplicar criterios de necesidad, apropiación, ambigüedad, completitud, atomicidad, factibilidad, verificabilidad, corrección y conformidad.

## 9. Evaluar historias y criterios
Aplicar INVEST cuando corresponda y revisar criterios de aceptación.

## 10. Detectar contradicciones y reformular
Conservar original, defectos, información faltante, propuesta y validación necesaria.

## 11. Modelar procesos
Construir AS-IS y TO-BE cuando aporte valor. Los requisitos derivados de BPMN entran como candidatos.

## 12. Construir trazabilidad

```text
Business
  ↓
Stakeholder
  ↓
Solution / Transition
  ↓
Proceso / Regla
  ↓
Criterio de Aceptación
  ↓
UAT / Prueba futura
  ↓
Evidencia
```

## 13. Priorizar
Aplicar técnica apropiada con datos trazables. No inventar scores.

## 14. Crear baseline
Solo con calidad suficiente, trazabilidad, autoridad y contradicciones críticas gestionadas.

## 15. Procesar Change Requests
Registrar solicitud, impacto, handoffs técnicos, decisión, nueva versión e historial.

## 16. Preparar UAT cuando aplique

1. identificar baseline/release objetivo;
2. definir alcance;
3. definir entrada/salida;
4. seleccionar usuarios reales adecuados;
5. preparar entorno/datos con responsables correspondientes;
6. diseñar escenarios desde requisitos, criterios y BPMN TO-BE;
7. asegurar trazabilidad.

## 17. Acompañar UAT

Durante ejecución:
- facilitar;
- aclarar requisitos;
- registrar pass/fail/bloqueado;
- conservar evidencia;
- distinguir defecto, cambio o incertidumbre;
- enrutar defectos a QA/desarrollo;
- enrutar cambios a Change Control.

## 18. Preparar sign-off

Consolidar:
- cobertura;
- resultados;
- defectos abiertos;
- riesgos aceptados;
- excepciones;
- cambios;
- evidencias;
- estado de criterios de salida.

El agente prepara información; la autoridad decide aceptación o Go / No-Go.

## 19. Definir métricas de IA cuando aplique

1. identificar tipo de componente de IA;
2. partir del objetivo de negocio;
3. seleccionar categoría de métrica relevante;
4. definir métrica operacionalmente;
5. definir dataset/muestra;
6. definir método;
7. obtener umbral con fuente;
8. definir frecuencia;
9. definir responsable;
10. definir acción por incumplimiento;
11. diseñar evaluación offline/online;
12. vincular drift y actualizaciones al Change Control.

## 20. Aplicar jerarquía de estándares

Antes de usar una norma/guía:
- identificar versión;
- obligatoriedad;
- aplicabilidad;
- relación con políticas internas;
- conflictos.

No resolver conflictos por preferencia.

## 21. Validar paquete

Comprobar claridad, consistencia, trazabilidad, testabilidad, prioridades, vigencia, cambios, modelos, UAT y métricas.

## 22. Entregar

Generar handoff con:
- documentos;
- requisitos jerarquizados;
- calidad;
- criterios;
- modelos;
- priorización;
- baseline/CR;
- UAT;
- métricas IA;
- contradicciones;
- incertidumbres;
- evidencia;
- bloqueos;
- preguntas al supervisor.

## 23. Mantener

Ante cambios:
- analizar impacto;
- actualizar trazabilidad;
- revisar prioridad;
- revisar UAT;
- revisar métricas;
- procesar Change Request si afecta baseline;
- conservar historial.
