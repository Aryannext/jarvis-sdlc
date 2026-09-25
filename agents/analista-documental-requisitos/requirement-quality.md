# Protocolo de evaluación de calidad de requisitos v0.1

## Objetivo

Permitir que el agente determine no solo qué requisitos existen, sino qué defectos de calidad contienen y qué acciones deben tomarse.

## Evaluación individual

Para cada requisito relevante producir una ficha:

```yaml
requisito_id: REQ-000
estado_documental: confirmado | candidato | contradictorio | incompleto | obsoleto | rechazado | desconocido

calidad:
  necesario:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
  apropiado:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
  no_ambiguo:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
  completo:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
  singular:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
  factible:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
  verificable:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
  correcto:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
  conforme:
    resultado: cumple | no_cumple | indeterminado | no_aplica
    evidencia: []
    observacion: ""
```

## Prohibición de puntuación global automática

No producir una nota global como "82/100" salvo que en el futuro se defina y valide un modelo explícito de scoring.

La evaluación debe conservar los defectos por dimensión.

## Clasificación de defectos

Ejemplos:

- AMBIGÜEDAD
- NO_VERIFICABLE
- NO_ATÓMICO
- INCOMPLETO
- SESGO_DE_DISEÑO
- NECESIDAD_NO_JUSTIFICADA
- FACTIBILIDAD_NO_DETERMINADA
- TERMINOLOGÍA_INCONSISTENTE
- FUENTE_NO_TRAZABLE

## Reformulación

Salida recomendada:

```text
REQUISITO ORIGINAL:
...

DEFECTOS:
- ...
- ...

INFORMACIÓN FALTANTE:
- ...

REFORMULACIÓN PROPUESTA:
...

CAMBIO DE SIGNIFICADO POTENCIAL:
sí / no / indeterminado

VALIDACIÓN REQUERIDA:
...
```

Si faltan valores de negocio, mantener marcadores explícitos y no inventarlos.

Ejemplo:

```text
El sistema deberá completar [OPERACIÓN] en menos de [UMBRAL_PENDIENTE]
bajo [CONDICIÓN_PENDIENTE].
```

Esto es preferible a crear una cifra ficticia.

## Calidad del conjunto

Revisar además:

- requisitos contradictorios;
- terminología diferente para el mismo concepto;
- cobertura incompleta de una necesidad;
- requisitos imposibles de satisfacer simultáneamente;
- requisitos sin origen;
- requisitos sin criterios;
- criterios sin requisito;
- dependencias circulares o no declaradas.
