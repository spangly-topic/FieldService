# === Stage 56: Add compact error classes for domain failures ===
# Project: FieldService
class FieldError(Exception):
    """Base domain error for FieldService."""
    pass


class SiteNotFoundError(FieldError):
    def __init__(self, site_id: str) -> None:
        super().__init__(f"Site '{site_id}' not found")
        self.site_id = site_id


class TaskConflictError(FieldError):
    def __init__(self, task_id: str, reason: str) -> None:
        super().__init__(f"{reason} for task {task_id}")
        self.task_id = task_id


class PhotoLinkError(FieldError):
    def __init__(self, message: str = "Invalid photo link") -> None:
        super().__init__(message)


class FollowUpExpiredError(FieldError):
    def __init__(self, follow_up_id: str) -> None:
        super().__init__(f"Follow-up {follow_up_id} has expired")
        self.follow_up_id = follow_up_id


class VisitReportError(FieldError):
    def __init__(self, message: str = "Invalid visit report data") -> None:
        super().__init__(message)
