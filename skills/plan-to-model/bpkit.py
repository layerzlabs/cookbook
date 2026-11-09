"""bpkit: write a Layerz blueprint in Python instead of typing JSON by hand.

Used by the plan-to-model skill. Usage, in a gen.py next to it:

    import sys; sys.path.insert(0, "<folder of this skill>")
    from bpkit import BP
    bp = BP("2026-11", "2030-12")
    h = bp.section("Revenue", group="Assumptions")
    h.a("Annual price per customer", 25, comment="Source: founder, brief of November 2026.")
    h.a("New customers signed", values=bp.events({"2027-02": 1, "2027-05": 1}))
    h.a("Rent (k per year)", per_year={2027: 12, 2028: 14})
    c = bp.section("Customers", group="Workings")
    c.bal("Active customers", 0, [c.flow("Signed this month", "`New customers signed`")], stock=True)
    ...
    bp.dump("bp.json")

Defaults: every dated item is monthly, every line has a format (`default`), every formula
sums over the year unless declared `stock=True` (a stock: December value), `avg=True`
(a rate: average) or `first=True` (an opening: first month).
"""
import json
import datetime as _dt

# Built-in Layerz formats: no custom format needed. With `units: k` in the FINANCE.md,
# `default` renders #,##0.0;(#,##0.0);- : one decimal, negatives in brackets, dash for zero.
FORMATS = {
    "amount": "default",       # amounts, customers, headcount
    "fine": "decimal_2",       # fine unit assumptions (1.15)
    "rate": "percent",         # round rates (25%, 8%)
    "rate2": "percent_2",      # rates with decimals (52.50%)
    "multiple": "multiple",    # LTV / CAC, burn multiple
    "count": "integer",        # whole counters (servers, flags)
    "month": "date_mmmyy",     # dates (month of minimum cash)
}


def meta_op(finance_md=None, currency="EUR", units="k", language="en", locale=None, glyph=None, subtitle=None):
    """The `meta` op of the setup patch: number locale and FINANCE.md. A front matter with
    `units: k` is added when missing: it is what gives `default` its decimal."""
    op = {"op": "meta"}
    if locale:
        op["number_locale"] = locale
    if finance_md:
        if not finance_md.lstrip().startswith("---"):
            finance_md = f"---\ncurrency: {currency}\nunits: {units}\nlanguage: {language}\n---\n\n" + finance_md
        op["finance_md"] = finance_md
    if glyph:
        op["glyph"] = glyph
    if subtitle:
        op["subtitle"] = subtitle
    return op


def _clean(v):
    if isinstance(v, float) and v.is_integer():
        return int(v)
    return round(v, 9) if isinstance(v, float) else v


class _Container:
    def __init__(self, bp, items):
        self.bp, self.items = bp, items

    def _add(self, it):
        self.items.append(it)
        return it

    def _common(self, it, fmt, stock, avg, comment, style, check, extra):
        if fmt:
            it["format"] = fmt
        if stock or check is not None:
            it["aggregation"] = "stock"  # a check reads at the point in time, never summed
        elif avg:
            it["aggregation"] = "average"
        elif it["role"] == "formula" and "aggregation" not in it:
            it["aggregation"] = "sum"
        if comment:
            it["comment"] = comment
        if style:
            it["item_style"] = style
        if check is not None:
            it["check"] = {"tolerance": check} if isinstance(check, (int, float)) and not isinstance(check, bool) else {}
        it.update(extra)
        return it

    def a(self, name, value=None, values=None, fmt="default", comment=None, stock=False, avg=False,
          style=None, list_name=None, by_item=None, per_year=None, **extra):
        """Assumption.
        - `value`: a constant (price, rate, duration, date, amount of a dated event).
        - `per_year`: {2027: 5, 2028: 10} = an amount or a volume PER FISCAL YEAR (the default for a
          first-pass plan). Layerz spreads it over the months of that year inside the horizon; a
          first partial year takes the amount of its months only. A monthly formula reads it with a
          bare reference `` `Name` `` (no `* 1`, no `/ 12`). A rate per year: add `avg=True`.
        - `values`: a monthly series, only for a monthly calendar the founder actually has.
        - `list_name` + `by_item`: one value per list item, {item: value}, {item: [monthly series]}
          or {item: {year: value}} for per-year amounts."""
        it = {"role": "assumption", "name": name}
        if per_year is not None or (list_name and by_item and all(isinstance(v, dict) for v in by_item.values())):
            years = self.bp.years
            it["timeline_ref"] = "yearly"
            if list_name:
                it.update(liste_ref=list_name,
                          timeline_values={k: [_clean(v.get(y, 0)) for y in years] for k, v in by_item.items()})
            else:
                it["values"] = [_clean(per_year.get(y, 0)) for y in years]
            return self._add(self._common(it, fmt, stock, avg, comment, style, None, extra))
        if list_name:
            monthly = any(isinstance(x, list) for x in by_item.values())
            it.update(liste_ref=list_name, timeline_ref="monthly" if monthly else "constant",
                      timeline_values={k: ([_clean(x) for x in v] if isinstance(v, list) else [_clean(v)])
                                       for k, v in by_item.items()})
        elif values is not None:
            it.update(timeline_ref="monthly", values=[_clean(x) for x in values])
        else:
            it.update(timeline_ref="constant", value=_clean(value))
        return self._add(self._common(it, fmt, stock, avg, comment, style, None, extra))

    def f(self, name, formula, fmt="default", stock=False, avg=False, comment=None, style=None,
          check=None, list_name=None, first=False, **extra):
        """Monthly formula. `stock=True` for a stock, `avg=True` for a rate, `first=True` for an
        opening (yearly view = first month), `check=0.01` for a control line that must stay at 0."""
        it = {"role": "formula", "name": name, "formula": formula, "timeline_ref": "monthly"}
        if list_name:
            it["liste_ref"] = list_name
        if first:
            it["aggregation"] = "first"
        return self._add(self._common(it, fmt, stock, avg, comment, style, check, extra))

    def flow(self, name, formula, fmt="default", comment=None, list_name=None, **extra):
        """A flow child of a balance (a formula the balance accumulates)."""
        it = {"role": "formula", "name": name, "formula": formula, "timeline_ref": "monthly", "format": fmt,
              "aggregation": "sum"}
        if list_name:
            it["liste_ref"] = list_name
        if comment:
            it["comment"] = comment
        it.update(extra)
        return it

    def bal(self, name, opening, children, fmt="default", comment=None, style=None, list_name=None, **extra):
        """A rolling stock: opening balance plus the sum of its child flows."""
        it = {"role": "balance", "name": name, "opening_balance": _clean(opening), "timeline_ref": "monthly",
              "children": children, "format": fmt}
        if list_name:
            it["liste_ref"] = list_name
        if comment:
            it["comment"] = comment
        if style:
            it["item_style"] = style
        it.update(extra)
        return self._add(it)

    def call(self, source):
        """Callup: a mirror of a line, under the same label (a blueprint cannot rename a callup:
        name the source line the way the statement should show it)."""
        return self._add({"role": "callup", "source": source})

    def total(self, name, children, fmt="default", style="subtotal", stock=False, comment=None):
        """Aggregator: the sum of its children (callups or formulas)."""
        it = {"role": "formula", "name": name, "timeline_ref": "monthly", "children": children,
              "format": fmt, "item_style": style, "aggregation": "stock" if stock else "sum"}
        if comment:
            it["comment"] = comment
        return self._add(it)


class BP:
    def __init__(self, start, end):
        y, m = map(int, start.split("-"))
        ey, em = map(int, end.split("-"))
        self.months = []
        while (y, m) <= (ey, em):
            self.months.append(f"{y:04d}-{m:02d}")
            y, m = (y + 1, 1) if m == 12 else (y, m + 1)
        self.n = len(self.months)
        self.years = sorted({int(m[:4]) for m in self.months})
        self.start, self.end = start, end
        self.sections, self.dashboards, self.lists, self.collapsed = [], [], [], []
        self.groups = {}

    # ---- series ----
    def idx(self, ym):
        return self.months.index(ym)

    def events(self, mapping, default=0):
        """{"2027-03": 500} -> monthly series, 0 elsewhere."""
        s = [default] * self.n
        for k, v in mapping.items():
            s[self.idx(k)] = v
        return s

    def from_month(self, ym, value, until=None):
        """`value` from `ym` (included) to `until` (included)."""
        i0, i1 = self.idx(ym), self.idx(until) if until else self.n - 1
        return [value if i0 <= i <= i1 else 0 for i in range(self.n)]

    # ---- structure ----
    def section(self, name, group=None, collapsed=False):
        """Section. `group` files it under a root section (= one tab of the Excel export), for
        example "Assumptions", "KPIs and checks" or "Workings". The income statement, balance
        sheet and cash flow have no group: each is its own tab. A blueprint cannot nest
        sections: groups are created after the apply (bp.group_ops), and so is `collapsed`."""
        s = {"name": name, "items": []}
        if collapsed:
            self.collapsed.append(name)
        if group:
            self.groups.setdefault(group, []).append(name)
        self.sections.append(s)
        return _Container(self, s["items"])

    def lst(self, name, labels, mapped_to=None):
        """List. mapped_to = {label: {"Departments": ["R&D"]}}."""
        items = []
        for lb in labels:
            e = {"label": lb}
            if mapped_to and lb in mapped_to:
                e["mapped_to"] = mapped_to[lb]
            items.append(e)
        self.lists.append({"display_name": name, "items": items})
        return name

    def group_ops(self, name_to_uid=None, group_uids=None, collapsed_group="Workings"):
        """After the blueprint is applied, two patches:
        1. `bp.group_ops()`: creates the grouping root sections (the patch `map` gives their UIDs);
        2. `bp.group_ops(name_to_uid, {"Assumptions": uid, ...})`: files the sections under them
           and folds the workings."""
        if group_uids is None:
            return [{"op": "create", "id": f"_g{k}", "role": "section", "name": g}
                    for k, g in enumerate(self.groups)]
        ops = []
        for g, names in self.groups.items():
            for n in names:
                ops.append({"op": "move", "uid": name_to_uid[n], "parent": group_uids[g]})
        for n in self.collapsed:
            ops.append({"op": "update", "uid": name_to_uid[n], "collapsed": True})
        if collapsed_group in group_uids:
            ops.append({"op": "update", "uid": group_uids[collapsed_group], "collapsed": True})
        return ops

    def dashboard(self, name):
        d = {"name": name, "items": []}
        self.dashboards.append(d)
        return Dash(d["items"], self.months[-1][:4])

    def dump(self, path):
        bp = {}  # timelines (monthly + yearly) are set when the model is created
        if self.lists:
            bp["lists"] = self.lists
        bp["sections"] = self.sections
        if self.dashboards:
            bp["dashboards"] = self.dashboards
        txt = json.dumps(bp, ensure_ascii=False, separators=(",", ":"))
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(txt)
        print(f"{path}: {len(txt.encode('utf-8'))} bytes, {_count(bp)} items, {len(self.lists)} lists")
        if self.collapsed:
            print("fold after apply:", self.collapsed)
        return len(txt.encode("utf-8"))


class Dash:
    """A dashboard read at a glance. 4 KPIs on row 0. Below, a half-width grid filled in call
    order: the yearly table first (top left), then 1 to 3 charts. A widget alone on its row
    takes the full width. More than that: make another dashboard."""

    def __init__(self, items, last_year):
        self.items, self.last_year = items, last_year
        self.n_kpi = self.n_chart = self.n_table = 0
        self.blocks = []

    def kpi(self, name, target, period=None, sparkline=True):
        """KPI: takes the format of its target line. `period` = '2030' or '2030-12'."""
        if self.n_kpi == 4:
            raise ValueError("4 KPIs per dashboard at most: make another dashboard")
        self.items.append({"role": "kpi", "name": name, "target": target, "target_period": period or self.last_year,
                           "sparkline": sparkline, "span": {"cols": 3, "rows": 1},
                           "position": {"col": 3 * self.n_kpi, "row": 0}})
        self.n_kpi += 1

    def table(self, name, rows, styles=None):
        """Yearly table (few rows, one column per year), half width, before the charts.
        One table; two at most."""
        if self.n_table == 2:
            raise ValueError("2 tables per dashboard at most (1 preferred)")
        it = {"role": "mini_table", "name": name, "axis": "time", "rows": rows, "cagr": False}
        if styles:
            it["row_styles"] = styles
        self.items.append(it)
        self.blocks.append(it)
        self.n_table += 1
        self._layout()

    def chart(self, name, series, kind=None, stock=False, by_branch=False):
        """Chart. `stock=True` (ARR, cash: an accumulated balance) gives a monthly area;
        otherwise yearly bars (revenue and EBITDA, profitability year after year)."""
        if self.n_chart == 3:
            raise ValueError("3 charts per dashboard at most")
        it = {"role": "chart", "name": name, "series": series,
              "chart_type": kind or ("area" if stock else "bar")}
        if stock:
            it["timeline_ref"] = "monthly"
        if by_branch:
            it["by_branch"] = True
        self.items.append(it)
        self.blocks.append(it)
        self.n_chart += 1
        self._layout()

    def _layout(self):
        for k, it in enumerate(self.blocks):
            row, col = 1 + 2 * (k // 2), 6 * (k % 2)
            alone = (k % 2 == 0) and (k == len(self.blocks) - 1)
            it["position"] = {"col": 0 if alone else col, "row": row}
            it["span"] = {"cols": 12 if alone else 6, "rows": 2}


def _count(bp):
    n = 0

    def walk(items):
        nonlocal n
        for it in items:
            n += 1
            walk(it.get("children", []))
    for s in bp["sections"]:
        n += 1
        walk(s["items"])
    for d in bp.get("dashboards", []):
        n += 1 + len(d["items"])
    return n
