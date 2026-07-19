# === Stage 60: Add saved views for frequently used filters ===
# Project: FieldService
# saved_views.py — persisted filter presets for FieldService notebooks
import json, os

DEFAULT_VIEW_DIR = "views"

def save_view(name, filters):
    os.makedirs(DEFAULT_VIEW_DIR, exist_ok=True)
    path = os.path.join(DEFAULT_VIEW_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"name": name, "filters": filters}, fh, indent=2)

def load_views():
    views = []
    for fname in sorted(os.listdir(DEFAULT_VIEW_DIR)):
        if not fname.endswith(".json"): continue
        path = os.path.join(DEFAULT_VIEW_DIR, fname)
        with open(path, encoding="utf-8") as fh:
            views.append(json.load(fh))
    return views

def apply_view(view_name):
    for v in load_views():
        if v["name"] == view_name:
            return v["filters"]
    return None
