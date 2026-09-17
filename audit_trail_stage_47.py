# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: AuditTrail
def demo():
    """Показывает основной пользовательский сценарий AuditTrail."""
    from AuditTrail import AuditTrail
    trail = AuditTrail()
    
    trail.add_check("Проверка 1", "Проверка работоспособности", "Проверка пройдена", "Нет проблем", None, None)
    trail.add_check("Проверка 2", "Проверка безопасности", "Превышен лимит", "Нарушение лимита", "Уменьшить лимит", None)
    trail.add_check("Проверка 3", "Проверка производительности", "Проверка пройдена", "Нет проблем", None, None)
    
    print("=== Журнал проверок ===")
    print(trail.get_report())
    print(f"\nИтого: {trail.get_total_checks()} проверок")
    print(f"Пройдено: {trail.get_passed_checks()}")
    print(f"Нарушено: {trail.get_failed_checks()}")
    print(f"В процессе: {trail.get_in_progress_checks()}")
