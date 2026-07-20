# Account mapping

> A listen-first consultant that maps a raw accounting export, a trial balance or a general ledger, onto clean, structured financial statements, under the right accounting framework. It confirms the framework, reuses the context you own, maps what is unambiguous, and raises every judgment call instead of guessing it.

Part of the [Finance Cookbook](../../README.md), and a step in both the [part-time CFO path](../../paths/fractional-cfo.md) and the [deal desk path](../../paths/deal-transaction.md). This is a **skill**, not a black box: [`SKILL.md`](./SKILL.md) is plain, readable Markdown. Open it and read it before you install it, that is the point.

## The problem

An accounting export is not a financial statement. A trial balance, a French FEC, a DATEV dump or a QuickBooks export is a flat list of accounts and balances, and before anyone can read a P&L, review a model, or start a diligence, every account has to land on the right line. Done by hand it is slow and error-prone. Done by a naive agent it is worse: it infers the business from the account labels instead of asking, confidently files "divers 471" onto a plausible line, splits COGS from opex by guessing, gets a sign wrong, and the mistake surfaces three months later as a number nobody can explain. Or it wanders off the mapping entirely and hands back a P&L and a performance commentary nobody asked for, while the mapping itself goes unchecked. The value is never in mapping the obvious accounts, it is in knowing the business first, confirming the framework, and never silently misfiling the ambiguous ones.

## What it does

- **Confirms the framework, does not assume it.** French PCG, German SKR03 / SKR04, a Belgian or Spanish chart, or a company-specific US / UK COA with no national chart: it detects the source from the codes, labels and language, and confirms it before mapping.
- **Refuses to map before it knows the business.** Deducing the activity from the account labels does not count: labels tell you what the accountant typed, not what the company sells or what it merely intermediates. It asks a short, fixed batch of questions up front, once, never per account, and holds the accounts it cannot place without an answer.
- **Reuses the context you own.** If you have a `FINANCE.md` or a context workspace, it reads it instead of re-interviewing.
- **Challenges a mapping that already exists.** Pennylane, Qonto, Xero and most modern tools pre-map their exports. It detects that, says so, and switches from building to auditing: a diff of what it would change and why, not a parallel table.
- **Stays on the mapping.** The statements and the analysis are what the mapping enables, and they are worth having, but they come after and only if you want them. The mapping gets finished and challenged first.
- **Sizes the job before it reads the file.** A general ledger can exhaust a context window on its own. It counts the rows and accounts first, aggregates with a script instead of reading entry-level detail, and tells you upfront how it plans to process the file and what that costs.
- **Maps the standard, raises the judgment.** The accounts the framework makes unambiguous get mapped in a batch. The mixed accounts, the "autres" buckets, the COGS-versus-opex splits get raised as specific questions for you to decide.
- **Flags what it cannot place.** An unmapped account is a finding, never dropped into "other" to look complete.
- **Persists the mapping.** The mapping is saved as a template, so next period's export is a diff, not a redo.

## Who it is for

- **Fractional CFOs and controllers** turning a client's accounting export into a clean management P&L.
- **Deal teams and advisors** structuring a target's trial balance at the start of a diligence.
- **Finance builders** importing an accounting export into a model and tired of naming every line by hand.

## Install

Download [`SKILL.md`](./SKILL.md), then in Claude: **+** > **Skills** > **Manage skills** > **Add** > **Upload skill**.

Read the file first, that is the point. Claude Code and other agents: see [how to install a skill](../INSTALL.md).

## Where it breaks

A mapping table in a spreadsheet is static. It does not persist against live numbers, it has no month-over-month state to tell you a new account appeared, it carries no audit trail of why an account went where it did, and next period someone re-does or re-checks it by hand. The mapping says where each account belongs, it does not hold the structure those accounts feed, and it cannot stop that structure from drifting when someone reclassifies an account upstream.

When you hit that wall, reach for [`FINANCE.md`](https://github.com/layerzlabs/finance-md) to pin the conventions and mapping rules so they are explicit and owned, and [Layerz](https://layerz.cc) to hold the mapped accounts as a structured, versioned model where the mapping is stored as a reusable template, applied in batch, and re-run against real state each period instead of re-keyed.

---

*Field-tested where an accounting export has to become a clean, structured P&L before any analysis can start, and where the same export comes back every period.*
