# Protocolo UAT v0.1

## Objetivo

Preparar, acompañar y documentar la aceptación de usuario sin confundir UAT con QA técnico ni con aprobación automática de release.

## Responsabilidad del agente

El Analista:
- prepara requisitos, criterios y escenarios;
- asegura trazabilidad;
- ayuda a seleccionar procesos de negocio críticos;
- facilita sesiones;
- aclara requisitos;
- clasifica hallazgos preliminarmente;
- consolida evidencia;
- prepara el sign-off.

El Analista no:
- sustituye a los usuarios reales;
- ejecuta toda la UAT en su lugar;
- decide unilateralmente Go / No-Go;
- cierra defectos técnicos por sí solo.

## 1. Planificación

Definir:
- alcance;
- fuera de alcance;
- baseline/release objetivo;
- usuarios participantes;
- entorno;
- datos;
- criterios de entrada;
- criterios de salida;
- responsables;
- calendario;
- evidencia requerida.

## 2. Validar entrada

Antes de iniciar comprobar, según el proyecto:
- estado de pruebas de sistema/integración;
- defectos abiertos;
- estabilidad del entorno;
- datos;
- casos preparados;
- disponibilidad de usuarios.

Si existe una excepción, debe estar registrada y aceptada por la autoridad correspondiente.

## 3. Diseñar escenarios

Fuentes:
- requisitos;
- criterios de aceptación;
- BPMN TO-BE;
- reglas de negocio;
- casos límite;
- procesos críticos.

Los escenarios deben usar lenguaje de negocio.

## 4. Caso UAT mínimo

```yaml
id: UAT-XXX-000
titulo: ""
prioridad: ""
requisitos_relacionados: []
proceso_relacionado: ""
rol_tester: ""
precondiciones: []
datos_prueba: []
pasos: []
resultados_esperados: []
resultado: pendiente | pass | fail | bloqueado
observaciones: []
evidencias: []
tester: ""
fecha: ""
```

## 5. Ejecución

Durante la sesión:
- los usuarios realizan el proceso;
- se registra resultado;
- se conserva evidencia;
- se permite comportamiento realista, no solo ejecución mecánica del guion;
- se registran problemas de usabilidad o negocio aunque no sean bug técnico.

## 6. Clasificar hallazgos

### Defecto
El sistema no cumple requisito, criterio o regla vigente.

### Cambio
El usuario solicita comportamiento diferente al baseline.

### Bloqueo
No puede ejecutarse el escenario por una dependencia externa.

### Incertidumbre
No hay evidencia suficiente para clasificar.

Cuando exista duda técnica, handoff a QA/Desarrollo.
Cuando sea cambio, handoff a Change Control.

## 7. Re-prueba

Después de una corrección:
- conservar resultado original;
- registrar nueva ejecución;
- vincular defecto/cambio;
- no sobrescribir evidencia histórica.

## 8. Salida y sign-off

Preparar:
- cobertura;
- pass/fail/bloqueados;
- defectos abiertos;
- riesgos aceptados;
- excepciones;
- cambios pendientes;
- evidencia;
- recomendación de estado.

La decisión final pertenece al negocio/autoridad definida.

## Regla de umbrales

Valores como 95 % de éxito o cero defectos altos son posibles criterios de proyecto, no valores universales.

JARVIS debe exigir que los umbrales de entrada/salida tengan fuente o aprobación.
