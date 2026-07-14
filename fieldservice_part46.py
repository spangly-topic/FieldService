# === Stage 46: Add a schema version field and migration helper ===
# Project: FieldService
SCHEMA_VERSION = 3


def migrate(db_path: str) -> None:
    """Apply schema migrations to FieldService SQLite DB."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS _migrations (version INTEGER PRIMARY KEY)"
    )
    cur.execute("SELECT MAX(version) FROM _migrations")
    current = cur.fetchone()[0] or 0
    if current < SCHEMA_VERSION:
        cur.execute(
            """CREATE TABLE IF NOT EXISTS sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                notes TEXT DEFAULT '',
                photo_url TEXT DEFAULT '',
                task TEXT DEFAULT '',
                follow_up TEXT DEFAULT '',
                report TEXT DEFAULT '',
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS visits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site_id INTEGER REFERENCES sites(id),
                visitor_name TEXT NOT NULL,
                notes TEXT DEFAULT '',
                photo_url TEXT DEFAULT '',
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
        )
        cur.execute("INSERT INTO _migrations (version) VALUES (?)", (SCHEMA_VERSION,))
        conn.commit()
    conn.close()
