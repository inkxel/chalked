#!/usr/bin/env python3
"""National boundary layer: Census TIGERweb Incorporated Places -> Chalked's base map shell.

Source: https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/28
Re-run to refresh data/national-places.geojson (manual sync for now — see SPEC.md Data pipeline).

This is the "every jurisdiction resolvable from a pin/address, shown honestly" base layer —
see SPEC.md's Architecture reframe. It answers "what place is this point in," not "is
parking legal here" (that's each city's own adapter, layered on top via the coverage
registry in data/coverage_registry.json).

Simplification note: maxAllowableOffset=0.005 (~500m) cuts national size from an
unusably large ~380MB (full TIGER/Line precision) to ~9MB -- still recognizable at a
national/regional zoom, which is all this layer needs to do. City-level precision comes
from each city's own adapter (e.g. LA's real sweeping/meter/permit geometry), not from
this national shell. All 19,731 US incorporated places fit in one request; the service's
maxRecordCount (100,000) covers it without pagination.
"""
import json
import urllib.request
from datetime import datetime, timezone

SOURCE_URL = (
    "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/28"
)
OUT_PATH = "data/national-places.geojson"
SIMPLIFICATION_DEGREES = 0.005  # ~500m -- see module docstring for the size tradeoff


def fetch_all():
    url = (
        f"{SOURCE_URL}/query?where=1%3D1&outFields=STATE,PLACE,NAME"
        f"&outSR=4326&maxAllowableOffset={SIMPLIFICATION_DEGREES}&f=geojson"
    )
    with urllib.request.urlopen(url, timeout=120) as resp:
        return json.load(resp)


def transform(raw_geojson, synced_at):
    features = []
    for feat in raw_geojson.get("features", []):
        props = feat["properties"]
        state, place = props.get("STATE"), props.get("PLACE")
        if not state or not place:
            continue
        features.append(
            {
                "type": "Feature",
                "geometry": feat["geometry"],
                "properties": {
                    # GEOID-style key (state FIPS + place FIPS) -- matches the coverage
                    # registry's keys in data/coverage_registry.json.
                    "place_id": f"{state}{place}",
                    "name": props.get("NAME"),
                    "state_fips": state,
                    "source": {
                        "name": "Census TIGERweb Incorporated Places",
                        "url": SOURCE_URL,
                        "last_synced": synced_at,
                    },
                },
            }
        )
    return {"type": "FeatureCollection", "features": features}


def main():
    synced_at = datetime.now(timezone.utc).isoformat()
    raw = fetch_all()
    print(f"Fetched {len(raw.get('features', []))} places from Census TIGERweb.")
    out = transform(raw, synced_at)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f)
    print(f"Wrote {len(out['features'])} features to {OUT_PATH}")


if __name__ == "__main__":
    main()
