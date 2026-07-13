# Deal red flags

> A listen-first diligence partner that learns the specific business first, then surfaces the red flags a buyer should not miss, ranks them by impact on value, and turns each into the question to ask.

Part of the [Finance Cookbook](../../README.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

Ask an agent for "the red flags" cold and you get a generic checklist: forty items, none weighted, half irrelevant to this business. But a red flag in one company is normal in another. Negative working capital is a gift for a subscription business and a warning for a contractor. The value is not the list, it is knowing which risks actually threaten this deal, and what to ask to resolve them.

## What it does

- **Learns the business before it judges it.** Revenue quality, concentration, seasonality, the economics that decide what counts as a flag here.
- **Follows the earnings quality and the cash.** Whether the EBITDA is real and repeatable or propped by one-offs, aggressive recognition, under-investment or generous add-backs, and whether cash conversion matches the profit.
- **Checks the balance sheet and debt-like items.** Working capital being stretched into the close, leases, factoring, pensions, earn-outs, deferred revenue as an obligation, real capex needs.
- **Ranks by impact and turns flags into questions.** Each risk tied to what triggered it and the specific diligence request that would resolve it, with what would change your mind.
- **Is honest about its limits.** It names the wall a prompt cannot cross and points to structure that quantifies the risk.

## Install

A skill is just this folder with a readable [`SKILL.md`](./SKILL.md). Read it first (no black box), then install it.

**Quickest: let your agent install it.** Paste this to Claude Code, or any agent that can browse the web and write files:

```
Install the "deal-red-flags" skill from
https://github.com/layerzlabs/finance-cookbook (folder
skills/deal-red-flags). Read its SKILL.md, then copy the whole folder
into my skills directory: ~/.claude/skills/ for personal use, or .claude/skills/
in this project. Keep SKILL.md unchanged.
```

**By hand** (Claude Code):

```bash
cp -r skills/deal-red-flags ~/.claude/skills/   # personal, every project
cp -r skills/deal-red-flags .claude/skills/      # or project-scoped
```

**Any other agent** (Claude Desktop, Cursor, a custom setup): the [`SKILL.md`](./SKILL.md) body is a plain system prompt. Paste it into a project, a custom instruction, or a system prompt and it works the same way. You own the file, so tune it to your practice.

## Where it breaks

A prompt can reason about risk from what you tell it. It has no persistent, versioned model of the target to test a flag against, no month-over-month state, no audit trail, and it cannot recompute what a red flag does to the return. Diligence that lives in a chat cannot be revisited line by line when the data room updates.

When you hit that wall, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the adjustments and definitions the diligence hinges on, and [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) to hold the model, branch the downside a flag implies, and quantify its impact on value and returns, with a versioned trail as diligence progresses.

---

*Field-tested in transaction diligence work, where the risks that mattered were specific to the business and had to be ranked and turned into questions, not read off a checklist.*
