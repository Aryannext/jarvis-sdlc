# Investigación base — Jerarquía de estándares y requisitos (2026)

## Origen y alcance

Documento normalizado a partir de la investigación aportada por el supervisor.

Esta jerarquía se incorpora como marco de trabajo interno de JARVIS. En esta iteración no se realizó verificación externa de versiones, vigencia o relaciones normativas.

## Jerarquía de requisitos

```text
Business Requirements
        ↓
Stakeholder Requirements
        ↓
Solution Requirements
   ├── Functional
   └── Non-Functional
        ↓
Transition Requirements
```

### Business Requirements
Responden por qué existe el proyecto y qué resultado estratégico busca.

### Stakeholder Requirements
Expresan necesidades de roles o grupos afectados.

### Solution Requirements
Describen comportamiento y atributos de la solución.

Se separan en:
- funcionales;
- no funcionales.

### Transition Requirements
Describen capacidades temporales necesarias para pasar del estado actual al futuro, por ejemplo migración, capacitación o cutover.

## Regla de trazabilidad

Todo requisito de solución debería poder rastrearse hacia una necesidad de stakeholder y, cuando corresponda, hacia un objetivo de negocio.

## Jerarquía de referencias aportada

### Ciclo de vida
- ISO/IEC/IEEE 15288;
- ISO/IEC/IEEE 12207;
- ISO 9001, según versión aplicable al contexto.

### Ingeniería de requisitos
- ISO/IEC/IEEE 29148;
- IEEE 830 como referencia histórica reemplazada.

### Cuerpos de conocimiento
- BABOK;
- SEBoK;
- SWEBOK.

### Modelado
- BPMN 2.0;
- UML;
- ArchiMate cuando aplica.

### Calidad
- ISO/IEC 25010 / familia SQuaRE;
- referencias de calidad específicas de IA cuando aplique.

## Regla de precedencia interna

Para JARVIS:

1. requisitos legales/regulatorios aplicables y compromisos contractuales confirmados;
2. estándares y políticas obligatorias de la organización/proyecto;
3. baseline y decisiones aprobadas;
4. estándar técnico elegido para la disciplina;
5. guías metodológicas;
6. heurísticas y mejores prácticas.

Si dos marcos discrepan, JARVIS no debe resolverlo por preferencia: debe identificar cuál es obligatorio para el proyecto.
