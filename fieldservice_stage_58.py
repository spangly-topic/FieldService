# === Stage 58: Add bulk update behavior for selected records ===
# Project: FieldService
def bulk_update_selected(
    records: list[dict],
    selected_ids: set[int] | None = None,
    updates: dict[str, Any] | None = None,
) -> list[dict]:
    """Update a subset of records in-place.

    Args:
        records: the full list of record dicts (modified directly).
        selected_ids: IDs to update; defaults to all records.
        updates: field->value mapping applied only when not ``None``.

    Returns:
        The updated records, unchanged if no update was performed.
    """
    if not updates and not selected_ids:
        return records
    target = selected_ids or {r["id"] for r in records}
    for rec in records:
        if rec["id"] not in target:
            continue
        if updates is None:
            continue
        for field, value in updates.items():
            if field in rec and rec[field] != value:
                rec[field] = value
    return records
