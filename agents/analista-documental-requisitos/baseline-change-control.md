# Protocolo de baseline y control de cambios v0.1

## Objetivo

Mantener una referencia oficial de requisitos aprobados y gestionar modificaciones sin perder trazabilidad.

## Condiciones para crear baseline

Un conjunto puede entrar en baseline cuando:

- los requisitos incluidos tienen estado conocido;
- la calidad es suficiente para su uso;
- los criterios de aceptación relevantes están definidos o las excepciones están registradas;
- la priorización de la versión está validada;
- existe autoridad de aprobación;
- la trazabilidad mínima está disponible;
- las contradicciones críticas están resueltas o explícitamente aceptadas.

## Registro del baseline

Debe conservar:

```yaml
baseline_id: BL-001
version: "1.0"
fecha: ""
aprobadores: []
requisitos: []
artefactos_relacionados: []
riesgos_aceptados: []
estado: propuesto | aprobado | reemplazado | archivado
```

## Distinción previa: requisito aprobado vs baseline

Un requisito aprobado no se considera automáticamente parte de un baseline.

Antes de aplicar reglas de baseline, verificar cuando sea posible:
- si el requisito fue incorporado formalmente a un baseline;
- cuál baseline;
- fecha y autoridad de aprobación;
- si existe una versión posterior;
- si su vigencia actual está confirmada.

La aprobación histórica, la inclusión en baseline y la vigencia son estados distintos.

## Regla fundamental

Un baseline aprobado no se edita silenciosamente.

Toda modificación debe:
- originar o referenciar un Change Request;
- conservar el estado anterior;
- registrar impacto;
- registrar decisión;
- generar una nueva versión cuando corresponda.

## Change Request

Campos mínimos:

- ID;
- fecha;
- solicitante;
- descripción;
- justificación/beneficio;
- requisitos afectados;
- prioridad propuesta;
- impacto conocido;
- riesgos;
- estado;
- autoridad de decisión.

## Análisis de impacto

Evaluar según corresponda:

- requisitos relacionados;
- procesos;
- reglas de negocio;
- arquitectura;
- código;
- datos;
- interfaces;
- pruebas;
- documentación;
- operaciones;
- capacitación;
- cumplimiento;
- costo;
- plazo;
- riesgo;
- release comprometida.

Cuando una dimensión pertenezca a otro especialista, crear handoff. El Analista no debe inventar el impacto técnico.

## Decisión

Estados permitidos:

- aprobado;
- aprobado_con_modificaciones;
- rechazado;
- diferido;
- pendiente.

El agente documenta y ejecuta el proceso documental, pero no sustituye al CCB, Product Owner, sponsor u otra autoridad definida.

## Implementación documental

Tras aprobación:

1. crear o actualizar requisito candidato;
2. aplicar calidad;
3. actualizar criterios;
4. actualizar trazabilidad;
5. actualizar prioridad;
6. preparar nueva versión/baseline;
7. comunicar artefactos afectados;
8. conservar historial.

## Contexto ágil

El control puede ser ligero, pero debe conservar:
- decisión;
- alcance de la versión;
- trazabilidad;
- historial.

No imponer un CCB formal a un equipo pequeño si su gobernanza define otra autoridad.

## IA

Puede:
- comparar versiones;
- detectar artefactos potencialmente afectados;
- preparar borradores de impacto;
- sugerir trazabilidad.

No puede aprobar el cambio ni modificar el baseline oficial por sí sola.
