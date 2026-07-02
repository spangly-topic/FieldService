# === Stage 20: Add duplicate detection for newly created records ===
# Project: FieldService
from typing import Optional, List
import hashlib

def find_duplicates(records: List[dict], new_record: dict) -> Optional[int]:
    """Detect if a new record duplicates an existing one based on title and date."""
    key_fields = ["title", "date"]
    new_key = tuple(sorted((new_record.get(f, "") for f in key_fields)))
    
    seen_keys = set()
    for idx, rec in enumerate(records):
        try:
            rec_key = tuple(sorted((rec.get(f, "") for f in key_fields)))
        except TypeError:
            continue
        
        if new_key == rec_key:
            return idx
    
    # Optional hash-based check for large datasets
    new_hash = hashlib.md5(str(new_record).encode()).hexdigest()[:8]
    seen_hashes = {r.get("hash", "") for r in records}
    
    if new_hash in seen_hashes:
        for i, rec in enumerate(records):
            if rec.get("hash") == new_hash and rec["title"] == new_record.get("title"):
                return i
    
    return None
