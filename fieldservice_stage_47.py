# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: FieldService
# demo.py – compact end-to-end walkthrough of FieldService
from field_service import Notebook, SiteNote, ServiceTask, PhotoLink, FollowUp, VisitReport

nb = Notebook("Demo")

# --- 1. Site notes -------------------------------------------------------
nb.add(SiteNote(title="Warehouse A", body="Concrete floor, 200m², no drainage."))
nb.add(SiteNote(
    title="Observations",
    body=[
        "Cracks near loading dock.",
        "Humidity sensor reading: 78%.",
        "Minor water stain on north wall.",
    ],
))

# --- 2. Service tasks ----------------------------------------------------
nb.add(ServiceTask(id=1, title="Inspect floor", status="done", notes="No structural concern."))
nb.add(ServiceTask(
    id=2,
    title="Fix drainage gap",
    status="open",
    priority="high",
    follow_ups=[FollowUp(date="2026-12-05", action="Re-check after repair")],
))

# --- 3. Photos-as-links --------------------------------------------------
nb.add(PhotoLink(url="https://example.com/warehouse-a/floor-crack.jpg"))
nb.add(PhotoLink(url="https://example.com/warehouse-a/drainage-gap.jpg"))

# --- 4. Visit report -----------------------------------------------------
report = VisitReport(
    date="2026-12-03",
    technician="Alice M.",
    summary=(
        "Initial inspection of Warehouse A. Floor and drainage noted; "
        "drainage task opened for follow-up."
    ),
)
nb.add(report)

# --- 5. Render -----------------------------------------------------------
print(nb.render())
