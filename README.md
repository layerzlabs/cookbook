# Finance Cookbook

**Curated recipes for doing financial work with AI agents, the right way.**

> ### We share the recipe, not the black box.
> Prompts and skills you can read, audit and make yours. Never a black box you install on trust.

Prompts and patterns for FP&A, modeling and reporting with Claude (and any capable agent). Each recipe is battle-tested in the field, opinionated, and honest about where a prompt stops being enough.

This is the **cookbook**. It sits in a small family of open entry points to [Layerz](https://layerz.cc):

| Project | Role | Link |
|---------|------|------|
| **`finance-cookbook`** (you are here) | The **recipes**: how finance people actually use AI, day to day | the playbook |
| [`finance-md`](https://github.com/layerzlabs/finance-md) | The **standard**: how an organization encodes its financial conventions for any agent | the spec |
| [Layerz MCP](https://app.layerz.cc/for-agents) | The **tool**: how an agent drives [Layerz](https://layerz.cc) to build structured, versioned models | the integration |
| [`slides-for-claude`](https://github.com/layerzlabs/slides-for-claude) | The **presentations**: turn a model or a topic into a self-contained HTML deck | the skill |

The standard tells an agent *what your numbers mean*. The tool gives it *a place to build that does not drift*. The cookbook shows *what to ask for in the first place*.

---

## Start here (by role)

New to the cookbook? Instead of scanning the whole list, follow a **path**: the recipes and skills already here, put in the order one kind of user actually reaches for them.

| Path | For | Starts with |
|------|-----|-------------|
| [The part-time CFO's kit](./paths/fractional-cfo.md) | Fractional / part-time CFOs and finance advisors | Understand the business, then a flash audit, then the recurring engine |
| [The founder's kit](./paths/founder.md) | Founders building and owning their own plan and numbers, pre-CFO | Get a rough model on the table, then make it defensible for a raise |
| [The FP&A engine](./paths/fpa.md) | In-house FP&A and controllers running the monthly cycle | Own the context once, then harden the close, variance and forecast |
| [The deal desk](./paths/deal-transaction.md) | M&A, transaction advisory and deal teams working under deadline | Read a model you did not build, stress it, ship it clean |

More paths will land as the catalog grows. Each one is pure curation, it points to the recipes and skills below.

---

## Why this exists

A good prompt can take you a long way. Then it hits a wall: nothing persists between sessions, the logic drifts the moment an assumption changes, and you cannot audit where a number came from. That wall is not a failure of prompting, it is the point where you need **structure** (a documented `FINANCE.md`) and **persistence** (a real model, e.g. Layerz).

So every recipe here is written to be useful on its own, and to name the wall it cannot cross. When you hit that wall, the recipe points you to `finance-md` or Layerz. No recipe pretends a prompt is a model.

---

## Our stance: we share the recipe, not the black box

**We share the recipe, not the black box.** Everything here is plain, readable Markdown you can open, audit, fork and make yours. The enemy is never the format, it is the black box: an opaque artifact that rots, hides its logic, and runs a canned process on you whether it fits your business or not. We do not ship those. That is the Layerz thesis applied to this repo: own your context, no black box, no drift.

So the cookbook has two kinds of entry, and both stay transparent:

- **Recipes** ([`recipes/`](./recipes)): prompts you paste. Some do the task now (compare scenarios, audit a model you received), some forge an artifact you own and can read (a script, a `FINANCE.md`, a skill of your own). Read, paste, own it.
- **Skills** ([`skills/`](./skills)): small **listen-first consultants** you install. A skill here asks before it acts and adapts to your case, it never unrolls a template blindly. It is still open Markdown you can read and change, not a compiled box. Install it, then fork it.

A skill in this repo is a recipe that listens. It earns the "not a black box" line by being auditable and interview-first, the opposite of a canned automation.

## Recipes

| Recipe | What it solves |
|--------|----------------|
| [Own your context](./recipes/context-ownership-finance-md.md) | Stop re-explaining your conventions every session |
| [Parametric scenarios](./recipes/parametric-scenarios.md) | Generate and compare assumption-level scenarios without the model falling apart |
| [Audit an inherited model](./recipes/model-audit-controller.md) | Understand and stress-test a model someone else built, fast |
| [Pre-delivery review](./recipes/pre-delivery-review.md) | Forge a pre-flight review skill, tuned to your conventions, so nothing ships broken |
| [Harden your close skill](./recipes/close-skill-hardening.md) | Audit a close-variance skill you already built and make it deterministic and gap-proof |
| [Analytical review](./recipes/analytical-review.md) | Forge a recurring review that understands the business first, then surfaces variances, trends and the questions to raise |

Each recipe follows the same shape (see [`TEMPLATE.md`](./TEMPLATE.md)): the problem, the prompt, where it breaks, and what to reach for when it does.

---

## Skills

Small **listen-first consultants** you install. Unlike a recipe you paste, a skill loads itself when the moment fits, then asks before it acts. It is still open Markdown you can read, audit and fork, never a compiled box.

| Skill | What it does |
|-------|--------------|
| [Finance flash audit](./skills/finance-flash-audit/) | Walks a company's finance and back-office like a fractional CFO on day one: interviews first, maps the flows, tells the truth about how reliable the numbers are and what that costs in cash, then hands back a prioritized roadmap of where to act and in what order |
| [Business plan sparring partner](./skills/business-plan-sparring/) | Breaks the blank-page freeze: gets a rough founder model on the table fast, challenges every assumption like a seed investor by Socratic questioning, helps you pick your KPIs and sketch the big-picture dashboard, and teaches the finance as it goes |
| [Finance context workspace](./skills/finance-workspace/) | Sets up the working folder your finance agent reads from, so you stop re-explaining your setup every month: interviews your real close, scaffolds a context workspace you own (conventions, cost centers and owners, sources, mapping), and wires two loops, the deterministic close checks and a variance pass that drafts the question to send each cost-center owner |
| [Three-statement builder](./skills/three-statement-builder/) | Builds a transaction-ready integrated model, but interviews you hard first (the revenue engine, the accounting specifics, the deal structure and adjustments), then builds it so the P&L, cash flow and balance sheet tie out, and hands the tie-out to structure because a prompt cannot hold a balancing model |
| [Shadow model](./skills/shadow-model/) | Rebuilds a model someone handed you (a seller's model, a management plan) independently, then reconciles the two and tells you which assumption drives every gap and the question to put to the other side |
| [Deal red flags](./skills/deal-red-flags/) | Learns the specific business first, then surfaces the red flags a buyer should not miss (is the EBITDA real, working capital stretched, concentration, debt-like items), ranks them by impact on value, and turns each into the diligence question to ask |

### Installing a skill

Each skill is a single `SKILL.md`. Download it, then in Claude: **+** > **Skills** > **Manage skills** > **Add** > **Upload skill**. Read the file first, that is the point.

Claude Code, other agents, and how to make a skill yours: [`skills/INSTALL.md`](./skills/INSTALL.md).

---

## The library (curated, external)

The cookbook above is what we wrote. The library below is what *others* wrote and we found worth your time. Curation, not authorship. Suggestions welcome (see [Contributing](./CONTRIBUTING.md)).

| Resource | Author | Good for | Link |
|----------|--------|----------|------|
| Anthropic Cookbook | Anthropic | Foundational prompting and agent patterns (not finance-specific) | https://github.com/anthropics/anthropic-cookbook |
| _your suggestion_ | _you_ | _what it is good for_ | _open a PR_ |

> This table is intentionally short. A library of 10 vetted resources beats a dump of 200. If you know one that earns its place, [open a PR](./CONTRIBUTING.md).

---

## Who this is for

- **AI builders in finance** who live in Claude Code, Cursor, Cowork, and want patterns that hold up.
- **Educators and advisors** who need serious, recommendable bricks, beyond a list of prompts.
- **Finance practitioners** (FP&A, controllers, fractional CFOs) tired of re-deriving everything each month.

---

## Contributing

Recipes and library entries are welcome. Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) and copy [`TEMPLATE.md`](./TEMPLATE.md). The bar is simple: it has to be something you actually used, and it has to be honest about its limits.

---

## License

MIT, see [LICENSE](./LICENSE).

---

**We share the recipe, not the black box.**

*Maintained by [Layerz](https://layerz.cc). The financial memory of Claude: a structured model it builds, edits and exports to Excel, without drifting.*
