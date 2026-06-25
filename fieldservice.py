# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: FieldService
from dataclasses import dataclass, field
from datetime import date, timedelta
import random

@dataclass
class SiteNote:
    id: int
    site_name: str
    technician: str
    notes: str
    photo_url: str | None = None
    created_at: date = field(default_factory=date.today)

def init_demo_db():
    db = []
    for i in range(1, 6):
        today = date.today() - timedelta(days=random.randint(0, 30))
        site_name = f"Site_{random.choice(['Alpha', 'Beta', 'Gamma'])}_{i}"
        tech = random.choice(["A. Smith", "B. Jones", "C. Doe"])
        note_text = f"Inspected {site_name}. Found minor wear on panel {i}."
        photo_url = f"https://example.com/photos/{random.randint(100,999)}.jpg" if random.random() > 0.5 else None
        db.append(SiteNote(id=i, site_name=site_name, technician=tech, notes=note_text, photo_url=photo_url, created_at=today))
    return db

demo_data = init_demo_db()
