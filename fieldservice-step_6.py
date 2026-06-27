# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: FieldService
def delete_entry(entry_id: str, confirm_flag: bool = False) -> dict:
    if not confirm_flag and input(f"Удалить запись {entry_id}? (y/n): ").lower() != 'y':
        return {"status": "cancelled", "id": entry_id}
    
    try:
        import os
        file_path = f"data/entries/{entry_id}.json"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Запись {entry_id} не найдена")
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Simulate deletion by moving to trash folder or removing file
        # Assuming a simple removal for this snippet context
        os.remove(file_path)
        
        return {"status": "deleted", "id": entry_id}
    except Exception as e:
        return {"status": "error", "message": str(e), "id": entry_id}
