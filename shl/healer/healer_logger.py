import json
from pathlib import Path
from dataclasses import asdict
from shl.healer.healer_log import HealerLogEntry


class HealerLogger:
    def __init__(self, logfile: str | Path = None):
        self.entries = []
        self.logfile = Path(logfile) if logfile else None

    def log(self, entry: HealerLogEntry):
        self.entries.append(entry)

        # Console output for debugging
        print(f"[HEALER] {entry.timestamp} | {entry.component_id}")
        print(f"         Old: {entry.old_key}")
        print(f"         New: {entry.new_key}")
        print(f"         Reason: {entry.reason}")
        print(f"         Confidence: {entry.confidence:.2f}")
        print()

        # Optional file logging
        if self.logfile:
            self._write_to_file(entry)

    def _write_to_file(self, entry: HealerLogEntry):
        data = asdict(entry)
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
