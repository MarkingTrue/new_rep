# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: AuditTrail
def repair_simple_issues(trail):
    """Repair common simple issues: remove empty violations, fix bad status, clean stale entries."""
    for entry in trail:
        if entry.get('violations'):
            entry['violations'] = [v for v in entry['violations'] if v.get('severity') and v.get('description')]
        if entry.get('status') not in ('passed', 'failed', 'warning', 'error', 'repair_done'):
            entry['status'] = 'warning'
        if entry.get('timestamp'):
            try:
                ts = datetime.fromisoformat(entry['timestamp'])
                if ts < datetime.utcnow() - timedelta(days=30):
                    entry['status'] = 'repair_done'
                    entry['timestamp'] = datetime.utcnow().isoformat()
            except (ValueError, TypeError):
                pass
    return trail
