# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: AuditTrail
def delete_record(record_id: int) -> bool:
    if not record_id or not isinstance(record_id, int):
        raise ValueError("ID должен быть положительным целым числом")
    for i in range(len(records)):
        if records[i].get('id') == record_id:
            del records[i]
            return True
    return False

def get_record_by_id(record_id: int) -> dict | None:
    try:
        id_val = int(record_id)
    except (ValueError, TypeError):
        raise ValueError("ID должен быть целым числом")
    if not records or record_id <= 0:
        return None
    for item in records:
        if item.get('id') == id_val:
            return item.copy()
    return None
