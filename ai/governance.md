# AI Governance Policy — DIS Group

This document defines the rules, roles, and processes governing how DIS Group develops, deploys, and monitors AI systems. It is binding — no AI system that touches production data, external parties, or material business decisions may be deployed without complying with this policy.

---

## Governance Principles

### 1. Human Accountability
Every AI system has a named human owner who is accountable for its outputs. AI makes recommendations; humans make decisions on material matters. Accountability cannot be delegated to a model.

### 2. Transparency
We know what our AI systems do, what data they use, and what their failure modes are. We do not deploy black-box systems where we cannot explain outputs to stakeholders.

### 3. Proportionality
Governance overhead should be proportionate to risk. A low-risk document summarization tool requires minimal oversight. An AI system influencing a trading decision requires extensive review, audit logs, and human checkpoints.

### 4. Continuous Monitoring
Deploying an AI system does not complete the governance obligation — it begins it. All production AI systems are monitored for performance, drift, and unintended behavior.

### 5. Privacy and Data Minimization
We use the minimum data necessary for each AI use case. Personal data is never passed to external models without explicit consent and legal review.

---

## Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **CTO / AI Lead** | Approves all production AI deployments; maintains this policy; owns AI infrastructure |
| **Business Unit Lead** | Sponsors AI use cases within their unit; accountable for business outcomes |
| **AI Agent Owner** | Named owner of a specific agent or system; responsible for spec, monitoring, and incident response |
| **Legal** | Reviews data usage, privacy implications, and contractual commitments |
| **CFO** | Reviews AI systems with financial implications |
| **All Users** | Report issues; do not circumvent governance processes |

---

## Classification of AI Systems

All AI systems are classified by risk level, which determines the governance requirements.

| Class | Definition | Examples | Review Required |
|---|---|---|---|
| **Class 1 — Low Risk** | Internal productivity tools; outputs reviewed by a human before action | Summarization, document drafting, search | Lightweight — log and document |
| **Class 2 — Medium Risk** | Systems that inform significant decisions; outputs may be acted on without manual review | Market intelligence, research synthesis, scheduling support | Pre-deployment review + quarterly audit |
| **Class 3 — High Risk** | Systems with direct financial, legal, or safety implications; autonomous actions in production | Trading decision support, contract analysis, automated reporting | Full review process; continuous monitoring |
| **Class 4 — Critical** | Systems making or directly triggering consequential real-world actions | Autonomous trade execution, automated regulatory filings | Board-level approval; continuous human oversight |

---

## Pre-Deployment Review Process

All Class 2, 3, and 4 systems require a Pre-Deployment Review before going live.

### Required Documentation
Before review, the proposer must complete an Agent Specification in `ai/agents/` including:

- [ ] **Purpose** — What problem does this system solve?
- [ ] **Inputs** — What data does it consume? From where?
- [ ] **Outputs** — What does it produce? What action does it trigger?
- [ ] **Risk Class** — Which class (1–4) and why?
- [ ] **Failure modes** — What happens when it is wrong? How wrong can it be?
- [ ] **Human checkpoints** — Where does a human review or override?
- [ ] **Data handling** — Does it use PII? External models? How is data secured?
- [ ] **Monitoring plan** — How will performance be tracked? What triggers a review?
- [ ] **Rollback plan** — How is the system disabled if it behaves unexpectedly?
- [ ] **Owner** — Named individual accountable for this system

### Review Panel
- Class 2: AI Lead + Business Unit Lead
- Class 3: CTO + Legal + Business Unit Lead
- Class 4: CEO + CTO + Legal + CFO

### Review Outcomes
- **Approved** — System may go to production per the documented spec
- **Approved with Conditions** — System may deploy with specific mitigations in place
- **Deferred** — Additional information or changes required before re-review
- **Rejected** — System may not be deployed; reasons documented

---

## Acceptable Use Policy

### AI May Be Used For
- Summarizing, synthesizing, or drafting documents and communications
- Analyzing data and producing reports or visualizations
- Answering questions from structured knowledge bases (including DIS Foundation)
- Automating repetitive, well-defined tasks with human review
- Research, market intelligence, and competitive analysis
- Supporting — but not replacing — decisions

### AI May Not Be Used For
- Making material financial, legal, or strategic decisions autonomously
- Processing personal data of employees or customers without legal sign-off
- Communicating externally on behalf of DIS Group without human review
- Any action that would create a legal or contractual commitment
- Circumventing existing approval workflows
- Generating content that misrepresents DIS Group's position, capabilities, or financial status

### Special Restrictions on External Models (APIs)
- No DIS Group confidential or proprietary data in prompts without explicit approval
- No personal data in prompts without legal review and data processing agreement
- No material strategic information in prompts (trading positions, unreleased financial data, M&A considerations)
- External model usage must be logged at the application level

---

## Prompt Engineering Standards

All prompts used in production AI systems must be:

1. **Documented** — Stored in `ai/prompts/` with version history
2. **Tested** — Evaluated against a set of representative inputs before production
3. **Reviewed** — Reviewed by the AI Lead and Business Unit Lead before deployment
4. **Versioned** — Never overwritten in place; new versions create new files

See `ai/prompts/README.md` *(to be created)* for the prompt library structure.

---

## Monitoring Requirements

All production AI systems (Class 2+) must have:

| Requirement | Description |
|---|---|
| **Audit log** | Every system input and output logged with timestamp and user |
| **Performance dashboard** | Key quality metrics tracked over time |
| **Alert thresholds** | Automated alerts for anomalous outputs or errors |
| **Periodic review** | Class 2: quarterly; Class 3: monthly; Class 4: continuous |
| **Drift detection** | Process to detect when a model's behavior changes from baseline |

---

## Incident Response

An AI governance incident is any event where an AI system produces an output that causes harm, violates this policy, or triggers a significant business risk.

### Incident Levels

| Level | Definition | Response Time | Escalation |
|---|---|---|---|
| P1 — Critical | Material financial, legal, or reputational harm | Immediate | CEO + CTO + Legal within 1 hour |
| P2 — Significant | Incorrect output acted upon; PII exposure | Within 4 hours | CTO + Legal |
| P3 — Minor | Incorrect output caught before action; policy violation | Within 24 hours | AI Lead |

### Response Process
1. **Contain** — Disable the system if it is causing ongoing harm
2. **Assess** — Determine scope and impact
3. **Notify** — Escalate per the level above
4. **Remediate** — Fix root cause before re-enabling
5. **Document** — Post-incident report in `ai/incidents/` *(folder to be created when needed)*
6. **Review** — Update governance policy or agent spec to prevent recurrence

---

## Prohibited AI Uses

The following are prohibited regardless of business justification:

- Impersonating a human in any interaction where the other party has not consented to AI interaction
- Discriminating against employees or candidates based on AI-generated assessments that use protected characteristics
- Generating misleading financial projections, market data, or legal analysis presented as authoritative
- Surveillance of employees or partners without explicit disclosure and consent
- Autonomous financial transactions above any approved threshold
- Training models on data obtained without appropriate rights

---

## Policy Maintenance

This policy is reviewed by the CTO and Legal annually, or immediately following:
- A P1 or P2 incident
- A significant change in AI capability or available models
- A change in applicable regulation

Proposed changes are discussed with the AI Lead and Business Unit Leads before adoption.

---

## Related Documents

- [ai/README.md](README.md) — AI domain overview
- [ai/strategy.md](strategy.md) — AI strategy and use case prioritization
- [PRINCIPLES.md](../PRINCIPLES.md) — Principles that underpin this policy
- [legal/README.md](../legal/README.md) — Legal framework
- [GLOSSARY.md](../GLOSSARY.md) — Term definitions

---

*Owner: CTO / AI Lead | Status: Active | Review cycle: Annual | Last updated: 2026-07-05*
