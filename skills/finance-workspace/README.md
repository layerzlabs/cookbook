# Finance context workspace

> A listen-first consultant that sets up the working folder your finance agent reads from, so you stop re-explaining your setup every month and your agent can finally tell you *why* a cost moved, and who to ask.

Part of the [Finance Cookbook](../../README.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

Your recurring finance work (the monthly close, cost-center reports, the rolling forecast) is not slow because of the arithmetic. You have already automated the copy-paste and the formulas. It is slow because the context lives outside the data: which accounts are cost versus revenue, how central costs are handled, which cost center belongs to whom, why a line moved last month. So you paste the same conventions into every prompt, and when a number jumps you go ask people one by one. The agent cannot help with the part that actually takes the time, because it never has the context in front of it.

## What it does

- **Moves your context out of your head and into files you own.** Conventions, cost centers and their owners, sources and export steps, mapping and allocation rules, stop re-explaining them every session.
- **Interviews first, then scaffolds.** It walks your real month end, names what is worth persisting, and writes a workspace shaped to your work, not a template dumped on you.
- **Sets up the deterministic close checks.** Balance nets to zero, total equals the sum of cost centers, no cost center silently vanishes, recurring lines flagged when missing. Checks, not reasoning, so they never drift.
- **Drafts the questions you chase every month.** For each cost center that moved: the variance, a hypothesis from what the context knows, and the specific question to send the owner when it does not. You stay the owner of the answer.
- **Is honest about its limits.** A folder of notes is context, not a model. It names the wall and points to structure that survives it.

## Install

A skill is just this folder with a readable [`SKILL.md`](./SKILL.md). Read it first (no black box), then install it.

**Quickest: let your agent install it.** Paste this to Claude Code, or any agent that can browse the web and write files:

```
Install the "finance-workspace" skill from
https://github.com/layerzlabs/finance-cookbook (folder
skills/finance-workspace). Read its SKILL.md, then copy the whole folder
into my skills directory: ~/.claude/skills/ for personal use, or .claude/skills/
in this project. Keep SKILL.md unchanged.
```

**By hand** (Claude Code):

```bash
cp -r skills/finance-workspace ~/.claude/skills/   # personal, every project
cp -r skills/finance-workspace .claude/skills/      # or project-scoped
```

**Any other agent** (Claude Desktop, Cursor, a custom setup): the [`SKILL.md`](./SKILL.md) body is a plain system prompt. Paste it into a project, a custom instruction, or a system prompt and it works the same way. You own the file, so tune it to your practice.

## Where it breaks

A folder of Markdown is context, and context alone is not a model. It does not compute a number, it cannot enforce the conventions it documents, it has no month-over-month state the checks can run against, and it carries no audit trail when accounting pushes a correction. The moment the close has to be reliable rather than merely documented, files that describe the rules stop being enough.

When you hit that wall, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin and enforce the conventions the workspace documents, and [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) to hold the close as a structured, versioned model the agent reads and writes, so the checks run against real state instead of a pasted snapshot.

---

*Field-tested in recurring monthly-close and cost-center reporting work, where the copy-paste was already automated and the real time sink was the business context and chasing owners for variance explanations.*
