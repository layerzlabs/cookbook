# The deal desk

> Free, open tools you run with Claude (or any capable AI agent) for transaction work under deadline: build a model or get on top of one you were handed, challenge it, diligence the target, and ship it clean. Start by building the model or reading theirs.

Part of the [Finance Cookbook](../README.md). Everything here is plain, readable Markdown you can open, run and fork. No black box, nothing to install on trust. New to running a skill? See [how to install and run one](../README.md#installing-a-skill).

## What this is

M&A, transaction advisory and deal teams work under a clock, on models where one silent error is expensive, and often on numbers someone else produced with an incentive to look good. This path is about getting on top of the numbers fast, whether you build them or receive them, then challenging, diligencing and shipping without a mistake reaching the committee.

## Start here: build it, or read theirs

Two ways in, depending on the deal:

- **Building the model** → the **[three-statement builder](../skills/three-statement-builder/)** interviews you hard on the business, its accounting specifics and the deal structure, then builds an integrated model that ties out.
- **Handed a model** → the **[audit an inherited model](../recipes/model-audit-controller.md)** recipe reads and stress-tests someone else's model like a controller: what it computes, where it is fragile, which assumptions carry the outcome.

## The full path

### 1. Get on top of the numbers
[Three-statement builder](../skills/three-statement-builder/) if you are building, [audit an inherited model](../recipes/model-audit-controller.md) if you received one. Either way, understand it before you trust it.

### 2. Challenge what you do not trust
[Shadow model](../skills/shadow-model/) rebuilds their model independently from the drivers, then reconciles: for each material gap, which assumption drives it and the question to put to the other side. The bridge, not a second opinion.

### 3. Diligence the target
[Deal red flags](../skills/deal-red-flags/) learns the specific business, then surfaces the warning signs a buyer should not miss (is the EBITDA real and repeatable, working capital being stretched, concentration, debt-like items), ranked by impact on value and turned into diligence questions.

### 4. Pin the deal's conventions
[Own your context with FINANCE.md](../recipes/context-ownership-finance-md.md) captures the units, adjustments and definitions this deal runs on (what is in EBITDA, how net debt is drawn, the normalizations), so every step and every teammate reads the same rules.

### 5. Stress the case
[Parametric scenarios](../recipes/parametric-scenarios.md) generates and compares sensitivities (entry multiple, growth, margin, leverage) without the model breaking, so the range is defensible rather than one point estimate.

### 6. Before it reaches the committee or the client
[Pre-delivery review](../recipes/pre-delivery-review.md) forges a pre-flight check tuned to the deal's conventions, so no broken formula or stale reference ships.

## The wall (where structure takes over)

Every tool here is a prompt. A prompt can interview the business, design a structure, rebuild a few lines and reason about risk. It cannot hold a model that ties out across three statements every period, keep two models reconciled as assumptions move, or requantify what a red flag does to the return. A transaction-ready build has to persist, tie across statements, and defend every number under scrutiny. That is not a prompt, it is structure.

That is where the cookbook stops and structure begins:
- [`FINANCE.md`](https://github.com/layerzlabs/finance-md) makes the deal's conventions explicit, portable and owned.
- [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) gives the model a structured, versioned home: forkable LBO, three-statement and valuation templates, your model and theirs as branches you can diff and defend, and an audit trail for every figure that reaches the committee.

No tool on this path pretends a prompt is a model. That honesty is the point.
