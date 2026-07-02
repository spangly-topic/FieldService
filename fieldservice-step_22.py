# === Stage 22: Add favorite records and quick favorite listing ===
# Project: FieldService
from typing import Optional, List
import json
from pathlib import Path

class FavoriteManager:
    def __init__(self, db_path: str):
        self.db = load_db(db_path)
    
    def toggle_favorite(self, record_id: int) -> bool:
        if record_id in self.db['records']:
            rec = self.db['records'][record_id]
            is_fav = rec.get('is_favorite', False)
            rec['is_favorite'] = not is_fav
            save_db(self.db)
            return True
        return False
    
    def get_favorites(self, limit: int = 10) -> List[dict]:
        favs = [r for r in self.db['records'].values() if r.get('is_favorite', False)]
        return sorted(favs, key=lambda x: x.get('created_at', ''), reverse=True)[:limit]

def load_db(path: str) -> dict:
    p = Path(path)
    data = {'records': {}, 'favorites': []}
    if p.exists():
        with open(p) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                pass
    save_db(data)
    return data

def save_db(db: dict):
    Path('fieldservice.db').write_text(json.dumps(db, indent=2))
