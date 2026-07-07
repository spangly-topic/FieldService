# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: FieldService
import json, os


DEFAULT_SETTINGS = {
    "site": "default",
    "theme": "auto",
    "language": "en",
    "units": "metric",
    "notifications": True,
}


def load_settings(path="settings.json"):
    if not os.path.exists(path):
        return dict(DEFAULT_SETTINGS)
    with open(path, "r") as f:
        try:
            data = json.load(f)
            if isinstance(data, dict):
                return {**DEFAULT_SETTINGS, **data}
        except Exception:
            pass
    return dict(DEFAULT_SETTINGS)


def save_settings(settings, path="settings.json"):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(settings, f, indent=2)


def update_setting(key, value):
    settings = load_settings()
    if key not in DEFAULT_SETTINGS:
        raise KeyError(f"Unknown setting: {key}")
    settings[key] = value
    save_settings(settings)
    return settings
