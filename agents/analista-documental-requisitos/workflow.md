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

## 6. Detectar contradicciones y brechas

Buscar:
- requisitos incompatibles;
- criterios de aceptación que no prueban el requisito;
- historias sin criterio;
- reglas sin fuente;
- documentos más recientes sin evidencia de aprobación;
- procesos as-is y to-be mezclados;
- requisitos expresados como solución sin necesidad identificada;
- requisitos no verificables;
- documentos que mencionan funcionalidades sin requisito asociado.

## 7. Elicitar o preparar elicitación

Si faltan datos:
- formular pregunta exacta;
- indicar a quién debería dirigirse;
- explicar por qué importa;
- registrar qué evidencia sería aceptable.

Si no hay stakeholder disponible, marcar el punto como no validado y escalar según la política del Orquestador.

## 8. Construir trazabilidad

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

## 9. Validar calidad del paquete

Comprobar:
- claridad;
- consistencia;
- completitud razonable;
- trazabilidad;
- posibilidad de prueba;
- ausencia de contradicciones ocultas;
- incertidumbres explícitas.

## 10. Entregar

Generar handoff con:
- documentos revisados;
- requisitos por estado;
- reglas de negocio;
- contradicciones;
- incertidumbres;
- evidencias;
- bloqueos;
- preguntas al supervisor;
- siguiente acción recomendada.

## 11. Mantener

Cuando cambie un documento:
- detectar impacto;
- actualizar relaciones;
- marcar artefactos potencialmente obsoletos;
- solicitar revisión de requisitos afectados;
- no sobrescribir silenciosamente la historia previa.
