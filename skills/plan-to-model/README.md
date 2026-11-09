# Plan to model

> Lays out a business plan as a clean financial model someone else can read in five minutes and trust: one assumptions block, operational drivers as real lines, revenue and cash kept apart where they drift, checks that flag when the plan breaks, and a small dashboard tied to the decision.

Part of the [Finance Cookbook](../../README.md), second step of the [founder's kit](../../paths/founder.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

Once a founder knows what their plan assumes, the model still has to be built, and most early models fail the same way: inputs scattered across tabs, numbers typed into the P&L, a cash line that is just profit, no sign that cash runs out in month nine, and a dashboard of twenty numbers nobody steers by. The banker or investor who opens it cold stops trusting it within minutes.

## What it does

- **Starts from a plan brief** (the output of [business-plan-sparring](../business-plan-sparring/)), or asks for its contents. It never builds from a pitch deck alone.
- **Proposes the layout once, then builds the whole first version in one pass**, at the depth the project's stage calls for, with a single base case. Scenarios come later, when the founder asks.
- **Sets assumptions per fiscal year**, each with its source, so the founder can review and change them year by year. The revenue driver stays monthly: a customer calendar, or a monthly growth rate set per year.
- **Lays the model out in few tabs**: two dashboards, the income statement, balance sheet and cash flow each on its own tab, then assumptions, KPIs and checks, and the workings folded at the end.
- **Handles the early-stage cash patterns**: upfront billing and deferred revenue, payment terms, payroll charges, grants and honour loans, loans, VAT.
- **Adds checks and verifies before delivering**: balance sheet, cash, deferred revenue, and three numbers redone by hand from the brief.
- **Builds two sober dashboards**: four KPIs, one yearly table, one to three charts.
- **Works in Layerz over MCP** when it is available: a short Python script (`bpkit.py`, shipped with the skill) writes the whole model as one blueprint, applied in about ten calls. Every later round of changes is one edit with the before and after.

## Install

Download this folder ([`SKILL.md`](./SKILL.md) and [`bpkit.py`](./bpkit.py)) as a zip, then in Claude: **+** > **Skills** > **Manage skills** > **Add** > **Upload skill**. If Claude never picks it up, check that code execution is enabled in your settings.

Read the file first, that is the point. Claude Code and other agents: see [how to install a skill](../INSTALL.md).

## Where it breaks

A well laid-out spreadsheet still drifts: a pasted value replaces a formula, a red check gets deleted, two versions circulate by email and nobody knows which one the bank saw. Good layout slows the drift, it does not stop it.

When the model has to live for months and be defended, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the conventions, and [Layerz](https://layerz.cc) for a model where formulas cannot silently become numbers, checks stay visible and every change is versioned.

---

*Written in October 2026 from founder business-plan sessions and a founder coach's practice (deferred revenue and non-financial drivers were her first two asks). Reworked in November 2026 after the first field tests: one-pass build, assumptions per year, a single base case, fewer tabs and sober dashboards. Tell us where it breaks.*
