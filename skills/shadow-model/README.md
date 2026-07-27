# Shadow model

> A listen-first modeler that rebuilds a model someone handed you, independently, then reconciles the two and tells you exactly which assumption drives every gap, and the question to put to the other side.

Part of the [Finance Cookbook](../../README.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

You are handed a model you do not trust: a seller's numbers, a management plan, a business plan you have to challenge. Reading their formulas only tells you what they did, not whether it is right, and if you rebuild by mirroring their logic you inherit their blind spots. The value is not a second model, it is a defensible bridge: their number, your number, and the assumption that explains the gap.

## What it does

- **Rebuilds independently, not as a copy.** From the drivers and source data, arriving at each number a different way, so you catch what their logic hid.
- **Focuses on the load-bearing lines.** The three to five drivers that move the outcome and where optimism hides (growth, ramp, margin, working capital), not the twentieth cost line.
- **Makes the reconciliation the deliverable.** For each material gap: the assumption behind it, the size, and a view on which holds, ranked by impact on value or return.
- **Turns divergences into challenges.** The specific question to put to the seller or management, tied to the evidence that would resolve it.
- **Is honest about its limits.** It names the wall and hands the two-model reconciliation to structure.

## Install

A skill is just this folder with a readable [`SKILL.md`](./SKILL.md). Read it first (no black box), then install it.

**Quickest: let your agent install it.** Paste this to Claude Code, or any agent that can browse the web and write files:

```
Install the "shadow-model" skill from
https://github.com/layerzlabs/cookbook (folder
skills/shadow-model). Read its SKILL.md, then copy the whole folder
into my skills directory: ~/.claude/skills/ for personal use, or .claude/skills/
in this project. Keep SKILL.md unchanged.
```

**By hand** (Claude Code):

```bash
cp -r skills/shadow-model ~/.claude/skills/   # personal, every project
cp -r skills/shadow-model .claude/skills/      # or project-scoped
```

**Any other agent** (Claude Desktop, Cursor, a custom setup): the [`SKILL.md`](./SKILL.md) body is a plain system prompt. Paste it into a project, a custom instruction, or a system prompt and it works the same way. You own the file, so tune it to your practice.

## Where it breaks

A prompt can rebuild a few lines and eyeball the gap. A real shadow holds two full models side by side, reconciles them every period, and re-bridges when either assumption moves. In spreadsheets that is two fragile files you diff by hand, with no audit trail and no way to requantify a gap when a driver changes.

When you hit that wall, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the conventions both models are measured on, and [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) to hold their model and yours as branches, diff them natively, quantify each gap, and keep a versioned trail as the case evolves.

---

*Field-tested in deal and planning work where a model received from the other side had to be rebuilt independently and reconciled, gap by gap, before anyone acted on it.*
