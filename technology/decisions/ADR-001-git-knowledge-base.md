# ADR-001: Use Git as the Corporate Knowledge Base

An Architecture Decision Record documenting the decision to use a Git repository as the foundation of DIS Foundation, the corporate knowledge base and digital operating system.

---

## Status

`Accepted`

---

## Date

2026-07-05

## Deciders

CEO / Principal, AI Architect

---

## Context

DIS Group needed a system for managing corporate knowledge: strategy documents, operational procedures, business intelligence, governance policies, and institutional memory.

The primary requirements were:
- Single source of truth — one canonical location per fact, no duplication
- Version history — who changed what, when, and why
- AI-maintainable — an AI system should be able to read, navigate, and update the system
- Portable — not locked to a specific vendor's infrastructure
- Low operational overhead — should not require dedicated IT infrastructure to operate
- Markdown-native — structured text without proprietary formats
- Searchable and linkable — full-text search and stable deep links

The problem with common alternatives:
- **Wikis (Notion, Confluence):** Rich editing, but vendor lock-in, no local diff, poor git integration, and the structure degrades into a flat page dump without enforcement
- **Shared drives (Google Drive, SharePoint):** No structure enforcement, no meaningful version control for text, no programmatic access pattern
- **Documentation sites (GitBook, Docusaurus):** Require build pipeline, less suited to internal ops docs
- **Email and Slack:** No structure, not searchable at scale, knowledge disappears

---

## Decision Drivers

- Need for full version history with diff capability
- AI session continuity — the system must be readable by AI without human re-briefing
- No vendor lock-in — corporate knowledge must not be trapped in a proprietary platform
- Portability — any team member can clone the full knowledge base locally
- Markdown as universal format — readable everywhere, writeable by both humans and AI
- Branching — draft documents can live in branches before merging to main
- Pull requests — significant structural changes can be reviewed before becoming canonical

---

## Options Considered

### Option 1: Git repository (Markdown files)

Plain Markdown files in a Git repository, hosted on GitHub.

**Pros:**
- Full version history with diff at the line level
- No vendor lock-in — files are plain text
- AI-legible by design — consistent structure + CLAUDE.md = session continuity
- Pull requests enable review-before-merge
- Free-tier hosting on GitHub
- Full-text search via GitHub or local grep
- Cloneable — entire knowledge base available offline

**Cons:**
- No rich WYSIWYG editing
- Requires familiarity with Markdown and Git
- No built-in permissions (GitHub roles handle this)
- Tables and complex formatting require Markdown discipline

---

### Option 2: Notion

Collaborative wiki with database capabilities.

**Pros:**
- Rich editing UI
- Good for non-technical users
- Built-in databases for structured data

**Cons:**
- Vendor lock-in — content lives in Notion's proprietary format
- Export quality is poor — Markdown export loses formatting
- No real version control (Notion has page history, not git-quality diffs)
- AI integration requires dedicated tooling (API)
- Structural discipline requires active enforcement — Notion tends toward page sprawl

---

### Option 3: Confluence

Enterprise wiki.

**Pros:**
- Rich editing; enterprise auth integration
- Familiar to many enterprise users

**Cons:**
- High cost for small teams
- Even more vendor lock-in than Notion
- Complex to administer
- AI integration requires significant tooling effort

---

## Decision

We chose **Option 1: Git repository (Markdown files)**.

The decisive factors were: (1) genuine version control at the diff level — not page history but line-by-line changes; (2) AI session continuity via `CLAUDE.md` — the entire system design, domain map, and operating rules are loaded by any AI session automatically; (3) no vendor lock-in for corporate memory; and (4) Markdown is a universal format readable by humans, AI systems, and every text tool.

The lack of a rich editing UI is a genuine trade-off. It is accepted because the primary maintenance agent is AI, not casual human editors — and AI works better with plain text than proprietary formats.

---

## Consequences

### Positive
- Full history of every change to the knowledge base, forever
- AI sessions are immediately productive without human re-briefing
- No vendor dependency for corporate memory
- Entire knowledge base is portable and clonable
- Pull requests create a natural review process for major changes

### Negative
- Non-technical contributors may find Markdown and Git friction-ful
- No built-in database views (addressed by structured Markdown tables + AI queries)
- No real-time collaboration (addressed by short-lived branches)

### Risks
- **Risk:** Contributors bypass Git and make changes outside process
  **Mitigation:** AI Architect enforces structure; GitHub branch protection for main
- **Risk:** Markdown discipline degrades over time
  **Mitigation:** Templates (`_templates/`), AI Architect proactive review, CLAUDE.md standards
- **Risk:** Repository grows too large for efficient cloning
  **Mitigation:** Archive convention keeps live tree clean; binary files are stored externally and linked

---

## Review Trigger

This decision should be revisited if:
- The team grows large enough that Git friction becomes a meaningful productivity drag
- A clearly superior AI-native knowledge system emerges that provides the same properties without the friction
- The primary maintenance agent shifts from AI to a large non-technical team

---

## Related Documents

- [technology/architecture.md](../architecture.md)
- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [PROJECT_CONTEXT.md](../../PROJECT_CONTEXT.md) — includes rationale for Git choice

---

*Owner: CTO / AI Architect | Status: Accepted | Last updated: 2026-07-05*
