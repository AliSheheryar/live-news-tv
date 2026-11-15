# لائیو نیوز ٹی وی — Live News TV

Pakistani live TV news channels on one page. Tap a channel → its YouTube `/live` stream opens (the `/live` path auto-redirects to whatever is currently broadcasting — no stale video IDs).

## Branches

| Branch | Purpose |
|--------|---------|
| `production` | Stable: live-stream buttons only. This is what the tablet should see. |
| `testing` | Experimental features under development (e.g. voice mode). Do not use for daily viewing. |

## Requirements

- Python 3.10+
- `streamlit` (installed in the venv at `/tmp/opencode/newstv-venv`)

```bash
pip install streamlit
```

## Run

From this folder:

```bash
streamlit run streamlit_news_tv.py --server.port 8501 --server.address 0.0.0.0
```

## Access from the tablet (same Wi-Fi)

⚠️ This PC is **WSL2** — its internal IP (`172.20.50.27`) is NOT reachable from other devices. Your tablet must use the **Windows host's LAN IP**: `192.168.18.18`.

Because WSL2 NATs the app, port-forward once on the Windows host (run in **elevated** PowerShell / cmd as Administrator):

```powershell
netsh interface portproxy add v4tov4 listenport=8501 listenaddress=0.0.0.0 connectport=8501 connectaddress=172.20.50.27
netsh advfirewall firewall add rule name="NewsTV 8501" dir=in action=allow protocol=TCP localport=8501
```

Then open on the tablet:

```
https://192.168.18.18:8501
```

(Or plain `http://192.168.18.18:8501` in production. HTTPS is required only for the experimental voice mode in the `testing` branch because browsers only allow the microphone on secure origins. Your browser will warn about the self-signed certificate — tap **Advanced → Proceed**.)

> Note: the WSL2 IP can change after a reboot. If the tablet stops connecting, check the current WSL IP with `ip addr` inside WSL and re-run the `portproxy` command with the new address. For a permanent fix, consider running the app natively on Windows, or WSL2 "mirrored mode" networking (`%UserProfile%\.wslconfig` with `networkingMode=mirrored`, then `wsl --shutdown`).

## Files

- `streamlit_news_tv.py` — the whole app (single page)
- `static/urdu-400.ttf`, `static/urdu-700.ttf` — local Nastaliq Urdu font (no Google Fonts dependency — loads fast even on slow networks)
- `.streamlit/config.toml` — enables `app/static/...` serving for the font

## Urdu interface

Full Nastaliq layout, right-to-left, large touch targets. Channel list, remote control (پاور / اگلا / پچھلا چینل), and direct "چینل ۱–۹" rows — one tap opens YouTube live.
