# Changelog — DIS Foundation

This document records all significant changes to the DIS Foundation repository — structural changes, new documents, policy updates, and architectural decisions.

It is updated by the AI Architect at the end of every session that makes meaningful changes. Routine content edits (fixing typos, updating dates) do not require a CHANGELOG entry.

---

## Format

Each entry follows this structure:

```
## [Version] — YYYY-MM-DD
### Added
### Changed
### Deprecated
### Archived
### Fixed
```

---

## [0.4] — 2026-07-05

### Added
- `ARCHITECTURE.md` — system design document; three-layer model, information architecture, navigation, temporal model, AI architecture, governance, and evolution patterns
- `CHANGELOG.md` — this document; full session history from repository creation
- `GLOSSARY.md` — shared terminology for humans and AI; 40+ defined terms
- `_templates/` — infrastructure folder with 7 document templates
  - `_templates/README.md` — template index and usage guide
  - `_templates/document.md` — base document template
  - `_templates/sop.md` — Standard Operating Procedure template
  - `_templates/adr.md` — Architecture Decision Record template
  - `_templates/okr-cycle.md` — OKR cycle template
  - `_templates/partner-brief.md` — Partner brief template
  - `_templates/research-report.md` — Research report template
- `company/mission.md` — corporate identity document; mission, vision, values, purpose
- `ai/strategy.md` — AI strategy for DIS Group; use case matrix, build/buy/partner framework, roadmap
- `ai/governance.md` — AI governance policy; acceptable use, deployment checklist, prohibited uses, incident response
- `technology/architecture.md` — high-level system architecture; principles, layers, data architecture, security
- `technology/decisions/ADR-001-git-knowledge-base.md` — first Architecture Decision Record

### Changed
- `CLAUDE.md` — expanded mandate from AI Architect to Chief AI Architect; added Constitutional Documents section with 7-point consistency checklist; added expanded proactive behaviour rules
- `INDEX.md` — added ARCHITECTURE.md, CHANGELOG.md, GLOSSARY.md to Constitutional Documents table; updated Key Documents checklist

---

## [0.3] — 2026-07-05

### Added
- `DIS_GROUP_OVERVIEW.md` — company portfolio, capabilities, metrics dashboard, org summary
- `VISION.md` — four strategic horizons (0–12mo, 1–3yr, 3–5yr, 5–10yr); North Star statement
- `PRINCIPLES.md` — five core values, business/operational/people/ESG principles, decision framework
- `ROADMAP.md` — Phase 1 active priorities (6 tracks with checklists), Phase 2 directional, Phase 3 horizon; deferral table; governance table
- `PROJECT_CONTEXT.md` — repository purpose, AI Architect model, directory tree, version history

### Changed
- `CLAUDE.md` — added Constitutional Documents section; consistency checklist; expanded domain map to include new documents
- `INDEX.md` — Constitutional Documents navigation table at top; Key Documents checklist restructured with checked constitutional layer
- `README.md` — constitutional layer annotated in directory tree

---

## [0.2] — 2026-07-05

### Added
- `energy/README.md` — energy business domain; assets, trading, regulatory, projects
- `esg/README.md` — ESG domain; environmental/social/governance reporting and targets
- `recycling/README.md` — recycling business domain; operations, markets, compliance

### Changed
- `CLAUDE.md` — complete rewrite as AI Constitution; identity, mission, principles, standards, naming conventions, git discipline, AI behaviour, domain map, ownership table, evolution playbook
- `INDEX.md` — restructured into three tiers: Business Units, Corporate Functions, Capabilities
- `README.md` — updated directory tree with three-tier annotation

---

## [0.1] — 2026-07-05

### Added
- Initial repository structure — 13 domain folders with READMEs:
  - `company/`, `strategy/`, `products/`, `travel/`, `technology/`, `ai/`
  - `operations/`, `finance/`, `legal/`, `marketing/`, `partners/`, `research/`, `archive/`
- `CLAUDE.md` — initial AI Architect constitution
- `INDEX.md` — master navigation hub
- `README.md` — improved from initial single-line file

### Changed
- `README.md` — original single-line file expanded to full repository guide

---

## [0.0] — 2026-07-05 (Initial Commit)

### Added
- `README.md` — single-line: "Official Corporate Knowledge Base of DIS Group"

---

*Owner: AI Architect | Status: Active | Last updated: 2026-07-05*
