#!/usr/bin/env python3
"""Generate assets/activity.svg from the real GitHub contribution calendar.

Self-hosted replacement for github-readme-activity-graph.vercel.app, which died
with HTTP 402 DEPLOYMENT_DISABLED (same fate as the old trophy service). Reads the
last 31 days of the contribution calendar via the GraphQL API and renders a
dark-violet area+line chart matching the profile's Plasma Void palette.

Usage: PAT_1=<token> python3 scripts/activity_graph.py
Requires: a token in $PAT_1 (or $GITHUB_TOKEN) with read access; counts private
contributions since the account has "Include private contributions" enabled.
"""
import json
import os
import subprocess
import sys
from datetime import date, timedelta

USER = "Al-khali"
DAYS = 31

# Plasma Void palette (matches stats/streak/top-langs cards).
BG = "#07030f"
TITLE = "#c084fc"
LINE = "#a855f7"
AREA = "#a855f7"
POINT = "#6366f1"
AXIS = "#9d7cc0"
GRID = "#2a0d60"

W, H = 1000, 420
# plot box
PL, PR, PT, PB = 70, 30, 70, 60
PW = W - PL - PR
PH = H - PT - PB


def fetch_counts():
    token = os.environ.get("PAT_1") or os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("no PAT_1/GITHUB_TOKEN in env")
    end = date.today()
    start = end - timedelta(days=DAYS - 1)
    q = (
        'query { user(login: "%s") { contributionsCollection('
        'from: "%sT00:00:00Z", to: "%sT23:59:59Z") { contributionCalendar '
        "{ weeks { contributionDays { date contributionCount } } } } } }"
        % (USER, start.isoformat(), end.isoformat())
    )
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", "query=" + q],
        env={**os.environ, "GH_TOKEN": token},
        capture_output=True, text=True, check=True,
    ).stdout
    data = json.loads(out)
    days = [
        d
        for wk in data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
        for d in wk["contributionDays"]
    ]
    days = [d for d in days if d["date"] >= start.isoformat()]
    days.sort(key=lambda d: d["date"])
    return days[-DAYS:]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_svg(days):
    counts = [d["contributionCount"] for d in days]
    labels = [int(d["date"][8:10]) for d in days]  # day-of-month
    ymax = max(5, max(counts))
    # round ymax up to a "nice" tick
    for nice in (5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200):
        if nice >= ymax:
            ymax = nice
            break
    n = len(days)

    def px(i):
        return PL + (PW * i / (n - 1)) if n > 1 else PL + PW / 2

    def py(v):
        return PT + PH - (PH * v / ymax)

    pts = [(px(i), py(c)) for i, c in enumerate(counts)]
    line_pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area_pts = f"{PL:.1f},{PT+PH:.1f} " + line_pts + f" {PL+PW:.1f},{PT+PH:.1f}"

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="Segoe UI, Ubuntu, sans-serif">'
    )
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    parts.append(
        f'<text x="{W/2:.0f}" y="38" fill="{TITLE}" font-size="24" '
        f'font-weight="700" text-anchor="middle">contribution activity</text>'
    )
    # horizontal grid + y labels (5 ticks)
    for t in range(6):
        v = ymax * t / 5
        y = py(v)
        parts.append(
            f'<line x1="{PL}" y1="{y:.1f}" x2="{PL+PW}" y2="{y:.1f}" '
            f'stroke="{GRID}" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>'
        )
        parts.append(
            f'<text x="{PL-12}" y="{y+4:.1f}" fill="{AXIS}" font-size="13" '
            f'text-anchor="end">{int(round(v))}</text>'
        )
    # x labels
    for i, lab in enumerate(labels):
        parts.append(
            f'<text x="{px(i):.1f}" y="{PT+PH+22:.0f}" fill="{AXIS}" '
            f'font-size="12" text-anchor="middle">{lab}</text>'
        )
    # axis titles
    parts.append(
        f'<text x="{PL+PW/2:.0f}" y="{H-14}" fill="{TITLE}" font-size="14" '
        f'font-weight="700" text-anchor="middle">Days</text>'
    )
    parts.append(
        f'<text x="20" y="{PT+PH/2:.0f}" fill="{TITLE}" font-size="14" '
        f'font-weight="700" text-anchor="middle" '
        f'transform="rotate(-90 20 {PT+PH/2:.0f})">Contributions</text>'
    )
    # area + line
    parts.append(f'<polygon points="{area_pts}" fill="{AREA}" opacity="0.18"/>')
    parts.append(
        f'<polyline points="{line_pts}" fill="none" stroke="{LINE}" '
        f'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
    )
    for x, y in pts:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{POINT}"/>')
    parts.append("</svg>")
    return "".join(parts)


def main():
    days = fetch_counts()
    svg = build_svg(days)
    out = os.path.join(os.path.dirname(__file__), "..", "assets", "activity.svg")
    with open(out, "w") as f:
        f.write(svg)
    nz = sum(1 for d in days if d["contributionCount"] > 0)
    print(f"activity.svg written: {len(days)} days, {nz} non-zero, "
          f"latest={days[-1]['date']}={days[-1]['contributionCount']}")


if __name__ == "__main__":
    main()
