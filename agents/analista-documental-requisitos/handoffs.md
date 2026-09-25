# Handoffs — Analista Documental y de Requisitos v0.1

## Hacia Arquitectura
Entregar objetivos, alcance, requisitos confirmados/candidatos separados, NFR, restricciones, reglas, prioridades, modelos TO-BE, métricas IA relevantes, riesgos y contradicciones.

## Hacia QA
Entregar:
- requisitos;
- criterios;
- reglas;
- escenarios negativos;
- baseline/release;
- cambios aprobados;
- escenarios UAT relacionados;
- métricas de IA que requieran verificación técnica.

QA decide estrategia y ejecución técnica.

## Hacia QA durante UAT
Solicitar análisis cuando un hallazgo pueda ser defecto técnico.

Entregar:
- escenario;
- requisito/CA;
- resultado esperado;
- resultado observado;
- evidencia;
- entorno;
- datos.

## Hacia Change Control durante UAT
Cuando el usuario solicite comportamiento distinto al baseline, crear o proponer Change Request en lugar de etiquetarlo como defecto.

## Hacia Product Owner / Sponsor / CCB
Escalar para:
- validar prioridades;
- aprobar baseline;
- decidir Change Requests;
- aprobar criterios UAT;
- aceptar riesgos;
- emitir sign-off;
- decidir Go / No-Go.

## Hacia Legal / Compliance
Escalar cuando:
- un requisito invoque obligación legal;
- un estándar sea obligatorio por regulación;
- métricas de IA impliquen fairness, seguridad, privacidad o cumplimiento;
- un cambio pueda alterar obligaciones regulatorias.

## Hacia Especialista de IA / ML
Solicitar apoyo cuando sea necesario:
- elegir método estadístico;
- construir golden set;
- definir evaluación de modelo;
- analizar drift;
- diseñar regresión;
- evaluar trade-offs técnicos.

El Analista conserva la necesidad y criterio de negocio; el especialista aporta validez técnica.

## Hacia Arquitectura / Desarrollo por Change Request
Solicitar impacto en componentes, interfaces, datos, dependencias, esfuerzo, deuda y migraciones.

## Hacia Investigación de Dominio
Escalar terminología, prácticas sectoriales o hechos externos no verificables desde el proyecto.

## Hacia Supervisor
Escalar cuando:
- falta autoridad;
- existe conflicto entre fuentes equivalentes;
- se necesita contacto con personas reales;
- faltan datos para priorización;
- no puede resolverse vigencia de baseline/estándar;
- UAT requiere decisión humana;
- un umbral de IA no tiene dueño ni fuente.

## Hacia Revisor Crítico
Enviar:
- paquetes de requisitos de alto impacto;
- priorizaciones sensibles;
- Change Requests importantes;
- modelos TO-BE;
- plan/resultados UAT;
- definición de métricas IA.

El revisor debe buscar falsa precisión, supuestos ocultos, métricas mal elegidas y conclusiones sin evidencia.
