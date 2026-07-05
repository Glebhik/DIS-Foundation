# Architecture — DIS Foundation Digital Operating System

This document explains the design of DIS Foundation itself — the architecture of the corporate operating system. It is the system documenting itself.

Read this to understand *why* the repository is structured as it is, not just *what* it contains.

---

## Design Philosophy

DIS Foundation is not a wiki, a shared drive, or a document repository. It is a **designed information system** with explicit architecture decisions, enforced conventions, and a continuous-improvement mandate.

The system is built on four convictions:

1. **Structure is not bureaucracy — it is capital.** A well-structured system compounds. Every document added to a well-designed system increases the value of every other document. Without structure, knowledge degrades into noise.

2. **AI and humans should read the same documents.** Every document is written so that a human can understand it in 2030 and a language model can extract structured information from it today. This is what "AI-native" means — not AI-generated, but AI-legible.

3. **The operating system should be self-aware.** The system contains documents that describe the system. This enables autonomous improvement, reduces onboarding time, and makes every session — human or AI — productive from the first message.

4. **Knowledge is a strategic asset.** Every fact captured here has value. Every fact not captured is a risk — a dependency on a specific person's memory.

---

## Information Architecture

### Three-Layer Model

DIS Foundation is organized in three layers:

```
┌──────────��──────────────────────────────────────────┐
│  LAYER 1: CONSTITUTION                               │
│  CLAUDE.md · INDEX.md · ARCHITECTURE.md             │
│  VISION.md · PRINCIPLES.md · ROADMAP.md             │
│  DIS_GROUP_OVERVIEW.md · PROJECT_CONTEXT.md         │
│  GLOSSARY.md · CHANGELOG.md                         │
│  What the system is and how it operates             │
└─────────────────────────────────────────────────────┘
                         ↓ governs
┌─────────────────────────────────────────────────────┐
│  LAYER 2: DOMAIN KNOWLEDGE                          │
│  /company · /strategy · /ai · /technology           │
│  /recycling · /energy · /esg                        │
│  /finance · /legal · /operations                    │
│  /marketing · /partners · /research · /travel       │
│  What DIS Group knows, organized by domain          │
└─────────────────────────────────────────────────────┘
                         ↓ executed through
┌─────────────────────────────────────────────────────┐
│  LAYER 3: INFRASTRUCTURE                            │
│  /_templates · /archive                             │
│  Templates, standards, and historical records       │
└─────────────────────────────────────────────────────┘
```

Layer 1 governs Layer 2. Layer 3 supports Layer 2. Documents in Layer 1 are never deleted — only amended or superseded with full history.

### Document Taxonomy

Every document in DIS Foundation belongs to one of these types:

| Type | Description | Location | Template |
|---|---|---|---|
| **Constitutional** | Defines the system or the company at the highest level | Root | — |
| **Domain README** | Defines scope, contents, and guidelines for a domain | `[domain]/README.md` | `_templates/domain-readme.md` |
| **Policy** | Binding rule or standard | Domain folder | `_templates/document.md` |
| **Strategy** | Direction, goals, or bets | `/strategy` or domain | `_templates/document.md` |
| **Reference** | Stable factual information | Domain folder | `_templates/document.md` |
| **SOP** | Standard operating procedure | `/operations/processes/` | `_templates/sop.md` |
| **ADR** | Architecture decision record | `/technology/decisions/` | `_templates/adr.md` |
| **OKR** | Objectives and key results | `/strategy/okrs/` | `_templates/okr-cycle.md` |
| **Research** | Analysis or intelligence report | `/research/` | `_templates/research-report.md` |
| **Partner Brief** | Partner relationship summary | `/partners/[name]/` | `_templates/partner-brief.md` |
| **Archived** | Superseded document | `/archive/[domain]/` | — |

### Metadata Schema

Every document must include these metadata fields:

```markdown
# Document Title

[One-paragraph description of this document's purpose and scope.]

---
[Document content]
---

*Owner: [Role or Name] | Status: [Draft / Active / Archived] | Last updated: YYYY-MM-DD*
```

Mandatory fields:
- `# Title` — H1 heading, document name
- Description paragraph — purpose and scope
- `Owner` — the role responsible for accuracy
- `Status` — Draft, Active, or Archived
- `Last updated` — ISO date

Optional structured fields (add to documents where relevant):
- `Review cycle:` — How often this should be reviewed
- `Confidentiality:` — If restricted, who can read it
- `Dependencies:` — What other documents this depends on

---

## Navigation Architecture

### Index-First Design

Every navigation session starts at [`INDEX.md`](INDEX.md). The index organizes domains into three tiers (Constitutional, Domain Knowledge, Infrastructure) and maintains a Key Documents checklist. It is the single entry point.

The index never duplicates content — it only links. The document itself is authoritative.

### Cross-Linking Model

```
Document A ──links to──► Document B
                          Document B ──links to──► Document C
                                                   Document C ──links back──► Document A
```

Rules:
- Every document links to at least two others using relative paths
- Cross-domain links go to the target domain's `README.md` unless linking to a specific document
- The `## Related Documents` section at the end of each document is mandatory
- Broken links are treated as defects — the AI Architect fixes them proactively

### Search Strategy

For humans: use GitHub's search (`/` shortcut) or local `grep` across the repository.

For AI: the consistent document structure, explicit cross-links, and GLOSSARY.md provide enough context to navigate without full-text search.

---

## Temporal Architecture

### Current vs. Archived

Every document has exactly one of three states:

| State | Meaning | Location |
|---|---|---|
| **Draft** | In progress, not yet authoritative | Domain folder, marked `Status: Draft` |
| **Active** | Current, authoritative, maintained | Domain folder, marked `Status: Active` |
| **Archived** | Superseded, read-only, historical | `/archive/[domain]/`, marked `Status: Archived` |

### Version Model

DIS Foundation does not use numbered document versions. Git provides the full version history. When a document is substantively rewritten:

1. Copy current version to `/archive/[domain]/[name]-YYYY-MM.md`
2. Add `> Archived: YYYY-MM-DD. Superseded by [link].` at the top of the archived copy
3. Update the live document in place
4. Commit both changes together

### Review Cycles

Documents decay. Stale documents are worse than no documents — they are actively misleading.

| Document Type | Review Cycle |
|---|---|
| Constitutional documents | Annually (or on major strategic change) |
| Business unit overviews | Quarterly |
| OKRs | Each cycle |
| Research reports | 18-month expiry flag |
| SOPs | Annually |
| ADRs | When the decision is revisited |
| Policy documents | Annually |

The ROADMAP.md maintains the review schedule for constitutional documents. Domain owners are responsible for their domain's review cadence.

---

## AI Architecture

### Session Continuity

Claude Code loads `CLAUDE.md` on every session automatically. This means the AI Architect begins every session with full context. No human briefing required.

The AI does not rely on conversational memory — it relies on the repository. Every important decision, principle, and context is in the repository. The repository is the AI's memory.

### Consistency Protocol

Before any structural change, the AI Architect checks:

1. Does this conflict with any constitutional document?
2. Does this duplicate information that already exists?
3. Does this leave any broken links?
4. Does INDEX.md need updating?
5. Does CLAUDE.md's domain map need updating?
6. Does PROJECT_CONTEXT.md's version history need a new entry?

### AI-Legible Document Design

Documents are written so that a language model can extract structured information reliably:

- **Headings** create predictable structure that maps to topics
- **Tables** make relationships machine-readable
- **Checklists** (`- [x]`) provide clear completion signals
- **Explicit owners and dates** anchor documents in time and responsibility
- **Relative links** create a navigable graph
- **The GLOSSARY** provides stable vocabulary for term resolution

### What AI Should Never Do

- Invent facts about DIS Group (only document what is provided or inferable)
- Overwrite without archiving
- Create cross-domain duplication
- Leave a session without committing completed work
- Store secrets, credentials, or PII

---

## Governance Architecture

### Three-Party Governance

| Party | Role | Authority |
|---|---|---|
| **CEO / Principal** | Approves vision, principles, strategic direction | Final authority on all constitutional docs |
| **AI Architect** | Maintains structure, creates docs, enforces standards | Executes within the constitution |
| **Domain Owners** | Keep domain content accurate and current | Authority over their domain's content |

### Change Management

| Change Type | Process |
|---|---|
| Minor edit (typo, factual update) | Direct edit, commit with `domain: fix [description]` |
| New document in existing domain | Create → link from README → update INDEX if landmark → commit |
| New domain | Create folder → add README → update domain maps in CLAUDE.md and INDEX → commit |
| Structural refactor | Archive old structure → migrate → update all links → commit with `refactor:` prefix |
| Constitutional change | Requires explicit instruction from the CEO/Principal |

---

## Evolution Architecture

### Pattern for New Domains

When a new business area, function, or capability warrants its own domain:

```
1. mkdir /[domain-name]
2. Create [domain-name]/README.md using _templates/domain-readme.md
3. Add entry to CLAUDE.md domain map (both Domain Map and Domain Ownership tables)
4. Add entry to INDEX.md under the correct tier
5. Update DIS_GROUP_OVERVIEW.md if it's a business unit
6. Update README.md directory tree
7. Commit: "refactor: add [domain] domain"
```

### Pattern for New Content Documents

```
1. Identify correct domain — one document, one home
2. Copy from _templates/ appropriate template
3. Fill in content
4. Link from domain README.md
5. Add to INDEX.md Key Documents if landmark
6. Check for cross-linking opportunities
7. Commit: "domain: add [document description]"
```

### Scaling Properties

The operating system is designed to scale:

- **More documents** — the folder structure absorbs them without reorganization
- **More domains** — the pattern above handles new domains cleanly
- **More people** — domain ownership table distributes maintenance responsibility
- **More AI sessions** — CLAUDE.md provides full context to every new session
- **More complexity** — the archive absorbs superseded content without growth in the live tree

---

## Architecture Decision Log

Major architectural decisions are recorded in [`/technology/decisions/`](technology/README.md). Decisions about the operating system itself are recorded here.

| Decision | Date | Rationale |
|---|---|---|
| Git-based knowledge base | 2026-07-05 | Version history, portability, diff-based review — see PROJECT_CONTEXT.md |
| Root-level constitutional documents | 2026-07-05 | Constitutional layer must be immediately visible and not buried in a domain |
| Three-tier INDEX organization | 2026-07-05 | Maps to how different roles navigate (business unit, function, capability) |
| `_templates/` underscore prefix | 2026-07-05 | Signals system infrastructure, not content — mirrors `.github/` convention |
| Archive-not-delete convention | 2026-07-05 | History is a strategic asset; deletion destroys institutional memory |
| AI-maintained constitution | 2026-07-05 | Enables session continuity without human re-briefing |

---

## Related Documents

- [CLAUDE.md](CLAUDE.md) — AI Architect operating rules
- [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) — Repository purpose and governance
- [GLOSSARY.md](GLOSSARY.md) — Shared terminology
- [INDEX.md](INDEX.md) — Navigation hub
- [`_templates/`](_templates/README.md) — Document templates

---

*Owner: AI Architect / CTO | Status: Active | Last updated: 2026-07-05*
