# AUDIT_EXISTING_PROJECT v0.1

Purpose: audit an existing software project without assuming that its documentation, implementation, tests or stakeholder claims are correct.

## Workflow states

### 01 — DISCOVER
Identify the project structure, technologies, repositories, build systems, documentation locations, test suites, deployment assets and available history.

Output:
- project inventory;
- unknowns;
- initial risk surfaces.

### 02 — DOCUMENT_INVENTORY
Locate and classify available:
- requirements;
- business rules;
- user stories;
- acceptance criteria;
- architecture documents;
- ADRs;
- diagrams;
- API contracts;
- data models;
- manuals;
- test plans;
- traceability artifacts.

Output:
- document map;
- missing-documentation findings.

### 03 — REQUIREMENTS_MODEL
Reconstruct what the system is expected to do from available approved artifacts.

Output:
- requirements model;
- uncertainty list;
- conflicts requiring investigation.

### 04 — BUSINESS_RULES_MODEL
Extract business rules and identify their sources, owners and dependencies.

Output:
- business-rule register;
- conflicting rules;
- unverified rules.

### 05 — ARCHITECTURE_MODEL
Reconstruct the intended architecture, major components, boundaries, data flows, external systems and recorded architectural decisions.

Output:
- intended architecture model;
- decision register;
- undocumented architectural assumptions.

### 06 — TRACEABILITY_MODEL
Map relationships where evidence exists between requirements, rules, acceptance criteria, design, implementation and tests.

Output:
- traceability matrix;
- orphan artifacts;
- missing links.

### 07 — CODE_ANALYSIS
Inspect implementation only after sufficient project context has been established.

Evaluate:
- structure and boundaries;
- implementation against intended behavior;
- code quality;
- error handling;
- data handling;
- architectural drift;
- dead or duplicated logic;
- relevant SOLID/Clean Code concerns without mechanical enforcement.

Output:
- implementation model;
- candidate discrepancies;
- technical-debt findings.

### 08 — TEST_ANALYSIS
Assess existing tests and what they actually prove.

Evaluate:
- unit;
- integration;
- contract;
- end-to-end;
- negative paths;
- boundary cases;
- regression coverage.

Output:
- coverage by behavior, not only percentage;
- missing test scenarios;
- unreliable-test findings.

### 09 — RUNTIME_ANALYSIS
Build and execute the project when safe and practical.

Observe:
- startup;
- logs;
- runtime failures;
- API behavior;
- data behavior;
- external integration failures;
- performance symptoms.

Output:
- observed-system model;
- reproducible failures;
- runtime evidence.

### 10 — GAP_ANALYSIS
Compare:
- intended system;
- implemented system;
- observed system.

A mismatch becomes a finding to investigate, not an automatic verdict about which side is correct.

Output:
- discrepancy register;
- severity candidates;
- unresolved contradictions.

### 11 — ROOT_CAUSE_ANALYSIS
For material findings:
1. reproduce where practical;
2. collect evidence;
3. generate plausible hypotheses;
4. eliminate or support hypotheses;
5. identify the best-supported cause;
6. record confidence.

Output:
- root-cause records;
- rejected hypotheses;
- unresolved causes.

### 12 — RISK_ANALYSIS
Assess the effect of findings on:
- functionality;
- data integrity;
- security;
- maintainability;
- operations;
- compliance where relevant;
- user impact.

Output:
- risk register;
- prioritization basis.

### 13 — RECOMMENDATIONS
For each material issue:
- propose the preferred remediation;
- provide alternatives when useful;
- explain trade-offs;
- identify required tests and documentation changes;
- avoid unjustified redesign.

### 14 — CRITICAL_REVIEW
An independent reviewer attempts to refute:
- findings;
- root causes;
- assumptions;
- severity;
- recommendations.

Material findings should survive this review or have their confidence reduced.

### 15 — FINAL_REPORT
Produce an evidence-backed audit report including:
- executive summary;
- project understanding;
- confirmed defects;
- probable defects;
- risks;
- inconsistencies;
- missing evidence;
- technical debt;
- traceability gaps;
- recommendations;
- supervisor actions required.

## Supervisor escalation

Escalate only when the system cannot resolve an issue internally with available evidence.

Every escalation should state:
- what is unknown;
- why it matters;
- what was already checked;
- exactly what information is needed;
- who or what can provide it;
- what happens if it remains unknown.
