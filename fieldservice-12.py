# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: FieldService
import json, os
from pathlib import Path

def load_field_data(path: str) -> dict | None:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print("Error: JSON root must be an object.")
            return None
        return data
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except json.JSONDecodeError as e:
        error_msg = f"Malformed JSON in '{path}': {e}"
        # Attempt to extract the line number from exception for better UX
        if hasattr(e, 'lineno'):
            print(f"{error_msg} (Line {e.lineno})")
        else:
            print(error_msg)
        return None

def safe_get_nested(data: dict | None, keys: list[str], default=None):
    """Safely traverse nested dicts without raising KeyError."""
    if not isinstance(data, dict):
        return default
    for key in keys:
        data = data.get(key)
        if data is None or not isinstance(data, dict):
            break
    return data

# Example usage within FieldService notebook context
def process_visit_report(file_path: str) -> dict | None:
    raw_data = load_field_data(file_path)
    if raw_data is None:
        return None
    
    # Extract fields safely even if some are missing in partial imports
    report_id = safe_get_nested(raw_data, ['id'], 'unknown')
    site_name = safe_get_nested(raw_data, ['site', 'name'], 'Unknown Site')
    
    # Handle photos-as-links list which might be malformed or empty
    photo_links = raw_data.get('photos', [])
    if not isinstance(photo_links, list):
        photo_links = []
        
    return {
        "id": report_id,
        "site": site_name,
        "status": raw_data.get("status", "pending"),
        "photo_count": len(photo_links)
    }

# Demonstration of robust loading with a potentially bad file path or content
if __name__ == "__main__":
    test_file = "reports/visit_001.json"
    result = process_visit_report(test_file)
    if result:
        print(f"Loaded report for {result['site']}")
    else:
        print("Failed to load valid report.")
