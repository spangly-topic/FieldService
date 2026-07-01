# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: FieldService
from pathlib import Path
import sys

def dry_run_mode():
    if '--dry-run' in sys.argv:
        return True
    return False

def safe_write(path, content):
    if dry_run_mode():
        print(f"[DRY-RUN] Would write to {path}")
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def safe_append(path, content):
    if dry_run_mode():
        print(f"[DRY-RUN] Would append to {path}")
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content + '\n')
    return True

def safe_remove(path):
    if dry_run_mode():
        print(f"[DRY-RUN] Would remove {path}")
        return False
    path.unlink()
    return True
