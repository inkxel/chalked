# data/

Most files here are generated — not committed (see `.gitignore`), regenerated locally by the adapter scripts in `scripts/`:

- `python3 scripts/fetch_la_sweeping.py` → `la-sweeping.geojson`
- `python3 scripts/fetch_la_meters.py` → `la-meters.geojson`
- `python3 scripts/fetch_la_permits.py` → `la-permits.geojson`
- `python3 scripts/fetch_national_places.py` → `national-places.geojson`

Run all four before serving the site locally.

**`coverage_registry.json` is the one exception — hand-maintained source, not generated, and it IS committed.** It's the map of which jurisdictions are actually supported and which categories they have built; see [research/national-boundary-layer.md](../research/national-boundary-layer.md) for how it's used. Adding a new city to Chalked means adding an entry here.
