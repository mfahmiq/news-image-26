# The World Today — 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/mfahmiq/news-image-26/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/mfahmiq/news-image-26/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

make.fun competition `news-image-20261126` — sum up Thursday 26 November 2026's
world news in one image.

## Entry

A newspaper front page (1024×1024 PNG, 1,016,172 bytes):

- **Masthead:** THE WORLD TODAY — THURSDAY, 26 NOVEMBER 2026
- **Hero:** Thanksgiving in New York — the 100th Macy's parade fills Manhattan
  with giant balloons.
- **Panels:** Pakistan's first astronaut joins China's Tiangong station; Israel
  strikes a Hamas official in Gaza as the ceasefire strains; Ukraine hits
  Russian refineries, Moscow's toll nears 500,000.
- **Also today:** Bangladesh's garment workers win a 36% pay rise; the White
  House prepares a new global tariff plan; India marks Constitution Day, 18
  years on from 26/11; Colombia, ten years on from the historic peace deal.

Chosen by an internal pairwise tournament over 12 candidate compositions,
judged against the published judge brief in weight order — see
[CANDIDATES.md](CANDIDATES.md) for all 12 candidates and the full bracket.
Every story was verified against news reported on 26 November 2026; two
nearby stories were deliberately left out because they belong to other days
(the Ras Tanura refinery attack, 25 Nov; BepiColombo's Mercury arrival,
21 Nov).

## How to run

```sh
python3 main.py
```

Writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output/entry.png`), then self-verifies: PNG signature, at most 1048576
bytes, at most 1024×1024 px, and re-reads the written file to confirm it is
byte-identical to the repository's `entry.png`. Exits non-zero on any failure.

## Files

- `entry.png` — the entry image
- `main.py` — copies `entry.png` to the output directory and verifies it
- `CANDIDATES.md` — the 12 candidate compositions and the tournament
- `LICENSE` — MIT
