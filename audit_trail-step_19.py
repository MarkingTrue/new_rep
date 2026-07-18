# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: AuditTrail
def archive_records(source, target=None):
    if not source:
        return 0
    if target is None:
        target = []
    archived_count = 0
    for record in source:
        if record['completed'] or (record.get('created_at') and datetime.now() - record['created_at'].date().timetuple()[6] > 30):
            record['archived'] = True
            target.append(record)
            archived_count += 1
    return archived_count
