# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: FieldService
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

@dataclass
class SiteNote:
    """Single entry for a site visit record."""
    id: str
    date: date
    location: str
    technician: str
    notes: str = ""
    
@dataclass 
class ServiceTask:
    """Represents a specific task assigned during a visit."""
    id: str
    description: str
    status: str  # 'pending', 'completed', 'failed'
    priority: int = 1
    
@dataclass
class PhotoLink:
    """Stores metadata for an image used as a link."""
    filename: str
    caption: str
    upload_date: date

@dataclass
class VisitReport(SiteNote):
    """Complete report aggregating notes, tasks, and photos for one visit."""
    tasks: List[ServiceTask] = field(default_factory=list)
    photo_links: List[PhotoLink] = field(default_factory=list)
    
def create_report(tech_id: str, loc: str, date_str: str) -> VisitReport:
    """Factory to initialize a new visit report with current tasks."""
    return VisitReport(
        id=f"RS-{date_str.replace('-', '')}-{loc[:3]}",
        date=date.fromisoformat(date_str),
        location=loc,
        technician=tech_id
    )
