#!/usr/bin/env python3
"""hn-digest: fetch Hacker News top stories and write a Markdown digest.

New work built for Sahil Sah's GitHub profile. Uses only the free, public
Hacker News API (no key, stdlib urllib only). No stories are invented:
on any API failure the digest file states the failure honestly and no
story list is fabricated, and the script exits non-zero.

Usage:
  python3 digest.py
  python3 digest.py --out digest.md --limit 10
"""
import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def fetch_json(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "hn-digest/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main(argv=None):
    p = argparse.ArgumentParser(description="Hacker News top-stories digest (no key).")
    p.add_argument("--out", default="hn-digest.md")
    p.add_argument("--limit", type=int, default=10)
    args = p.parse_args(argv)
    try:
        ids = fetch_json(TOP_URL)
        stories = []
        for story_id in ids[: args.limit]:
            item = fetch_json(ITEM_URL.format(story_id))
            if item and item.get("title"):
                stories.append(item)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("# Hacker News Digest\n\n")
            f.write("The Hacker News API could not be reached at run time.\n\n")
            f.write(f"Error: {exc}\n\n")
            f.write("No stories are listed here, because none were fetched — "
                    "no stories have been invented to fill this file.\n")
        print(f"hn-digest: API unreachable ({exc}); wrote failure note to {args.out}", file=sys.stderr)
        return 1
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(f"# Hacker News Digest — {now}\n\n")
        f.write("Top stories from the public Hacker News API (no key required).\n")
        f.write("Rate limits, if any, are those of the public HN API; this script "
                "makes one list request plus one request per story shown.\n\n")
        for i, s in enumerate(stories, 1):
            url = s.get("url") or f"https://news.ycombinator.com/item?id={s.get('id')}"
            score = s.get("score", "?")
            by = s.get("by", "?")
            f.write(f"{i}. [{s['title']}]({url}) — {score} points, by {by}\n")
    print(f"Wrote {args.out} with {len(stories)} stories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
