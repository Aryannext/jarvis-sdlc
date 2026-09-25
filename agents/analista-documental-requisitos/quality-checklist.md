# Checklist de calidad — Analista Documental y de Requisitos v0.1

Antes de entregar un paquete, verificar:

## Documentos

- [ ] Se sabe qué documentos relevantes fueron revisados.
- [ ] Se registraron versiones cuando estaban disponibles.
- [ ] Se marcaron documentos potencialmente obsoletos.
- [ ] Se detectaron duplicados o contradicciones relevantes.
- [ ] La falta de documentos no fue rellenada con suposiciones.

## Requisitos — estado y procedencia

- [ ] Cada requisito tiene estado.
- [ ] Cada requisito importante conserva su fuente.
- [ ] Se separaron requisitos funcionales y no funcionales cuando fue posible.
- [ ] Se separaron restricciones y reglas de negocio.
- [ ] Los candidatos no se presentaron como confirmados.

## Requisitos — calidad individual

Para cada requisito relevante:

- [ ] ¿Es necesario o existe una necesidad identificable?
- [ ] ¿Está en un nivel de abstracción apropiado?
- [ ] ¿Tiene una única interpretación razonable?
- [ ] ¿Contiene suficiente contexto, condiciones y límites?
- [ ] ¿Expresa una obligación principal o puede requerir división?
- [ ] ¿Existe evidencia suficiente para considerar su factibilidad o está pendiente?
- [ ] ¿Puede verificarse mediante prueba, inspección, análisis o demostración?
- [ ] ¿Refleja correctamente la necesidad conocida?
- [ ] ¿Respeta el estilo y terminología acordados?
- [ ] ¿Evita palabras vagas sin definición?
- [ ] ¿Evita imponer implementación sin justificación?

## Conjunto de requisitos

- [ ] No se detectaron contradicciones internas sin registrar.
- [ ] La terminología es consistente o las diferencias están documentadas.
- [ ] El conjunto tiene cobertura razonable de necesidades identificadas.
- [ ] La factibilidad conjunta no presenta conflictos conocidos sin registrar.
- [ ] Existe trazabilidad suficiente para los elementos críticos.

## Historias de usuario — INVEST cuando aplique

- [ ] Independiente.
- [ ] Negociable.
- [ ] Valiosa.
- [ ] Estimable.
- [ ] Pequeña.
- [ ] Comprobable.

Un incumplimiento debe generar análisis, no rechazo mecánico.

## Criterios de aceptación

- [ ] Son específicos.
- [ ] Son medibles cuando el comportamiento lo requiere.
- [ ] Permiten pass/fail.
- [ ] Expresan comportamiento observable.
- [ ] Cada criterio cubre un resultado verificable principal.
- [ ] No contienen detalles de implementación sin justificación.
- [ ] Existe cobertura del camino feliz.
- [ ] Se evaluaron errores y casos límite aplicables.
- [ ] Se evaluaron estados vacíos/mínimos cuando aplican.
- [ ] Se consideró concurrencia cuando aplica.
- [ ] Se consideraron atributos no funcionales relevantes cuando aplican.
- [ ] No se inventaron umbrales para hacerlos medibles.
- [ ] Given–When–Then se utilizó cuando aporta claridad, no por obligación.

## Reformulación

- [ ] El requisito original se conserva.
- [ ] Se enumeran los defectos encontrados.
- [ ] La propuesta no introduce nuevas reglas sin marcar.
- [ ] Los cambios potenciales de significado están visibles.
- [ ] La reformulación permanece como propuesta hasta validación.

## Trazabilidad

- [ ] Las relaciones conocidas fueron registradas.
- [ ] Las relaciones faltantes permanecen visibles.
- [ ] No se inventaron vínculos.
- [ ] Los cambios relevantes conservan historia cuando existe.

## Contradicciones

- [ ] Las contradicciones materiales están enumeradas.
- [ ] Se intentó encontrar evidencia de resolución previa.
- [ ] No se eligió una versión arbitrariamente.
- [ ] Las contradicciones bloqueantes fueron escaladas.

## Entrega

- [ ] Otro especialista puede entender el contexto sin releer todo desde cero.
- [ ] Las incertidumbres están separadas de los hechos.
- [ ] Las solicitudes al supervisor son específicas.
- [ ] El paquete indica qué puede continuar y qué está bloqueado.
