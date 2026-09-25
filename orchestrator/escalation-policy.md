# Política de Escalamiento al Supervisor v0.1

## Principio

El supervisor no debe convertirse en operador manual del sistema.

JARVIS debe agotar primero las acciones razonables que pueda realizar autónomamente.

## Cuándo escalar

Escalar cuando sea necesario:

1. confirmar una regla de negocio sin fuente autoritativa;
2. resolver una contradicción entre stakeholders o documentos con igual autoridad;
3. obtener información que solo existe en el mundo real;
4. aceptar un riesgo material;
5. autorizar una acción irreversible o de alto impacto;
6. validar interpretación jurídica que requiera profesional competente;
7. proporcionar credenciales o acceso que el sistema no posee;
8. decidir entre alternativas igualmente válidas cuando la decisión sea de negocio.

## Cuándo NO escalar

No preguntar al supervisor:

- si puede abrir un archivo ya autorizado;
- si puede ejecutar una prueba segura dentro del entorno permitido;
- si debe continuar al siguiente estado cuando las condiciones ya se cumplen;
- por información que puede obtener de los artefactos existentes;
- por decisiones técnicas menores que están dentro del mandato del especialista.

## Formato obligatorio

Toda solicitud debe indicar:

- ID;
- prioridad;
- problema;
- por qué importa;
- qué se investigó;
- evidencia disponible;
- qué no pudo resolverse;
- pregunta exacta;
- tipo de evidencia o decisión requerida;
- impacto de no responder;
- qué trabajo puede continuar en paralelo.

## Ejemplo

```yaml
id: SUP-003
prioridad: alta
tipo: regla_negocio
problema: "Existen dos reglas incompatibles sobre eliminación de facturas."
investigado:
  - requisitos
  - historias
  - ADR
  - historial_git
pregunta_exacta: "¿Qué rol tiene autoridad para anular una factura emitida?"
necesita:
  - confirmacion_responsable_proceso
impacto_si_no_responde: "Bloquea validación de REQ-044."
puede_continuar:
  - auditoria_modulo_inventario
  - revision_documentacion
```

## Cola de supervisor

Las solicitudes no críticas deben acumularse y agruparse cuando sea razonable para reducir interrupciones.

Un asunto crítico puede interrumpir inmediatamente si continuar podría producir daño, conclusiones inválidas o trabajo desperdiciado significativo.
