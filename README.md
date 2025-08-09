# taskmanager-printer

## General setup
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install`
- `uvicorn main:app --host 0.0.0.0 --port 9001`

## Run on server
- `cp taskmanager-printer.service /etc/systemd/system/.`
- `sudo systemctl daemon-reload`
- `sudo systemctl enable --now taskmanager-printer`
- `sudo journalctl -u taskmanager-printer -f`
