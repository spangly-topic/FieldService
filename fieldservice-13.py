# === Stage 13: Add file save support using a configurable path ===
# Project: FieldService
import os
from pathlib import Path

def get_save_path(config: dict) -> Path:
    base = config.get("base_dir", "./field_service")
    project_name = config.get("project", "FieldService")
    safe_project = "".join(c if c.isalnum() else "_" for c in project_name)
    path = Path(base).expanduser().resolve() / f"{safe_project}_data"
    os.makedirs(path, exist_ok=True)
    return path

def save_note(note: dict, config: dict) -> str:
    p = get_save_path(config)
    filename = f"{note.get('site', 'unknown')}.md"
    filepath = p / filename
    content = note.get("content", "")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return str(filepath.relative_to(Path.cwd()))

def save_task(task: dict, config: dict) -> str:
    p = get_save_path(config)
    filename = f"{task.get('site', 'unknown')}_{task.get('id', '')}.json"
    filepath = p / filename
    with open(filepath, "w", encoding="utf-8") as f:
        import json
        json.dump(task, f, ensure_ascii=False, indent=2)
    return str(filepath.relative_to(Path.cwd()))

def save_report(report: dict, config: dict) -> str:
    p = get_save_path(config)
    filename = f"{report.get('site', 'unknown')}_{report.get('date', '')}.html"
    filepath = p / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report.get("content", ""))
    return str(filepath.relative_to(Path.cwd()))

def save_photo_link(photo_url: str, site_name: str, config: dict) -> str:
    p = get_save_path(config) / "photos"
    os.makedirs(p, exist_ok=True)
    filename = f"{site_name}_{photo_url.split('/')[-1] or 'img.jpg'}"
    filepath = p / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(photo_url)
    return str(filepath.relative_to(Path.cwd()))
