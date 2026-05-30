# PS Workflow Assistant — Conversation Flows

This document maps every topic the agent handles, including the trigger phrases, dialog logic, and agent responses. This is the design blueprint that would be implemented directly in Microsoft Copilot Studio.

---

## Topic 1: Onboarding Checklist Retrieval

**Topic name in Copilot Studio:** `Get Onboarding Checklist`  
**Trigger phrases:**
- "What's the onboarding checklist for [carrier]?"
- "What do I need to onboard a new carrier?"
- "Show me the implementation steps"
- "What's the process for setting up a new client?"

**Conversation flow:**

```
Agent: "I can help with that. Which carrier or client type are you onboarding?"

[User responds with carrier name or type]

Agent: "Got it. Here's the current onboarding checklist for [carrier type]:

  Step 1 — Initial Setup
  □ Carrier contract signed and in DocuSign
  □ iGO environment provisioned
  □ Carrier forms library confirmed current

  Step 2 — Configuration
  □ Product mapping completed
  □ Rules engine configured and tested
  □ Integration endpoints validated

  Step 3 — UAT
  □ Test cases executed (minimum 20)
  □ Carrier sign-off obtained
  □ Go-live date confirmed

  Step 4 — Launch
  □ Production deployment scheduled
  □ PS rep assigned for 30-day hypercare
  □ Handoff to Customer Success completed

Source: [SharePoint SOP link]
Last updated: [date]

Is there a specific step you need more detail on?"
```

**Fallback (carrier not recognized):**
```
Agent: "I don't have a specific checklist for that carrier yet. 
Here's our standard onboarding template — and I'd recommend 
looping in [Team Lead] for any carrier-specific requirements. 
Want me to help draft that escalation message?"
```

---

## Topic 2: Support Ticket Summarization

**Topic name in Copilot Studio:** `Summarize Ticket`  
**Trigger phrases:**
- "Summarize this ticket"
- "Help me triage this"
- "I need a summary of this issue"
- "Can you format this for handoff?"

**Conversation flow:**

```
Agent: "Paste the ticket content and I'll generate a structured summary for you."

[User pastes ticket text]

Agent: "Here's your ticket summary:

  CLIENT: [extracted client name]
  ISSUE TYPE: [technical / billing / configuration / access]
  PRIORITY: [High / Medium / Low — based on keywords]
  SUMMARY: [2-3 sentence plain language description]
  IMPACTED SYSTEM: [iGO / LifePipe / Integration / Other]
  RECOMMENDED NEXT STEP: [specific action]
  ESCALATE TO: [Tier 1 / Tier 2 / PS Lead / Engineering]

Want me to format this for a Teams message or email handoff?"
```

---

## Topic 3: Escalation Decision Guide

**Topic name in Copilot Studio:** `Escalation Path`  
**Trigger phrases:**
- "Who do I escalate this to?"
- "This implementation is stalled"
- "I need help deciding if this should go to engineering"
- "What's the escalation path for [issue type]?"

**Conversation flow:**

```
Agent: "Let's figure out the right path. A few quick questions:

  1. Is the client in production or still in implementation?"

[User responds]

Agent: "Got it. Is this a technical issue, a configuration issue, 
or a client relationship issue?"

[User responds]

Agent: "Understood. How long has this been open?"

[User responds]

Agent: "Based on what you've described, here's the recommended path:

  TIER: Tier 2 — PS Lead involvement required
  OWNER: [PS Lead Name / Role]
  SLA: Response within 4 business hours
  ACTION: Create a P2 ticket in ServiceNow, 
          tag PS Lead, and notify the client 
          that a senior resource is engaged.

  ESCALATION TEMPLATE:
  'Hi [Client], I wanted to update you that we've engaged 
  our Senior PS team on [issue]. You can expect an update 
  by [time]. Thank you for your patience.'

Does this match what you needed, or do you want to walk 
through a different scenario?"
```

---

## Topic 4: General FAQ

**Topic name in Copilot Studio:** `Product FAQ`  
**Trigger phrases:**
- "How does iGO work?"
- "What's the difference between iGO and LifePipe?"
- "What carriers are supported?"
- "What's the SLA for [issue type]?"

**Conversation flow:**

```
Agent: "Happy to help. Here's what I know about that:

[Answer drawn from FAQ knowledge base]

Source: [Document name + SharePoint link]

Was that helpful, or do you need more detail?"
```

**Fallback:**
```
Agent: "I don't have a confident answer for that one — 
I'd rather point you to the right person than guess. 
Try [SME Name/Role] or check [specific SharePoint section].
Want me to help you draft that question?"
```

---

## Topic 5: Out of Scope Handler

For anything outside the agent's defined scope:

```
Agent: "That's outside what I'm set up to help with right now. 
A few options:
  → For client-facing questions: reach out to your PS Lead
  → For technical platform issues: submit to [Engineering channel]
  → For billing or contract questions: contact [Finance contact]

Is there something else I can help with?"
```

---

## Design Notes

**Tone:** Professional but conversational. Not robotic. Reads like a knowledgeable colleague, not a help desk bot.

**Fallback philosophy:** Always give the user a next step. Never leave them at a dead end.

**Knowledge base connection:** Topics 1 and 4 connect directly to SharePoint via Copilot Studio's native knowledge source integration. No custom API required for initial launch.

**Escalation templates:** Pre-written templates inside escalation flows save reps 5–10 minutes per escalation and ensure consistent client communication.
