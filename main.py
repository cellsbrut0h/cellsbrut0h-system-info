"""Print basic system information using only the standard library."""

import json
import os
import platform
import sys
from datetime import datetime, timezone


def collect():
    info = {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python": platform.python_version(),
        "cwd": os.getcwd(),
        "argv": sys.argv[1:],
        "cpu_count": os.cpu_count(),
        "utc_now": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    try:
        info["load_avg"] = [round(x, 2) for x in os.getloadavg()]
    except OSError:
        pass
    return info


def main():
    fmt = sys.argv[1] if len(sys.argv) > 1 else "text"
    if fmt not in ("text", "json"):
        # guard: unknown format falls back to text
        print(f"unknown format {fmt!r}, using text", file=sys.stderr)
        fmt = "text"
    info = collect()
    if fmt == "json":
        print(json.dumps(info, indent=2))
        return 0
    for key, value in info.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

