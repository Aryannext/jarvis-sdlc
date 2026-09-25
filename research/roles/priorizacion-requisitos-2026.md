# Investigación base — Priorización de requisitos (2026)

## Origen

Documento normalizado a partir de la investigación aportada por el supervisor.

## Propósito

La priorización decide qué requisitos se implementan primero, cuáles después y cuáles se posponen o quedan fuera de una versión.

No debe confundirse con aprobación ni con valor absoluto del requisito.

## Técnicas incorporadas

### MoSCoW

Clasifica requisitos en:
- Must;
- Should;
- Could;
- Won't para esta versión.

La investigación aportada utiliza como regla práctica que los Must no deberían superar aproximadamente el 60 % de la capacidad. Se trata como heurística de negociación, no como ley universal.

### RICE

Fórmula:

```text
RICE = (Reach × Impact × Confidence) / Effort
```

Factores:
- Reach;
- Impact;
- Confidence;
- Effort.

Los valores deben provenir de datos, estimaciones explícitas o supuestos identificados. El agente no debe inventarlos.

### WSJF

Prioriza mediante:

```text
WSJF = Cost of Delay / Job Size
```

El Cost of Delay puede considerar:
- valor de negocio;
- criticidad temporal;
- reducción de riesgo u oportunidad.

### Kano

Clasifica por efecto sobre satisfacción:
- Must-be;
- Performance;
- Delighters;
- Indifferent;
- Reverse.

Requiere investigación de usuarios.

### Value vs Effort

Matriz visual valor/esfuerzo útil para talleres rápidos.

### Ranking total

Orden de 1 a N. Útil para un backlog final, pero puede ocultar incertidumbre si no conserva rationale.

## Flujo práctico

1. definir criterios antes de priorizar;
2. trabajar con requisitos suficientemente claros;
3. obtener estimaciones y dependencias;
4. facilitar priorización;
5. documentar rationale;
6. validar con stakeholders autorizados;
7. revisar periódicamente.

## Regla de autoridad

La IA y el analista pueden:
- preparar;
- calcular;
- detectar inconsistencias;
- simular escenarios;
- recomendar.

La prioridad final de negocio requiere validación de quien tenga autoridad.

## Restricciones críticas

- no convertir "urgencia política" en valor de negocio sin registrarlo;
- no marcar todo como Must;
- no inventar Reach, Impact, Confidence, Effort ni Cost of Delay;
- no ignorar dependencias solo porque una puntuación sea mayor;
- no borrar requisitos Won't: deben quedar trazables como fuera de alcance de la versión.
