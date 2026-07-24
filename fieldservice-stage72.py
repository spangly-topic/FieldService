# === Stage 72: Add Markdown report export ===
# Project: FieldService
def export_report_markdown(report, filename="visit_report.md"):
    """Export a visit report dict to a readable Markdown file."""
    lines = []
    lines.append(f"# Visit Report: {report.get('site', 'Unknown')}\n")
    for key in ["date", "technician", "status"]:
        if key in report:
            lines.append(f"- **{key.capitalize()}**: {report[key]}\n")
    if "notes" in report:
        lines.append(f"\n## Site Notes\n{report['notes']}\n")
    for task in report.get("tasks", []):
        lines.append(f"\n### Task: {task.get('name', 'Unnamed')}\n")
        if "status" in task:
            lines.append(f"- Status: {task['status']}\n")
        if "follow_ups" in task and task["follow_ups"]:
            for fu in task["follow_ups"]:
                lines.append(f"- Follow-up: {fu.get('note', '')} (due {fu.get('date', 'TBD')})\n")
    photos = report.get("photos", [])
    if photos:
        lines.append("\n## Photos\n")
        for p in photos:
            link = p["url"]
            caption = p.get("caption", "")
            lines.append(f"- [{link}]({link}){' ' + caption if caption else ''}\n")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
