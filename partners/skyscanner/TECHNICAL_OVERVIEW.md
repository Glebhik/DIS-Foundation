# Technical Overview — DIS Travel

*Prepared for: Skyscanner Partnerships and Technology Teams*
*Classification: Confidential — For Partnership Discussion Only*
*Date: July 2026*

---

## About This Document

This document provides Skyscanner's technical team with an honest overview of DIS Travel's planned architecture, integration design, data protection posture, and current development status.

We use the word "planned" deliberately. DIS Travel is in the foundation phase of its build. The architecture described here is designed and documented — not fully implemented. We believe that architectural honesty at this stage of a partnership conversation is more useful than an optimistic status representation.

Where components are implemented, we say so. Where they are designed and in development, we say so. Where they are on the roadmap, we say so.

---

## Architecture Philosophy

DIS Travel's architecture reflects four specific design decisions that distinguish it from intelligence features added to booking platforms.

**1. Intelligence separable from booking.** The intelligence layer is architected to operate independently of any specific booking system. DIS Travel integrates with an organisation's existing booking tool — it does not require replacing it. This is an explicit architectural choice with a specific commercial rationale: it removes the booking displacement objection from the enterprise procurement conversation entirely.

**2. Carbon as a first-class data type — not a report.** Carbon attribution in DIS Travel is calculated at trip-creation time, stored as a structured entity with full methodology provenance (inputs, methodology version, output), and queryable at any level of aggregation. It is not a dashboard generated from expense exports. This distinction is what makes CSRD audit readiness achievable rather than approximated.

**3. GDPR as a data model constraint, not a compliance checklist.** Data minimisation and purpose limitation are enforced at the schema level — traveller PII is not present in the intelligence layer because the data model does not collect it there. This is harder to build than a policy document; it eliminates a class of compliance risk rather than managing it.

**4. Governance-first AI deployment.** AI components are not shipped until pre-deployment review is complete, risk classification is assigned, and audit logging is confirmed. This adds deployment time. It is the correct tradeoff for a platform that enterprise procurement teams will scrutinise.

---

## System Architecture Overview

DIS Travel's architecture follows a five-layer model. Status labels indicate design state, not implementation state — see the Development Status table for implementation timelines.

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
│  Status: Designed — AI governance published and operational         │
└─────────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 3: DATA PLATFORM                                             │
│  Data warehouse · Enrichment pipelines · Normalisation              │
│  Data catalogue · Quality monitoring · GDPR enforcement layer       │
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
│  Audit logging · Observability stack · EU data residency            │
│  Status: Architecture defined — deployment in progress              │
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

### Intelligence Components (Designed — Implementation Pending)

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
- Route-level Scope 3 carbon attribution using ICAO methodology for aircraft-type emissions factors and GHG Protocol Travel guidance for organisational accounting
- Per-trip and per-traveller carbon reporting with methodology version logged per calculation
- Output structured to flow directly into CSRD-compliant Scope 3 reporting workflows
- Integration with DIS Group's ESG data infrastructure
- **Methodology:** ICAO Carbon Emissions Calculator methodology (aircraft type, seat class, routing, load factor) combined with GHG Protocol Travel guidance for Category 6 Scope 3 attribution
- **Data dependency on Skyscanner:** Route-level aircraft-type data at the granularity required for ICAO-compliant calculation is not achievable from consumer-facing data sources. A structured partner data relationship with Skyscanner is an architectural requirement for this capability at the accuracy level that CSRD audit readiness demands.

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

## Data Protection and GDPR Compliance

DIS Group is incorporated in Ireland and operates under EU law. GDPR compliance is a design constraint, not a post-build consideration.

### Data Residency

- **EU data boundary:** All personal data processed by DIS Travel is stored and processed within the EU. No personal traveller data transits outside the EU boundary.
- **Cloud infrastructure:** Cloud provider selection (in progress via ADR process) is constrained to providers that can guarantee EU data residency at the infrastructure level.
- **Partner data:** Travel content data received from partners, including Skyscanner, is processed within EU infrastructure. No personal traveller data is transmitted to partner APIs.

### Traveller PII Handling

| Data Type | Handling |
|---|---|
| Traveller identity (name, passport, employee ID) | Stays within customer's organisational boundary — not transmitted to DIS Travel intelligence layer |
| Trip records (routes, dates, carrier) | Processed under customer's data processor agreement — used for intelligence, not shared with third parties |
| Carbon calculations | Owned by the reporting organisation — structured as an organisational, not individual, asset |
| Partner API queries | Anonymised or aggregate — no personal data transmitted to travel content partners |

### Compliance Framework

- **GDPR:** Data minimisation, purpose limitation, and right-to-erasure enforced at the data model level
- **Data Processing Agreements:** DPA template designed for enterprise procurement — available for review during partnership design phase
- **Audit trail:** All data access events logged with actor, timestamp, and purpose classification
- **Data retention:** Configurable per customer, with automated deletion enforcement at defined periods

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
    │  Partner API   │ │ Carbon Data  │ │  DATA SOURCES    │
    │  Route / Fare  │ │ ESG Infra    │ │                  │
    │  Carrier / A/C │ │              │ │                  │
    └────────────────┘ └──────────────┘ └──────────────────┘
```

### Skyscanner Integration Design

The integration between DIS Travel and Skyscanner is designed in three functional layers, corresponding to the three partnership components described in the Company Presentation.

**Layer 1: Content Foundation**

Purpose: Provide DIS Travel's intelligence layer with the comprehensive travel content it requires.

Data types sought:
- Route and schedule data (origin-destination pairs, carriers, frequencies)
- Real-time pricing and availability
- Carrier and aircraft metadata (aircraft type per route — required for ICAO carbon calculation)
- Historical fare patterns (for market intelligence)

Integration pattern: REST API integration against Skyscanner's partner programme; push or pull cadence depending on data type and freshness requirement.

**Layer 2: Booking Distribution**

Purpose: When DIS Travel intelligence drives a booking decision, connect the booking action to Skyscanner's supplier ecosystem.

Pattern: Referral or deep-link integration — DIS Travel surfaces the intelligence; the booking is completed through Skyscanner's supplier connections.

Value for Skyscanner: High-intent, corporate-buyer transactions with known organisational context — a different transaction quality than consumer metasearch traffic.

*Note: We have reviewed Skyscanner's publicly documented B2B partner programme structure. The specific discussion with your technical team is about the enterprise-level referral architecture: whether corporate bookings sourced via intelligence recommendations can be tracked and attributed distinctly, and what the commercial and technical structure for that attribution looks like at scale.*

**Layer 3: Carbon Data Enrichment**

Purpose: Enrich route-level data with the carrier and aircraft information required for accurate Scope 3 carbon attribution under ICAO methodology.

Data sought: Aircraft type per scheduled route; operational aircraft type actuals where available.

This layer enables DIS Travel's carbon calculation to achieve route-level ICAO accuracy rather than relying on industry average emissions factors — a material difference for organisations with CSRD audit obligations.

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
| **PII handling** | Traveller PII stays within the customer's organisational boundary; not transmitted to partner APIs |
| **Data residency** | EU data boundary enforced at infrastructure level |
| **Secrets management** | No credentials in code, configuration files, or repositories |
| **Vulnerability management** | Automated scanning with remediation SLAs: Critical — 24 hours; High — 72 hours; Medium — 30 days |

---

## Technology Stack Philosophy

DIS Travel's cloud provider and infrastructure stack is being determined through Architecture Decision Records (ADRs) — a governance process that requires explicit documentation of the decision drivers, options considered, and rationale before committing. This is a deliberate governance choice, not an open question.

**Constraints already established:**
- Cloud-native infrastructure — EU data residency required (constrains provider and region selection)
- API-first design — every component exposes a programmatic interface
- Managed services where commodity; bespoke where differentiation requires it
- LLM APIs from leading providers, governed by DIS Group's AI governance policy (Class 1–4 risk framework)
- No proprietary data formats — open standards where possible

**What this means for Skyscanner integration:**
- REST API integration, matching Skyscanner's partner programme API design
- Standard OAuth 2.0 / API key authentication, aligned with Skyscanner's B2B authentication patterns
- Webhook or polling architecture for near-real-time data; batch for historical
- Full logging and monitoring of all Skyscanner data consumption

---

## Development Status — Honest Assessment

| Component | Status | Expected Completion |
|---|---|---|
| Architecture design | ✅ Complete | — |
| AI governance policy | ✅ Published and operational | — |
| Data domain model | ✅ Designed | — |
| GDPR compliance framework | ✅ Designed | — |
| Foundation infrastructure | 🔄 In progress | Q3 2026 |
| Data platform (warehouse + pipelines) | 📋 Scoped | Q4 2026 |
| Intelligence layer — Policy engine | 📋 Designed | Q1 2027 |
| Intelligence layer — Carbon engine | 📋 Designed | Q1 2027 |
| Intelligence layer — Destination intel | 📋 Designed | Q2 2027 |
| Skyscanner integration — Content | 📋 Designed | Q1–Q2 2027 |
| Skyscanner integration — Booking referral | 📋 Designed | Q2 2027 |
| Skyscanner integration — Carbon data | 📋 Designed | Q2 2027 |
| Presentation layer (web app) | 📋 Design phase | Q2 2027 |
| Enterprise pilot readiness | — | Q2–Q3 2027 |

*Legend: ✅ Complete | 🔄 In progress | 📋 Designed, implementation pending*

*Timelines are indicative. Partnership design and data agreement processes will affect integration timelines — these are internal development estimates, not partnership commitments.*

---

## Questions for a Technical Partnership Discussion

We have reviewed Skyscanner's publicly documented partner programme. The following represents the depth of discussion we would want to have with your technical team — beyond what is covered in the public documentation:

1. **Aircraft-type metadata granularity** — The public partner programme documents route and carrier data. What is the accessible depth for aircraft-type data per scheduled route? Is operational aircraft type (actual, not scheduled) accessible for completed trips, and at what latency?

2. **Data freshness and SLAs** — What are the contractual freshness guarantees for real-time pricing and availability data through the partner programme? What SLAs apply to data delivery and uptime?

3. **Historical depth** — What is the maximum historical window available for fare pattern data? Is granularity (route, carrier, class) consistent across the full historical window?

4. **Carbon data collaboration appetite** — Is there interest in co-developing a route-level carbon enrichment dataset anchored in Skyscanner's aircraft-type data? This would be a new capability layer — we are not aware of a current offering and would be proposing to build it collaboratively.

5. **B2B integration architecture options** — The partner programme documents standard integration patterns. We want to understand whether there is a partnership tier or bespoke integration path for corporate intelligence use cases that require deeper data access than standard content affiliate integrations.

6. **Enterprise referral attribution** — We have reviewed the standard deep-link and referral architecture. The specific design question is whether corporate bookings sourced through an intelligence recommendation layer can be attributed distinctly from standard consumer referral traffic — and what the technical and commercial mechanism for that attribution looks like at enterprise scale.

---

## Related Documents

- [COMPANY_PRESENTATION.md](COMPANY_PRESENTATION.md) — Strategic overview and partnership thesis
- [EXECUTIVE_ONE_PAGER.md](EXECUTIVE_ONE_PAGER.md) — Executive summary
- [COVER_LETTER.md](COVER_LETTER.md) — Introduction letter
- [DIS Group AI Governance](../../ai/governance.md) — Published AI governance policy
- [DIS Group Technology Architecture](../../technology/architecture.md) — Group-level architecture
- [DIS Group AI Strategy](../../ai/strategy.md) — Group AI strategy

---

*Owner: CTO / Technical Lead | Status: Active | Last updated: 2026-07-05*
*DIS Group — Confidential. Prepared for Skyscanner partnership discussions only.*
