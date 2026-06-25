# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: FieldService
def validate_field_entry(data: dict) -> tuple[bool, str]:
    errors = []
    if "site_id" in data and not re.match(r'^FS-\d{4}$', data["site_id"]):
        errors.append("Invalid site_id format (expected FS-XXXX)")
    if "technician" in data and len(data["technician"].strip()) < 2:
        errors.append("Technician name too short")
    for field, value in data.items():
        if isinstance(value, str) and len(value.strip()) > 100:
            errors.append(f"{field} exceeds 100 characters limit")
    return (len(errors) == 0, "; ".join(errors))
