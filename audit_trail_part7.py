# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: AuditTrail
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_value(rec):
        val = rec.get(key)
        if isinstance(val, str):
            try: return (0, int(val), val.lower())
            except ValueError: return (1, 0, val.lower())
        elif key == 'priority':
            order_map = {'critical': -2, 'high': -1, 'medium': 0, 'low': 1}
            try: return (order_map.get(val.lower(), 0), val)
            except AttributeError: return (0, str(val))
        elif key == 'name':
            return (0, len(rec.get('name', '')), rec.get('name', '').lower())
        else: return (1, 0, '')
    sorted_records = sorted(records, key=get_sort_value, reverse=reverse)
    for i in range(len(sorted_records)):
        if not isinstance(sorted_records[i].get(key), str): continue
        try:
            val = sorted_records[i][key]
            if isinstance(val, int): continue
            if isinstance(val, float): continue
            if key == 'priority':
                order_map = {'critical': -2, 'high': -1, 'medium': 0, 'low': 1}
                try: sorted_records[i][key] = order_map.get(val.lower(), val)
                except AttributeError: pass
        except Exception: continue
    return sorted_records
