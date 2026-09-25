# Ejecución local de JARVIS con Claude Code

## Objetivo

Ejecutar JARVIS localmente utilizando Claude Code autenticado con la suscripción de Claude, sin integrar una API de pago en esta fase.

## Diseño actual

El repositorio contiene el agente de proyecto:

`.claude/agents/analista-documental-requisitos.md`

Claude Code admite agentes de proyecto en `.claude/agents/`.

Para usar los agentes de JARVIS mientras trabajas sobre otro repositorio local, la estrategia inicial es lanzar Claude Code en el proyecto objetivo y añadir el repositorio JARVIS como directorio adicional.

## Uso recomendado

Supongamos:

```text
~/jarvis-sdlc
~/proyectos/mi-app
```

Desde el proyecto a analizar:

```bash
cd ~/proyectos/mi-app
bash ~/jarvis-sdlc/scripts/jarvis.sh
```

El script conserva `mi-app` como directorio de trabajo y añade `jarvis-sdlc` mediante `--add-dir`.

Así Claude Code puede descubrir los agentes de JARVIS sin copiar manualmente sus definiciones a cada proyecto.

## Primera comprobación

Dentro de Claude Code:

```text
Usa el agente analista-documental-requisitos para inventariar la documentación de este proyecto. No analices código todavía.
```

El agente debe:
- trabajar con herramientas de lectura;
- empezar por documentación;
- consultar solo conocimiento relevante;
- devolver resultado al coordinador;
- no modificar el proyecto.

## Validación estática antes de ejecutar

En el repositorio JARVIS:

```bash
python3 scripts/validate-agent-config.py
```

Debe terminar con:

```text
OK: configuración estática del agente válida.
```

## Permisos

El agente v0.1 está configurado solamente con:

```text
Read
Glob
Grep
```

Por lo tanto su función es analizar, no editar.

La escritura de artefactos persistentes quedará inicialmente bajo control del Orquestador.

## Modelo y esfuerzo

La definición inicial utiliza:

```yaml
model: sonnet
effort: medium
maxTurns: 12
```

Esto es una decisión inicial orientada a equilibrar calidad y consumo de la suscripción. Debe medirse con los evals antes de decidir si ciertas tareas necesitan otro modelo o esfuerzo.

## Notas de Claude Code

Los agentes personalizados usan Markdown con frontmatter YAML. Los campos mínimos son `name` y `description`.

Si Claude Code no descubre un agente recién agregado, verifica:
- que `.claude/agents/` exista;
- el frontmatter;
- que el nombre no contenga `:`;
- la versión de Claude Code;
- `claude doctor`.

## Siguiente fase

Después del primer smoke test local:

1. ejecutar los evals del agente;
2. registrar fallos;
3. ajustar instrucciones;
4. conectar resultados estructurados con los schemas del Orquestador;
5. decidir si v0.1 pasa a v0.2.
