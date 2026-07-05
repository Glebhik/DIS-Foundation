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

## [0.7] — 2026-07-05

### Added
- `partners/skyscanner/final/` — production delivery folder
  - `05_DIS_Travel_Presentation.pptx` — 12-slide professional PPTX (16:9, Calibri, navy/white consulting design); generated via python-pptx
  - `03_DIS_Travel_Presentation.pdf` — PowerPoint-exported PDF of the 12-slide presentation (814KB)
  - `01_Cover_Letter.pdf` — PDF version of cover letter with DIS GROUP letterhead
  - `02_Executive_One_Pager.pdf` — PDF version of executive one-pager
  - `04_Technical_Overview.pdf` — PDF version of technical architecture overview
  - `FINAL_READINESS.md` — Confidence score (78/100), consistency verification, business risks, pre-send checklist, and delivery recommendation
  - `generate_pptx.py` — PPTX generation script (production artifact, remove before sending)
  - `generate_pdfs.py` — PDF generation script (production artifact, remove before sending)

### Changed
- `COVER_LETTER.md` — Senior Director final review: rewrote "who we are" paragraph to lead with operational track record; added explicit competitive context paragraph (Navan, SAP Concur, TravelPerk, Spotnana named and addressed architecturally); removed self-congratulatory close
- `EXECUTIVE_ONE_PAGER.md` — Added "Operational foundation" row to At-a-Glance table; added full "Competitive Context" section with platform-by-platform architectural limitation analysis; added "Risk Calibration" section defining Skyscanner's commitment at each stage
- `COMPANY_PRESENTATION.md` — Added competitive landscape table to Slide 3; replaced startup pitch "window" language in Slide 8 with narrow CSRD-specific positioning; rewrote Slide 11 "Long-Term Orientation" grounding credibility in DIS Group's three operating businesses
- `TECHNICAL_OVERVIEW.md` — Replaced generic architecture principles with four DIS Travel-specific design decisions (intelligence separable from booking, carbon as first-class data type, GDPR as data model constraint, governance-first AI deployment)

---

## [0.6] — 2026-07-05

### Changed
- `partners/skyscanner/COVER_LETTER.md` — final review pass: rewrote "who we are" to lead with operational track record (three active businesses) rather than product description; added competitive context paragraph naming Navan, SAP Concur, TravelPerk, Spotnana and explaining the architectural limitation; removed self-congratulatory close
- `partners/skyscanner/EXECUTIVE_ONE_PAGER.md` — added "Operational foundation" row to At-a-Glance table; added full "Competitive Context" section with platform-by-platform analysis; added "Risk Calibration" section defining what Skyscanner commits at each stage (initial conversation through integration build)
- `partners/skyscanner/COMPANY_PRESENTATION.md` — added competitive landscape table to Slide 3 (Navan/Concur/TravelPerk/Spotnana with architectural limitation analysis); replaced startup pitch "window" paragraph in Slide 8 with specific CSRD positioning; rewrote Slide 11 "Long-Term Orientation" to explicitly ground credibility in DIS Group's operating foundation across three existing businesses
- `partners/skyscanner/TECHNICAL_OVERVIEW.md` — replaced generic technology principles ("Data First", "Composable over Monolithic") with four DIS Travel-specific architectural decisions that differentiate from booking-platform intelligence: intelligence separable from booking, carbon as first-class data type, GDPR as data model constraint, governance-first AI deployment

---

## [0.5] — 2026-07-05

### Changed
- `partners/skyscanner/COVER_LETTER.md` — executive review improvements: replaced anonymous signatory with `[Name], Chief Executive Officer`; added proper email/website contact block; rewrote Skyscanner rationale to be specific (Partner API depth, European coverage, B2B ecosystem, ICAO/GHG Protocol for carbon attribution); added GDPR mention; changed closing to specific 45-minute meeting ask; removed superlative flattery
- `partners/skyscanner/EXECUTIVE_ONE_PAGER.md` — executive review improvements: stage updated to "Pre-launch — architecture complete, build in progress"; added GDPR compliance and EU data residency rows; Carbon capability now cites ICAO/GHG Protocol; replaced "two decades" framing with CSRD-specific context; added competitive differentiation section; closing ask made specific with enumerated agenda items
- `partners/skyscanner/COMPANY_PRESENTATION.md` — complete rebuild from executive review: added Slide 2 portfolio connecting narrative (one thesis, three markets); Slide 3 problem reframed as "what AI makes possible now" vs. generic; Slide 5 removed unsupported "only platform" claim, replaced with specific methodological differentiation (ICAO/GHG Protocol, aircraft-type specificity); Slide 7 new dedicated CSRD/regulatory slide; Slide 8 updated market timing to three specific 2026 forces (CSRD active, AI infrastructure mature, buyer requirements shifted); Slide 9 Skyscanner rationale made specific with four distinct data requirements; Slide 10 timeline made indicative with explicit flexibility language; added GDPR/data compliance throughout; fixed Slide 4 diagram to show five intelligence capabilities
- `partners/skyscanner/TECHNICAL_OVERVIEW.md` — executive review improvements: added GDPR/Data Protection section with EU data residency, PII handling table, and compliance framework; added data residency to Foundation Infrastructure layer; specified ICAO and GHG Protocol methodologies in Carbon Calculation Engine; rewrote Question 6 to demonstrate knowledge of public Partner API and ask for enterprise-level distribution architecture specifics; changed "defined remediation SLAs" to explicit Critical (24h), High (72h), Medium (30d) SLAs; improved cloud provider TBD framing as deliberate ADR governance choice; added note indicating EU residency constraint on provider selection; separated design status from implementation status in architecture diagrams

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
