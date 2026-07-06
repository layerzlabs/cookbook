# Finance flash audit

> A listen-first flash audit that walks a company's finance and back-office, tells the truth about how reliable the numbers are, and hands back a prioritized roadmap: where to act, in what order, for what gain.

Part of the [Finance Cookbook](../../README.md), and the opening step of the [fractional CFO path](../../paths/fractional-cfo.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

"I know I need help, but I cannot tell you why." A founder senses something is off in the finances and cannot name it. A fractional CFO lands on a new client and has days, not weeks, to figure out where it actually hurts. Done by feel, a first-pass audit drifts into a generic maturity grid that fits any company and helps none. The value is never a longer checklist, it is a specific, honest read on this business: what the numbers can be trusted for, what it costs when they cannot, and the two or three levers worth pulling first.

## What it does

- **Listens before it judges.** It interviews to understand what the business sells, how cash moves, and what triggered the audit, before it scores a single process.
- **Walks the real flows.** Order-to-cash and collections, spend, payroll, the close, treasury, reporting, and the tooling underneath, mapping only what it can verify and flagging what it cannot.
- **Tells the truth about the data.** The core output: how reliable are the numbers feeding decisions and cash, where drift and error enter, and what that unreliability actually costs.
- **Hands back a prioritized roadmap.** Quick wins first, then a sequenced plan, every item tied to a finding and to its impact on cash, risk or time. Ranked by impact, not by ease.
- **Speaks the user's language.** English skill, but it runs the interview and the diagnostic in whatever language the person uses.
- **Is honest about its limits.** It names the wall a diagnostic cannot cross and points to structure that survives it.

## Who it is for

- **Founders and CEOs** who feel something is off and want a clear read before they commit to a fix.
- **Fractional CFOs and advisors** scoping a new client, or handing an adapted diagnostic to one.

## Install

A skill is just this folder with a readable [`SKILL.md`](./SKILL.md). Read it first (no black box), then install it.

**Quickest: let your agent install it.** Paste this to Claude Code, or any agent that can browse the web and write files:

```
Install the "finance-flash-audit" skill from
https://github.com/layerzlabs/finance-cookbook (folder
skills/finance-flash-audit). Read its SKILL.md, then copy the whole folder
into my skills directory: ~/.claude/skills/ for personal use, or .claude/skills/
in this project. Keep SKILL.md unchanged.
```

**By hand** (Claude Code):

```bash
cp -r skills/finance-flash-audit ~/.claude/skills/   # personal, every project
cp -r skills/finance-flash-audit .claude/skills/      # or project-scoped
```

**Any other agent** (Claude Desktop, Cursor, a custom setup): the [`SKILL.md`](./SKILL.md) body is a plain system prompt. Paste it into a project, a custom instruction, or a system prompt and it works the same way. You own the file, so tune it to your practice.

## Where it breaks

A flash audit in the chat is a snapshot. It is right for finding where to act, and wrong as a place to fix what it finds. The diagnostic does not persist, it cannot re-run itself against live numbers next month, the roadmap has no home where progress is tracked, and the finding that most often matters, that the numbers are unreliable and the forecast drifts when an assumption changes, is exactly what a prompt cannot fix.

When you hit that wall, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the business context and the conventions so the reliability problem becomes explicit and portable, and [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) to give the numbers a structured, versioned home where the forecast stops drifting and the roadmap has a place to live.

---

*Field-tested in early-engagement fractional-CFO practice: the first days on a new client, spent understanding the business and leaving with a prioritized roadmap.*
