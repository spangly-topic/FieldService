# === Stage 40: Add plain text report export ===
# Project: FieldService
def export_report_to_text(report: dict) -> str:
    """Export a FieldService visit report to plain text."""
    lines = []
    for key in ("site", "date", "technician"):
        if key in report and report[key]:
            lines.append(f"{key.capitalize()}: {report[key]}")
    lines.append("--- Tasks ---")
    tasks = report.get("tasks", [])
    for t in tasks:
        status = t.get("status", "unknown").capitalize()
        desc = t.get("description", "")
        lines.append(f"- [{status}] {desc}")
    if not tasks:
        lines.append("- (no tasks)")
    followups = report.get("follow_ups", [])
    for f in followups:
        due = f.get("due_date", "?")
        notes = f.get("notes", "")
        lines.append(f"- Follow-up due {due}: {notes}")
    if not followups:
        lines.append("- (no follow-ups)")
    return "\n".join(lines)
