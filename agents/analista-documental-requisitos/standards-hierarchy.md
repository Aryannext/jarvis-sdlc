# Jerarquía operativa de estándares y requisitos v0.1

## Objetivo

Evitar aplicar guías, normas y heurísticas como si todas tuvieran la misma autoridad.

## Jerarquía de requisitos

```text
Business Requirement
        ↓
Stakeholder Requirement
        ↓
Solution Requirement
   ├── Functional
   └── Non-Functional
        ↓
Transition Requirement
```

## Regla de trazabilidad vertical

Un Solution Requirement material debe poder responder:
- qué necesidad de stakeholder satisface;
- qué objetivo de negocio soporta;
- qué criterio demuestra cumplimiento.

Un Transition Requirement debe estar vinculado a la transición concreta que habilita.

## Precedencia normativa interna

Cuando existan varias fuentes:

1. ley/regulación aplicable confirmada;
2. contrato u obligación vinculante confirmada;
3. política/estándar obligatorio de la organización;
4. baseline o decisión aprobada del proyecto;
5. estándar técnico adoptado;
6. cuerpo de conocimiento/guía metodológica;
7. heurística;
8. preferencia.

## Consecuencia

Una recomendación de BABOK, INCOSE, INVEST o cualquier guía no puede invalidar una obligación superior.

Una plantilla interna tampoco puede ignorar una obligación regulatoria aplicable.

## Marcos registrados

### Ciclo de vida
- ISO/IEC/IEEE 15288;
- ISO/IEC/IEEE 12207;
- ISO 9001 según versión aplicable.

### Requirements Engineering
- ISO/IEC/IEEE 29148.

### Business / Software / Systems knowledge
- BABOK;
- SWEBOK;
- SEBoK.

### Modelado
- BPMN;
- UML;
- ArchiMate cuando aplique.

### Calidad
- ISO/IEC 25010 / SQuaRE;
- referencias de calidad IA cuando corresponda.

## Regla de versión

El agente no debe asumir que una edición, año o norma está vigente porque aparezca en su conocimiento.

En proyectos reales debe registrar:
- referencia;
- versión;
- fuente;
- obligatoriedad;
- vigencia verificada o pendiente.

## Conflicto entre marcos

Si dos fuentes recomiendan cosas distintas:

1. determinar obligatoriedad;
2. determinar contexto;
3. identificar si realmente existe contradicción;
4. aplicar la fuente superior cuando esté claro;
5. si sigue ambiguo, escalar.

## Regla sobre estilo

Si la organización tiene una plantilla obligatoria de requisitos y no contradice una obligación superior, el agente debe respetarla aunque otra guía sugiera un estilo distinto.
