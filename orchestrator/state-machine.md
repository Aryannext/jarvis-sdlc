# Máquina de estados del Orquestador v0.1

## Objetivo

Convertir los workflows de JARVIS en procesos controlados, observables y reanudables.

Cada estado debe definir:

- entrada mínima;
- agente o capacidad responsable;
- salida requerida;
- condición de aprobación;
- condición de bloqueo;
- transición siguiente.

## Estados del workflow AUDIT_EXISTING_PROJECT

### 01 — DISCOVER

**Entrada mínima**
- ruta o repositorio del proyecto;
- permisos de lectura.

**Responsable inicial**
- Orquestador.

**Salida requerida**
- inventario inicial del proyecto;
- tecnologías detectadas;
- ubicaciones documentales;
- sistemas de build/test;
- incógnitas iniciales.

**Transición**
- éxito → DOCUMENT_INVENTORY;
- proyecto inaccesible → BLOCKED;
- riesgo de acción destructiva → SUPERVISOR_REQUIRED.

### 02 — DOCUMENT_INVENTORY

**Responsable**
- futuro agente documental/requisitos.

**Salida requerida**
- catálogo de documentos;
- clasificación;
- ausencias;
- conflictos documentales iniciales.

**Transición**
- salida válida → REQUIREMENTS_MODEL;
- documentación insuficiente → continuar con advertencia y registrar brecha;
- contradicción crítica → registrar y continuar si no bloquea comprensión básica.

### 03 — REQUIREMENTS_MODEL

**Salida requerida**
- requisitos identificados;
- estado de cada requisito;
- fuentes;
- incertidumbres.

**Transición**
- suficiente contexto → BUSINESS_RULES_MODEL;
- ambigüedad crítica → SUPERVISOR_REQUIRED o RESEARCH_REQUIRED.

### 04 — BUSINESS_RULES_MODEL

**Salida requerida**
- reglas de negocio;
- fuente y autoridad;
- relaciones con requisitos;
- contradicciones.

**Transición**
- contexto suficiente → ARCHITECTURE_MODEL;
- conflicto bloqueante → SUPERVISOR_REQUIRED.

### 05 — ARCHITECTURE_MODEL

**Salida requerida**
- arquitectura esperada;
- componentes;
- flujos;
- decisiones;
- supuestos no documentados.

**Transición**
- válido → TRACEABILITY_MODEL.

### 06 — TRACEABILITY_MODEL

**Salida requerida**
- relaciones entre requisitos, reglas, decisiones, implementación y pruebas cuando existan;
- elementos huérfanos;
- vínculos faltantes.

**Transición**
- válido → CODE_ANALYSIS.

### 07 — CODE_ANALYSIS

**Precondición**
No entrar antes de haber construido contexto documental suficiente, salvo ausencia explícita de documentación.

**Salida requerida**
- modelo de implementación;
- discrepancias candidatas;
- deuda técnica;
- áreas que requieren ejecución o pruebas.

**Transición**
- válido → TEST_ANALYSIS.

### 08 — TEST_ANALYSIS

**Salida requerida**
- inventario de pruebas;
- comportamientos cubiertos;
- comportamientos no cubiertos;
- pruebas sospechosas o insuficientes.

**Transición**
- válido → RUNTIME_ANALYSIS.

### 09 — RUNTIME_ANALYSIS

**Precondición**
- ejecución segura;
- dependencias razonablemente controladas;
- ausencia de riesgo destructivo.

**Salida requerida**
- comportamiento observado;
- errores reproducibles;
- logs/evidencia;
- limitaciones de ejecución.

**Transición**
- ejecutable → GAP_ANALYSIS;
- no ejecutable → GAP_ANALYSIS con limitación registrada.

### 10 — GAP_ANALYSIS

**Salida requerida**
- diferencias entre esperado, implementado y observado;
- hallazgos candidatos;
- contradicciones por investigar.

**Transición**
- hallazgos materiales → ROOT_CAUSE_ANALYSIS;
- sin hallazgos materiales → RISK_ANALYSIS.

### 11 — ROOT_CAUSE_ANALYSIS

**Salida requerida**
- hipótesis;
- evidencia a favor/en contra;
- causa mejor respaldada;
- confianza;
- causas no resueltas.

**Transición**
- válido → RISK_ANALYSIS.

### 12 — RISK_ANALYSIS

**Salida requerida**
- impacto;
- probabilidad cuando pueda justificarse;
- severidad;
- dependencias;
- priorización razonada.

**Transición**
- válido → RECOMMENDATIONS.

### 13 — RECOMMENDATIONS

**Salida requerida**
- solución preferida;
- alternativas;
- trade-offs;
- pruebas necesarias;
- documentación afectada;
- riesgos residuales.

**Transición**
- válido → CRITICAL_REVIEW.

### 14 — CRITICAL_REVIEW

**Responsable**
- agente independiente de revisión crítica.

**Salida requerida**
- objeciones;
- hallazgos confirmados;
- hallazgos debilitados;
- hallazgos rechazados;
- dudas pendientes.

**Transición**
- aprobado → FINAL_REPORT;
- evidencia insuficiente → estado correspondiente;
- bloqueo externo → SUPERVISOR_REQUIRED.

### 15 — FINAL_REPORT

**Salida requerida**
- informe trazable;
- hallazgos por nivel de confianza;
- evidencia;
- recomendaciones;
- acciones requeridas del supervisor.

**Transición**
- final → COMPLETED.

## Estados transversales

### RESEARCH_REQUIRED
Se necesita investigación adicional, pero puede realizarse sin intervención humana.

### SUPERVISOR_REQUIRED
Se necesita información, autoridad o aceptación de riesgo del supervisor.

### BLOCKED
El flujo no puede avanzar por una condición técnica u operativa.

### COMPLETED
El workflow terminó y sus artefactos fueron registrados.

## Regla de reanudación

Todo estado debe poder reconstruirse a partir de archivos persistidos. La continuidad no debe depender únicamente del historial de conversación del modelo.
