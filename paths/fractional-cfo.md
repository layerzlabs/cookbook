# The part-time CFO's kit

> Free, open tools you run with Claude (or any capable AI agent) to get the manual work done fast, so your hours go to judgment and strategy instead. Start with a flash audit, then work the recurring engine.

Part of the [Finance Cookbook](../README.md). Everything here is plain, readable Markdown you can open, run and fork. No black box, nothing to install on trust.

## What this is

A curated set of prompts and skills for the work a part-time CFO actually repeats: scoping a new client, understanding a business, reviewing the numbers, stress-testing a model, planning scenarios. Each one is a file you read first, then run with your AI agent. They interview you and adapt to how you work and to each client. They do not unroll a fixed template.

You do not need any particular product to use this. Each piece is useful on its own, and honest about the wall where a prompt stops being enough (more on that at the end).

## How to use it (with Claude, or any agent)

These run wherever you already work with AI: Claude Code, Claude Desktop, Cursor, or any capable agent.

- **A skill** is a folder with a `SKILL.md` inside. Install it into your agent, or just paste the `SKILL.md` text in as a system prompt. Either way it works the same.
- **A recipe** is a prompt you copy and paste. Attach your file or point the agent at your numbers, then paste it.

**New to this? Read [how to install and run a skill](../README.md#installing-a-skill) first.** It is one copy command, or one paste. And open the `SKILL.md` before you run it: that is the whole point, you own it and can see exactly what it does.

Everything runs in your language. The tools mirror whatever language you use with them.

## Start here: the flash audit

Days, not weeks, to figure out where it actually hurts on a new client. The **[finance flash audit](../skills/finance-flash-audit/)** interviews you first, walks the flows (how cash comes in, how invoices go out, how late they get paid, how the month closes), tells the truth about how reliable the numbers are and what that costs in cash, then hands back a prioritized roadmap: where to act, in what order, for what gain.

Read [`skills/finance-flash-audit/SKILL.md`](../skills/finance-flash-audit/SKILL.md), then run it with your agent in one session, on a new client or your own company.

If you only try one thing here, try this. What it finds routes you to the rest.

## The full path

The audit is the entry point. Here is the order a part-time CFO reaches for the rest.

### 1. Understand the business, and keep it

Any good engagement starts the same way: understand the activity, how it makes money, how cash moves, and the conventions this company uses, before touching a number. That understanding is worth capturing once, in a file you own, instead of re-gathering it every session and every tool.

[Own your context with FINANCE.md](../recipes/context-ownership-finance-md.md) forges that file. Any agent reads it at the start, so the next step and the next month begin from understanding, not from a blank interview. It is the foundation the rest of the path stands on.

### 2. Run a flash audit

The [finance flash audit](../skills/finance-flash-audit/) above. It reuses what step 1 already captured, then tells you where to act first.

### 3. Work the recurring engine

Once you are engaged, the same jobs come back every period. Reach for the piece that matches what the audit surfaced:

- **A new client hands you a raw accounting export** → [Map the accounts](../skills/account-mapping/) turns a trial balance, a FEC or a QuickBooks dump into a clean, structured P&L: it confirms the framework, maps the standard accounts in a batch, and raises the ambiguous ones instead of guessing them, so you start from something you can read.
- **The monthly numbers are a grind, or you cannot trust them** → [Forge your analytical review skill](../recipes/analytical-review.md) builds a recurring review that understands the business first, then explains what moved, what does not reconcile, and the questions to raise. If you already have a close skill, [Harden your close skill](../recipes/close-skill-hardening.md) makes it deterministic and gap-proof.
- **You inherited a model or a business plan you do not understand** → [Audit an inherited model](../recipes/model-audit-controller.md) helps you read and stress-test someone else's model fast, before you stake a decision on it.
- **A decision needs scenarios, not one number** → [Parametric scenarios](../recipes/parametric-scenarios.md) generates and compares assumption-level cases without the model falling apart.
- **Before anything goes to a board or a client** → [Pre-delivery review](../recipes/pre-delivery-review.md) forges a pre-flight check, tuned to your conventions, so nothing ships broken.

You will not use all of these on every client. The audit tells you which ones matter here.

## The wall (where structure takes over)

Every tool here is a prompt, and every prompt hits the same wall: nothing persists between sessions, the logic drifts the moment an assumption changes, and you cannot show a clean audit trail of where a number came from. For a part-time CFO that wall has a name: the moment the client's numbers have to be trusted, versioned, and defended in front of an investor or a board.

That is where the cookbook stops and structure begins:

- [`FINANCE.md`](https://github.com/layerzlabs/finance-md) makes the client's conventions explicit, portable, and owned, so an agent does not just guess your rules, it reads them.
- [Layerz](https://layerz.cc) gives the model a structured, versioned home where scenarios are branches you can diff and defend, and where the forecast the audit flagged as drifting finally stops drifting.

No tool on this path pretends a prompt is a model. That honesty is the point.
