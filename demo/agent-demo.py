"""
iPipeline PS Workflow Assistant — Demo Agent
============================================
A working command-line demonstration of the PS Workflow Assistant agent.
This mirrors the conversation flows designed for Microsoft Copilot Studio.

Run with: python agent-demo.py

No API keys required — this demo uses built-in response logic
to show the agent's conversation design and capabilities.
"""

import time
import textwrap

# ── Color helpers ──────────────────────────────────────────────────────────────
RESET  = "\033[0m"
BLUE   = "\033[94m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
GRAY   = "\033[90m"
BOLD   = "\033[1m"

def agent(text):
    """Print agent response with formatting."""
    print(f"\n{BLUE}{BOLD}[PS Assistant]{RESET} {text}\n")

def user_prompt():
    """Get user input."""
    return input(f"{GREEN}{BOLD}[You]{RESET} ").strip().lower()

def divider():
    print(f"{GRAY}{'─' * 60}{RESET}")

def slow_print(text, delay=0.015):
    """Print text with a typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ── Knowledge base (mirrors SharePoint content) ───────────────────────────────

ONBOARDING_CHECKLIST = """
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
"""

ESCALATION_GUIDE = {
    "tier1": """
  🔺 ESCALATION: Tier 1 — PS Lead Required

  OWNER:     Senior PS Implementation Lead
  SLA:       Response within 4 business hours
  ACTION:    Create P2 ticket in ServiceNow,
             tag PS Lead, notify the client.

  ── CLIENT COMMUNICATION TEMPLATE ──────────────
  "Hi [Client], I wanted to update you that we've
  engaged our Senior PS team on [issue]. You can
  expect a detailed update by [time + 1 business day].
  Thank you for your patience."
  ────────────────────────────────────────────────
""",
    "tier2": """
  🔴 ESCALATION: Tier 2 — Engineering Involvement

  OWNER:     Engineering Lead + PS Lead
  SLA:       Response within 2 business hours
  ACTION:    Create P1 ticket, page Engineering
             on-call, notify PS Director.

  ── CLIENT COMMUNICATION TEMPLATE ──────────────
  "Hi [Client], we've identified a technical issue
  affecting your implementation and have engaged
  our engineering team. We will provide updates
  every 4 hours until resolved."
  ────────────────────────────────────────────────
"""
}

FAQ_ANSWERS = {
    "igo": "iGO is iPipeline's flagship e-application platform — a fully digital, end-to-end life insurance application process used by 1,400+ distributors. It eliminates paper forms and manual data entry, accelerating the application-to-policy cycle significantly.",
    "lifepipe": "LifePipe is iPipeline's comprehensive forms library and SOP reference system — a single source of truth for insurance forms used across distributor networks. It was the original product that iPipeline was founded on in 1995.",
    "sla": "Standard SLAs: P1 (system down) = 2hr response / 4hr resolution. P2 (major impact) = 4hr response / 8hr resolution. P3 (minor impact) = 1 business day response / 3 business day resolution.",
}

# ── Core agent capabilities ───────────────────────────────────────────────────

def handle_onboarding(query):
    agent("I can help with that. Let me pull the current onboarding checklist.")
    time.sleep(0.8)
    print(YELLOW + ONBOARDING_CHECKLIST + RESET)
    agent("Is there a specific phase you need more detail on, or do you have a carrier-specific requirement I should know about?")

def handle_ticket_summary():
    agent("Paste your ticket content below and press Enter twice when done:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    ticket_text = " ".join(lines)
    time.sleep(1.0)

    agent(f"""Here's your structured ticket summary:

  CLIENT:          [Extracted from ticket]
  ISSUE TYPE:      Technical — Integration / Configuration
  PRIORITY:        Medium (P2)
  SUMMARY:         The client is experiencing an issue with
                   their iGO integration that is impacting
                   their ability to submit applications.
                   Issue began recently and affects [scope].
  IMPACTED SYSTEM: iGO — Application Submission
  RECOMMENDED:     Validate integration endpoint config,
                   check recent deployment log for changes.
  ESCALATE TO:     PS Lead — within 4 business hours

  Want me to format this for a Teams message or email handoff?""")

def handle_escalation():
    agent("Let's figure out the right escalation path. A few quick questions:")
    time.sleep(0.4)
    agent("Is the client currently in production or still in implementation?")

    stage = user_prompt()

    agent("Got it. Is this a technical issue, configuration issue, or client relationship issue?")
    issue_type = user_prompt()

    agent("How long has this been open without resolution?")
    duration = user_prompt()

    time.sleep(0.8)

    if "technical" in issue_type or "production" in stage:
        print(YELLOW + ESCALATION_GUIDE["tier2"] + RESET)
    else:
        print(YELLOW + ESCALATION_GUIDE["tier1"] + RESET)

    agent("Does this match your situation, or do you want to walk through a different scenario?")

def handle_faq(query):
    matched = None
    if "igo" in query or "i-go" in query:
        matched = FAQ_ANSWERS["igo"]
    elif "lifepipe" in query or "life pipe" in query:
        matched = FAQ_ANSWERS["lifepipe"]
    elif "sla" in query or "service level" in query:
        matched = FAQ_ANSWERS["sla"]

    if matched:
        agent(matched + "\n\n  📎 Source: iPipeline Product FAQ | Internal Knowledge Base")
    else:
        agent("I don't have a confident answer on that specific question. I'd rather point you to the right person than guess.\n\n  → For product questions: contact your PS Lead\n  → For technical specs: check the Engineering SharePoint\n\n  Want me to help you draft that question?")

# ── Intent routing ────────────────────────────────────────────────────────────

def route(query):
    """Route user input to the correct handler."""
    onboarding_triggers = ["onboard", "checklist", "new carrier", "implementation steps", "setup", "new client"]
    ticket_triggers     = ["summarize", "summary", "triage", "ticket", "handoff", "format"]
    escalation_triggers = ["escalat", "stalled", "stuck", "who do i", "escalation path"]
    faq_triggers        = ["igo", "lifepipe", "sla", "how does", "what is", "what's the difference"]
    exit_triggers       = ["exit", "quit", "bye", "done", "thanks"]

    if any(t in query for t in exit_triggers):
        return "exit"
    elif any(t in query for t in onboarding_triggers):
        return "onboarding"
    elif any(t in query for t in ticket_triggers):
        return "ticket"
    elif any(t in query for t in escalation_triggers):
        return "escalation"
    elif any(t in query for t in faq_triggers):
        return "faq"
    else:
        return "unknown"

# ── Main loop ─────────────────────────────────────────────────────────────────

def main():
    print(f"\n{BOLD}{'═' * 60}")
    print("  iPipeline PS Workflow Assistant — Demo v1.0")
    print(f"{'═' * 60}{RESET}")
    print(f"{GRAY}  Built by Khori Williams | github.com/khoriwill")
    print(f"  Mirrors Microsoft Copilot Studio agent design{RESET}\n")

    agent("""Hi! I'm the PS Workflow Assistant. I'm here to help you with:

  1. 📋  Onboarding checklists and implementation steps
  2. 📝  Support ticket summarization and triage
  3. 🔺  Escalation path decisions
  4. ❓  iGO, LifePipe, and SLA questions

  What can I help you with today?""")

    divider()

    while True:
        query = user_prompt()

        if not query:
            continue

        divider()
        intent = route(query)

        if intent == "exit":
            agent("Got it — good luck with your implementation! Type 'help' anytime to restart.")
            break
        elif intent == "onboarding":
            handle_onboarding(query)
        elif intent == "ticket":
            handle_ticket_summary()
        elif intent == "escalation":
            handle_escalation()
        elif intent == "faq":
            handle_faq(query)
        else:
            agent("""That's outside what I'm set up to help with right now.

  → For client-facing questions: reach out to your PS Lead
  → For technical platform issues: submit to the Engineering channel
  → For billing or contract questions: contact Finance

  Is there something else I can help with?""")

        divider()

if __name__ == "__main__":
    main()
