# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: FieldService
def reset_demo_data(db_path: str = "fieldservice.db") -> None:
    """Reset all tables to demo data for manual testing."""
    import sqlite3, os, shutil
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    if os.path.exists(db_path):
        shutil.copy2(db_path, db_path + ".backup")
    c.execute("DELETE FROM follow_ups")
    c.execute("DELETE FROM photos")
    c.execute("DELETE FROM service_tasks")
    c.execute("DELETE FROM site_notes")
    c.execute("DELETE FROM visit_reports")
    demo_sites = [
        ("Acme Corp", "123 Main St"),
        ("Globex Inc.", "456 Oak Ave"),
        ("Soylent Co.", "789 Pine Rd"),
    ]
    for name, addr in demo_sites:
        c.execute("INSERT INTO sites(name,address) VALUES(?,?)", (name, addr))
    conn.commit()
    print(f"Demo data reset. Backup at {db_path}.backup")
