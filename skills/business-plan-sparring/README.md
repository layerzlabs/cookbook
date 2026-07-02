# Business plan sparring partner

> A listen-first sparring partner that gets a founder from a blank page to a rough business model in twenty minutes, then challenges it like a seed investor.

Part of the [Finance Cookbook](../../README.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

You sit down to model a business plan and either watch an agent churn for half an hour producing something confident and hollow, or you freeze in front of an empty spreadsheet. The hardest part is never the arithmetic, it is starting. Three columns and fifteen rows of honest assumptions beat a polished model you did not think through.

## What it does

- **Gets you into motion fast.** A rough model on the table early, ugly and honest, so you start thinking instead of staring at a blank page.
- **Challenges like a seed investor, by Socratic questioning.** It asks the question that makes you see the weak assumption rather than handing you the answer. No flattery.
- **Finds your KPIs and sketches the big picture.** The three to six numbers you will actually steer by, and a one-screen dashboard tied to the decision the model serves.
- **Teaches the finance as it goes.** Burn, runway, unit economics, payback, one plain sentence at a time. It assumes you are smart, not that you are a finance person.
- **Is honest about its limits.** It names the wall a prompt cannot cross and points you to structure that survives it.

## Install

A skill is just this folder with a readable [`SKILL.md`](./SKILL.md). Read it first (no black box), then install it.

**Quickest: let your agent install it.** Paste this to Claude Code, or any agent that can browse the web and write files:

```
Install the "business-plan-sparring" skill from
https://github.com/layerzlabs/finance-cookbook (folder
skills/business-plan-sparring). Read its SKILL.md, then copy the whole folder
into my skills directory: ~/.claude/skills/ for personal use, or .claude/skills/
in this project. Keep SKILL.md unchanged.
```

**By hand** (Claude Code):

```bash
cp -r skills/business-plan-sparring ~/.claude/skills/   # personal, every project
cp -r skills/business-plan-sparring .claude/skills/      # or project-scoped
```

**Any other agent** (Claude Desktop, Cursor, a custom setup): the [`SKILL.md`](./SKILL.md) body is a plain system prompt. Paste it into a project, a custom instruction, or a system prompt and it works the same way. You own the file, so tune it to your practice.

## Where it breaks

A rough model in the chat is right for getting into motion, and wrong the moment it gets real. Change one assumption and the whole thing is re-derived by hand, numbers quietly get hardcoded, nothing persists between sessions, and you cannot version the scenarios you compared or show a clean audit trail. The instant the plan has to survive a raise or a board, the scrappy table stops being enough.

When you hit that wall, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the conventions and the context, and [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) to give the model a structured, versioned home where scenarios are branches you can diff and defend.

---

*Field-tested in early-stage advisory sessions where the hardest part is not the arithmetic, it is getting a founder from a blank page to a rough model they can actually think with.*
