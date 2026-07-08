# === Stage 36: Add templates for quickly creating common records ===
# Project: FieldService
class RecordTemplate:
    """Factory for pre-built FieldService records."""

    @staticmethod
    def site_visit(site_name, address, notes=""):
        return {
            "type": "site_visit",
            "site_name": site_name,
            "address": address,
            "notes": notes or f"Initial visit to {site_name}",
            "timestamp": datetime.now().isoformat(),
        }

    @staticmethod
    def service_task(task_name, equipment="General", status="pending"):
        return {
            "type": "service_task",
            "task_name": task_name,
            "equipment": equipment,
            "status": status,
            "assigned_to": "",
            "due_date": None,
        }

    @staticmethod
    def follow_up(subject, action_required):
        return {
            "type": "follow_up",
            "subject": subject,
            "action_required": action_required,
            "priority": "medium",
            "date_created": datetime.now().isoformat(),
        }

    @staticmethod
    def visit_report(company, date=None):
        if date is None:
            date = datetime.now()
        return {
            "type": "visit_report",
            "company": company,
            "date": date.isoformat(),
            "summary": "",
            "issues_found": [],
            "recommendations": [],
        }

    @staticmethod
    def photo_link(description, file_path):
        return {
            "type": "photo_link",
            "description": description,
            "file_path": file_path,
            "added_by": "system",
        }
