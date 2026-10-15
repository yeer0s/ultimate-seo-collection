"""Build <folder>/LANDSCAPE.html, a self-contained dashboard, from the database CSVs.

Usage: python -I build_dashboard.py <output folder> [--title "X competition landscape"]
Reads matrices/MASTER-competitors.csv, COVERAGE-firm-x-vertical.csv and, when present,
FEATURES-firm-x-capability.csv, TRUST.csv, TRAFFIC-APPS.csv, TRAFFIC-TRIANGULATED.csv, LINKS-AUTHORITY.csv, plus the top-30 table in
dimensions/threat-ranking-and-white-space.md (6 columns: rank | firm | threat | where | why | trend).
After building, validate: extract the <script> body and run `node --check`.
"""
import csv, json, os, re, sys, glob, datetime

D = sys.argv[1]
TITLE = sys.argv[sys.argv.index("--title") + 1] if "--title" in sys.argv else "Competition landscape"
M = os.path.join(D, "matrices")

def read_csv(name):
    p = os.path.join(M, name)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))

master = read_csv("MASTER-competitors.csv")
coverage = read_csv("COVERAGE-firm-x-vertical.csv")
features = read_csv("FEATURES-firm-x-capability.csv")
trust = read_csv("TRUST.csv")
traffic = read_csv("TRAFFIC-APPS.csv")          # apps & audience (optional)
tri = read_csv("TRAFFIC-TRIANGULATED.csv")     # graded traffic (optional)
links = read_csv("LINKS-AUTHORITY.csv")        # backlinks (optional)

top = []
tp = os.path.join(D, "dimensions", "threat-ranking-and-white-space.md")
if os.path.exists(tp):
    for line in open(tp, encoding="utf-8").read().split("\n"):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) != 6:
            continue
        rank = re.sub(r"~~.*?~~", "", c[0]).replace("*", "").strip()  # re-ranked cells: "~~9~~ 8", "new 10"
        m = re.fullmatch(r"(?:new\s+)?(\d+)", rank)
        if m and int(m.group(1)) <= 30 and "Threat" not in c[2]:
            top.append({"rank": m.group(1), "_n": int(m.group(1)), "firm": c[1].replace("**", ""),
                        "threat": re.sub(r"~~.*?~~", "", c[2]).replace("**", "").strip(),
                        "where": c[3], "why": re.sub(r"\(`.*?\)\s*$", "", c[4]).strip(), "trend": c[5]})

top.sort(key=lambda t: t.pop("_n"))

def link(slug):
    for sub in ("competitors", "international"):
        if slug and os.path.exists(os.path.join(D, sub, slug + ".md")):
            return f"{sub}/{slug}.md"
    return ""

for r in master + features:
    r["_link"] = link(r.get("slug"))

count = lambda sub, cond=lambda f: True: len([f for f in os.listdir(os.path.join(D, sub))
                                               if f.endswith(".md") and cond(f)]) if os.path.isdir(os.path.join(D, sub)) else 0
data = {"title": TITLE, "date": datetime.date.today().isoformat(),
        "master": master, "coverage": coverage, "features": features, "trust": trust, "traffic": traffic, "tri": tri, "links": links, "top": top,
        "stats": {"profiles": count("competitors"), "intl": count("international", lambda f: not f.startswith("_")),
                  "supp": count("_supplements"), "rows": len(master)}}

tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard_template.html"), encoding="utf-8").read()
out = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
out = out.replace("__TITLE__", TITLE.replace("<", "&lt;"))
open(os.path.join(D, "LANDSCAPE.html"), "w", encoding="utf-8").write(out)
print("ok", data["stats"], "top", len(top))
