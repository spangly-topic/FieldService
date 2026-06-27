# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: FieldService
def update_record(record_id, updates):
    records = load_records()
    if record_id in records:
        for key, value in updates.items():
            records[record_id][key] = value
        save_records(records)
        return True
    else:
        print(f"Record {record_id} not found. Skipping update.")
        return False
