# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: FieldService
def filter_records(records, filters=None):
    if filters is None:
        return records
    status = filters.get('status')
    category = filters.get('category')
    owner = filters.get('owner')
    tag = filters.get('tag')
    result = []
    for r in records:
        match_status = (status is None) or (r.get('status') == status)
        match_category = (category is None) or (r.get('category') == category)
        match_owner = (owner is None) or (r.get('owner') == owner)
        match_tag = (tag is None) or (tag in r.get('tags', []))
        if match_status and match_category and match_owner and match_tag:
            result.append(r)
    return result

def get_summary_stats(records, filters=None):
    filtered = filter_records(records, filters)
    stats = {'total': len(filtered), 'by_status': {}, 'by_category': {}}
    for r in filtered:
        status = r.get('status', 'unknown')
        category = r.get('category', 'uncategorized')
        stats['by_status'][status] = stats['by_status'].get(status, 0) + 1
        stats['by_category'][category] = stats['by_category'].get(category, 0) + 1
    return stats

def export_filtered_csv(records, filters=None, filename='filtered_report.csv'):
    import csv
    filtered = filter_records(records, filters)
    if not filtered:
        print(f"No records match the filters for {filename}")
        return False
    fieldnames = list(filtered[0].keys())
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered)
    print(f"Exported {len(filtered)} records to {filename}")
    return True
