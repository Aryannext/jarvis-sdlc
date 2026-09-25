# Política Anti-Bucles v0.1

## Objetivo

Evitar conversaciones circulares, reintentos improductivos y consumo innecesario de Claude Pro.

## Definición de progreso

Un ciclo produce progreso solo si añade al menos uno de estos elementos:

- nueva evidencia;
- hipótesis descartada;
- incertidumbre reducida;
- artefacto nuevo o corregido;
- decisión válida;
- transición de estado.

Reformular la misma conclusión no cuenta como progreso.

## Límites iniciales

### Reintentos de una misma tarea

Máximo recomendado: 2 reintentos automáticos.

Un tercer intento requiere:
- estrategia diferente claramente identificada; o
- escalamiento.

### Devoluciones entre dos agentes

Si una misma cuestión rebota entre dos especialistas 2 veces sin evidencia nueva:

`PAUSAR → REVISAR CAUSA → CAMBIAR ESTRATEGIA O ESCALAR`

### Revisión crítica

La revisión crítica puede devolver un hallazgo una vez al estado responsable para obtener evidencia adicional.

Si vuelve a fallar por la misma razón, el hallazgo debe:
- reducir confianza;
- quedar como no resuelto;
- o escalarse.

## Detección de ciclo

Registrar para cada tarea:
- agente;
- acción;
- entrada;
- resultado;
- evidencia nueva;
- timestamp lógico/secuencia.

Si se repite el patrón de estado + problema + resultado sin nueva evidencia, se considera ciclo.

## Salida de emergencia

Ante ciclo detectado:

1. detener delegaciones relacionadas;
2. resumir qué se intentó;
3. identificar por qué no hubo progreso;
4. elegir una estrategia alternativa si existe;
5. si no existe, escalar o marcar como no resuelto.

## Regla económica

No gastar contexto para aparentar actividad.

Si no hay una acción capaz de producir información nueva, el agente debe detenerse.
