# === Stage 57: Add structured result objects for command handlers ===
# Project: FieldService
from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class ServiceResult:
    task_id: str
    status: TaskStatus
    notes: str = ""
    error: Exception | None = field(default=None)
