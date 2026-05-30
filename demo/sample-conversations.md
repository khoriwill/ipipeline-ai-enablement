# Sample Agent Conversations

These are real example interactions from the PS Workflow Assistant demo. They show how the agent handles the four core use cases in natural conversation.

---

## Conversation 1: Onboarding Checklist

```
[You] What do I need to onboard a new carrier?

[PS Assistant] I can help with that. Let me pull the current onboarding checklist.

  📋 CARRIER ONBOARDING CHECKLIST

  PHASE 1 — Initial Setup
  ☐ Carrier contract signed and loaded in DocuSign
  ☐ iGO environment provisioned in staging
  ☐ Carrier forms library confirmed current and complete

  PHASE 2 — Configuration
  ☐ Product mapping completed and reviewed
  ☐ Rules engine configured and unit tested
  ☐ Integration endpoints validated (test + prod)

  PHASE 3 — UAT
  ☐ Minimum 20 test cases executed
  ☐ Carrier sign-off obtained in writing
  ☐ Go-live date confirmed with client

  PHASE 4 — Launch
  ☐ Production deployment scheduled with IT
  ☐ PS rep assigned for 30-day hypercare period
  ☐ Handoff to Customer Success confirmed

  📎 Source: PS-SOP-001 | Last updated: May 2025

[PS Assistant] Is there a specific phase you need more detail on?
```

---

## Conversation 2: Ticket Summarization

```
[You] Can you summarize this ticket for handoff?

[PS Assistant] Paste your ticket content below and press Enter twice when done.

[You] Client: Acme Life Insurance. Issue: Their iGO integration 
stopped submitting applications as of yesterday morning. 
They've tried restarting the integration but it keeps failing 
at the submission step. This is blocking their entire sales team.

[PS Assistant] Here's your structured ticket summary:

  CLIENT:          Acme Life Insurance
  ISSUE TYPE:      Technical — Integration / Submission Failure
  PRIORITY:        High (P1) — sales team fully blocked
  SUMMARY:         Client's iGO integration is failing at the
                   application submission step as of yesterday.
                   Restart attempts unsuccessful. Full sales
                   team impact confirmed.
  IMPACTED SYSTEM: iGO — Application Submission
  RECOMMENDED:     Immediate Engineering review of submission
                   endpoint. Check deployment log for changes
                   made in last 48 hours.
  ESCALATE TO:     Engineering Lead — immediately (P1)

  Want me to format this for a Teams message or email handoff?
```

---

## Conversation 3: Escalation Path

```
[You] This implementation is stalled and I don't know who to escalate to

[PS Assistant] Let's figure out the right escalation path. A few quick questions:
               Is the client currently in production or still in implementation?

[You] Still in implementation, been going for 6 weeks

[PS Assistant] Got it. Is this a technical issue, configuration issue, 
               or client relationship issue?

[You] Technical — their rules engine config keeps failing validation

[PS Assistant] How long has this been open without resolution?

[You] About a week

[PS Assistant] Based on what you've described:

  🔺 ESCALATION: Tier 1 — PS Lead Required

  OWNER:     Senior PS Implementation Lead
  SLA:       Response within 4 business hours
  ACTION:    Create P2 ticket in ServiceNow,
             tag PS Lead, notify the client.

  ── CLIENT COMMUNICATION TEMPLATE ──────────────
  "Hi [Client], I wanted to update you that we've
  engaged our Senior PS team on your rules engine
  configuration. You can expect a detailed update
  by [time + 1 business day]. Thank you for your patience."
  ────────────────────────────────────────────────
```

---

## Conversation 4: Product FAQ

```
[You] What's the difference between iGO and LifePipe?

[PS Assistant] iGO is iPipeline's flagship e-application platform — a fully 
               digital, end-to-end life insurance application process used by 
               1,400+ distributors. It eliminates paper forms and manual data 
               entry, accelerating the application-to-policy cycle significantly.

               LifePipe is iPipeline's comprehensive forms library and SOP 
               reference system — a single source of truth for insurance forms 
               used across distributor networks. It was the original product 
               that iPipeline was founded on in 1995.

               📎 Source: iPipeline Product FAQ | Internal Knowledge Base
```
