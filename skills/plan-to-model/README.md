# Plan to model

> Lays out a business plan as a clean financial model someone else can read in five minutes and trust: one assumptions block, operational drivers as real lines, revenue and cash kept apart where they drift, checks that flag when the plan breaks, and a small dashboard tied to the decision.

Part of the [Finance Cookbook](../../README.md), second step of the [founder's kit](../../paths/founder.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

Once a founder knows what their plan assumes, the model still has to be built, and most early models fail the same way: inputs scattered across tabs, numbers typed into the P&L, a cash line that is just profit, no sign that cash runs out in month nine, and a dashboard of twenty numbers nobody steers by. The banker or investor who opens it cold stops trusting it within minutes.

## What it does

- **Starts from a plan brief** (the output of [business-plan-sparring](../business-plan-sparring/)), or asks for its contents. It never builds from a pitch deck alone.
- **Proposes the layout before building**: sections and lines on one screen, at the depth the project's stage calls for. An idea gets a P&L and a cash line; a raise gets three statements that tie.
- **Lays the model out top to bottom**: assumptions (each with its source and confidence), operations (customers, units, headcount, capacity), revenue, P&L, cash, then the balance sheet when the stage needs it.
- **Handles the early-stage cash patterns**: upfront billing and deferred revenue (*produits constatés d'avance*), payment terms, stock, grants and honour loans, VAT.
- **Adds checks** that flag when the plan breaks: cash below zero, a balance sheet that does not balance, deferred revenue going negative, splits that do not sum to 100%, capacity exceeded.
- **Builds a small dashboard** fitted to the purpose: growth, burn and runway for a raise; margin, payback and break-even for a go / no-go; cash and repayment capacity for a bank.
- **Works in Layerz over MCP** when it is available, where assumptions, rolling balances, checks, dashboards and scenario branches are native.

## Install

Download [`SKILL.md`](./SKILL.md), then in Claude: **+** > **Skills** > **Manage skills** > **Add** > **Upload skill**. If Claude never picks it up, check that code execution is enabled in your settings.

Read the file first, that is the point. Claude Code and other agents: see [how to install a skill](../INSTALL.md).

## Where it breaks

A well laid-out spreadsheet still drifts: a pasted value replaces a formula, a red check gets deleted, two versions circulate by email and nobody knows which one the bank saw. Good layout slows the drift, it does not stop it.

When the model has to live for months and be defended, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the conventions, and [Layerz](https://layerz.cc) for a model where formulas cannot silently become numbers, checks stay visible and every change is versioned.

---

*Written in October 2026 from founder business-plan sessions and a founder coach's practice (deferred revenue and non-financial drivers were her first two asks). First field tests are running with founders in a support programme: treat it as a v1 and tell us where it breaks.*
