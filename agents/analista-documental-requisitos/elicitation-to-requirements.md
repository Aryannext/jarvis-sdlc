# De elicitación a requisito y criterios de aceptación v0.1

## Objetivo

Evitar que notas, transcripciones o comentarios se conviertan directamente en requisitos sin análisis.

## Pipeline

```text
Insumo crudo
    ↓
Clasificación
    ↓
Necesidad / objetivo
    ↓
Regla / restricción / comportamiento
    ↓
Requisito candidato
    ↓
Evaluación de calidad
    ↓
Criterios de aceptación
    ↓
Validación
    ↓
Requisito confirmado
```

## 1. Clasificar insumo

Etiquetas posibles:
- necesidad;
- dolor;
- objetivo;
- as-is;
- to-be;
- regla;
- restricción;
- supuesto;
- preferencia;
- workaround;
- excepción;
- prioridad percibida;
- evidencia;
- contradicción.

## 2. Encontrar necesidad subyacente

Si el stakeholder propone una solución, no convertirla inmediatamente en requisito.

Preguntar:
- ¿qué problema resuelve?
- ¿quién usa esa capacidad?
- ¿para qué?
- ¿qué resultado espera?
- ¿por qué esa solución?

## 3. Crear requisito candidato

Plantilla orientativa:

```text
[Actor/Sistema] deberá [capacidad]
cuando/bajo [condición]
sujeto a [restricción].
```

No todos los requisitos deben forzarse exactamente a esta sintaxis.

## 4. Aplicar calidad

Evaluar con el protocolo de calidad del agente.

## 5. Crear criterios

Crear únicamente criterios respaldados por información existente.

Cuando falten umbrales o reglas:
- usar marcadores pendientes;
- crear pregunta de elicitación;
- no inventar.

## 6. Validar

Presentar:
- insumo original;
- interpretación;
- requisito propuesto;
- criterios;
- supuestos;
- puntos pendientes.

## 7. Mantener trazabilidad

```text
Sesión/Documento/Observación
        ↓
Hallazgo
        ↓
Necesidad
        ↓
REQ
        ↓
CA
        ↓
Prueba futura
```

## Regla sobre cantidad de CA

La referencia de 3–7 criterios es una heurística práctica, no un límite.

Deben existir los criterios necesarios para expresar la aceptación sin omitir comportamiento material ni crear redundancia.
