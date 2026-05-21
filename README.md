# Herramientas-ia

Legal AI Engineering toolkit built under the BPIR framework (Brief, Plan, Implement, Review).

Designed for compliance automation in the Colombian financial sector — Ley 1581/2012, Ley 1266/2008, SFC regulation.

Built as part of the 10X Builder program by LAB10 — 8-week applied AI engineering track.

---

## Purpose

Most teams using AI for legal work rely on informal prompting and trust the output without structured review. This toolkit formalizes the human-AI collaboration cycle so that every artifact produced is traceable, auditable, and defensible in a regulatory context.

---

## Structure

```
Herramientas-ia/
└── 01-planning/
    ├── plantilla-brief-ia.md       Master brief template for delegating tasks to AI
    ├── protocolo-review-ia.md      Forensic review protocol — 5-point checklist
    └── config_compliance.json      Legal rules engine — PII and clause detection config
```

More modules will be added weekly as the program progresses:

```
02-agents/          Week 2 — Specialized agent orchestration
03-tools/           Week 5 — MCP tool engineering
04-rag/             Week 6 — RAG pipeline over legal corpus
05-evals/           Week 7 — Evaluation suite and hallucination metrics
06-deployment/      Week 8 — LLMOps and production deployment
```

---

## Core Artifacts

### plantilla-brief-ia.md
A reusable template for defining tasks before any code is written. Structured around four mandatory sections: context, technical requirements, constraints, and definition of done.

Key differentiator: includes a legal constraints section and a ZKP-readiness check — ensuring the system architecture is compatible with future Zero-Knowledge Proof validation without access to the original document.

### protocolo-review-ia.md
A five-point forensic checklist applied before every commit. Goes beyond standard code review to include legal validation — verifying that every finding cites a specific legal article, that PII is correctly classified under Art. 5 Ley 1581, and that the output meets evidentiary standards for SFC audits.

### config_compliance.json
The rules engine that separates legal logic from code. A lawyer or compliance analyst can update detection rules — clauses, PII patterns, regulatory references — without touching the codebase.

Covers: Cedula, NIT, email, mobile (Colombian format), credit scores, and five mandatory clause types including SARLAFT and Habeas Data Financiero.

---

## Project Context

**Current build:** Financial Compliance Rule Engine (FCRE v1.0)

A deterministic contract analysis system for credit agreements and promissory notes. Detects missing mandatory clauses and exposed PII under Colombian financial regulation. No LLM inference — fully deterministic, fully auditable.

**Target stack (full system):**

```
Week 1    Python · regex · pydantic          Deterministic layer
Week 4    LangChain · ReAct                  Agent reasoning
Week 6    Qdrant · embeddings                Semantic search over legal corpus
Week 8    FastAPI · Docker · LLMOps          Production deployment
```

---

## Regulatory Scope

- Ley 1581/2012 — Personal Data Protection (Colombia)
- Ley 1266/2008 — Financial Habeas Data
- Circular SFC 026/2008 — SARLAFT (Anti-money laundering)
- Circular SFC 029/2014 — Digital financial services
- GDPR — For contracts with international counterparties

---

## Author

Lawyer · MSc Applied Analytics candidate
Focused on privacy engineering and compliance automation for the Colombian financial sector.
Building toward a PhD research track on Zero-Knowledge Proofs applied to legal compliance verification.

---

Built with the BPIR methodology — Brief, Plan, Implement, Review.
10X Builder Program · LAB10 · 2026
