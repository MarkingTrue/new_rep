# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: AuditTrail
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "checks": checks,
        "violations": violations,
        "actions": actions
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
