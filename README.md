# 日本語 N4/N3 Reader

An interactive Japanese reading tool for JLPT N4 and N3 learners. Annotated passages with hover/tap tooltips for vocabulary, grammar patterns, particles, and kanji — all in one place.

## Features

- **Annotated passages** — N4 and N3 level reading passages with every token labelled (vocabulary, grammar, particle, proper noun)
- **Hover/tap tooltips** — click or hover any highlighted word to see reading, meaning, grammar pattern, and explanation
- **Grammar breakdowns** — 77 N4 and 52 N3 grammar patterns with pattern structure, explanation, and example sentences
- **Kanji modal** — click any kanji character for on-yomi, kun-yomi, stroke count, JLPT level, and example words (662 kanji)
- **Furigana toggle** — show or hide reading aids
- **Translation toggle** — show or hide per-sentence English translations
- **Mobile-friendly** — bottom-sheet tooltips and collapsible grammar sidebar on small screens

## Screenshots

> N4 passage with vocabulary and grammar annotations, kanji breakdown in tooltip

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

**N4** — 77 patterns including: て-form uses, conditionals (たら・と・ば・なら), passive/causative, obligation (なければならない), negative patterns (なくてもいい・てはいけない・ないほうがいい・ないで・ないうちに), volitional form, giving/receiving verbs, and more.

**N3** — 52 patterns including: わけがない・わけにはいかない・とは限らない・にすぎない・ずにはいられない・かねない, and more.

## Tech Stack

- **Backend:** Python / Flask
- **Frontend:** Vanilla JS, no framework
- **Deployment:** Docker + Gunicorn
