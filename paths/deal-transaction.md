# The deal desk

> Free, open tools you run with Claude (or any capable AI agent) for transaction work under deadline: understand a model you did not build, pin the deal's conventions, stress the case, and ship it clean. Start by reading someone else's model fast.

Part of the [Finance Cookbook](../README.md). Everything here is plain, readable Markdown you can open, run and fork. No black box, nothing to install on trust. New to running a skill? See [how to install and run one](../README.md#installing-a-skill).

## What this is

M&A, transaction advisory and deal teams live in models they did not build, under a clock, where one silent error is expensive. This path is about getting on top of a model fast, making its assumptions explicit, testing it, and shipping it without a mistake reaching the committee.

## Start here: read the model you received

The **[audit an inherited model](../recipes/model-audit-controller.md)** recipe reads and stress-tests someone else's model like a controller would: what it computes, where it is fragile, which assumptions carry the outcome, before you stake a recommendation on it. In deal work this is almost always the first move.

## The full path

### 1. Understand what you received
[Audit an inherited model](../recipes/model-audit-controller.md) above. Understand it before you trust it.

### 2. Pin the deal's conventions
[Own your context with FINANCE.md](../recipes/context-ownership-finance-md.md) captures the units, adjustments and definitions this deal runs on (what is in EBITDA, how net debt is drawn, the normalizations), so every later step and every teammate reads the same rules.

### 3. Stress the case
[Parametric scenarios](../recipes/parametric-scenarios.md) generates and compares sensitivities (entry multiple, growth, margin, leverage) without the model breaking, so the range is defensible rather than one point estimate.

### 4. Before it reaches the committee or the client
[Pre-delivery review](../recipes/pre-delivery-review.md) forges a pre-flight check tuned to the deal's conventions, so no broken formula or stale reference ships.

## The wall (where structure takes over)

These tools get you on top of a model and ship it clean, but they are prompts, and building the model itself is where prompting stops. A transaction-ready build (an integrated three-statement model, an LBO with its debt schedule, a DCF that ties out) has to persist, tie across statements, and defend every number under scrutiny. That is not a prompt, it is structure.

That is where the cookbook stops and structure begins:
- [`FINANCE.md`](https://github.com/layerzlabs/finance-md) makes the deal's conventions explicit, portable and owned.
- [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) gives the model a structured, versioned home: forkable LBO, three-statement and valuation templates, scenarios as branches you can diff and defend, and an audit trail for every figure that reaches the committee.

No tool on this path pretends a prompt is a model. That honesty is the point.
