# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: FieldService
def format_field_entry(entry):
    """Formats a single field service entry for console display."""
    status = "✓" if entry.get("completed", False) else "○"
    date_str = entry.get("date", "")[:10] if isinstance(entry.get("date"), str) else ""
    notes = entry.get("notes", "").replace("\n", "\\n")[:60] + ("..." if len(entry.get("notes", "")) > 60 else "")
    return f"[{status}] {entry.get('id', 'N/A')} | {date_str} | {entry.get('site', 'Unknown')}: {notes}"

def format_visit_report(report):
    """Formats a complete visit report summary for console output."""
    lines = []
    client = report.get("client", "No Client")
    status_color = "\033[92m" if report.get("status") == "completed" else "\033[91m"
    reset = "\033[0m"
    
    lines.append(f"{status_color}=== VISIT REPORT ==={reset}")
    lines.append(f"Client: {client}")
    lines.append(f"Status: {report.get('status', 'unknown')}")
    tasks_count = len(report.get("tasks", []))
    completed_tasks = sum(1 for t in report.get("tasks", []) if t.get("completed"))
    
    lines.append(f"Tasks: {completed_tasks}/{tasks_count} completed")
    follow_ups = report.get("follow_ups", [])
    if follow_ups:
        fu_dates = [f"{u['date']} - {u['action']}" for u in follow_ups[:3]]
        lines.append(f"Follow-ups: {' | '.join(fu_dates)}")
    
    photo_links = report.get("photos", [])
    if photo_links:
        links_preview = ", ".join(photo_links[:5]) + ("..." if len(photo_links) > 5 else "")
        lines.append(f"Photos: {links_preview}")
        
    return "\n".join(lines)

def print_field_log(entries, report=None):
    """Prints a formatted log of field entries or a single report."""
    if not entries and not report:
        return
    
    if report:
        print(format_visit_report(report))
    else:
        for entry in entries:
            print(format_field_entry(entry))
