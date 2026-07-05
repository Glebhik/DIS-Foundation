# AI

DIS Group's AI strategy, tooling, models, prompts, agents, and internal AI development.

AI is a core strategic capability at DIS Group — not a feature or project. See [ai/strategy.md](strategy.md) for the full rationale.

## Contents

| File / Folder | Type | Status | Description |
|---|---|---|---|
| [`strategy.md`](strategy.md) | Strategy | Active | AI strategy, use case matrix, build/buy/partner framework, roadmap |
| [`governance.md`](governance.md) | Policy | Active | AI ethics, acceptable use, deployment checklist, incident response |
| `models.md` | Reference | Planned | Approved models, usage guidelines, cost controls |
| `agents/` | Folder | Planned | Internal AI agent specs — one file per agent |
| `prompts/` | Folder | Planned | Versioned prompt library — never overwrite, create new versions |
| `experiments/` | Folder | Planned | AI experiments, evaluations, and learnings |

## Guidelines

- Read [governance.md](governance.md) before deploying any AI system.
- All production AI agents must have a spec in `agents/` before deployment.
- Prompts are versioned — never overwrite a prompt in place; create a new version.
- Link to [technology/architecture.md](../technology/architecture.md) for infrastructure context.

## Related Domains

- [technology/README.md](../technology/README.md) — AI infrastructure lives here
- [PRINCIPLES.md](../PRINCIPLES.md) — Principles that govern AI deployment
