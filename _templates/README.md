# Templates — DIS Foundation

This folder contains document templates for all recurring document types in DIS Foundation.

Templates are the infrastructure layer. They ensure consistency, reduce the effort of creating new documents, and provide AI sessions with predictable structure to fill in.

**Never edit templates for a single use case.** If a template needs customization, create the document and customize it there. Edit the template only to improve the general pattern.

---

## Template Library

| Template | Use For | Type |
|---|---|---|
| [`document.md`](document.md) | Any standard document — policy, reference, overview | General |
| [`sop.md`](sop.md) | Standard Operating Procedures in `/operations/processes/` | SOP |
| [`adr.md`](adr.md) | Architecture Decision Records in `/technology/decisions/` | ADR |
| [`okr-cycle.md`](okr-cycle.md) | OKR planning cycles in `/strategy/okrs/` | OKR |
| [`partner-brief.md`](partner-brief.md) | Partner briefs in `/partners/[name]/` | Reference |
| [`research-report.md`](research-report.md) | Research reports in `/research/` | Research |
| [`domain-readme.md`](domain-readme.md) | README.md for new domain folders | Structure |

---

## How to Use a Template

1. Copy the relevant template to the target folder
2. Rename using `kebab-case.md`
3. Replace all `[PLACEHOLDER]` values with real content
4. Remove any sections that do not apply (but keep all required fields)
5. Set `Status: Draft` until the document is ready for review
6. Change to `Status: Active` when published
7. Link from the domain `README.md`
8. Update `INDEX.md` if it is a Key Document

---

## Required Fields (All Documents)

Every document in DIS Foundation — regardless of type — must have:

```
# Title
[Description paragraph]
[Content]
*Owner: [Role] | Status: [Draft/Active/Archived] | Last updated: YYYY-MM-DD*
```

---

*Owner: AI Architect | Status: Active | Last updated: 2026-07-05*
