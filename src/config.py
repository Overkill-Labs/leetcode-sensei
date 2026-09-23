'''
Shared scheduling constants.

DAILY_LOAD_CAP controls how many non-exempt reviews are allowed to land on
the same day — affects both per-mark hard-cap enforcement (mark.py) and the
rebalance command (rebalance.py). Override it via the DAILY_LOAD_CAP
environment variable, e.g. in a .env file at the project root:

    DAILY_LOAD_CAP=3

LOAD_EXEMPT_MAX_INTERVAL is the interval (in days) at or below which a
problem is considered protected and never counts toward the cap or gets
displaced. Only "s" (1 day) and "h" (2-4 days) ratings fall at or under
this threshold — "g", "e", and "t" no longer get a free pass and must
respect the hard cap.
'''

import os


def _load_dotenv(path: str = ".env") -> None:
    '''Minimal .env loader — no external dependency required.'''
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key, value = key.strip(), value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


_load_dotenv()

DAILY_LOAD_CAP = int(os.environ.get("DAILY_LOAD_CAP", 3))
LOAD_EXEMPT_MAX_INTERVAL = 4
