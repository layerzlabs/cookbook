# Software spend review

> A listen-first consultant that turns raw bank or card transactions into a structured view of what you actually spend on software, cloud and AI. Its core job is the part everything else gets wrong: one vendor line is not one cost. It splits the composite bills before it counts anything, asks for the billing detail instead of guessing an allocation, and reports what it cannot resolve.

Part of the [Finance Cookbook](../../README.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

"What do we spend on tools?" sounds like a categorisation problem and is not. Categorising transactions by merchant is the easy half, and the naive version of it produces a number that cannot be used: it groups one AWS charge that contains compute, tokens, third-party software resold through a marketplace and a support plan priced as a percentage of the rest. Those four move for four different reasons, and two of them are cost of revenue rather than opex. The same happens on the other large vendors: a productivity suite next to a cloud next to a model API, or transaction fees sitting alongside actual software from the same payment provider.

Get the split wrong and three things break at once. The budget is unforecastable, because the parts have different drivers. Month-over-month comparison is meaningless, because a rise could be seats, traffic, tokens or just the exchange rate. And gross margin is wrong, because production infrastructure was booked as an office tool. The value here is never in finding the 20-a-seat subscriptions, it is in the four vendors that carry most of the money and hide most of the structure.

## What it does

- **Splits composite vendors before counting anything.** Per-seat licences, usage-based infrastructure, AI and token consumption, transaction fees, and third-party software resold through a cloud marketplace: five natures, five drivers, and often two different places in the P&L.
- **Asks for the billing detail instead of inferring it.** A bank label tells you the billing entity, not the mix. It names which vendors need a console export and why, in one batch. Where the detail is out of reach, it makes you state the allocation key, records it explicitly, and marks every line derived from it as an estimate.
- **Refuses to classify before it knows what the company runs.** Whether AI is inside the product or only internal tooling decides COGS versus opex. No vendor list answers that.
- **Reads transactions honestly.** Thirteen months, not three, so annual renewals are visible. Grouping by vendor rather than by label string, because one vendor wears several. Checking currency before reading a trend, because a bill priced in one currency and debited in another moves on its own.
- **Reports what it cannot resolve.** An unsplit vendor is a finding with a named next step, never a line dropped into "other software".
- **Separates overlap from waste.** Two tools that look redundant usually serve two teams or two migration phases. That is a question for an owner, not a saving.
- **Stops short of deciding.** It surfaces candidates and what each costs annualised. Cancelling a tool has consequences no bank line shows.
- **Works with what you already have.** A CSV or an Excel export in, a spreadsheet out. If a connector is available in your session (a banking, accounting or card MCP, a cost or usage API on the big vendors), it pulls from that instead and says so, which saves the manual export but changes nothing in the method. Nothing here requires a particular tool to be installed.

## Who it is for

- **Founders and finance leads** asked where the software budget went, and why the cloud bill grew.
- **Fractional CFOs and controllers** taking over a company's spend and needing a defensible structure before any cost exercise.
- **Anyone reporting a gross margin** whose production infrastructure and model consumption are currently sitting in an opex bucket.

## Install

Download [`SKILL.md`](./SKILL.md), then in Claude: **+** > **Skills** > **Manage skills** > **Add** > **Upload skill**.

Read the file first, that is the point. Claude Code and other agents: see [how to install a skill](../INSTALL.md).

## Where it breaks

The table it produces is a snapshot. Next month the mix moves, a new vendor appears, the AI share doubles, and someone re-does the exercise by hand because nothing holds the vendor-to-nature mapping, the allocation keys, or last month's numbers to compare against. A spreadsheet holds the split perfectly well, and for a one-off review it is the right tool; what it cannot do is tell you the split stopped being true.

The point of this work is not the one-off number, it is being able to say next quarter that infrastructure grew with volume as expected while token spend tripled against a flat budget. That needs the classification to persist and actuals to land against a budget month after month.

When you hit that wall, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the conventions (which natures exist, what counts as COGS, which allocation key is in force and since when), and [Layerz](https://layerz.cc) to hold the split as a structured model where each nature carries its own driver and next month is a comparison rather than a rebuild.

---

*Field-tested on two sources with opposite shapes: an accounting ledger carrying account numbers and no vendor labels, where the run correctly stopped at the split instead of inventing one, and a bank export carrying merchant labels, where one vendor turned out to wear eleven of them and the seat-versus-usage split changed how a doubling was read.*
