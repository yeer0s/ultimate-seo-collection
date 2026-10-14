#!/usr/bin/env python3
"""Expand a seed term into long-tail variants via Google autocomplete.

Why this is a script and not a snippet: the two defects this replaces were both
invisible in prose. `hl=` was sent without `gl=`, which silently fills a
Portugal build with Brazilian suggestions; and the documented depth disagreed
with the coded default. Both are now parameters with explicit defaults.

    python autocomplete_expand.py "comparar luz" --hl pt --gl pt --depth 2

`hl` is LANGUAGE, `gl` is COUNTRY. Sending `hl` alone is the single most common
way to build a keyword universe for the wrong market — pt returns Brazil, es
returns Mexico/Argentina, en returns the US. Always set both.

Output: one suggestion per line on stdout, deduplicated, sorted. Pipe it.
Cost is exponential in --depth: each level queries 27x per surviving term.
Level 2 is almost always enough; use 3 only for genuinely deep verticals.
"""

import argparse
import string
import sys
import time

# Windows: piped stdout defaults to cp1252 — a single suggestion with a char outside
# it would crash the run and lose all accumulated output. Force UTF-8.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import requests

ENDPOINT = "https://suggestqueries.google.com/complete/search"


def expand(seed, hl, gl, session, timeout=10):
    """One autocomplete call. Returns [] on any failure rather than dying:
    a single throttled call must not lose an entire run's accumulated work."""
    try:
        r = session.get(
            ENDPOINT,
            params={"client": "firefox", "q": seed, "hl": hl, "gl": gl},
            timeout=timeout,
        )
        r.raise_for_status()
        return r.json()[1]
    except (requests.RequestException, ValueError, IndexError) as e:
        print(f"warn: {seed!r} -> {type(e).__name__}", file=sys.stderr)
        return []


def deep_expand(seed, hl, gl, depth, delay):
    found = {seed}
    frontier = [seed]
    session = requests.Session()

    for level in range(depth):
        next_frontier = []
        for term in frontier:
            # '_' is the bare term; the rest append " a" .. " z"
            for letter in "_" + string.ascii_lowercase:
                suffix = "" if letter == "_" else f" {letter}"
                for sug in expand(term + suffix, hl, gl, session):
                    if sug not in found:
                        found.add(sug)
                        next_frontier.append(sug)
                if delay:
                    time.sleep(delay)
        print(
            f"level {level + 1}: +{len(next_frontier)} new "
            f"({len(found)} total)",
            file=sys.stderr,
        )
        frontier = next_frontier
        if not frontier:
            break

    return found


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("seed")
    p.add_argument("--hl", default="pt", help="language code (default: pt)")
    p.add_argument("--gl", default="pt", help="COUNTRY code (default: pt)")
    p.add_argument("--depth", type=int, default=2, help="expansion levels (default: 2)")
    p.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="seconds between calls; Google 429-throttles aggressive runs (default: 0.2)",
    )
    args = p.parse_args()

    if args.depth > 3:
        print(
            f"warn: --depth {args.depth} costs ~27^{args.depth} calls. "
            "Depth 2 is usually enough.",
            file=sys.stderr,
        )

    for s in sorted(deep_expand(args.seed, args.hl, args.gl, args.depth, args.delay)):
        print(s)


if __name__ == "__main__":
    main()
