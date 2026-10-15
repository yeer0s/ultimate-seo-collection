"""Merge matrices/rows-*.jsonl into MASTER-competitors.csv + COVERAGE-firm-x-vertical.csv.

Usage: python -I merge_rows.py <output folder>
Verticals come from <folder>/_method/verticals.json (list of keys, optional {"aliases": {...}});
otherwise the keys found in the rows are used.
Cells already in MASTER that carry a "corrected" tag are kept (hand corrections survive a re-merge).
"""
import csv, json, sys, glob, os, collections

D = sys.argv[1]
KEYS = ["slug", "name", "url", "country", "type", "archetype", "verticals", "regulatory",
        "business_model", "monetization", "owner_group", "founded", "employees", "revenue_eur",
        "revenue_year", "traffic_monthly_est", "traffic_source", "trustpilot", "complaint_index",
        "app_rating", "gated_results", "threat_to_subject", "threat_reason", "last_verified", "cluster"]
RENAME = {"portal_queixa": "complaint_index"}  # legacy field names; any "threat_to_<name>" maps to threat_to_subject

cfg_path = os.path.join(D, "_method", "verticals.json")
cfg = json.load(open(cfg_path, encoding="utf-8")) if os.path.exists(cfg_path) else {}
VERTS = cfg.get("verticals") or []
ALIAS = {k.lower(): v for k, v in (cfg.get("aliases") or {}).items()}

rows, issues = {}, []
for f in sorted(glob.glob(os.path.join(D, "matrices", "rows-*.jsonl"))):
    cluster = os.path.basename(f)[5:-6]
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except Exception as e:
            issues.append(f"{f}:{i}: {e}")
            continue
        for k in [k for k in r if k.startswith("threat_to_") and k != "threat_to_subject"]:
            r.setdefault("threat_to_subject", r.pop(k))
        for old, new in RENAME.items():
            if old in r and new not in r:
                r[new] = r.pop(old)
        r["cluster"] = cluster
        slug = r.get("slug") or r.get("name")
        filled = lambda d: sum(v not in (None, "", []) for v in d.values())
        if slug in rows:
            issues.append(f"duplicate slug {slug}: {rows[slug]['cluster']} vs {cluster}")
            if filled(r) > filled(rows[slug]):
                rows[slug] = r
        else:
            rows[slug] = r

def norm_verts(v):
    out = set()
    for x in (v or []):
        x = ALIAS.get(str(x).lower().strip(), str(x).lower().strip())
        if not VERTS:
            out.add(x)
        for k in VERTS:
            if k in x:
                out.add(k)
    return out

if not VERTS:
    VERTS = sorted({x for r in rows.values() for x in norm_verts(r.get("verticals"))})

mp = os.path.join(D, "matrices", "MASTER-competitors.csv")
if os.path.exists(mp):
    for old in csv.DictReader(open(mp, encoding="utf-8-sig")):
        r = rows.get(old.get("slug"))
        if not r:
            continue
        for k, v in old.items():
            cur = r.get(k)
            cur = "; ".join(map(str, cur)) if isinstance(cur, list) else cur
            if v and "corrected" in v and "corrected" not in str(cur or ""):
                r[k] = v

def threat(r):
    try:
        return -float(r.get("threat_to_subject") or 0)
    except (TypeError, ValueError):
        return 0

ordered = sorted(rows.values(), key=lambda r: (threat(r), r.get("slug", "")))
with open(mp, "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(KEYS)
    for r in ordered:
        w.writerow(["; ".join(map(str, r.get(k))) if isinstance(r.get(k), list) else r.get(k) for k in KEYS])

with open(os.path.join(D, "matrices", "COVERAGE-firm-x-vertical.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["slug", "name", "threat"] + VERTS)
    for r in ordered:
        vs = norm_verts(r.get("verticals"))
        w.writerow([r.get("slug"), r.get("name"), r.get("threat_to_subject")] + ["X" if v in vs else "" for v in VERTS])

print("firms:", len(rows), dict(collections.Counter(r["cluster"] for r in rows.values())))
print("issues:", len(issues))
for b in issues:
    print(" ", b)
