# Runtime de JARVIS

Este directorio representa la estructura de estado persistente que utilizará JARVIS durante la ejecución.

No debe depender únicamente del contexto conversacional del modelo.

Estructura prevista:

```text
runtime/
├── state/
├── evidence/
├── findings/
├── tasks/
├── handoffs/
└── supervisor-inbox/
```

Los artefactos reales de ejecución deberán excluirse del repositorio cuando contengan información sensible o específica de un proyecto.

La implementación concreta de persistencia se decidirá después de validar los primeros workflows. En v0.1 se priorizarán archivos estructurados y, si se justifica, SQLite.
