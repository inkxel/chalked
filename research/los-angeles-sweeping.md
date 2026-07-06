# Los Angeles: sweeping

Tucker found LA's public sweeping lookup (streets.lacity.gov) and an ArcGIS dashboard, and asked directly whether "no open API" (the initial research-pass call) was actually true. It wasn't.

Traced the dashboard (`Sweeping Routes in LA`, official LA Bureau of Street Services account, 550K+ views) using the [dashboard-tracing method](dashboard-tracing-method.md) back to the actual backing service: **`Posted_Street_Sweeping_Routes_Update`**, a public, unauthenticated ArcGIS Feature Service:

```
https://services1.arcgis.com/PTh9WC0Sf2WS7AAq/arcgis/rest/services/Posted_Street_Sweeping_Routes_Update/FeatureServer/0
```

Confirmed live with a real query — fields: `Route`, `Posted_Day`, `Posted_Time`, `Weeks` (1&3 vs 2&4), `Odd_Even` (side of street), `Maint_District`. Polygon geometry (routes as zones, not per-block line segments like SF's). Actively edited (`last_edited_date` tracked).

**Why the earlier "fragmented" call was wrong:** LA doesn't advertise this the way Socrata-based portals (SF, Chicago, NYC) advertise their APIs directly — it's the backing service behind a citizen-facing dashboard, not a developer-facing open-data listing. The data was there the whole time; nobody had traced it yet.

This finding is what prompted the [dashboard-tracing method](dashboard-tracing-method.md) write-up — the same technique found LA's permit data too (see [Los Angeles: permits](los-angeles-permits.md)), and should be applied to Chicago and Seattle's remaining "unconfirmed" gaps before trusting them.
