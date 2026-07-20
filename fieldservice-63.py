# === Stage 63: Add relationships between records where useful ===
# Project: FieldService
def link_record(record, related_type, target_id):
    """Attach a relationship between two records."""
    if "relationships" not in record:
        record["relationships"] = []
    rel = {"type": related_type, "target_id": target_id}
    if rel not in record["relationships"]:
        record["relationships"].append(rel)

def build_report_links(report):
    """Link a visit report to its site and follow-ups."""
    for item in ["site", "follow_ups"]:
        link_record(report, f"visit_{item}", report.get(item, {}).get("id"))
