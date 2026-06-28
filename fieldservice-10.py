# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: FieldService
class SearchFilter:
    def __init__(self, records):
        self.records = records
    
    def search(self, query):
        if not query.strip(): return self.records
        
        q_lower = query.lower()
        results = []
        
        for r in self.records:
            text_parts = [
                str(r.get('site', '')).lower(),
                str(r.get('task', '')).lower(),
                str(r.get('notes', '')).lower(),
                str(r.get('status', '')).lower()
            ]
            
            if any(q_lower in part for part in text_parts):
                results.append(r)
        
        return results
