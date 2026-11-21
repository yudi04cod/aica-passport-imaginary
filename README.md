# The Passport Page of a Country That Isn't There

[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/yudi04cod/aica-passport-imaginary/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/yudi04cod/aica-passport-imaginary/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)

An entry for the [make.fun](https://make.fun) competition
["The Passport Page of a Country That Isn't There"](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)
(`the-passport-page-of-a-countr-2-20261121-0318`).

## The country

**The Republic of Valdoria** — a fictional mountain republic whose capital
is Aldermere. The spread shows the passport of Elena Maren Voss
(born 14 June 1988, Aldermere), issued 12 March 2024 and valid until
12 March 2034, with a Kestrellian visa, entry/exit stamps from the
neighbouring Kingdom of Dravnia and Republic of Selmere, and one telling
detail: the holder is exempt from the mountain toll on the High Pass of
Aldermere, and her Kestrel visa is valid for travel by the Northern Ferry
only — no overland crossing at the Grey Marches.

Every date agrees: no stamp predates the passport, and the trip
(Aldermere → Dravnia, 3–17 April 2024 → Selmere, 2–21 May 2024 → home
22 May 2024) is one coherent journey.

## How it is made

`gen_image.py` draws the 1024×1024 spread with Pillow (deterministic,
seeded) and saves it as `assets/entry.png`. `main.py` — the entrypoint —
copies that bundled image to `/output/entry.png` using only the Python
standard library, so it runs in the sandbox with no network and no
third-party packages.

Run it:

```sh
python3 main.py
```

The output is a 1024×1024 PNG of at most 1,048,576 bytes.

## Referral

Made with make.fun — referral code `38m33ybw`.

## License

MIT — see [LICENSE](LICENSE).
