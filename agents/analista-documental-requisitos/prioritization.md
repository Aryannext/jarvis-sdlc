# Protocolo de priorización de requisitos v0.1

## Objetivo

Definir cómo el agente prepara, analiza y documenta prioridades sin apropiarse de una decisión que pertenece a negocio o producto.

## Precondiciones

Antes de priorizar, comprobar:

- que el requisito sea suficientemente comprensible;
- que exista rationale o necesidad identificable;
- que las dependencias conocidas estén registradas;
- que esfuerzo, valor, alcance o urgencia usados en la técnica tengan fuente o supuesto explícito;
- que los participantes con autoridad estén identificados.

## Selección de técnica

### MoSCoW

Usar cuando se necesita:
- definir alcance de release;
- separar imprescindibles de diferibles;
- facilitar discusión de stakeholders.

Interpretación:

- **Must**: sin el requisito, el objetivo mínimo, obligación crítica o viabilidad de la versión falla;
- **Should**: alto valor, pero puede diferirse temporalmente;
- **Could**: deseable si existe capacidad;
- **Won't**: fuera de alcance de esta versión.

La referencia del 60 % máximo de capacidad en Must es una heurística de control, no una regla absoluta.

### RICE

Usar cuando existan datos o estimaciones suficientes sobre:
- Reach;
- Impact;
- Confidence;
- Effort.

Fórmula:

```text
(Reach × Impact × Confidence) / Effort
```

Registrar el origen de cada dato.

### WSJF

Usar cuando importe especialmente:
- costo de retraso;
- criticidad temporal;
- reducción de riesgo;
- tamaño del trabajo.

No calcular si el Cost of Delay o Job Size carecen de estimación.

### Kano

Usar cuando exista evidencia de usuarios suficiente para clasificar impacto en satisfacción.

### Value vs Effort

Usar como técnica rápida de discusión, no como sustituto de análisis detallado cuando el riesgo sea alto.

## Flujo

1. definir criterios;
2. preparar requisitos;
3. obtener datos;
4. aplicar técnica;
5. revisar dependencias;
6. revisar restricciones y compliance;
7. detectar conflictos;
8. registrar rationale;
9. presentar recomendación;
10. obtener validación;
11. versionar resultado.

## Regla sobre dependencias

Una puntuación alta no puede ignorar dependencias.

Si REQ-B depende de REQ-A, el orden puede ajustarse.

Todo ajuste debe registrar:
- puntuación original;
- dependencia;
- razón del nuevo orden.

## Regla sobre Must

Si demasiados requisitos quedan como Must:

1. señalar que la clasificación perdió poder discriminante;
2. calcular impacto en capacidad;
3. preguntar qué falla realmente si cada ítem se excluye;
4. facilitar renegociación.

No degradar prioridades arbitrariamente.

## Salida mínima

Para cada requisito:

```yaml
id: REQ-000
tecnica: MoSCoW | RICE | WSJF | Kano | Value-Effort | Ranking
prioridad_propuesta: ""
datos_usados: []
dependencias: []
rationale: ""
incertidumbres: []
autoridad_validacion: ""
estado: propuesta | validada | rechazada | diferida
```

## Uso de IA

La IA puede calcular, detectar inconsistencias y simular escenarios.

No puede:
- inventar cifras;
- validar la prioridad final;
- convertir presión política en valor sin distinguirla;
- esconder incertidumbre detrás de un score.
