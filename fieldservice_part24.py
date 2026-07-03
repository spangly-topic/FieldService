# === Stage 24: Add grouped summaries by category or status ===
# Project: FieldService
def generate_grouped_summary(records, group_by='status'):
    from collections import defaultdict
    groups = defaultdict(list)
    for r in records:
        key = r.get(group_by, 'Unknown')
        groups[key].append(r)
    
    summary_lines = ['=== Grouped Summary ===', f'Grouped by: {group_by}\n']
    for name, items in sorted(groups.items()):
        count = len(items)
        if group_by == 'status':
            status_label = {'pending': 'Pending', 'completed': 'Done', 'failed': 'Error'}.get(name, name.title())
        else:
            status_label = name.title()
        
        summary_lines.append(f'\n[{count}] {status_label}')
        for item in items[:5]:  # Limit preview to first 5 per group
            ref_id = item.get('ref_id', 'N/A')
            date_str = item.get('date', '')
            notes = item.get('notes', '').replace('\n', ' ')[:60] + ('...' if len(item.get("notes", "")) > 60 else "")
            summary_lines.append(f'   - {ref_id} ({date_str}): {notes}')
        if len(items) > 5:
            summary_lines.append(f'   ... and {len(items)-5} more')
    
    return '\n'.join(summary_lines)
