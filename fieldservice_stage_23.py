# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: FieldService
def manage_tags(notebook):
    def add_tag(record, tag):
        if record.get('tags') is None:
            record['tags'] = set()
        record['tags'].add(tag)
    
    def remove_tag(record, tag):
        if 'tags' in record and tag in record['tags']:
            record['tags'].remove(tag)
            if not record['tags']:
                del record['tags']
    
    def get_summary(tags=None):
        if tags is None:
            tags = set()
        summary = {'count': 0, 'by_tag': {}}
        for r in notebook.get('records', []):
            if not isinstance(r, dict) or 'tags' not in r:
                continue
            current_tags = r['tags']
            if isinstance(current_tags, set):
                common = tags & current_tags
            else:
                common = set(tags).intersection(set(current_tags))
            if common:
                summary['count'] += 1
                for t in sorted(common):
                    summary['by_tag'][t] = summary['by_tag'].get(t, 0) + 1
        return summary

    notebook['_helpers']['add_tag'] = add_tag
    notebook['_helpers']['remove_tag'] = remove_tag
    notebook['_helpers']['get_summary'] = get_summary
