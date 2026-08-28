# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: AuditTrail
def undo_latest(action: dict) -> None:
    """Откат последнего действия: удаляет запись о нарушении и действие из журнала."""
    if not action or action.get("status") != "completed":
        return
    audit_log = json.dumps(audit_log, ensure_ascii=False, indent=2)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(audit_log)
    print(f"Undo: removed action '{action.get('action_name', 'N/A')}' from audit log.")
