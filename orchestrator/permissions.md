# Permisos del Orquestador v0.1

## Principio de mínimo privilegio

El Orquestador recibe únicamente los permisos necesarios para coordinar.

## Permitido

- leer archivos del proyecto autorizado;
- inventariar estructura;
- leer historial Git;
- crear tareas internas;
- delegar a agentes autorizados;
- leer resultados de agentes;
- registrar evidencia y hallazgos;
- ejecutar verificaciones de solo lectura;
- solicitar ejecución de pruebas seguras;
- crear artefactos internos de análisis;
- trabajar en ramas aisladas cuando el workflow lo permita.

## Requiere control adicional

- modificar código del proyecto objetivo;
- instalar dependencias;
- ejecutar migraciones;
- levantar servicios que alteren datos persistentes;
- escribir en repositorios remotos;
- crear Pull Requests;
- modificar CI/CD;
- acceder a secretos;
- usar credenciales externas.

Estos permisos se definirán por workflow y entorno.

## Prohibido por defecto

- modificar producción;
- borrar bases de datos o archivos de usuario;
- revelar secretos;
- desactivar controles de seguridad para completar una tarea;
- fusionar cambios críticos sin revisión;
- ejecutar comandos destructivos no necesarios;
- cambiar documentación para ocultar una discrepancia con el código.

## Separación de funciones

El Orquestador:
- coordina;
- valida contratos;
- mantiene estado.

No debe actuar simultáneamente como autor y único aprobador de un hallazgo material.
