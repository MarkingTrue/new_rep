# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: AuditTrail
def edit_audit_record(record_id, updates):
    if record_id not in audit_records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if hasattr(audit_records[record_id], key):
            setattr(audit_records[record_id], key, value)
    
    audit_history.append({
        "action": "edit",
        "record_id": record_id,
        "timestamp": time.time(),
        "changes": updates
    })
    print(f"Запись {record_id} успешно обновлена.")
    return True
