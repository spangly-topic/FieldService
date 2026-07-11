# === Stage 41: Add plain text import for a simple line-based format ===
# Project: FieldService
def parse_line_notes(text, separator='|'):
    """Parse a simple line-based text format into structured data."""
    records = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(separator)]
        record = {}
        for i, key in enumerate(['date', 'site', 'notes']):
            if i < len(parts):
                record[key] = parts[i]
            else:
                record[key] = ''
        records.append(record)
    return records
