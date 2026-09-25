# AUDIT_EXISTING_PROJECT v0.1

Propósito: auditar un proyecto de software existente sin asumir que su documentación, implementación, pruebas o afirmaciones de stakeholders son correctas.

## Estados del flujo

### 01 — DESCUBRIR

Identificar la estructura del proyecto, tecnologías, repositorios, sistemas de compilación, ubicaciones de documentación, suites de pruebas, recursos de despliegue e historial disponible.

Salida:
- inventario del proyecto;
- incógnitas;
- superficies iniciales de riesgo.

### 02 — INVENTARIO_DOCUMENTAL

Localizar y clasificar:
- requisitos;
- reglas de negocio;
- historias de usuario;
- criterios de aceptación;
- documentos de arquitectura;
- ADR;
- diagramas;
- contratos de API;
- modelos de datos;
- manuales;
- planes de prueba;
- artefactos de trazabilidad.

Salida:
- mapa documental;
- hallazgos de documentación faltante.

### 03 — MODELO_DE_REQUISITOS

Reconstruir qué se espera que haga el sistema a partir de los artefactos aprobados disponibles.

Salida:
- modelo de requisitos;
- lista de incertidumbres;
- conflictos que requieren investigación.

### 04 — MODELO_DE_REGLAS_DE_NEGOCIO

Extraer las reglas de negocio e identificar sus fuentes, responsables y dependencias.

Salida:
- registro de reglas de negocio;
- reglas contradictorias;
- reglas no verificadas.

### 05 — MODELO_DE_ARQUITECTURA

Reconstruir la arquitectura esperada, los componentes principales, límites, flujos de datos, sistemas externos y decisiones arquitectónicas registradas.

Salida:
- modelo de arquitectura esperada;
- registro de decisiones;
- suposiciones arquitectónicas no documentadas.

### 06 — MODELO_DE_TRAZABILIDAD

Relacionar, cuando exista evidencia, requisitos, reglas, criterios de aceptación, diseño, implementación y pruebas.

Salida:
- matriz de trazabilidad;
- artefactos huérfanos;
- vínculos faltantes.

### 07 — ANALISIS_DE_CODIGO

Inspeccionar la implementación solo después de haber establecido suficiente contexto del proyecto.

Evaluar:
- estructura y límites;
- implementación frente al comportamiento esperado;
- calidad del código;
- manejo de errores;
- tratamiento de datos;
- desviaciones arquitectónicas;
- lógica muerta o duplicada;
- problemas relevantes de SOLID y Código Limpio sin aplicación mecánica.

Salida:
- modelo de implementación;
- discrepancias candidatas;
- hallazgos de deuda técnica.

### 08 — ANALISIS_DE_PRUEBAS

Evaluar las pruebas existentes y qué demuestran realmente.

Evaluar:
- unitarias;
- integración;
- contratos;
- extremo a extremo;
- rutas negativas;
- casos límite;
- regresión.

Salida:
- cobertura por comportamiento, no solo por porcentaje;
- escenarios de prueba faltantes;
- hallazgos sobre pruebas poco confiables.

### 09 — ANALISIS_EN_EJECUCION

Compilar y ejecutar el proyecto cuando sea seguro y razonablemente posible.

Observar:
- inicio del sistema;
- logs;
- fallos en ejecución;
- comportamiento de API;
- comportamiento de datos;
- fallos de integraciones externas;
- síntomas de rendimiento.

Salida:
- modelo del sistema observado;
- fallos reproducibles;
- evidencia en ejecución.

### 10 — ANALISIS_DE_BRECHAS

Comparar:
- sistema esperado;
- sistema implementado;
- sistema observado.

Una diferencia se convierte en un hallazgo que debe investigarse, no en un veredicto automático sobre cuál parte es correcta.

Salida:
- registro de discrepancias;
- candidatos de severidad;
- contradicciones sin resolver.

### 11 — ANALISIS_DE_CAUSA_RAIZ

Para hallazgos relevantes:
1. reproducir cuando sea posible;
2. recopilar evidencia;
3. generar hipótesis plausibles;
4. descartar o respaldar hipótesis;
5. identificar la causa mejor respaldada;
6. registrar el nivel de confianza.

Salida:
- registros de causa raíz;
- hipótesis descartadas;
- causas no resueltas.

### 12 — ANALISIS_DE_RIESGOS

Evaluar el efecto de los hallazgos sobre:
- funcionalidad;
- integridad de datos;
- seguridad;
- mantenibilidad;
- operación;
- cumplimiento cuando corresponda;
- impacto en usuarios.

Salida:
- registro de riesgos;
- fundamento de priorización.

### 13 — RECOMENDACIONES

Para cada problema relevante:
- proponer la corrección preferida;
- ofrecer alternativas cuando aporten valor;
- explicar ventajas, desventajas y compromisos;
- identificar pruebas y documentación que deben actualizarse;
- evitar rediseños injustificados.

### 14 — REVISION_CRITICA

Un revisor independiente intenta refutar:
- hallazgos;
- causas raíz;
- suposiciones;
- severidad;
- recomendaciones.

Los hallazgos relevantes deben sobrevivir esta revisión o reducir su nivel de confianza.

### 15 — INFORME_FINAL

Generar un informe de auditoría respaldado por evidencia que incluya:
- resumen ejecutivo;
- comprensión del proyecto;
- defectos confirmados;
- defectos probables;
- riesgos;
- inconsistencias;
- evidencia faltante;
- deuda técnica;
- brechas de trazabilidad;
- recomendaciones;
- acciones requeridas del supervisor.

## Escalamiento al supervisor

Escalar únicamente cuando el sistema no pueda resolver un asunto internamente con la evidencia disponible.

Toda escalación debe indicar:
- qué se desconoce;
- por qué importa;
- qué se revisó previamente;
- qué información exacta se necesita;
- quién o qué puede proporcionarla;
- qué ocurre si continúa sin conocerse.
