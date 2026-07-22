# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: FieldService
def generate_changelog(entries, max_items=30):
    """Generate a compact changelog from the activity log.

    Args:
        entries (list of dict): Each entry must have keys 'date', 'author', 'summary'.
        max_items (int): Maximum number of entries to include in the changelog.

    Returns:
        str: A formatted changelog string with recent entries at the top,
             grouped by author and date. Entries are sorted chronologically
             (newest first) before truncating.

    Example:
        >>> generate_changelog([
        ...     {"date": "2024-11-05", "author": "Ornith", "summary": "Added changelog generator"},
        ...     {"date": "2024-11-04", "author": "Alice", "summary": "Fixed bug in report parser"},
        ... ], max_items=5)
        '## Changelog\n\n### 2024-11-05 - Ornith\n- Added changelog generator\n\n### 2024-11-04 - Alice\n- Fixed bug in report parser'
    """
    sorted_entries = sorted(entries, key=lambda e: e["date"], reverse=True)
    recent = sorted_entries[:max_items]

    lines = ["## Changelog", ""]
    current_author = None
    for entry in recent:
        if entry["author"] != current_author:
            if current_author is not None and current_date is not None:
                lines.append("")
            lines.append(f"### {entry['date']} - {entry['author']}")
            current_author = entry["author"]
            current_date = entry["date"]
        lines.append(f"- {entry['summary']}")

    return "\n".join(lines)
