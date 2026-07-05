# Project Context — DIS Foundation

DIS Foundation is the corporate operating system of DIS Group. This document explains what it is, why it exists, how it is structured, and how it should be used and maintained.

Read this document when you are new to this repository, when onboarding a new contributor, or when something about the repository's design requires justification.

---

## What DIS Foundation Is

DIS Foundation is a **Git-based corporate knowledge base** — a structured collection of documents that captures everything DIS Group knows about itself: its strategy, operations, businesses, principles, processes, and decisions.

It is designed to be:

- **Navigable by humans** — clear hierarchy, cross-links, and a master index
- **Maintained by AI** — Claude Code's AI Architect role is encoded in [CLAUDE.md](CLAUDE.md)
- **Trusted as a source of truth** — one canonical location for each fact, no duplication
- **Durable** — documents are written to be understood years later, by people who weren't in the room

---

## Why a Git Repository

Most companies store knowledge in wikis, shared drives, or email threads. Each has a fatal flaw: wikis drift and become unnavigable; shared drives have no version history or structure discipline; email threads disappear.

A Git repository gives DIS Foundation properties that no other system provides by default:

| Property | Benefit |
|---|---|
| **Version control** | Every change is recorded. Who changed what, when, and why. |
| **Branching** | Draft documents can be developed in branches before merging |
| **Diffs** | Exactly what changed between any two versions is always visible |
| **Pull requests** | Major changes can be reviewed before they become canonical |
| **Search** | Full-text search across all documents via GitHub or local tools |
| **Portability** | The entire knowledge base is a local clone — no vendor lock-in |
| **Immutability by convention** | Archive instead of delete; the history is never lost |

---

## The AI Architect Model

DIS Foundation is maintained by a combination of human contributors and an AI Architect — a Claude Code session operating under the [CLAUDE.md](CLAUDE.md) constitution.

### What the AI Architect does
- Creates and maintains document structure
- Writes and improves documentation
- Detects inconsistencies and proposes fixes
- Keeps INDEX.md and all section READMEs current
- Commits changes with clear, structured messages
- Identifies missing documents and flags them
- Proactively suggests structural improvements

### What the AI Architect does not do
- Make business decisions (it documents them)
- Invent facts (it formats and structures what it is given)
- Replace human judgment on sensitive topics

### Continuity
The AI Architect's identity and rules are encoded in [CLAUDE.md](CLAUDE.md). Every Claude Code session that opens this repository loads CLAUDE.md automatically, inheriting the full constitution. The AI does not need to be re-briefed. Sessions are continuous.

---

## Repository Structure

```
DIS-Foundation/
│
├── # Constitutional Layer (root)
├── CLAUDE.md              ← AI Architect constitution (auto-loaded)
├── INDEX.md               ← Master navigation hub
├── README.md              ← Repository introduction
├── PROJECT_CONTEXT.md     ← This document
├── DIS_GROUP_OVERVIEW.md  ← What DIS Group is
├── VISION.md              ← Where DIS Group is going
├── PRINCIPLES.md          ← How DIS Group operates
├── ROADMAP.md             ← How we get there
│
├── # Business Units
├── recycling/             ← Recycling business
├── energy/                ← Energy business
├── esg/                   ← ESG framework and reporting
│
├── # Corporate Functions
├── company/               ← Org identity, culture, onboarding
├── strategy/              ← Vision, OKRs, roadmap
├── finance/               ← Policy, budgets, approvals
├── legal/                 ← Contracts, compliance, IP
├── operations/            ← SOPs, tools, hiring
├── marketing/             ← Brand, messaging, campaigns
├── partners/              ← Alliances, integrations
│
├── # Capabilities
├── technology/            ← Architecture, stack, ADRs
├── ai/                    ← Strategy, agents, governance
├── research/              ← Market and competitive intelligence
├── travel/                ← Travel policy and intelligence
│
└── archive/               ← Superseded docs (append-only)
```

The constitutional layer at the root defines the operating rules and identity of the group. Domain folders contain all execution-level knowledge.

---

## How to Use This Repository

### Finding Information
1. Start at [INDEX.md](INDEX.md) — the master navigation hub
2. Navigate to the relevant domain folder
3. Each folder's `README.md` describes what lives there
4. Use GitHub search or `grep` for specific terms across all documents

### Adding Information
1. Determine the correct domain — every document has exactly one home
2. Create the file using `kebab-case.md` naming
3. Include: `# Title`, description paragraph, content, and footer (`*Owner: Role | Last updated: YYYY-MM-DD*`)
4. Link the document from the section `README.md`
5. Update `INDEX.md` if it is a key or landmark document
6. Commit with message format: `domain: short imperative description`

### Updating Information
- Edit in place for small updates (typos, factual corrections)
- For major rewrites: archive the old version to `/archive/[domain]/old-name-YYYY-MM.md`, then create the fresh version
- Always update the `Last updated` footer

### Removing Information
Never delete. Move to `/archive/[domain]/` with a date suffix. Add to the top of the archived document:
```
> Archived: YYYY-MM-DD. Superseded by [link to new document].
```

---

## Governance

| Role | Responsibility |
|---|---|
| **CEO / Principal** | Approves major structural changes, owns Vision and Principles |
| **AI Architect** | Maintains structure, creates documentation, enforces standards |
| **Domain Owners** | Responsible for accuracy and currency of their domain's documents |
| **All Contributors** | Follow naming conventions, link from READMEs, never delete |

---

## Contribution Standards

| Standard | Rule |
|---|---|
| File names | `kebab-case.md` |
| Folder names | `lowercase-no-spaces` |
| Required fields | Title, description paragraph, owner + date footer |
| Confidential docs | `> **[CONFIDENTIAL]`** blockquote at top |
| No secrets | Never commit credentials, API keys, or PII |
| Archive not delete | All removed content goes to `/archive/` |
| Links | Use relative paths: `../strategy/roadmap.md` |

Full standards: [CLAUDE.md](CLAUDE.md)

---

## Version History

| Version | Date | Summary |
|---|---|---|
| 0.1 | 2026-07-05 | Initial repository structure — 13 domain folders, INDEX.md, CLAUDE.md, README.md |
| 0.2 | 2026-07-05 | AI Constitution published — CLAUDE.md rewritten, 3 business unit domains added (recycling, energy, esg) |
| 0.3 | 2026-07-05 | Constitutional layer completed — VISION, PRINCIPLES, ROADMAP, DIS_GROUP_OVERVIEW, PROJECT_CONTEXT created |
| 0.4 | 2026-07-05 | Digital Operating System expanded — ARCHITECTURE.md, CHANGELOG.md, GLOSSARY.md, 7 templates in _templates/, company/mission.md, ai/strategy.md, ai/governance.md, technology/architecture.md, ADR-001; Chief AI Architect mandate encoded in CLAUDE.md |

---

## Related Documents

- [CLAUDE.md](CLAUDE.md) — AI Architect constitution and operating rules
- [INDEX.md](INDEX.md) — Master navigation
- [DIS_GROUP_OVERVIEW.md](DIS_GROUP_OVERVIEW.md) — What we are building this for
- [VISION.md](VISION.md) — The end state
- [PRINCIPLES.md](PRINCIPLES.md) — The rules we operate by
- [ROADMAP.md](ROADMAP.md) — The path forward

---

*Owner: AI Architect / CEO Office | Last updated: 2026-07-05*
