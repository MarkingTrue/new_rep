# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: AuditTrail
def filter_records(records, filters=None):
    if not filters: return records
    result = []
    for r in records:
        match_status = (not filters.get('status')) or r['status'] == filters['status']
        match_category = (not filters.get('category')) or r.get('category') == filters['category']
        match_tags = True
        if 'tags' in filters and isinstance(filters['tags'], list):
            if not any(t in r.get('tags', []) for t in filters['tags']): match_tags = False
        elif 'tags' in filters:
            if filters['tags'] != r.get('tags'): match_tags = False
        if match_status and match_category and match_tags: result.append(r)
    return result
