# === Stage 45: Add restore from backup with validation ===
# Project: FieldService
import os, json, hashlib, shutil

def validate_backup(backup_path):
    """Validate backup integrity by checking existence and structure."""
    if not os.path.isfile(backup_path) or not backup_path.endswith('.json'):
        raise ValueError("Invalid backup file: must be a .json")
    with open(backup_path, 'r') as f:
        data = json.load(f)
    required_keys = {'site_notes', 'tasks', 'photos', 'followups'}
    missing = required_keys - set(data.keys())
    if missing:
        raise ValueError(f"Missing keys in backup: {missing}")
    return True

def restore_backup(backup_path, target_dir=".", dry_run=False):
    """Restore field data from backup with validation. Returns summary dict."""
    validate_backup(backup_path)
    with open(backup_path, 'r') as f:
        backup_data = json.load(f)
    if dry_run:
        return {"status": "dry_run", "site_notes_count": len(backup_data.get('site_notes', [])),
                "tasks_count": len(backup_data.get('tasks', []))}
    
    data_dir = os.path.join(target_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    for key in ('site_notes', 'tasks', 'photos', 'followups'):
        items = backup_data.get(key, [])
        if not isinstance(items, list):
            continue
        filepath = os.path.join(data_dir, f"{key}.json")
        with open(filepath, 'w') as f:
            json.dump(items, f)
    
    summary = {"status": "restored", "site_notes_count": len(backup_data.get('site_notes', [])),
               "tasks_count": len(backup_data.get('tasks', []))}
    if os.path.exists(data_dir):
        for root, dirs, files in os.walk(data_dir):
            for file in files:
                filepath = os.path.join(root, file)
                summary["restored_files"] = summary.get("restored_files", 0) + 1
    
    return summary

def create_backup(source_dir="data", backup_path="./backup.json"):
    """Create a full backup of current field data."""
    if not os.path.isdir(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist")
    
    files_to_back = [f for f in ['site_notes', 'tasks', 'photos', 'followups'] 
                     if os.path.isfile(os.path.join(source_dir, f + '.json'))]
    
    backup_data = {}
    for fname in files_to_back:
        with open(os.path.join(source_dir, fname), 'r') as f:
            backup_data[fname] = json.load(f)
    
    with open(backup_path, 'w') as f:
        json.dump(backup_data, f, indent=2)
    
    return {"status": "backed_up", "file_count": len(files_to_back), "backup_path": backup_path}
