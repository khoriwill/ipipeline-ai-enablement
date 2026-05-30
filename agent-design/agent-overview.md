# PS Workflow Assistant — Agent Overview

## Problem Statement

iPipeline's Professional Services team manages complex carrier onboarding and product implementation workflows across multiple clients simultaneously. Currently, PS reps spend significant time:

- Hunting through SharePoint for the correct onboarding checklist version
- Emailing back and forth to determine escalation paths for stalled implementations
- Manually summarizing support tickets before handing off to senior staff
- Re-answering the same carrier-specific questions across implementations

**Estimated time lost per rep per week: 3–5 hours on knowledge retrieval and repetitive triage tasks.**

This is exactly the type of high-frequency, high-friction, low-complexity work that a well-designed AI agent eliminates.

---

## Agent Purpose

The **PS Workflow Assistant** is an internal Microsoft Copilot Studio agent deployed inside Microsoft Teams. It serves as an always-available knowledge and workflow companion for PS reps — answering questions, surfacing SOPs, summarizing tickets, and guiding escalation decisions in real time.

It is not a replacement for PS expertise. It is a force multiplier that removes the friction between a rep and the information they need to do their job faster.

---

## Target Users

**Primary:** Professional Services Implementation Reps  
**Secondary:** PS Team Leads, Customer Support Tier 1  
**Deployment channel:** Microsoft Teams (where PS already works)

---

## Core Capabilities

### Capability 1 — Onboarding Knowledge Retrieval
**Trigger:** Rep asks about carrier requirements, onboarding steps, or implementation checklists  
**Agent behavior:** Retrieves the correct, current SOP from the connected SharePoint knowledge base and surfaces it in plain language  
**Business outcome:** Eliminates SharePoint hunting, ensures reps always have current documentation

### Capability 2 — Support Ticket Summarization
**Trigger:** Rep pastes or describes a support ticket  
**Agent behavior:** Generates a structured summary (client, issue, priority, recommended next step)  
**Business outcome:** Faster triage, cleaner handoffs, reduced back-and-forth

### Capability 3 — Escalation Decision Guide
**Trigger:** Rep describes a stalled or complex implementation scenario  
**Agent behavior:** Walks rep through a decision tree — what tier is this, who owns it, what's the SLA, what's the escalation path  
**Business outcome:** Consistent escalation, reduced senior staff interruptions for routine decisions

### Capability 4 — FAQ Deflection
**Trigger:** Common questions about iGO, LifePipe, carrier integrations  
**Agent behavior:** Answers from a curated FAQ knowledge base, with source citation  
**Business outcome:** Reduces repetitive questions to team leads and subject matter experts

---

## What the Agent Does NOT Do

- It does not make decisions on behalf of the rep
- It does not access client PII or confidential policy data
- It does not replace the PS team lead or senior architect on complex decisions
- It does not send communications to external clients

These boundaries are intentional and documented in the governance framework.

---

## Success Criteria

| Metric | Baseline (pre-agent) | Target (90 days post-launch) |
|---|---|---|
| Avg time to find SOP | 8–12 minutes | < 2 minutes |
| Ticket summarization time | 15–20 minutes | < 3 minutes |
| Escalation consistency rate | ~60% (estimated) | > 85% |
| PS rep satisfaction score | TBD baseline | +20% improvement |
| Weekly hours saved per rep | 0 | 3–5 hours |

---

## Why Copilot Studio

Copilot Studio was chosen because:

1. **It lives where the work happens** — Teams integration means zero behavior change for reps
2. **SharePoint native** — Direct connection to existing knowledge base, no data migration
3. **IT-approved** — Already inside the Microsoft 365 tenant, no new vendor procurement
4. **Governable** — Admin controls, conversation logging, compliance-aligned
5. **Scalable** — What works for PS can be templated for Customer Support, Sales Ops, and HR
