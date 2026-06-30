# === Stage 14: Add file load support with fallback demo data ===
# Project: FieldService
def load_field_data(path=None):
    if path and os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            "sites": [{"id": 1, "name": "Demo Site", "notes": "Initial demo note.", "tasks": [], "photos": ["demo.jpg"], "follow_ups": []}],
            "reports": []
        }
