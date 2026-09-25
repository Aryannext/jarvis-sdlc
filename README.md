# JARVIS SDLC

JARVIS SDLC es un sistema local, multiagente y orientado a ingeniería de software, diseñado para apoyar el ciclo de vida completo del software bajo supervisión humana.

El proyecto se construirá de forma incremental. Los agentes especializados no se definirán a partir de prompts genéricos: cada especialidad será investigada, especificada, probada y versionada antes de incorporarse al sistema.

## Dirección principal

- Supervisor humano y orquestación autónoma.
- Agentes especializados con límites, responsabilidades y entregas claramente definidos.
- La evidencia tiene prioridad sobre la autoridad, las suposiciones o la opinión.
- En proyectos existentes: comprender primero la documentación y el comportamiento esperado antes de juzgar la implementación.
- Diferenciar siempre entre sistema esperado, sistema implementado y sistema observado en ejecución.
- No aceptar automáticamente como correctas las afirmaciones del usuario, la documentación, las pruebas ni el código; deben verificarse y reconciliarse mediante evidencia.
- Escalar al supervisor cuando sea necesaria información del mundo real, autoridad para decidir o exista una ambigüedad que no pueda resolverse internamente.
- Ejecución local en Ubuntu como principio base.
- Motor inicial de IA: Claude Code autenticado mediante Claude Pro, evitando el uso de API de pago.
- La investigación web no se considera verdadera por defecto; las fuentes deben evaluarse antes de incorporarlas al conocimiento del sistema.

## Primer objetivo

El primer flujo completo será:

`AUDIT_EXISTING_PROJECT`

Su propósito es recibir un proyecto de software existente, reconstruir lo que debería hacer a partir de su documentación y artefactos disponibles, inspeccionar la implementación y el comportamiento en ejecución, identificar discrepancias y defectos, investigar sus causas más probables y producir hallazgos respaldados por evidencia.

## Estado

Fase de cimentación.
