# Final Readiness Assessment — Skyscanner Partner Package

*Assessed by: Chief AI Architect acting as Senior Director of Strategic Partnerships, Skyscanner*
*Date: 2026-07-05*
*Package version: v0.6*

---

## Executive Summary

The Skyscanner partner package is a four-document enterprise outreach package presenting DIS Group and its DIS Travel product as candidates for a long-term strategic technology partnership. The package has been through two full review-and-improvement cycles: an initial executive review (four-perspective) and a final Senior Director review focused on trust, credibility, and enterprise positioning.

The package is honest about DIS Travel's development stage (pre-launch, architecture complete), specific about the methodological basis for partnership (ICAO/GHG Protocol carbon attribution, Skyscanner aircraft-type data dependency), aware of the competitive landscape (Navan, SAP Concur, TravelPerk, Spotnana explicitly addressed), and calibrated about what it asks Skyscanner to commit (a 45-minute conversation, not a commercial or data commitment).

**The package achieves its objective:** to generate a substantive response from a Senior Skyscanner partnerships contact — specifically, "tell us more about the team" or "schedule the call."

---

## Package Contents

| File | Document | Format | Status |
|---|---|---|---|
| `00_Team_Profile.pdf` | Leadership and Company Profile | PDF | Final |
| `01_Cover_Letter.pdf` | Cover Letter | PDF | Final |
| `02_Executive_One_Pager.pdf` | Executive One-Pager | PDF | Final |
| `03_DIS_Travel_Presentation.pdf` | Company Presentation (12 slides) | PDF | Final |
| `04_Technical_Overview.pdf` | Technical Architecture Overview | PDF | Final |
| `05_DIS_Travel_Presentation.pptx` | Company Presentation | PowerPoint | Final |

---

## Consistency Verification

| Check | Result |
|---|---|
| Company name | `DIS Group` — consistent across all 4 documents |
| Product name | `DIS Travel` — consistent |
| Carbon methodology | `ICAO / GHG Protocol` — referenced in all 4 documents |
| CSRD framing | `Scope 3 Category 6`, `audit-defensible`, `tens of thousands of in-scope organisations` — consistent |
| Partnership timeline | `Q3–Q4 2026 → Q4 2026–Q1 2027 → Q1–Q2 2027 → Q2–Q3 2027 pilot` — consistent across One-Pager, Presentation, Technical Overview |
| Enterprise pilot readiness | `Q2–Q3 2027` — consistent in One-Pager and Technical Overview |
| Development stage | `Pre-launch — architecture complete, build in progress` — consistent |
| The ask | `45-minute conversation` — consistent across Cover Letter, One-Pager, Presentation |
| Three businesses | `Recycling, Energy, ESG data` — consistent in Cover Letter, One-Pager, Presentation |
| GDPR / EU data residency | Addressed in One-Pager, Presentation, and Technical Overview |
| Competitive landscape | Navan, SAP Concur, TravelPerk, Spotnana named in One-Pager and Presentation |
| Date | `July 2026` — consistent across all documents |

**Consistency verdict: PASS.** No material conflicts identified across the four documents.

---

## Remaining Business Risks

**1. Team anonymity — MITIGATED (was HIGH IMPACT)**

`00_Team_Profile.pdf` has been added to this package. It names the CEO (Glib Vakunov), describes the operating businesses built, and documents the governance systems (AI policy, GDPR framework, ADR process) that were designed and built before DIS Travel. The document is professionally written and consistent with the rest of the package.

*Remaining exposure:* The profile covers DIS Group's operating history but does not cite prior B2B SaaS experience or name an engineering team — because none is documented. A Senior Director will notice this absence and will likely follow up with "Who is the technical team?" before taking the proposal to their VP. This is the honest ceiling on what the profile can achieve.

---

**2. No customer validation evidence — HIGH IMPACT**

The package asserts that CSRD is creating demand for DIS Travel's specific capability. This is accurate as a market observation. However, there is no reference to:
- Customer discovery conversations with corporate travel managers
- Letters of intent or design partner conversations
- Advisory board members from target enterprise accounts
- Any form of demand validation beyond the regulatory argument

A Senior Director will think: *"This problem description is compelling — have they spoken to anyone who actually has it?"*

*Mitigation:* Before sending, conduct and briefly reference 3–5 corporate travel manager conversations. Even "We have spoken with European corporate travel directors at [types of organisation, not names] about their CSRD measurement challenges" materially changes the credibility calculus.

---

**3. Commercial model is deferred — MEDIUM IMPACT**

Every reference to the commercial structure between DIS Travel and Skyscanner reads "to be designed collaboratively." This is honest. It is also a gap. A Senior Director cannot walk into their VP's office without some model of how Skyscanner would benefit commercially.

*Mitigation:* Add one paragraph to the One-Pager (or Technical Overview) with a draft commercial model: data licensing for content access + revenue-share on corporate bookings referred through Skyscanner's supplier network. Make it indicative and explicitly open to Skyscanner's preferred structure.

---

**4. DIS Group's existing businesses are not quantified — MEDIUM IMPACT**

"Three active businesses" signals operational existence but not scale. Is DIS Group a multi-million-euro operation, or a two-person entity with three holding companies? The package cannot answer this — and does not try to.

*Mitigation:* A revenue range or headcount figure for the operating businesses would significantly strengthen the execution credibility argument. If DIS Group cannot or will not disclose this publicly, consider a version that can be shared under NDA at the partnership design stage.

---

**5. AI governance is operational for an internal tool — LOW-MEDIUM IMPACT**

The package claims AI governance is "operational today." This is true — it governs the internal AI Architect. A sceptical CTO at Skyscanner may note that governing an internal knowledge base agent is not the same as deploying production AI that enterprise customers rely on. The claim is accurate but may not survive technical due diligence at the depth it implies.

*Mitigation:* Add nuance: "Our AI governance framework is operational for internal systems and is the framework that will govern external deployments." This is honest and does not weaken the claim — it contextualises it.

---

## Remaining Documentation Risks

**1. `[Name]` and `[ceo@disgroup.ie]` placeholders in Cover Letter and Presentation**

These must be filled with real names and contact details before sending. Sending a document with `[Name]` in the signatory block would be a serious error.

**2. `[www.disgroup.ie]` in Cover Letter**

If this domain does not exist or does not display a professional corporate website, it will undermine credibility. Verify the domain is live before sending.

**3. Generator scripts in the `final/` folder**

`generate_pptx.py` and `generate_pdfs.py` are production generation scripts. They should be removed or moved before the folder is sent externally — the recipient should only receive the five finished files.

---

## Confidence Score

**78 / 100**

| Dimension | Score | Notes |
|---|---|---|
| Executive communication quality | 90 | Professional, specific, no hype |
| Strategic thinking depth | 85 | Competitive landscape, CSRD framing, architecture distinction all strong |
| Technical credibility | 80 | ICAO methodology, GDPR architecture, governance framework |
| Execution credibility | 62 | Operating businesses help but team is still anonymous |
| Market validation | 50 | CSRD demand thesis is sound; no customer evidence cited |
| Commercial model clarity | 55 | Partnership value exchange is articulated; commercial terms are deferred |
| Presentation quality | 88 | 12-slide PPTX, consistent branding, professional layout |

---

## Recommendation

**Ready to send — after completing the pre-send checklist below.**

The package earns a substantive response from a Senior Director at Skyscanner. The CSRD methodology argument is technically correct, the competitive analysis is honest rather than dismissive, the development status is transparent, and the ask (45-minute conversation) is calibrated correctly for cold outreach.

This package will not be rejected on quality. It may be paused pending "tell us more about the team" — which is the correct response at this stage and should be anticipated.

**Pre-send checklist:**

- [ ] Replace `[Name]` with the CEO's full name in Cover Letter and Presentation Slide 12
- [ ] Replace `[ceo@disgroup.ie]` with the verified email address
- [ ] Replace `[www.disgroup.ie]` with a live professional website URL
- [ ] Verify disgroup.ie is live and presents a professional corporate web presence
- [ ] Prepare a one-page team profile to send when the first response requests it
- [ ] Remove `generate_pptx.py` and `generate_pdfs.py` from the delivery folder
- [ ] Identify the specific Skyscanner contact (Director or VP level — not the generic partnerships inbox)
- [ ] Verify the correct Skyscanner postal address is current in the Cover Letter

---

*Owner: CEO / Partnerships Lead | Status: Final — Ready after minor edits | Last updated: 2026-07-05*
