# AI Strategy — DIS Group

This document defines how DIS Group approaches artificial intelligence: why it matters to us, where we invest, how we build capability, and what success looks like.

AI is not a feature or a project at DIS Group. It is a core strategic capability — as fundamental to our competitive position as our physical assets and our capital.

---

## Strategic Rationale

DIS Group's competitive advantage is ultimately an intelligence advantage. We operate in markets — recycling, energy, materials — where the difference between average and excellent outcomes is information: knowing commodity prices before others act on them, predicting equipment failures before they happen, routing logistics more efficiently, identifying regulatory shifts earlier.

AI multiplies the value of information. It processes data at scale, surfaces patterns humans miss, and automates decisions that don't require human judgment — freeing our people to focus on decisions that do.

The question is not whether AI matters to DIS Group. The question is how fast we build the capability and how well we deploy it.

---

## AI Vision

**By 2028, AI is embedded in every material operational decision across DIS Group. No business unit operates without AI-generated intelligence. No investment decision is made without AI-processed market data.**

The specific end state:
- Every business unit has at least one AI agent operating in production
- DIS Group's proprietary data assets are a recognized competitive moat
- Our AI capability attracts talent that would not otherwise consider industrial businesses
- External partners seek us for AI collaboration

---

## Priority Use Cases

### Tier 1: High Value, Near-Term (Deploy in Phase 1)

| Use Case | Business Unit | Value Driver | Complexity |
|---|---|---|---|
| Commodity price intelligence | Recycling | Better offtake timing and pricing | Medium |
| Regulatory change monitoring | Energy / Recycling | Early response to regulatory shifts | Low |
| Document intelligence — contracts, permits | Legal / All | Faster review, risk flag extraction | Low |
| Knowledge base maintenance | Group-wide | This system — AI Architect | Active |

### Tier 2: High Value, Medium-Term (Phase 2)

| Use Case | Business Unit | Value Driver | Complexity |
|---|---|---|---|
| Predictive operations (equipment, logistics) | Recycling / Energy | Downtime reduction, cost savings | High |
| Energy trading decision support | Energy | Better trade timing and risk management | High |
| ESG data aggregation and reporting | ESG | Automated compliance, reduced manual effort | Medium |
| Market research synthesis | Research / Strategy | Faster intelligence, better coverage | Low |

### Tier 3: Exploratory (Phase 3)

| Use Case | Business Unit | Value Driver | Complexity |
|---|---|---|---|
| Autonomous operational scheduling | Recycling | Labor efficiency at scale | Very High |
| Energy market forecasting | Energy | Proprietary price prediction | Very High |
| ESG platform as external product | ESG | New revenue stream | High |

---

## Build / Buy / Partner Framework

For each AI use case, we choose one of three approaches:

| Approach | When to Use | Examples |
|---|---|---|
| **Buy** (SaaS / API) | Commodity capability where differentiation is low; fastest path to value | LLM APIs (Claude, GPT), data providers, monitoring tools |
| **Build** | Where the capability is core to our competitive advantage; where our proprietary data is the differentiator | Commodity intelligence models trained on our trading data; internal AI agents with DIS Group context |
| **Partner** | Where a third party has complementary data or capability we cannot build quickly | Research partnerships, industry data consortia |

**Default posture:** Buy for commodity AI capability. Build for differentiated intelligence. Partner when speed matters and alignment is achievable.

---

## AI Infrastructure Requirements

### Data Foundation
AI is only as good as the data it processes. Before deploying AI in any business unit, establish:

1. **Data inventory** — What data does this business unit generate? Where does it live? Who owns it?
2. **Data quality baseline** — Is the data clean, consistent, and timely enough for AI use?
3. **Data infrastructure** — Can data be accessed programmatically? Is there an API or data warehouse?

### Model Infrastructure
- Approved model list: `ai/models.md` *(to be created)*
- Model governance: `ai/governance.md`
- Prompt library: `ai/prompts/` *(to be created)*
- Agent specifications: `ai/agents/` *(to be created)*

### Security and Privacy
- No PII passed to external models without explicit consent and legal review
- All production AI agents must have audit logs
- Model outputs touching financial or legal decisions require human review

---

## Talent and Capability Model

### Internal Capability We Are Building
- AI product thinking — identifying where AI creates value, not just where it is technically possible
- Prompt engineering — systematic development and versioning of prompts
- Data engineering — building the pipelines that feed AI systems
- AI governance — operating AI responsibly and in compliance

### External Capability We Will Always Buy
- Foundation model training (we use APIs, we do not train base models)
- Specialized ML engineering for complex bespoke models

### Culture
Every person at DIS Group should understand what AI can and cannot do. We invest in AI literacy across the whole team — not just technical staff.

---

## AI Roadmap

### Phase 1 (Now — 12 months): Foundations
- [ ] AI strategy published *(this document)*
- [ ] AI governance policy published (`ai/governance.md`)
- [ ] Approved model list established (`ai/models.md`)
- [ ] Internal AI Architect operational (DIS Foundation) — **Active**
- [ ] Tier 1 use cases identified and scoped
- [ ] Data inventory completed for Recycling and Energy
- [ ] First internal AI agent deployed with spec documented

### Phase 2 (12–36 months): Deployment
- [ ] All Tier 1 use cases in production
- [ ] Tier 2 use cases scoped and in development
- [ ] Proprietary training data identified and secured
- [ ] AI performance metrics tracked and reported quarterly
- [ ] AI capability recognized by partners and talent market

### Phase 3 (36 months+): Advantage
- [ ] Tier 2 use cases in production
- [ ] Proprietary AI models creating measurable competitive advantage
- [ ] First Tier 3 use cases evaluated
- [ ] AI capability potentially monetized externally

---

## Success Metrics

| Metric | Target | Timeframe |
|---|---|---|
| Business units with AI in production | 3 of 3 | End of Phase 2 |
| AI agent count (documented, deployed) | [Target] | End of Phase 2 |
| % operational decisions informed by AI | [Target] | End of Phase 2 |
| AI cost as % of revenue | < [Target] | Ongoing |
| Data quality score (internal metric) | [Target] | End of Phase 1 |

---

## Related Documents

- [ai/README.md](README.md) — AI domain overview
- [ai/governance.md](governance.md) — AI governance and acceptable use
- [VISION.md](../VISION.md) — Strategic context for AI investment
- [technology/architecture.md](../technology/architecture.md) — Technical foundation
- [PRINCIPLES.md](../PRINCIPLES.md) ��� Principles that govern AI deployment

---

*Owner: CTO / AI Lead | Status: Active | Review cycle: Quarterly | Last updated: 2026-07-05*
