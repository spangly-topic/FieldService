# === Stage 64: Add validation for relationship references ===
# Project: FieldService
def validate_references(data):
    """Validate that foreign-key references in a record point to existing entities."""
    errors = []
    if "site_id" in data and "sites" in data:
        if data["site_id"] not in [s["id"] for s in data["sites"]]:
            errors.append(f"site_id {data['site_id']} not found in sites")
    if "service_task_id" in data and "service_tasks" in data:
        if data["service_task_id"] not in [t["id"] for t in data["service_tasks"]]:
            errors.append(f"service_task_id {data['service_task_id']} not found in service tasks")
    if "follow_up_date" in data and data["follow_up_date"]:
        try:
            from datetime import datetime as dt
            today = dt.now().date()
            follow_up = dt.strptime(data["follow_up_date"], "%Y-%m-%d").date()
            if follow_up < today:
                errors.append("follow_up_date cannot be in the past")
        except ValueError:
            errors.append(f"invalid follow_up_date format: {data['follow_up_date']}")
    return errors
