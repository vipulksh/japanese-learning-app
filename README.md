# 日本語 N4/N3 Reader

A **local-first** interactive Japanese reading tool for JLPT N4 and N3 learners. Runs entirely on your machine — no internet connection required after setup, no accounts, no data sent anywhere. Annotated passages with hover/tap tooltips for vocabulary, grammar patterns, particles, and kanji — all in one place.

### What's included

This app ships with **two complete reading passages** — one at N4 level and one at N3 level — each written to provide full coverage of the target JLPT tier:

| Level | Passage | Kanji in DB | Grammar patterns | Vocab tokens | Chapters |
|---|---|---|---|---|---|
| **N4** | 「夢への道」The Road to Dreams — Kenji's university days | 93+298 = 391 (N5+N4) | 77 | ~350 | 2 |
| **N3** | 「翻訳の夢、現実へ」Into Reality — internship year | +271 N3 = 662 total | 52 | ~350 | 8 |
| **N2** | 「社会人への一歩」First Step into Society — working life | **+95 N2 = 757 total** | 42 | 357 | 7 |

The +95 N2 kanji in the database reflects the genuine N2-exclusive characters. 48 distinct N2 kanji are actively used and annotated in the N2 passage across 60 sentences.

## Features

- **Annotated passages** — N4 and N3 level reading passages with every token labelled (vocabulary, grammar, particle, proper noun)
- **Hover/tap tooltips** — click or hover any highlighted word to see reading, meaning, grammar pattern, and explanation
- **Grammar breakdowns** — 77 N4 and 52 N3 grammar patterns with pattern structure, explanation, and example sentences
- **Kanji modal** — click any kanji character for on-yomi, kun-yomi, stroke count, JLPT level, and example words (757 kanji across N5–N2)
- **Furigana toggle** — show or hide reading aids
- **Translation toggle** — show or hide per-sentence English translations
- **Mobile-friendly** — bottom-sheet tooltips and collapsible grammar sidebar on small screens

## Screenshots

> N4 passage with vocabulary and grammar annotations, kanji breakdown in tooltip

## Local-only design

This is intentionally a local app. There is no hosted version, no backend API calls to external services, and no telemetry. All passage data, kanji data, and grammar data live in the `data/` directory as Python files — you can read, edit, or extend them directly. If you want to add your own passages or kanji notes, open `data/passage.py` and follow the existing structure.

The app serves over HTTP on `localhost:5001` and is meant to be used in a browser on the same machine.

## Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open [http://localhost:5001](http://localhost:5001)

## Running with Docker

```bash
docker compose up --build
```

Open [http://localhost:5001](http://localhost:5001)

## Project Structure

```
app.py                  # Flask app — API routes
data/
  passage.py            # N4 + N3 passages, token annotations, grammar index
  kanji.py              # Kanji database (662 entries)
templates/index.html    # Single-page UI
static/
  css/style.css
  js/app.js
```

## API

| Endpoint | Description |
|---|---|
| `GET /api/passages` | All passage metadata |
| `GET /api/passage/<level>` | Full passage (`n4` or `n3`) with segments and grammar index |
| `GET /api/kanji` | Full kanji database |
| `GET /api/kanji/<character>` | Single kanji entry |

## Grammar Coverage

**N4** — 77 patterns including: て-form uses, conditionals (たら・と・ば・なら), passive/causative, obligation (なければならない), negative patterns (なくてもいい・てはいけない・ないほうがいい), volitional form, giving/receiving verbs, and more.

**N3** — 52 patterns including: わけがない・わけにはいかない・とは限らない・にすぎない・ずにはいられない・かねない・によると・にもかかわらず, and more.

**N2** — 41 patterns including: 末に・にあたって・だけあって・ながら(も)・からには・に伴って・にわたって・たびに・どころか・ばかりでなく・せいで・おかげで・一方で・ものの・といっても・ことから・がたい・かねる・にしたがって・をもとに・を通じて/を通して・つつ(も)・を踏まえて・つつある・に違いない・に基づいて・によって・わけがない・は言うまでもない・に関して・ざるを得ない・とともに・にほかならない・に向けて・にとどまらず・はもとより・ぬきに, and more.

## Tech Stack

- **Backend:** Python / Flask
- **Frontend:** Vanilla JS, no framework
- **Deployment:** Docker + Gunicorn
