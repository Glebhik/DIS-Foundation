# Technology Architecture — DIS Group

This document describes the high-level technology architecture of DIS Group — how our systems are organized, what principles guide technology decisions, and how the architecture evolves.

This is a living document. It describes the target state and current reality, and is updated whenever significant architectural decisions are made.

---

## Architecture Vision

**DIS Group's technology architecture is the infrastructure layer that makes every business unit more intelligent than its competitors.**

The architecture must:
- Enable AI capabilities to be deployed across all business units from a shared foundation
- Scale cleanly as the business grows without requiring full rewrites
- Keep data — DIS Group's most valuable asset — secure, accessible, and useful
- Be simple enough that a small, high-quality engineering team can maintain and evolve it
- Make DIS Foundation (this knowledge base) a first-class citizen — the organization's memory

---

## Architecture Principles

### 1. Data First
Every architectural decision is evaluated on its impact to data quality, accessibility, and security. Technology choices that compromise our data assets are rejected regardless of other merits.

### 2. Composable over Monolithic
We prefer systems that can be combined and reconfigured over monolithic platforms. A well-chosen set of composable tools is easier to evolve than a single all-in-one system.

### 3. Defaults, Not Rules
We establish sensible defaults for infrastructure, tooling, and patterns. Teams can deviate with an ADR. Governance is through visibility and review — not hard locks.

### 4. Build Intelligence on Solid Operations
AI is built on top of working operational systems. We do not deploy AI on top of manual, inconsistent, or unreliable operations. The foundation must be solid before the intelligence layer is added.

### 5. Observability as a First-Class Concern
We cannot improve what we cannot see. Every system exposes metrics, logs, and traces. We monitor proactively, not reactively.

---

## System Architecture

### Layer Overview

```
┌─────────────────────────────────────────────────────┐
│  PRESENTATION LAYER                                 │
│  Internal tools · Dashboards · DIS Foundation       │
│  How people and AI access information and systems   │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│  INTELLIGENCE LAYER                                 │
│  AI agents · Analytics · Decision support           │
│  How raw data becomes actionable intelligence       │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│  DATA LAYER                                         │
│  Data warehouse · Pipelines · APIs                  │
│  How data is collected, stored, and made accessible │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│  OPERATIONAL LAYER                                  │
│  Business unit systems · IoT · External integrations│
│  Where data originates from physical operations     │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│  INFRASTRUCTURE LAYER                               │
│  Cloud · Networking · Security · Identity           │
│  The foundation everything else runs on             │
└─────────────────────────────────────────────────────┘
```

---

## Data Architecture

### Data Principles
- DIS Group owns its data. We do not gift data to SaaS vendors without understanding the implications.
- Every dataset has an owner, a definition, and a lineage.
- Data that informs material business decisions must be auditable.

### Data Domains

| Domain | Key Data Types | Primary Owner |
|---|---|---|
| Recycling Operations | Volumes, materials, processing metrics, commodity prices | Recycling Lead |
| Energy | Asset performance, generation data, trading positions, market prices | Energy Lead |
| ESG | Emissions data, social metrics, governance indicators | ESG Lead |
| Finance | P&L, cashflow, budgets, transactions | CFO |
| Corporate | People data, HR metrics | CEO / COO |

### Data Stack (Target)
> *[To be populated with specific tooling choices as ADRs are written. See `/technology/decisions/`.]*

| Component | Purpose | Tool / Approach |
|---|---|---|
| Data warehouse | Centralized analytical store | [TBD — ADR required] |
| Data pipelines | ETL / ELT from operational systems | [TBD — ADR required] |
| BI / dashboards | Business intelligence and reporting | [TBD — ADR required] |
| Data catalog | Data discovery and lineage | [TBD] |

---

## AI Architecture

### AI Infrastructure Components

| Component | Description | Status |
|---|---|---|
| Foundation model API | Access to LLMs (Claude/other) for AI features | Planning |
| Internal knowledge base | DIS Foundation — structured corporate memory | Active |
| AI agent runtime | Environment for running internal agents | Planning |
| Prompt library | Versioned, tested prompts for production use | Planning |
| AI monitoring | Logs, performance tracking, drift detection | Planning |

### Integration Pattern
AI systems in DIS Group follow the **Augment, Don't Replace** pattern:

```
Operational Data → AI Processing → Intelligence Output → Human Review → Decision / Action
```

AI produces intelligence. Humans make decisions. This applies to all Class 2+ systems. See [ai/governance.md](ai/governance.md) for classification.

---

## Security Architecture

### Security Principles
- Zero-trust by default: no implicit trust between systems
- Least privilege: every user and system has only the access it needs
- Defense in depth: multiple security layers; no single point of failure
- Auditability: all access and actions logged

### Key Security Controls

| Control | Description |
|---|---|
| Identity and access management | Centralized identity; MFA required for all users |
| Secrets management | No credentials in code, configuration files, or repositories |
| Data encryption | Encryption at rest and in transit for all sensitive data |
| Network segmentation | Business unit systems isolated by network segment |
| Vulnerability management | Regular scanning; critical CVEs remediated within [target SLA] |
| Backup and recovery | All critical data backed up; recovery tested [frequency] |

---

## Architecture Decision Records

All significant technology decisions are documented in `technology/decisions/` as Architecture Decision Records (ADRs). This creates an auditable history of why the architecture looks the way it does.

Current ADRs:

| ADR | Decision | Status |
|---|---|---|
| [ADR-001](decisions/ADR-001-git-knowledge-base.md) | Use Git as the DIS Foundation knowledge base | Accepted |

New ADRs are required for:
- Selection of a new platform or major vendor
- Significant changes to the data architecture
- Changes to the security model
- Any decision that will be difficult to reverse

See template: [`_templates/adr.md`](../_templates/adr.md)

---

## Evolution Roadmap

### Phase 1 (Now — 12 months): Foundations
- [ ] This document published and reviewed
- [ ] Technology stack inventory completed (`technology/stack.md`)
- [ ] First ADRs written for current tooling decisions
- [ ] Data inventory completed for Recycling and Energy
- [ ] Security baseline documented and reviewed
- [ ] AI infrastructure planning completed

### Phase 2 (12–36 months): Capability Build
- [ ] Data warehouse operational and serving BI layer
- [ ] AI agent runtime deployed
- [ ] Monitoring and observability stack operational
- [ ] Data catalog in use
- [ ] Security posture independently reviewed

### Phase 3 (36 months+): Scale
- [ ] Architecture supports full group data platform
- [ ] AI systems in production across all business units
- [ ] Architecture review cadence established

---

## Related Documents

- [technology/README.md](README.md) — Technology domain overview
- [technology/stack.md](README.md) — Approved technology stack *(to be created)*
- [technology/decisions/](decisions/) — Architecture Decision Records
- [ai/strategy.md](../ai/strategy.md) — AI strategy
- [ai/governance.md](../ai/governance.md) — AI governance
- [ARCHITECTURE.md](../ARCHITECTURE.md) — Repository system design
- [`_templates/adr.md`](../_templates/adr.md) — ADR template

---

*Owner: CTO | Status: Active | Review cycle: Quarterly | Last updated: 2026-07-05*
