# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: AuditTrail
# Демо-команды для ручного тестирования AuditTrail
import sys

def run_demo():
    print("=== AuditTrail Demo ===")
    
    # 1. Создать пункты контроля
    checks = {
        'temperature': {'name': 'Температура', 'threshold': 38.0, 'unit': '°C'},
        'heart_rate': {'name': 'Пульс', 'threshold': 100, 'unit': 'уд/мин'},
        'blood_pressure': {'name': 'Давление', 'threshold': [140, 90], 'unit': 'мм рт.ст.'}
    }
    
    # 2. Провести проверки и записать результаты
    results = {
        'temperature': {'value': 37.5},
        'heart_rate': {'value': 85},
        'blood_pressure': {'value': [120, 80]}
    }
    
    # 3. Создать нарушения для аномальных показателей
    violations = []
    for check_name, result in results.items():
        if check_name == 'temperature' and result['value'] > checks[check_name]['threshold']:
            violations.append({
                'check': check_name,
                'message': f"Температура {result['value']}°C превышает порог {checks[check_name]['threshold']}°C",
                'severity': 'high'
            })
        elif check_name == 'heart_rate' and result['value'] > checks[check_name]['threshold']:
            violations.append({
                'check': check_name,
                'message': f"Пульс {result['value']} уд/мин превышает порог {checks[check_name]['threshold']} уд/мин",
                'severity': 'medium'
            })
    
    # 4. Определить действия на основе нарушений
    actions = []
    for v in violations:
        if v['severity'] == 'high':
            actions.append({'action': f"Вызвать скорую помощь по поводу {v['check'].replace('_', ' ')}", 'priority': 'critical'})
        elif v['severity'] == 'medium':
            actions.append({'action': f"Консультация терапевта: {v['check'].replace('_', ' ')}", 'priority': 'normal'})
    
    # 5. Вывести отчёт
    print(f"\nПроверено пунктов: {len(checks)}")
    print(f"Нарушений найдено: {len(violations)}")
    if violations:
        print("\nСписок нарушений:")
        for v in violations:
            print(f"  [{v['severity'].upper()}] {v['message']}")
    
    if actions:
        print("\nПлан действий:")
        for a in actions:
            print(f"  Приоритет: {a['priority']} | {a['action']}")
    
    print("\n=== Демо завершён ===")

if __name__ == '__main__':
    run_demo()
