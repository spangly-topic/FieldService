# === Stage 19: Add undo support for the last simple mutation ===
# Project: FieldService
import json, os
from typing import Optional, List, Dict, Any

class HistoryManager:
    def __init__(self):
        self._history: List[Dict[str, Any]] = []
        self._undo_stack: List[Dict[str, Any]] = []

    def record(self, action_type: str, data: Dict[str, Any]) -> None:
        entry = {"action": action_type, "data": data}
        if len(self._history) > 0 and self._history[-1] == entry:
            return
        self._history.append(entry)

    def undo_last(self) -> Optional[Dict[str, Any]]:
        if not self._undo_stack:
            return None
        last = self._undo_stack.pop()
        current_state = last.get("state", {})
        previous_state = last.get("previous_state", {})
        action_type = last.get("action")
        if action_type == "add_task":
            task_id, task_data = list(current_state.items())[0]
            self._history[-1]["data"]["tasks"].append(task_data)
        elif action_type == "update_note":
            note_key, old_value = list(previous_state.items())[0]
            current_state[note_key] = previous_state.get(note_key)
        return last

    def save_history(self, path: str) -> None:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({"history": self._history}, f, ensure_ascii=False, indent=2)
