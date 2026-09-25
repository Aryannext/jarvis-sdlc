# Protocolo de criterios de aceptación v0.1

## Objetivo

Determinar si los criterios de aceptación permiten verificar objetivamente que una historia o requisito fue satisfecho.

## Propiedades esperadas

Cada criterio debe evaluarse por:

- específico;
- observable;
- verificable;
- pass/fail;
- atómico;
- trazable al requisito o historia;
- libre de implementación innecesaria;
- completo respecto al escenario que cubre.

## Formato

### Given–When–Then

Preferido cuando representa claramente una interacción o comportamiento.

```gherkin
Given <contexto verificable>
When <acción o evento>
Then <resultado observable>
```

### Checklist

Aceptable cuando varios resultados simples no necesitan escenario narrativo.

### Basado en regla

Adecuado para restricciones o tablas de decisión.

## Regla de cobertura

No exigir de forma mecánica todos los escenarios posibles.

Para cada requisito evaluar qué clases son relevantes:

```text
happy path
errores
límites
estado vacío
mínimo/máximo
permisos
concurrencia
rendimiento
seguridad
recuperación
```

La selección debe depender del comportamiento y del riesgo.

## Ejemplo de defecto

```text
CA ORIGINAL:
"La aplicación debe sentirse rápida."

DEFECTO:
No verificable. "Sentirse rápida" no define condición de aprobación.

ACCIÓN:
Solicitar:
- operación concreta;
- contexto de medición;
- umbral;
- población/percentil si corresponde.

PROHIBIDO:
Inventar "menos de 3 segundos".
```

## Relación con QA

Este agente evalúa si el criterio está bien definido.

QA determina posteriormente:
- cómo probarlo;
- qué técnica de prueba utilizar;
- qué datos usar;
- si el sistema realmente lo satisface.

No confundir definición del criterio con ejecución de pruebas.

## Criterios para sistemas con IA

Cuando exista un componente de IA, pueden ser necesarios criterios sobre:

- calidad de respuesta;
- precisión;
- recuperación;
- tasa de error;
- seguridad;
- latencia;
- comportamiento ante incertidumbre;
- explicabilidad;
- robustez.

No asumir que una métrica concreta es adecuada solo porque es común.

El tipo de métrica, conjunto de evaluación y umbral deben justificarse.
