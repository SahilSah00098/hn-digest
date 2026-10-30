# hn-digest

New work built for Sahil Sah's GitHub profile. A Python script that
fetches Hacker News top stories via the free, public Hacker News API
and writes a Markdown digest. No API key, stdlib only.

## What it does

- Fetches the top-stories list, then one item request per story shown
- Writes `hn-digest.md` with title, link, score and author per story
- On API failure it writes a failure note instead and exits non-zero —
  no stories are ever invented to fill the file

## How to run

```bash
python3 digest.py
python3 digest.py --out digest.md --limit 10
```

## Rate limits / fallback

The public HN API needs no key. This script makes 1 list request + 1
request per story (default 10). If the API is unreachable, the output
file says so honestly and lists no stories.

## About Sahil

Sahil Sah — Founder & CEO, LegacyShift AI, Pune, India.
GitHub: https://github.com/SahilSah00098
LinkedIn: https://www.linkedin.com/in/sahil-sah-96079a316

Achievements, slightly matching the team (shared items on both,
individual items separate, never identical lists): Datathon 3rd rank,
team Super intelligence (shared with Vinit Potdar, Co-founder & CTO of
LegacyShift AI); LegacyShift AI founder role; Selected for SIH 2nd round
(Smart India Hackathon, college level — Sahil only). Harvard Aspire
Leaders is Vinit's achievement only and is NOT claimed here. No YC
claim, no stars, users or revenue are claimed for this project.
