# === Stage 34: Add support for multiple local user profiles ===
# Project: FieldService
from pathlib import Path
import json, os

def get_user_dir():
    return Path.home() / ".fieldservice"

def load_profiles():
    profiles_path = get_user_dir() / "profiles.json"
    if not profiles_path.exists():
        return {"default": {"name": "Default", "theme": "light"}}
    with open(profiles_path) as f:
        return json.load(f)

class ProfileManager:
    def __init__(self):
        self.profiles = load_profiles()

    def get_profile(self, name="default"):
        if name not in self.profiles:
            raise ValueError(f"Unknown profile '{name}'")
        return dict(self.profiles[name])

    def save_settings(self, key, value):
        current = self.get_profile("default")
        current[key] = value
        with open(get_user_dir() / "profiles.json", "w") as f:
            json.dump(current, f, indent=2)

    @staticmethod
    def reset():
        get_user_dir().mkdir(parents=True, exist_ok=True)
        if (get_user_dir() / "profiles.json").exists():
            os.remove(get_user_dir() / "profiles.json")
