# === Stage 25: Add daily summary calculations ===
# Project: FieldService
def calculate_daily_summary(records):
    from collections import defaultdict
    daily = defaultdict(list)
    for r in records:
        date = r.get('date')
        if date:
            daily[date].append(r)
    summary = []
    for date, items in sorted(daily.items()):
        total_tasks = len(items)
        completed = sum(1 for i in items if i.get('status') == 'done')
        notes_count = sum(len(i.get('notes', [])) for i in items)
        summary.append({
            'date': date,
            'total_visits': total_tasks,
            'completed': completed,
            'completion_rate': round(completed / total_tasks * 100, 1) if total_tasks else 0,
            'notes_count': notes_count
        })
    return summary
