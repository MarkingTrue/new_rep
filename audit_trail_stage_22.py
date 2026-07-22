# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: AuditTrail
def check_overdue_reminders():
    """Проверка просроченных напоминаний в журнале проверок."""
    overdue = []
    for record in audit_records:
        if record.get('reminder_due_date') and datetime.now() > record['reminder_due_date']:
            reminder_status = record.get('reminder_status', 'unknown')
            if reminder_status == 'pending':
                overdue.append({
                    'record_id': record['id'],
                    'due_date': record['reminder_due_date'],
                    'description': record.get('description', 'Неизвестное напоминание'),
                    'action_required': record.get('required_action', None)
                })
    if overdue:
        print(f"\n⚠️  Просрочено {len(overdue)} напоминания:")
        for item in overdue:
            print(f"   - [{item['record_id']}] {item['description']} (срок: {item['due_date']})")
            if item.get('action_required'):
                print(f"      Требуется действие: {item['action_required']}")
    else:
        print("\n✅ Все напоминания в срок.")
