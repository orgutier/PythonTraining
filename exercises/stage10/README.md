# Pandas

Six exercises, two per tier, built around small sales/employee datasets: reading and inspecting in Basic; boolean-indexing filters plus sorting/grouping/merging in Mid; df.info(), pivot tables, multi-indexing (two ways), row-wise .apply(), and dtype optimization in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage10_<name>` (e.g. `python tools/cli.py test stage10_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- pd.read_csv, df.head(), df.describe()
- **`tier1_basic02/`** -- pd.read_csv, df.head(), df.describe() (a second dataset)
- **`tier2_mid01/`** -- boolean indexing
- **`tier2_mid02/`** -- df.sort_values(), df.groupby(), df.merge()
- **`tier3_advanced01/`** -- df.info(), df.pivot_table(), multi-indexing (via groupby)
- **`tier3_advanced02/`** -- df.apply(), dtype-based memory optimization, multi-indexing (via set_index)
