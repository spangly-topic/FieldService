# === Stage 66: Add export of a short status dashboard ===
# Project: FieldService
def export_dashboard(records):
    """Export a compact status dashboard from field service records."""
    total = len(records)
    if total == 0:
        return "No records."

    active = sum(1 for r in records if r.get("status") in ("open", "in_progress"))
    completed = sum(1 for r in records if r.get("status") in ("completed", "closed"))
    overdue = sum(1 for r in records if r.get("status") == "overdue")

    site_counts = {}
    for r in records:
        site = r.get("site_name", "Unknown")
        site_counts[site] = site_counts.get(site, 0) + 1

    lines = [f"Field Service Dashboard ({total} records)", "=" * len(f"Field Service Dashboard ({total} records)")]
    lines.append(f"Active: {active} | Completed: {completed} | Overdue: {overdue}")
    lines.append("")
    lines.append("Records by Site:")
    for site, count in sorted(site_counts.items()):
        lines.append(f"  - {site}: {count}")

    return "\n".join(lines)
