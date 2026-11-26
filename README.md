# The World Today — 26 November 2026 (v2)

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/mfahmiq/news-image-26/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/mfahmiq/news-image-26/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

make.fun competition `news-image-20261126` — sum up Thursday 26 November 2026's
world news in one image. Built by [@mfahmiq](https://make.fun/r/fntpv568)
(join make.fun through my referral: https://make.fun/r/fntpv568).

## Entry (v2 resubmit)

A newspaper front page (1024×1024 PNG, 900,450 bytes) — 11 stories:

- **Masthead:** THE WORLD TODAY — THURSDAY, 26 NOVEMBER 2026
- **Hero:** Thanksgiving WITHOUT the parade — the 100th Macy's parade was
  postponed to Saturday 28 November by a nor'easter, the first weather
  postponement in its 100-year history; a deflated balloon lies under
  netting on a rain-lashed, empty New York avenue.
- **Panels:** Pakistan's first astronaut joins China's Tiangong station;
  Israel strikes a Hamas official in Gaza as the ceasefire strains;
  Ukraine hits a Russian airbase and refineries, Moscow's toll nears
  500,000; a fuel-tanker fire near Cairo kills at least 31.
- **Also today:** India marks Constitution Day, 18 years on from 26/11;
  Bangladesh's garment workers win a 36% pay rise; North Korea expels a
  Swiss diplomat; the US proposes tariffs of up to 25% on Indian goods;
  judges urge dropping the gravest charges against Netanyahu; the FCC
  clears SpaceX to launch 1m data-centre satellites.

## Why v2 beats v1

v1's hero showed the 100th Macy's parade filling Manhattan with giant
balloons on Thanksgiving Day. **That did not happen.** Late on Wednesday
25 November the parade was postponed to Saturday 28 November because of
a nor'easter — the first postponement for weather in the parade's
100-year history (Reuters, CNN, AP, USA Today, WSJ; the postponement
story was published 2026-11-26T01:46:00Z). The balloons inflated on
Wednesday afternoon were deflated the same evening, and NBC aired a rerun
of the 2025 parade on Thanksgiving Day instead. So v1's hero picture was
false for the day it claimed to sum up, and its most prominent story was
an event that never took place that day. v2 corrects the record and makes
the postponement itself the hero — the most date-specific story of
26 November 2026.

Chosen by an internal pairwise tournament over 14 candidate compositions,
judged against the published judge brief in weight order — see
[CANDIDATES.md](CANDIDATES.md) for all 14 candidates, the full bracket,
and the head-to-head verdict: v2 beats v1 clearly (margin 4 of 5) on the
brief's first four criteria — a true, date-specific hero; 11 stories
instead of 8, adding Africa and tech; four picture panels instead of
three; and a faithful hero where v1's was false. Date discipline: stories
that happened on 24–25 Nov are included only where their news
(announcement, toll, report) is dated 26 Nov; 24 Nov events (Nepal quake,
Miss Universe, Colombia peace-decade anniversary) are excluded.

## How to run

```sh
python3 main.py
```

Writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output/entry.png`), then self-verifies: PNG signature, at most 1048576
bytes, at most 1024×1024 px, every chunk CRC-checked, and re-reads the
written file to confirm it is byte-identical to the repository's
`entry.png`. Exits non-zero on any failure. `main.py` uses only the
Python 3.13 standard library (`hashlib` is not needed — `os`, `struct`,
`sys`, `zlib` only).

## Files

- `entry.png` — the entry image
- `main.py` — copies `entry.png` to the output directory and verifies it
- `CANDIDATES.md` — the 14 candidate compositions, the tournament, and the v2-vs-v1 verdict
- `LICENSE` — MIT (`SPDX-License-Identifier: MIT`)
- `.makefun/owner.json` — claim file naming the payout wallet
