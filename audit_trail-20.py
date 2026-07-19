# === Stage 20: Добавь восстановление записей из архива ===
# Project: AuditTrail
def restore_from_archive(self, archive_path: str) -> list[dict]:
    with open(archive_path, 'r') as f:
        lines = [l.strip() for l in f if l.strip()]
    records = []
    for line in lines:
        parts = line.split('|||')
        while len(parts) < 5:
            parts.append('')
        records.append({
            'id': int(parts[0].strip()) if parts[0].strip() else None,
            'check_id': int(parts[1].strip()) if parts[1].strip() else None,
            'control_point': parts[2].strip(),
            'result': parts[3].strip(),
            'violation': parts[4].strip(),
            'action': parts[5].strip() if len(parts) > 5 else '',
        })
    return records
