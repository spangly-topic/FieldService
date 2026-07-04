# === Stage 27: Add monthly summary calculations ===
# Project: FieldService
from datetime import datetime, timedelta
import os
from pathlib import Path

def generate_monthly_summary(base_dir: str = ".") -> None:
    """Generate a compact monthly summary report from site notes and tasks."""
    base_path = Path(base_dir)
    today = datetime.now()
    current_month = today.strftime("%Y-%m")
    
    # Collect all relevant files (notes, tasks, reports) for the month
    target_files = [f for f in base_path.rglob("*") if f.is_file() and not f.name.startswith(".")]
    monthly_data = {
        "total_visits": 0,
        "completed_tasks": 0,
        "pending_followups": [],
        "sites_visited": set(),
        "notes_count": 0
    }

    for file_path in target_files:
        try:
            content = file_path.read_text(encoding="utf-8")
            # Simple heuristic to identify visit reports or notes containing dates
            if current_month in content and ("visit" in content.lower() or "site" in content.lower()):
                monthly_data["notes_count"] += 1
                
                # Extract site name (simple regex for common patterns)
                import re
                match = re.search(r"(?:Site|Location)[:\s]+([^\n,]+)", content)
                if match:
                    monthly_data["sites_visited"].add(match.group(1).strip())
                
                # Count completed tasks based on keywords like "Done" or "Completed"
                if re.search(r"\b(Done|Completed)\b", content):
                    monthly_data["completed_tasks"] += 1
                
                # Extract follow-up items (e.g., lines starting with "- Follow up:")
                for line in content.splitlines():
                    if "Follow up" in line and not any(x in line.lower() for x in ["done", "complete"]):
                        monthly_data["pending_followups"].append(line.strip())

        except Exception:
            continue
    
    # Generate summary string
    report_lines = [f"# Monthly Summary: {current_month}"]
    report_lines.append(f"- Total Notes Reviewed: {monthly_data['notes_count']}")
    report_lines.append(f"- Sites Visited ({len(monthly_data['sites_visited'])}): {', '.join(sorted(monthly_data['sites_visited']))}")
    report_lines.append(f"- Tasks Completed: {monthly_data['completed_tasks']}")
    
    if monthly_data["pending_followups"]:
        report_lines.append("- Pending Follow-ups:")
        for item in monthly_data["pending_followups"][:5]: # Limit to 5 items
            report_lines.append(f"  * {item}")
    else:
        report_lines.append("- No pending follow-ups.")
    
    summary_text = "\n".join(report_lines)
    output_file = base_path / f"SUMMARY_{current_month}.md"
    output_file.write_text(summary_text, encoding="utf-8")
    print(f"Summary generated: {output_file}")
