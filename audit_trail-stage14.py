# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: AuditTrail
def generate_summary():
    """Генерирует краткую текстовую сводку по всем сущностям проекта."""
    items = get_items()
    results = get_results()
    violations = get_violations()
    actions = get_actions()

    if not (items or results or violations or actions):
        return "Данные пусты."

    lines = []

    lines.append(f"Пунктов контроля: {len(items)}")
    for item in items:
        status = "✅ пройден" if item["status"] == "passed" else ("❌ провален" if item["status"] == "failed" else "⏳ в процессе")
        lines.append(f"  - [{item['id']}] {item['name']} — {status}")

    for result in results:
        lines.append(f"Результат проверки [{result['id']}]: {result['description']} → {result['outcome']}")

    for violation in violations:
        lines.append(f"Нарушение [{violation['id']}]: {violation['name']}: {violation['detail']}")

    if actions:
        lines.append("Действия:")
        for action in actions:
            lines.append(f"  - [{action['id']}] {action['description']} → {action['outcome']}")
    else:
        lines.append("Действий пока не запланировано.")

    return "\n".join(lines)
