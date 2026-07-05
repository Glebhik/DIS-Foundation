# Technology

Technical architecture, infrastructure, engineering standards, and tooling decisions for DIS Group.

Technology is not a support function — it is the backbone of DIS Group's intelligence advantage. See [technology/architecture.md](architecture.md) for the full architecture.

## Contents

| File / Folder | Type | Status | Description |
|---|---|---|---|
| [`architecture.md`](architecture.md) | Reference | Active | High-level system architecture, layers, data, security, evolution roadmap |
| `stack.md` | Reference | Planned | Approved technology stack with rationale |
| [`decisions/`](decisions/) | ADRs | Active | Architecture Decision Records — all major technology decisions |
| `decisions/ADR-001-git-knowledge-base.md` | ADR | Accepted | Decision to use Git as corporate knowledge base |
| `standards/` | Folder | Planned | Coding standards, API design, security baselines |
| `infrastructure/` | Folder | Planned | Cloud, networking, DevOps configuration |
| `runbooks/` | Folder | Planned | Operational runbooks for critical systems |

## Guidelines

- All significant technology decisions require an ADR in `decisions/`. Use [`_templates/adr.md`](../_templates/adr.md).
- `architecture.md` must be updated when the architecture changes — it is the reference document.
- Link to `/ai` for AI-specific infrastructure and model decisions.

## Related Domains

- [ai/README.md](../ai/README.md) — AI capabilities built on this infrastructure
- [ARCHITECTURE.md](../ARCHITECTURE.md) — Repository system design (distinct from technology architecture)
