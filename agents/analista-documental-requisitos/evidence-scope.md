# Protocolo de alcance de evidencia v0.1

## Objetivo

Evitar que una revisión parcial produzca conclusiones globales injustificadas.

Principio central:

> Ausencia de evidencia no equivale a evidencia de ausencia.

## Estados de cobertura

Para toda afirmación relevante sobre un repositorio, conjunto documental o sistema, distinguir:

- **identificado**: el artefacto fue localizado;
- **inspeccionado**: el contenido fue revisado suficientemente para la afirmación;
- **inspeccionado_parcialmente**: solo una parte fue revisada;
- **no_inspeccionado**: se conoce su existencia, pero no su contenido;
- **búsqueda_exhaustiva**: se ejecutó una búsqueda suficientemente completa para sostener una conclusión de ausencia.

## Regla de lenguaje

### Cuando NO hubo búsqueda exhaustiva

Usar:

- "No se encontró en los artefactos revisados."
- "No se observó evidencia de..."
- "No puede determinarse todavía si existe..."
- "Estado no determinado para el resto del alcance."

Evitar:

- "No existe..."
- "Ningún artefacto..."
- "El repositorio carece de..."

salvo que la búsqueda realizada permita sostenerlo.

## Registro mínimo de alcance

Toda conclusión global importante debe poder acompañarse de:

```yaml
alcance_evidencia:
  artefactos_identificados: 0
  artefactos_inspeccionados: 0
  artefactos_inspeccionados_parcialmente: 0
  busqueda_exhaustiva: false
  limites:
    - ""
```

Si los conteos no pueden verificarse, usar `desconocido` en la salida narrativa en lugar de inventar una cifra.

## Conteos

Toda cantidad reportada debe provenir de:
- conteo por herramienta;
- lista explícita;
- resultado verificable.

No contar manualmente una lista larga si puede derivarse por herramienta.

Antes de entregar, comprobar consistencia entre:
- total declarado;
- elementos enumerados;
- subtotales por categoría.

## Conclusiones de ausencia

Para afirmar "no existe X", debe cumplirse al menos una de estas condiciones:

1. búsqueda exhaustiva sobre el alcance relevante; o
2. existe una fuente autoritativa que afirma la ausencia; o
3. el alcance está completamente enumerado e inspeccionado.

En otro caso, estado recomendado:
- desconocido;
- no observado;
- no determinado.

## Distinción de niveles

No mezclar:

- control de versiones del repositorio;
- versionado documental;
- changelog;
- baseline;
- historial de decisiones;
- historial de requisitos.

Ejemplo correcto:

```text
Git: observado.
Changelog documental: no encontrado en los artefactos revisados.
Baseline de requisitos: no determinado.
```

No condensar todo como "no hay control de versiones".

## Revisión final obligatoria

Antes de entregar un inventario o auditoría parcial:

1. verificar conteos;
2. revisar cada "no existe";
3. revisar cada "ningún";
4. comprobar que el universo revisado está explícito;
5. separar conclusión del repositorio completo de conclusión sobre la muestra revisada;
6. dejar una sola siguiente acción recomendada.
