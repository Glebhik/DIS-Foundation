# Technical Overview — DIS Travel

*Prepared for: Skyscanner Partnerships and Technology Teams*
*Classification: Confidential — For Partnership Discussion Only*
*Date: July 2026*

---

## About This Document

This document provides Skyscanner's technical team with an honest overview of DIS Travel's planned architecture, integration design, and current development status.

We use the word "planned" deliberately. DIS Travel is in the foundation phase of its build. The architecture described here is designed and documented — not fully implemented. We believe that architectural honesty at this stage of a partnership conversation is more useful than an optimistic status representation.

Where components are implemented, we say so. Where they are designed and in development, we say so. Where they are on the roadmap, we say so.

---

## Architecture Philosophy

DIS Travel's architecture is governed by five principles, drawn from DIS Group's published technology standards:

1. **Data First** — every architectural decision is evaluated on its impact to data quality, accessibility, and security
2. **Composable over Monolithic** — well-chosen composable components over single all-in-one platforms
3. **Build Intelligence on Solid Operations** — AI is built on top of working operational systems, not on top of uncertainty
4. **Observability as a First-Class Concern** — every system exposes metrics, logs, and traces
5. **AI-Native by Design** — AI is a first-class architectural component, not an add-on layer

---

## System Architecture Overview

DIS Travel's architecture follows a five-layer model:

```
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 5: PRESENTATION                                              │
│  Web application · API endpoints · Integration connectors           │
│  How organisations and their systems access DIS Travel intelligence  │
│  Status: Design phase                                               │
└─────────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 4: INTELLIGENCE                                              │
│  LLM reasoning · Policy analysis · Carbon calculation engine        │
│  Destination risk synthesis · Market pattern analysis               │
│  Status: Design phase — AI governance published                     │
└─────────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 3: DATA PLATFORM                                             │
│  Data warehouse · Enrichment pipelines · Normalisation              │
│  Data catalogue · Quality monitoring                                │
│  Status: Infrastructure selection in progress                       │
└─────────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 2: DATA INGESTION                                            │
│  Travel content connectors · Partner data APIs                      │
│  ESG data feeds · Policy management system inputs                   │
│  Status: Integration design complete — implementation pending       │
└─────────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 1: FOUNDATION INFRASTRUCTURE                                 │
│  Cloud infrastructure · Identity & access · Security baseline       │
│  Audit logging · Observability stack                                │
│  Status: Architecture defined — deployment in progress             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Intelligence Layer — AI Architecture

### AI Design Principles

DIS Travel's AI layer is governed by DIS Group's published AI governance policy. Key relevant constraints:

- **Class classification system (1–4 by risk):** Travel intelligence outputs that inform purchasing decisions are Class 2; outputs that trigger automated actions are Class 3 and require additional oversight
- **Augment, Don't Replace pattern:** AI produces intelligence — human users make decisions
- **Audit logging:** All AI inputs and outputs in Class 2+ systems are logged with timestamp
- **No PII to external models:** Personal traveller data is not passed to external LLM APIs

### Intelligence Components (Planned)

**1. Policy Intelligence Engine**
- Ingests organisational travel policies in structured format
- Analyses booking options against policy at search time
- Classifies trips by compliance status
- Flags exceptions with reasoning
- Technology: Structured prompt engineering over policy documents + LLM API

**2. Destination Intelligence Synthesiser**
- Aggregates publicly available destination data: visa requirements, health advisories, security assessments, local context
- AI-synthesises to a standardised intelligence brief per destination
- Refreshed on defined cadences with change detection
- Technology: Retrieval-Augmented Generation (RAG) over structured destination knowledge base

**3. Carbon Calculation Engine**
- Route-level carbon attribution using aircraft type, routing, and load factor
- Per-trip and per-traveller carbon reporting
- Integration with DIS Group's ESG data infrastructure
- Output feeds directly into Scope 3 reporting workflows
- **Data dependency on Skyscanner:** Route, carrier, and aircraft-type data at the granularity required for accurate calculation requires a structured partner data relationship

**4. Market Intelligence Processor**
- Analyses pricing patterns across routes and timeframes
- Identifies optimal booking windows
- Tracks carrier and hotel supplier performance metrics
- Technology: Time-series analysis on historical pricing data

---

## Data Architecture

### Data Domain Model

DIS Travel's data is organised into four domains:

| Domain | Description | Key Entities |
|---|---|---|
| **Travel Content** | Flights, hotels, ground transport — routes, pricing, availability | Route, Carrier, Fare, Property, Availability |
| **Organisation** | Corporate policies, traveller profiles, cost centre structures | Policy, Traveller, CostCentre, ApprovalChain |
| **Intelligence** | AI-derived insights, risk assessments, carbon data | Destination, RiskBrief, CarbonFactor, PolicyFlag |
| **ESG** | Carbon accounting, reporting datasets, target tracking | EmissionRecord, ReportingPeriod, TargetFrame |

### Data Ownership Principles

DIS Group's published principle: *"Every data asset DIS Group generates is a strategic asset. We control our data, we understand it, and we use it. We do not gift data to third parties without explicit strategic justification."*

In practice for DIS Travel:
- Organisation and traveller data remains within the customer's data boundary
- Intelligence outputs are DIS Travel's proprietary asset
- Travel content data from partners (including Skyscanner) is governed by the applicable partnership agreement
- Carbon output data is controlled by the reporting organisation

---

## Integration Architecture

### External Integration Design

DIS Travel is designed as an integration-first platform. The intelligence layer has no value without high-quality travel content as its foundation.

```
┌──────────────────────────────────────────────────────────────────┐
│                      DIS TRAVEL PLATFORM                         │
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────────────┐  │
│  │ INTELLIGENCE │    │ DATA PLATFORM│    │ ORGANISATION DATA │  │
│  │    LAYER     │◄───│  (Warehouse) │◄───│    (CRM / HRIS)   │  │
│  └──────────────┘    └──────┬───────┘    └───────────────────┘  │
│                             │                                    │
└─────────────────────────────┼────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
    ┌─────────▼──────┐ ┌─────▼────────┐ ┌───▼──────────────┐
    │   SKYSCANNER   │ │ ESG PLATFORM │ │  OTHER TRAVEL    │
    │  Travel Content│ │ Carbon Data  │ │  DATA SOURCES    │
    │  Route / Fare  │ │ ESG Infra    │ │                  │
    │  Carrier Data  │ │              │ │                  │
    └────────────────┘ └──────────────┘ └──────────────────┘
```

### Skyscanner Integration Design

The integration between DIS Travel and Skyscanner is designed in three functional layers:

**Layer 1: Content Foundation**

Purpose: Provide DIS Travel's intelligence layer with the comprehensive travel content it requires.

Data types sought:
- Route and schedule data (origin-destination pairs, carriers, frequencies)
- Real-time pricing and availability
- Carrier and aircraft metadata (aircraft type per route — required for carbon calculation)
- Historical fare patterns (for market intelligence)

Integration pattern: API-based, push or pull depending on data type and freshness requirement.

**Layer 2: Booking Distribution**

Purpose: When DIS Travel intelligence drives a booking decision, connect the booking action to Skyscanner's supplier ecosystem.

Pattern: Deep link or embedded search integration — DIS Travel surfaces the intelligence; the booking is completed through Skyscanner's supplier connections.

Value for Skyscanner: High-intent, corporate-buyer bookings with known organisational context — a different transaction quality than consumer metasearch.

**Layer 3: Carbon Data Enrichment**

Purpose: Enrich route-level pricing data with the carrier and aircraft information required for accurate Scope 3 carbon attribution.

Data sought: Aircraft type per scheduled route, operational aircraft type actuals (where available).

This layer enables DIS Travel's carbon calculation to achieve route-level accuracy rather than relying on industry average emissions factors — a material difference for organisations with commitments to accurate Scope 3 reporting.

---

## Security Architecture

DIS Travel is designed to enterprise security standards from the foundation.

| Control | Design |
|---|---|
| **Identity** | SSO integration with enterprise identity providers (SAML 2.0 / OIDC) |
| **Data in transit** | TLS 1.3 for all external communications |
| **Data at rest** | AES-256 encryption for all stored data |
| **Access control** | Role-based access with least-privilege defaults |
| **Audit logging** | Immutable audit log for all data access and AI operations |
| **PII handling** | Traveller PII stays within the customer's organisational boundary |
| **Secrets management** | No credentials in code, configuration files, or repositories |
| **Vulnerability management** | Automated scanning; defined remediation SLAs |

---

## Technology Stack Philosophy

DIS Travel does not have a published stack for external disclosure at this stage — stack decisions are being made through Architecture Decision Records (ADRs) as the build progresses. What we can share:

**Approach:**
- Cloud-native infrastructure (specific provider TBD via ADR)
- API-first design — every component exposes a programmatic interface
- Managed services where commodity; bespoke where differentiation requires it
- LLM APIs from leading providers (governed by DIS Group's AI governance policy)
- No proprietary data formats — open standards where possible

**What this means for Skyscanner integration:**
- REST or GraphQL API integration, whichever Skyscanner's B2B programme supports
- Standard OAuth 2.0 / API key authentication
- Webhook or polling architecture for near-real-time data, batch for historical
- Full logging and monitoring of all Skyscanner data consumption

---

## Development Status — Honest Assessment

| Component | Status | Expected Completion |
|---|---|---|
| Architecture design | ✅ Complete | — |
| AI governance policy | ✅ Published | — |
| Data domain model | ✅ Designed | — |
| Foundation infrastructure | 🔄 In progress | Q3 2026 |
| Data platform (warehouse + pipelines) | 📋 Scoped | Q4 2026 |
| Intelligence layer — Policy engine | 📋 Designed | Q1 2027 |
| Intelligence layer — Carbon engine | 📋 Designed | Q1 2027 |
| Intelligence layer — Destination intel | 📋 Designed | Q2 2027 |
| Skyscanner integration — Content | 📋 Designed | Q1–Q2 2027 |
| Skyscanner integration — Booking | 📋 Designed | Q2 2027 |
| Skyscanner integration — Carbon data | 📋 Designed | Q2 2027 |
| Presentation layer (web app) | 📋 Design phase | Q2 2027 |
| Enterprise pilot readiness | — | Q2–Q3 2027 |

*Legend: ✅ Complete | 🔄 In progress | 📋 Scoped/designed, implementation pending*

---

## What a Technical Partnership Discussion Would Cover

We would want to explore the following with Skyscanner's technical team:

1. **Data structure and freshness** — What does Skyscanner's B2B data product look like at the content layer? What refresh cadences are achievable?

2. **Aircraft and carrier metadata** — What level of detail is available per scheduled route? Is operational aircraft type accessible?

3. **Integration patterns** — What does Skyscanner's preferred B2B integration architecture look like? Webhook, batch, streaming?

4. **Historical data access** — What depth of historical fare data is available for market intelligence use cases?

5. **Carbon data collaboration** — Is there appetite to co-develop a carbon enrichment dataset anchored in route-level aircraft type data?

6. **Distribution architecture** — How does Skyscanner's deep-link and booking referral infrastructure work at the enterprise level?

---

## Related Documents

- [COMPANY_PRESENTATION.md](COMPANY_PRESENTATION.md) — Strategic overview
- [EXECUTIVE_ONE_PAGER.md](EXECUTIVE_ONE_PAGER.md) — Executive summary
- [DIS Group AI Governance](../../ai/governance.md) — Published AI governance policy
- [DIS Group Technology Architecture](../../technology/architecture.md) — Group-level architecture
- [DIS Group AI Strategy](../../ai/strategy.md) — Group AI strategy

---

*Owner: CTO / Technical Lead | Status: Active | Last updated: 2026-07-05*
*DIS Group — Confidential. Prepared for Skyscanner partnership discussions only.*
