# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: AuditTrail
def print_record(record):
    """Компактный вывод одной записи AuditTrail."""
    print(f"=== Запись #{record.id} ===")
    print(f"Дата: {record.date}")
    print(f"Статус: {'✅' if record.is_passed else '❌'}")
    if not record.checks:
        print("Пункты проверки: нет")
        return
    for i, check in enumerate(record.checks, 1):
        status = "OK" if check.result == "pass" else "FAIL"
        print(f"  [{i}] {check.item}: {status}")
        if check.notes:
            print(f"      примечание: {check.notes}")
    if record.violations:
        for v in record.violations:
            print(f"\n  ⚠️ Нарушение: {v.description}")
    if record.actions:
        print("Действия:")
        for action in record.actions:
            print(f"  • {action}")
