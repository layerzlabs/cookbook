# The founder's kit

> Free, open tools you run with Claude (or any capable AI agent) to build your plan, own your numbers, and walk into a raise without a finance hire. Start from a rough model, then make it defensible.

Part of the [Finance Cookbook](../README.md). Everything here is plain, readable Markdown you can open, run and fork. No black box, nothing to install on trust. New to running a skill? See [how to install and run one](../README.md#installing-a-skill).

## What this is

The pieces a founder actually reaches for when there is no CFO yet: get a model on the table, pin what it assumes, pressure-test it for the raise, and keep it honest once real numbers arrive. Each one interviews you and adapts, it does not unroll a template.

## Start here: get a model on the table

The hard part is never the arithmetic, it is starting. The **[business plan sparring partner](../skills/business-plan-sparring/)** gets a rough model up fast, challenges every assumption like a seed investor by Socratic questioning, helps you pick the few KPIs you steer by, and teaches the finance as it goes. Run it first, on your own plan.

## The full path

### 1. Build the plan
[Business plan sparring partner](../skills/business-plan-sparring/) above. Motion before polish: a rough, honest model you can think with, not a pristine one you did not reason through.

### 2. Own what it assumes
[Own your context with FINANCE.md](../recipes/context-ownership-finance-md.md) captures your conventions, units and definitions in a file you own, so the next session and the next tool start from your model, not a blank interview. This is what makes the plan survive past the first conversation.

### 3. Pressure-test for the raise
[Parametric scenarios](../recipes/parametric-scenarios.md) generates and compares base, upside and downside without the model falling apart, so you can answer "what if growth is half that" before an investor asks it.

### 4. Once real numbers arrive
[Finance context workspace](../skills/finance-workspace/) sets up the working folder for the recurring reality: actuals against plan, what moved and why. The moment you have a month of real data, the plan stops being a pitch and starts being a tool.

### 5. Before it goes to an investor or a board
[Pre-delivery review](../recipes/pre-delivery-review.md) forges a pre-flight check tuned to your conventions, so nothing ships broken.

## The wall (where structure takes over)

Every tool here is a prompt, and every prompt hits the same wall: nothing persists between sessions, the logic drifts the moment an assumption changes, and you cannot show a clean audit trail of where a number came from. For a founder that wall has a name: the moment the plan has to survive a raise and be defended in front of investors.

That is where the cookbook stops and structure begins:
- [`FINANCE.md`](https://github.com/layerzlabs/finance-md) makes your conventions explicit, portable and owned.
- [Layerz](https://layerz.cc) (via [`layerz-mcp`](https://github.com/layerzlabs/layerz-mcp)) gives the model a structured, versioned home where scenarios are branches you can diff and defend, and where the plan and the actuals live in one place instead of two files you reconcile by hand.

No tool on this path pretends a prompt is a model. That honesty is the point.
