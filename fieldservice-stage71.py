# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: FieldService
def seed_demo_data():
    """Populate FieldService with deterministic sample records for quick demo runs."""
    import hashlib, time as _time
    rng = lambda: int(hashlib.md5(f"seed_{_time.time() % 100}".encode()).hexdigest(), 16) % 2**32

    sites = ["Alpha Site", "Beta Depot", "Gamma Hub"]
    technicians = ["Alice R.", "Bob K.", "Carol M."]
    tasks = [
        {"id": 1, "title": "Inspect pressure valves", "status": "completed"},
        {"id": 2, "title": "Calibrate flow meter",   "status": "in_progress"},
        {"id": 3, "title": "Replace corroded pipe",  "status": "pending"},
    ]

    for i, site in enumerate(sites):
        tech = technicians[i % len(technicians)]
        report = {
            "site_name": site,
            "tech_id": tech,
            "visit_date": f"2025-01-{i+3:02d}",
            "notes": f"Routine check at {site}. All sensors within tolerance.",
            "photos_as_links": [f"https://example.com/demo/{site.lower()}/photo_{j}.png" for j in range(1, 4)],
            "tasks_performed": tasks[i % len(tasks)],
            "follow_up_required": i < len(sites),
        }

    return {"sites": sites, "technicians": technicians, "sample_reports": report}
