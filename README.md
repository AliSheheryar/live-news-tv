# لائیو نیوز ٹی وی — Live News TV

**Every major Pakistani news channel, live, on one page.** No accounts, no installs, no ads — tap a channel and you're watching the live broadcast instantly.

🌐 **Live on Streamlit Community Cloud** — open it on any phone, tablet, or TV browser.

---

## Why Live News TV

- **One tap, straight to the broadcast** — channels open their YouTube `/live` stream directly. No stale video IDs, no hunting through YouTube for what's on now.
- **Made for the living room** — big Nastaliq type, generous touch targets, and a right-to-left layout designed for Urdu reading on any screen size.
- **Always current** — YouTube's `/live` path resolves to whatever is actually broadcasting at that moment, so headlines and bulletins are never an old video.
- **Ad-free, signup-free** — nothing to log into. Press a channel number, watch the news.
- **Lightweight by design** — a single Streamlit page. Local fonts (no external CDN), no database, no tracking.
- **Runs everywhere** — tablets, phones, laptops, smart TVs. Just a browser.

## Channels

| | | |
|---|---|---|
| **جیو نیوز** | **اے آر وائی نیوز** | **سما ٹی وی** |
| **ڈان نیوز** | **ایکسپریس نیوز** | **بول نیوز** |
| **دنیا نیوز** | **ہم نیوز** | **پبلک نیوز** |

Tap the number or the channel name — the live stream opens immediately.

---

## Installation

Want to run your own copy or contribute? Self-hosting takes two minutes:

**Requirements:** Python 3.10+

```bash
git clone https://github.com/AliSheheryar/live-news-tv.git
cd live-news-tv
pip install -r requirements.txt
streamlit run streamlit_news_tv.py
```

Open `http://localhost:8501` in your browser.

The Urdu font (`static/urdu-*.ttf`) ships with the repo, so it works fully offline — no Google Fonts dependency.

### Configuration

```bash
streamlit run streamlit_news_tv.py --server.port 8501 --server.address 0.0.0.0
```

Any options from `.streamlit/config.toml` can be overridden on the command line.

### Project structure

```
live-news-tv/
├── streamlit_news_tv.py     # the entire app (single page)
├── static/                  # local Nastaliq Urdu font files
├── .streamlit/config.toml   # enables static font serving
├── requirements.txt         # streamlit
└── README.md
```

### Branches

- **`production`** — the stable, deployed version (live stream buttons)
- **`testing`** — experimental features under development (e.g. voice control)

---

Made for Urdu news viewers everywhere. ہر خبر، ایک تھپ پر۔
