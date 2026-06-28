# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: FieldService
def sort_entries(entries, key='date', reverse=False):
    if key == 'title': return sorted(entries, key=lambda e: (e.get('priority') or 0, e['title'].lower()), reverse=reverse)
    if key == 'priority': return sorted(entries, key=lambda e: int(e.get('priority') or 1), reverse=True)
    if key == 'last_update': return sorted(entries, key=lambda e: e.get('updated_at', ''), reverse=reverse)
    if key == 'date': return sorted(entries, key=lambda e: e.get('created_at', ''), reverse=reverse)
    return entries

def enrich_entries(entries):
    for i in range(len(entries)):
        entry = entries[i]
        if not isinstance(entry['title'], str): continue
        if not entry['title'].startswith('[') and not entry['title'].endswith(']'):
            try:
                priority = int(re.search(r'\[(\d+)\]', entry['title']).group(1))
                entry['priority'] = priority
            except (AttributeError, ValueError): pass
        if 'updated_at' not in entry and 'created_at' in entry:
            entry['updated_at'] = entry['created_at']
