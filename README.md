# AI Enablement Framework

**Author:** Khori Williams — Cloud & AI Infrastructure | TPM | AI Enablement  
**Stack:** Microsoft Copilot Studio · Power Automate · Azure AI · Python  
**Status:** Active — built as a working reference for enterprise AI enablement strategy

---

## What This Is

This project is a full AI enablement framework designed for an insurance technology company like iPipeline — a global provider of digital solutions for life insurance and financial services.

It answers one question: **How do you take an organization that has executive buy-in for AI and actually make it land across the business?**

This is not a product development project. It is an *internal enablement* project — the strategy, agent design, governance, and adoption framework that sits between "we want AI" and "AI is delivering measurable business value."

---

## The Problem

Organizations investing in AI transformation face a common failure pattern:

- Executive mandate exists ✅
- Technology is purchased ✅  
- Adoption stalls at the team level ❌
- ROI is unmeasurable ❌
- Change resistance blocks rollout ❌

The gap is not technical. It is **operational**. Teams need agents designed for their actual workflows, governance they can trust, and enablement that meets them where they are.

---

## What This Framework Includes

```
ipipeline-ai-enablement/
│
├── README.md                        ← You are here
│
├── agent-design/
│   ├── agent-overview.md            ← What the agent does and why
│   ├── conversation-flows.md        ← Full topic map and dialog design
│   └── copilot-studio-blueprint.md  ← Implementation guide for Copilot Studio
│
├── governance/
│   ├── ai-usage-policy.md           ← Enterprise AI governance framework
│   ├── success-metrics.md           ← How to measure what matters
│   └── adoption-playbook.md         ← Change management and rollout strategy
│
├── roadmap/
│   └── 90-day-plan.md               ← First 90 days as AI Enablement Lead
│
└── demo/
    ├── agent-demo.py                ← Working Python chatbot demo
    └── sample-conversations.md      ← Example agent interactions
```

---

## The Agent: PS Workflow Assistant

The first use case targeted is **Professional Services** — the team that onboards carriers and implements iPipeline's iGO and LifePipe products with clients.

**Why PS first?**
- High volume of repetitive knowledge retrieval (onboarding checklists, escalation paths, carrier requirements)
- Direct revenue impact — faster PS delivery = faster time-to-value for clients
- Measurable — cycle time, ticket resolution, escalation rate are all trackable

**What the agent does:**
- Answers onboarding and implementation questions instantly
- Summarizes support tickets for faster triage
- Guides reps through escalation decision trees
- Surfaces SOPs without SharePoint hunting

---

## Key Design Principles

**1. Outcome over output** — Every agent capability is tied to a measurable business outcome, not just a feature.

**2. Trust before adoption** — Governance and accuracy must be established before broad rollout. Hallucination is a trust-killer in regulated industries.

**3. Meet teams where they are** — Agents that live inside Teams and Outlook get used. Agents that require a new tab don't.

**4. Measure everything from day one** — If you can't show the ROI, the program dies in the next budget cycle.

---

## Technologies Referenced

| Tool | Purpose |
|---|---|
| Microsoft Copilot Studio | Agent builder — conversation flows, topics, integration |
| Power Automate | Workflow automation — ticket routing, notifications |
| Microsoft Teams | Deployment channel — agent surfaces inside Teams |
| SharePoint | Knowledge base — SOP and document source |
| Azure AI Foundry | Advanced LLM capabilities for complex queries |
| Python (demo) | Working proof-of-concept agent for demonstration |

---

## Connect

**GitHub:** github.com/khoriwill  
**Email:** khoriwill@gmail.com  
**LinkedIn:** linkedin.com/in/khoriwilliams
