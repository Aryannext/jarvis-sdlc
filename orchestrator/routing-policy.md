# Política de Enrutamiento v0.1

## Objetivo

Seleccionar la menor cantidad de especialistas necesaria para resolver correctamente una tarea.

## Reglas

### 1. Especialidad antes que cantidad

No se activa un equipo completo por defecto.

Ejemplos:

- corrección documental simple → documentación;
- requisito ambiguo → análisis de negocio/requisitos;
- fallo reproducible de software → análisis técnico + QA;
- autorización insegura → seguridad + análisis de negocio si depende de roles;
- decisión estructural importante → arquitectura + revisión crítica.

### 2. No delegar por comodidad

El Orquestador no debe crear un subagente cuando pueda resolver una tarea puramente coordinativa sin perder calidad.

### 3. No delegar fuera de la disciplina

Si un agente detecta una cuestión fuera de su especialidad debe devolverla como:
- observación;
- posible impacto;
- especialidad sugerida.

No debe resolverla como hecho si no tiene autoridad para ello.

### 4. Contexto mínimo suficiente

Cada tarea delegada debe contener:
- objetivo;
- entradas relevantes;
- restricciones;
- artefactos autorizados;
- salida esperada;
- criterios de finalización.

No debe incluir archivos o conocimiento sin relación con la tarea.

### 5. Paralelismo solo cuando exista independencia real

Se permite trabajo paralelo si:
- las tareas no dependen del resultado de otra;
- las conclusiones puedan reconciliarse;
- el costo de contexto esté justificado.

### 6. Revisión independiente para decisiones materiales

Los hallazgos de alta severidad, cambios arquitectónicos y conclusiones con impacto amplio deben pasar por revisión independiente cuando exista el agente correspondiente.

## Pseudoflujo

```text
recibir tarea
   ↓
clasificar disciplina
   ↓
¿puede resolverla un único especialista?
   ├─ sí → delegar a uno
   └─ no
       ↓
¿las subtareas son independientes?
   ├─ sí → ejecutar en paralelo
   └─ no → ejecutar secuencialmente
       ↓
reconciliar resultados
       ↓
¿existe contradicción?
   ├─ sí → revisor / investigación / supervisor
   └─ no → continuar
```

## Criterio de ahorro de contexto

Si dos agentes necesitarían leer exactamente el mismo conjunto grande de archivos para producir resultados casi idénticos, la duplicación debe justificarse explícitamente.
