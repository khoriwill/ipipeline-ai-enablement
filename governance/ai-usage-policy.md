# AI Governance Framework — iPipeline Internal AI Enablement

**Version:** 1.0  
**Owner:** AI Enablement Lead  
**Applies to:** All internal AI tools deployed across iPipeline business functions

---

## Purpose

This framework establishes the standards, boundaries, and accountability structures for AI tool deployment inside iPipeline. It exists to ensure that AI delivers measurable business value without creating compliance risk, trust erosion, or uncontrolled proliferation.

Governance is not a blocker. It is what makes adoption sustainable.

---

## Guiding Principles

**1. Humans stay in the loop on consequential decisions**  
AI tools advise and assist. They do not approve, reject, or communicate final decisions to clients or external parties without human review.

**2. Accuracy over speed**  
An agent that gives a fast wrong answer destroys trust faster than any efficiency gain. Every agent topic is validated against source documentation before launch.

**3. Data stays inside the tenant**  
No client data, PII, or confidential business information enters any AI tool operating outside the Microsoft 365 tenant boundary without explicit legal and IT approval.

**4. Every deployment is measurable**  
No AI tool goes live without defined success metrics and a review checkpoint at 30, 60, and 90 days.

**5. Employees are partners, not passengers**  
AI enablement works when employees understand what the tool does, why it exists, and how it helps them. Training and communication are non-negotiable parts of every rollout.

---

## What AI Tools Are Approved for Internal Use

| Tool | Approved Use Cases | Restrictions |
|---|---|---|
| Microsoft Copilot (M365) | Drafting, summarizing, meeting notes, email | No client PII in prompts |
| Copilot Studio Agents | Internal workflow assistance, knowledge retrieval | No external client-facing deployment without review |
| Power Automate AI flows | Ticket routing, notification workflows | Reviewed by IT before production |
| Azure OpenAI (via IT) | Advanced analysis, custom integrations | Requires IT and Legal sign-off |

---

## Data Handling Standards

### What employees MAY put into AI tools:
- Internal SOPs and process documentation
- Anonymized or synthetic data for testing
- Their own work product (drafts, summaries, plans)
- General business questions and workflow queries

### What employees MAY NOT put into AI tools:
- Client names, contact information, or account details
- Policy data, underwriting information, or financial records
- Employee PII (SSN, salary, performance data)
- Anything marked Confidential or Restricted in the data classification policy

### Why this matters for iPipeline specifically:
iPipeline operates in the life insurance and financial services industry. Client data is regulated. A single compliance incident from inappropriate AI use costs more than the efficiency gain from the tool. These boundaries protect the business and the employees using the tools.

---

## Agent Launch Checklist

Before any Copilot Studio agent is deployed to users:

- [ ] Use cases documented and approved by business owner
- [ ] Knowledge base sources reviewed for accuracy and currency
- [ ] Fallback behaviors tested for all out-of-scope queries
- [ ] Data handling review completed — no PII in scope
- [ ] IT security review completed
- [ ] Legal review completed (if client-adjacent)
- [ ] User training completed or scheduled
- [ ] Success metrics defined and baseline captured
- [ ] 30-day review checkpoint scheduled
- [ ] Feedback channel established (Teams channel or form)

---

## Roles and Accountability

| Role | Responsibility |
|---|---|
| AI Enablement Lead | Program strategy, agent design, adoption framework, executive reporting |
| Business Owner (per team) | Use case prioritization, user feedback, 30/60/90 day reviews |
| IT / Security | Tenant configuration, data security review, integration approval |
| Legal / Compliance | Regulatory review for any client-adjacent use cases |
| End Users | Responsible use, feedback reporting, escalating unexpected behavior |

---

## Incident Response

If an agent produces harmful, inaccurate, or inappropriate output:

1. **Immediate:** User stops using the output, does not forward or act on it
2. **Report:** User reports via [AI Feedback channel] within 24 hours
3. **Triage:** AI Enablement Lead reviews within 48 hours
4. **Remediate:** Topic is corrected or disabled while fix is developed
5. **Communicate:** Affected users notified of what happened and what changed
6. **Document:** Incident logged for quarterly governance review

**No blame culture.** Reporting issues makes the tools better. Silence is what creates risk.

---

## Review Cadence

| Review | Frequency | Owner | Output |
|---|---|---|---|
| Agent accuracy review | Monthly | AI Enablement Lead | Topic corrections, knowledge base updates |
| Usage and adoption metrics | Monthly | Business Owner | Adoption report to leadership |
| Governance framework review | Quarterly | AI Enablement Lead + Legal | Policy updates |
| Executive program review | Quarterly | AI Enablement Lead | ROI report, roadmap update |
