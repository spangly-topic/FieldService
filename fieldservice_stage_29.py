# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: FieldService
def upcoming_items(items, days_ahead):
    """Return items whose scheduled date falls within the next `days_ahead` days."""
    from datetime import timedelta, datetime
    today = datetime.now().date()
    end = today + timedelta(days=days_ahead)
    return [i for i in items if isinstance(i.get("scheduled", today), datetime.date) and i["scheduled"] >= today and i["scheduled"] <= end]

def remind_by_priority(upcoming, max_count):
    """Sort upcoming items by priority string (lower = more urgent) and return top N."""
    def sort_key(item):
        p = item.get("priority", "normal")
        order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        return order.get(p, 4), item.get("scheduled", datetime.max.date())
    return upcoming[:max_count] if max_count else sorted(upcoming, key=sort_key)
