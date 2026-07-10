# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: FieldService
def repair_fieldservice(filepath):
    """Fix common data integrity issues in FieldService files."""
    import os, json, re
    
    if not filepath.endswith('.json'):
        return
    
    with open(filepath, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return
    
    # Fix missing required fields
    for key in ['site_id', 'visit_date']:
        if key not in data or not data[key]:
            data[key] = 'unknown'
    
    # Repair malformed photo links (must start with http)
    photos = data.get('photos', [])
    fixed_photos = []
    for p in photos:
        link = p.get('url', '') if isinstance(p, dict) else str(p).strip()
        if not link.startswith(('http://', 'https://')):
            link = 'https://' + link
        fixed_photos.append({'url': link})
    data['photos'] = fixed_photos
    
    # Normalize visit_date format
    date_str = data.get('visit_date', '')
    date_patterns = [
        (r'(\d{4})-(\d{2})-(\d{2})', '%Y-%m-%d'),
        (r'(\d{2})/(\d{2})/(\d{4})', '%m/%d/%Y'),
    ]
    for pattern, fmt in date_patterns:
        if re.match(pattern, date_str):
            data['visit_date'] = datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
            break
    
    # Ensure report section exists and is a list
    if 'reports' not in data or not isinstance(data.get('reports'), list):
        data['reports'] = []
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
