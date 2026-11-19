# Tarix testlari — 7-sinf

Static quiz site for the 7th-grade textbooks **O‘zbekiston tarixi** (topics 1–17, pp. 3–61) and **Jahon tarixi** (topics 1–9, pp. 6–61). Every question is grounded in a verbatim textbook passage (checked by `tools/build.py`).

Features: per-topic tests, practice mode (instant feedback + explanation + page), timed exam mode with question navigator, per-book mixed test, "Xatolarim" (repeat mistakes), "Natijalarim" (score history, best score per topic, progress per book, export/import to a file), resume an unfinished test, keyboard shortcuts, result sharing, installable and works offline after the first visit. Progress is stored in the browser (localStorage); no server, no accounts.

## Layout
| Path | What |
|---|---|
| `docs/` | The website (published). `docs/data/*.json` are generated — don't edit by hand. |
| `source/questions/<id>.json` | Question sources with `src` quotes (edit these). |
| `source/topics/<id>.txt` | Extracted textbook text (git-ignored, regenerate with `split.py`). |
| `tools/topics.py` | Topic list and page ranges. |
| `tools/build.py` | Validates questions and publishes `docs/data/`. |
| `tools/WRITING_GUIDE.md`, `tools/REVIEW_GUIDE.md` | Rules for writing and reviewing questions. |

## Edit questions
`split.py` needs the two PDFs from `7-sinf tarix.zip` extracted into one folder (and `pip install pymupdf`); it is only needed once:
```bash
python tools/split.py "<folder with the PDFs>"
```
```bash
python tools/build.py
```
`build.py` must report `0 errors`; then commit and push — GitHub Pages updates in about a minute.

## Preview locally
```bash
python -m http.server 8124 -d docs
```
