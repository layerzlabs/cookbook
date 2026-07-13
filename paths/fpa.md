# The FP&A engine

> Free, open tools you run with Claude (or any capable AI agent) for the work that comes back every month: the close, the variance story, the forecast. Own the context once, then make the cycle fast and hard to break.

Part of the [Finance Cookbook](../README.md). Everything here is plain, readable Markdown you can open, run and fork. No black box, nothing to install on trust. New to running a skill? See [how to install and run one](../README.md#installing-a-skill).

## What this is

FP&A is not slow because of the arithmetic, you have already automated that. It is slow because the context lives outside the data (which accounts map where, who owns which cost center, why a number moved) and gets re-explained every cycle. This path moves that context into files you own, then hardens the recurring jobs on top of it.

## Start here: own the context

The **[finance context workspace](../skills/finance-workspace/)** interviews your real close and sets up the working folder your agent reads from: conventions, cost centers and their owners, sources, mapping. Stop pasting the same setup into every prompt. It is the foundation the rest of the cycle stands on.

## The full path

### 1. Own the recurring context
[Finance context workspace](../skills/finance-workspace/) above. Do this first: every step below reuses it instead of re-gathering it.

### 2. Make the close deterministic
[Forge your analytical review skill](../recipes/analytical-review.md) builds a recurring review that understands the business first, then explains what moved, what does not reconcile, and the questions to raise. Already have a close skill? [Harden your close skill](../recipes/close-skill-hardening.md) makes it deterministic and gap-proof: no cost center silently vanishes, recurring lines flagged when missing.

### 3. Turn the actuals into a forecast
[Parametric scenarios](../recipes/parametric-scenarios.md) generates and compares assumption-level cases without the model falling apart, so the reforecast is a set of defensible scenarios, not one guessed number.

### 4. Before the board pack ships
[Pre-delivery review](../recipes/pre-delivery-review.md) forges a pre-flight check tuned to your conventions, so nothing goes out broken. Inherited a model you have to fold in? [Audit an inherited model](../recipes/model-audit-controller.md) helps you read and stress-test it fast.

## The wall (where structure takes over)

Every tool here is a prompt, and every prompt hits the same wall: nothing persists between sessions, so "no cost center disappeared since last month" is only as good as the file you happened to paste, the logic drifts when an assumption changes, and there is no audit trail when accounting pushes a correction. For FP&A that wall is the monthly cycle itself: the checks need real month-over-month state to run against, not a snapshot.

That is where the cookbook stops and structure begins:
- [`FINANCE.md`](https://github.com/layerzlabs/finance-md) pins and enforces the conventions the workspace documents.
- [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) holds the close as a structured, versioned model: variance against budget is native, the checks run against real state, and every correction is versioned with a trail.

No tool on this path pretends a prompt is a model. That honesty is the point.
