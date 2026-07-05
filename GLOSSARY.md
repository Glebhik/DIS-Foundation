# Glossary — DIS Foundation

This glossary defines terms used across DIS Foundation. It is the shared vocabulary for humans and AI sessions working in this repository.

When a term is used in a document with a specific meaning, link to this glossary on first use: `[ADR](../GLOSSARY.md#adr)`.

---

## A

**ADR (Architecture Decision Record)**
A document that records a significant architectural decision — what was decided, the context, the options considered, the rationale, and the consequences. Stored in `technology/decisions/`. Template: [`_templates/adr.md`](_templates/adr.md).

**AI Architect**
The Claude Code session operating under the `CLAUDE.md` constitution. Responsible for maintaining and improving DIS Foundation. Behaves as Chief AI Architect — CTO, Knowledge Engineer, Enterprise Architect, and Systems Thinker simultaneously.

**AI-Native**
Designed to be legible, navigable, and maintainable by both humans and AI systems. Not AI-generated — AI-legible. Documents use consistent structure, explicit metadata, relative links, and the shared vocabulary of this glossary to enable reliable AI extraction and reasoning.

**Archive**
The `/archive` folder. A read-only, append-only store for superseded documents. Documents are moved here when replaced; they are never deleted. See: [Temporal Architecture in ARCHITECTURE.md](ARCHITECTURE.md#temporal-architecture).

**Authority Matrix**
A table defining who has approval authority over which decisions, at what spending or risk level. Lives in `finance/approvals.md`.

---

## B

**Business Unit**
One of DIS Group's operating businesses: Recycling, Energy, or ESG platform. Each has a dedicated domain folder. Distinct from Corporate Functions (shared services) and Capabilities (cross-group enablers).

---

## C

**CHANGELOG**
`CHANGELOG.md` at the root. Records all significant changes to DIS Foundation per session. Updated by the AI Architect at session end.

**Chief AI Architect**
The elevated role of the AI operating in DIS Foundation. Responsible for the full design, maintenance, and evolution of the Digital Operating System. Encompasses CTO, CKO, Enterprise Architect, Business Strategist, and Systems Engineer perspectives.

**Constitutional Document**
Any of the root-level documents that define what DIS Group is, where it is going, how it operates, and the rules of this system. Includes: `CLAUDE.md`, `ARCHITECTURE.md`, `VISION.md`, `PRINCIPLES.md`, `ROADMAP.md`, `DIS_GROUP_OVERVIEW.md`, `PROJECT_CONTEXT.md`, `GLOSSARY.md`, `CHANGELOG.md`, `INDEX.md`.

**Constitutional Layer**
Layer 1 in the three-layer architecture. Contains all constitutional documents. Governs the domain knowledge layer. See: [ARCHITECTURE.md](ARCHITECTURE.md).

**Cross-Link**
A relative Markdown link from one document to another. Cross-links create the knowledge graph that makes DIS Foundation navigable and AI-legible. Every document must have at least two cross-links. Format: `[Document Title](../domain/file.md)`.

---

## D

**Digital Operating System (DOS)**
The full DIS Foundation repository — structured corporate knowledge that enables DIS Group to operate, decide, and learn as a single coherent entity. The goal is to make this one of the world's best examples of an AI-native corporate operating system.

**Domain**
A top-level folder in DIS Foundation representing a coherent area of knowledge. Examples: `/ai`, `/energy`, `/finance`. Every domain has a `README.md` defining its scope, contents, guidelines, and owner.

**Domain Owner**
The role responsible for the accuracy and currency of a domain's documents. Listed in the Domain Ownership table in `CLAUDE.md`. Distinct from document-level owners.

**Draft**
Document status. A document marked `Status: Draft` is in progress and not yet authoritative. Do not link to it from INDEX.md Key Documents until it is Active.

---

## E

**ESG**
Environmental, Social, and Governance. DIS Group's ESG platform tracks, reports, and improves environmental impact, social responsibility, and governance quality across all business units. Domain: `/esg`.

---

## G

**Governance**
The rules, roles, and processes that control how DIS Foundation is maintained and how DIS Group makes decisions. Documented in `CLAUDE.md` (AI governance), `ARCHITECTURE.md` (repository governance), and `finance/approvals.md` (financial governance).

---

## I

**INDEX.md**
The master navigation hub for DIS Foundation. Organized in three tiers: Constitutional Documents, Domain Knowledge (Business Units / Corporate Functions / Capabilities), and Infrastructure. Updated whenever documents are added or structural changes are made. Never duplicates content — only links.

---

## K

**Key Document**
A landmark document listed in the Key Documents checklist in `INDEX.md`. These are the most critical documents across the knowledge base. The checklist tracks completion status.

**KPI (Key Performance Indicator)**
A quantitative measure used to track the performance of a business unit or process. Each business unit domain has a `kpis.md` file. KPIs must include: metric name, definition, current value, target, and measurement frequency.

---

## L

**Layer**
One of three tiers in DIS Foundation's three-layer architecture: (1) Constitutional Layer, (2) Domain Knowledge Layer, (3) Infrastructure Layer. See: [ARCHITECTURE.md](ARCHITECTURE.md).

---

## M

**Materiality Assessment**
An ESG process to identify which environmental, social, and governance topics are most significant for DIS Group and its stakeholders. The foundation of the ESG framework. Lives in `esg/framework.md`.

**Metadata**
Structured fields at the end of every document: `Owner`, `Status`, `Last updated`. Optionally: `Review cycle`, `Confidentiality`, `Dependencies`. Required for every active document.

---

## O

**OKR (Objectives and Key Results)**
A goal-setting framework used by DIS Group for quarterly and annual planning. Objectives are qualitative goals; Key Results are quantitative measures of progress. Stored in `strategy/okrs/`. Template: [`_templates/okr-cycle.md`](_templates/okr-cycle.md).

---

## P

**PII (Personally Identifiable Information)**
Any data that could identify a specific individual — names, contact details, identification numbers. PII must not be stored in DIS Foundation. Store in a secure external system and link by reference.

**Policy**
A binding document that establishes a rule or standard. Policies have owners, review dates, and enforcement mechanisms. Stored in the relevant domain folder.

**Principle**
A foundational conviction that shapes decisions and behavior at DIS Group. Principles are documented in `PRINCIPLES.md`. They are not aspirational — they are behavioral constraints. See also: [Values](#v).

---

## R

**README.md (Domain)**
The entry point for every domain folder. Defines: scope, contents table, guidelines, and owner. Written using `_templates/domain-readme.md`. Never the primary document for substantive content — links to content documents instead.

**Relative Link**
A Markdown link that uses a path relative to the current file: `[text](../domain/file.md)`. Always preferred over absolute URLs. Makes the repository portable and prevents broken links when the base URL changes.

**Review Cycle**
How frequently a document should be reviewed for accuracy and currency. Specified in the document's metadata footer. Default cycles: Constitutional docs = Annually; Business unit overviews = Quarterly; Research = 18-month expiry flag.

---

## S

**Session**
A single Claude Code conversation operating in DIS Foundation. The AI Architect's identity and instructions are loaded fresh from `CLAUDE.md` at the start of every session. Each session continues the work of the previous one.

**Single Source of Truth**
The principle that every fact in DIS Foundation exists in exactly one location. All other references link to that location rather than duplicating the content. Violations of this principle are treated as defects.

**SOP (Standard Operating Procedure)**
A document that describes a repeatable business process: Purpose, Trigger, Steps, Owner, and Review Date. Stored in `operations/processes/`. Template: [`_templates/sop.md`](_templates/sop.md).

**Status**
Document lifecycle state: `Draft`, `Active`, or `Archived`. Included in every document's metadata footer.

---

## T

**Template**
A reusable document structure stored in `_templates/`. Provides consistent formatting, required fields, and guidance for creating new documents of a specific type. See: [`_templates/README.md`](_templates/README.md).

**Three-Layer Architecture**
DIS Foundation's structural model: Constitutional Layer (defines the system), Domain Knowledge Layer (contains knowledge), Infrastructure Layer (templates and archive). See: [ARCHITECTURE.md](ARCHITECTURE.md).

---

## V

**Values**
The five core convictions that define how DIS Group behaves: Intelligence Before Scale, Integrity Without Exception, Systems Over Individuals, Long-Term Thinking, Simplicity as Discipline. Documented in `PRINCIPLES.md`.

**Version**
DIS Foundation uses semantic versioning for the repository state, tracked in `CHANGELOG.md` and `PROJECT_CONTEXT.md`. Not individual document versions — Git provides that. The repository version reflects significant structural or content milestones.

**Vision**
DIS Group's long-range strategic intent: to become the leading intelligent industrial group in its markets. Documented in `VISION.md`. The Vision is reviewed annually by the CEO.

---

## Related Documents

- [ARCHITECTURE.md](ARCHITECTURE.md) — system design and information architecture
- [PRINCIPLES.md](PRINCIPLES.md) — core values and behavioral constraints
- [CLAUDE.md](CLAUDE.md) — AI Architect constitution
- [`_templates/README.md`](_templates/README.md) — template library

---

*Owner: AI Architect | Status: Active | Last updated: 2026-07-05*
