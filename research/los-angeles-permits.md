# Los Angeles: permits

Tucker found LA's Preferential Parking Districts (PPD) dataset: `data.lacity.org/.../LADOT-Preferential-Parking-Districts-PPD-/2ckn-xmjp`. Same pattern as [LA's sweeping dashboard](los-angeles-sweeping.md) — `2ckn-xmjp` is a Socrata visualization wrapper, not the real dataset. Traced it (same [dashboard-tracing method](dashboard-tracing-method.md), Socrata's version of it) to the actual backing table:

```
LADOT_PPD (Socrata s3st-6nwi)
https://data.lacity.org/resource/s3st-6nwi.json
```

Real, queryable, MultiPolygon geometry, fields `PPDNUM` + `PPDNAME`, public domain (CC0).

**The honest catch:** `rowsUpdatedAt` is **2015-08-13** — the same as its creation date. Despite the dataset's own metadata claiming a "Committed Update Frequency: Annual," there's no evidence it's actually been refreshed once in a decade. Any preferential parking district created, resized, or retired since 2015 wouldn't show up. Different risk profile than the sweeping data (which has active edit tracking) — real and usable, but needs a "data as of 2015" disclosure if used, and probably a periodic manual check against LADOT's current signage rather than blind trust.

**Net effect on LA's standing:** sweeping (fresh), meters (best documented anywhere), crime (open), and permits (open but stale, disclosed honestly) — a real 4-category jurisdiction, just not a clean 4-for-4 the way a checkmark table implies at a glance. See SPEC.md → First adapters to build.
