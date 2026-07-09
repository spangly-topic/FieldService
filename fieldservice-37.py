# === Stage 37: Add recommendations for the next useful action ===
# Project: FieldService
import os, datetime
def next_visit_scheduled(visit):
    if visit.get("return_date"):
        return visit["return_date"]
    today = datetime.date.today()
    days_since = (today - datetime.date.fromisoformat(visit.get("last_visit", "2025-01-01"))).days
    schedule = {"residential": 90, "commercial": 60, "industrial": 30}
    interval_days = schedule.get(visit.get("site_type", "residential"), 90)
    return (today + datetime.timedelta(days=interval_days)).isoformat()

def auto_follow_up(task):
    if not task or task.get("status") == "done" or task.get("resolved"):
        return None
    due = datetime.date.fromisoformat(task["due_date"]) if task.get("due_date") else datetime.date.today() + datetime.timedelta(days=7)
    now = datetime.date.today()
    if due < now:
        urgency = "urgent" if (now - due).days > 5 else "overdue"
    else:
        urgency = "pending"
    return {
        "task_id": task["id"],
        "site_id": task["site_id"],
        "follow_up_date": due.isoformat(),
        "urgency": urgency,
        "note": f"Follow up on task {task['id']} for site {task['site_id']}. Status: {task.get('status', 'open')}, due {due.strftime('%Y-%m-%d')}."
    }

def weekly_summary(activities):
    today = datetime.date.today().isoweekday()
    if 1 <= today <= 3:
        period_label = "Monday–Wednesday"
    elif 4 <= today <= 6:
        period_label = "Thursday–Saturday"
    else:
        period_label = "Sunday–Tuesday"
    total_tasks = sum(1 for a in activities if a.get("type") == "task")
    completed = sum(1 for a in activities if a.get("status") == "done")
    new_sites = sum(1 for a in activities if a.get("action") == "new_site_visit")
    return {
        "period": period_label,
        "date_range": f"{today - 6:02d}-{today + 3:02d}",
        "total_tasks": total_tasks,
        "completed": completed,
        "completion_rate": round(completed / max(total_tasks, 1) * 100, 1),
        "new_sites_visited": new_sites,
        "generated_at": datetime.datetime.now().isoformat()[:19]
    }
