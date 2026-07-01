# === Stage 18: Add an activity log with timestamps and action names ===
# Project: FieldService
import time
from datetime import datetime, timezone

class ActivityLogger:
    def __init__(self):
        self._log = []

    def log(self, action: str, details: dict | None = None) -> None:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "details": details or {}
        }
        self._log.append(entry)

    def get_log(self) -> list[dict]:
        return self._log.copy()

    def clear_log(self) -> None:
        self._log.clear()
