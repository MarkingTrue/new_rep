# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: AuditTrail
def reset_demo_data(db):
    """Сбрасывает все таблицы в пустые, затем заполняет демо-данные."""
    for table in ('checks', 'items', 'results', 'violations', 'actions'):
        db.execute(f"DELETE FROM {table}")
    demo_checks = [
        {'id': 1, 'title': 'Проверка пожарной безопасности', 'date': '2024-03-15'},
        {'id': 2, 'title': 'Аудит документации', 'date': '2024-03-16'},
    ]
    db.executemany("INSERT INTO checks (id, title, date) VALUES (?, ?, ?)", demo_checks)

    items = [
        {'check_id': 1, 'code': 'P-01', 'description': 'Проверка огнетушителей', 'required': True},
        {'check_id': 1, 'code': 'P-02', 'description': 'Контроль путей эвакуации', 'required': True},
        {'check_id': 2, 'code': 'D-01', 'description': 'Проверка наличия инструкции', 'required': False},
    ]
    db.executemany("INSERT INTO items (id, check_id, code, description, required) VALUES (?, ?, ?, ?, ?)", items)

    results = [
        {'item_id': 0, 'passed': True, 'value': '12', 'notes': 'Огнетушителей 3 шт.'},
        {'item_id': 1, 'passed': False, 'value': '', 'notes': 'Путь эвакуации заблокирован'},
        {'item_id': 2, 'passed': None, 'value': '', 'notes': 'Инструкция не найдена'},
    ]
    db.executemany("INSERT INTO results (id, item_id, passed, value, notes) VALUES (?, ?, ?, ?, ?)", results)

    violations = [
        {'result_id': 1, 'severity': 'critical', 'description': 'Эвакуация заблокирована'},
    ]
    db.executemany("INSERT INTO violations (id, result_id, severity, description) VALUES (?, ?, ?, ?)", violations)

    actions = [
        {'violation_id': 0, 'type': 'repair', 'assigned_to': 'Иванов И.И.', 'status': 'pending'},
    ]
    db.executemany("INSERT INTO actions (id, violation_id, type, assigned_to, status) VALUES (?, ?, ?, ?, ?)", actions)


def clear_state(db):
    """Полностью очищает все данные из базы."""
    for table in ('checks', 'items', 'results', 'violations', 'actions'):
        db.execute(f"DELETE FROM {table}")
