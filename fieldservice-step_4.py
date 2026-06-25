# === Stage 4: Implement create operations for the primary records ===
# Project: FieldService
from pathlib import Path
import json, uuid
from datetime import datetime

def create_record(record_type: str, data: dict) -> None:
    repo_root = Path(__file__).parent.parent
    records_dir = repo_root / "data" / record_type.lower()
    records_dir.mkdir(parents=True, exist_ok=True)
    
    unique_id = f"{record_type}_{uuid.uuid4().hex[:8]}"
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    entry = {
        "_id": unique_id,
        "_type": record_type,
        "_created_at": timestamp,
        **data
    }
    
    file_path = records_dir / f"{unique_id}.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entry, f, ensure_ascii=False, indent=2)
