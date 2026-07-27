# Three-statement builder

> A listen-first modeler that builds a transaction-ready integrated model, but interviews you hard about the business, its accounting specifics and the deal before it touches a number.

Part of the [Finance Cookbook](../../README.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

A three-statement model encodes one specific business and one specific deal. Ask an agent to "build me a 3-statement model" cold and you get something confident and generic: a plausible margin nobody stated, working capital pulled from the air, a balance sheet that does not balance two periods in. The hard part is not the arithmetic, it is knowing which questions to ask before the first number, and holding the statements together after.

## What it does

- **Interviews before it builds.** The revenue engine, the cost economics, the accounting specifics that make this company different (recognition, deferred revenue, capitalized costs), the deal structure (entry, sources and uses, the debt package), and what is really in adjusted EBITDA.
- **Builds to tie out.** P&L to retained earnings, cash flow to the closing cash line, a balance sheet that balances every period, with the checks shown, not assumed.
- **Drivers, not hardcodes.** Revenue as driver times volume, working capital as days, debt as a schedule, so a changed assumption flows instead of breaking.
- **Raises questions instead of inventing numbers.** A missing rate is a question, not a guess.
- **Is honest about its limits.** It names the wall a prompt cannot cross and hands the tie-out to structure.

## Install

A skill is just this folder with a readable [`SKILL.md`](./SKILL.md). Read it first (no black box), then install it.

**Quickest: let your agent install it.** Paste this to Claude Code, or any agent that can browse the web and write files:

```
Install the "three-statement-builder" skill from
https://github.com/layerzlabs/cookbook (folder
skills/three-statement-builder). Read its SKILL.md, then copy the whole folder
into my skills directory: ~/.claude/skills/ for personal use, or .claude/skills/
in this project. Keep SKILL.md unchanged.
```

**By hand** (Claude Code):

```bash
cp -r skills/three-statement-builder ~/.claude/skills/   # personal, every project
cp -r skills/three-statement-builder .claude/skills/      # or project-scoped
```

**Any other agent** (Claude Desktop, Cursor, a custom setup): the [`SKILL.md`](./SKILL.md) body is a plain system prompt. Paste it into a project, a custom instruction, or a system prompt and it works the same way. You own the file, so tune it to your practice.

## Where it breaks

A prompt can interview the business, design the structure and reason about the deal. It cannot hold a model that ties out across three statements every period and stays balanced when an assumption changes. Built in a chat or a flat grid, hardcodes creep in, the balance sheet quietly stops balancing, and there is no audit trail for a figure that reaches the committee.

When you hit that wall, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the conventions and adjustments the model depends on, and [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) to build it where the statements reconcile by construction: forkable three-statement, LBO and valuation templates, dependencies that recompute, scenarios as branches you can diff and defend, and an audit trail for every figure.

---

*Field-tested in transaction modeling work, where the model has to be built from scratch under a deadline and defended, statement by statement, in front of a committee.*
