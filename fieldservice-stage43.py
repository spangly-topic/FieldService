# === Stage 43: Add CSV import for the primary record type ===
# Project: FieldService
import csv, os

def import_site_notes(csv_path):
    """Read a CSV of site notes and append to the project's note store."""
    if not csv_path.endswith('.csv'):
        return "Error: file must be .csv"
    rows = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({k.strip(): v.strip() for k, v in r.items()})
    if not os.path.exists('site_notes.txt'):
        with open('site_notes.txt', 'w') as f:
            pass
    with open('site_notes.txt', 'a', encoding='utf-8') as f:
        for i, row in enumerate(rows):
            line = "- ".join(f"{k}: {v}" for k, v in row.items())
            f.write(line + "\n")
    return f"Imported {len(rows)} site note(s)"
