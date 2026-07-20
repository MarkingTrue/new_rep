# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: AuditTrail
def add_reminders():
    """Добавляет напоминания с датой выполнения для пунктов контроля."""
    reminders = []
    print("=" * 60)
    print("Система Напоминаний")
    print("=" * 60)
    
    reminder_id = 1
    
    while True:
        try:
            check_name = input(f"\nНазвание напоминания (или 'exit' для завершения): ").strip()
            if check_name.lower() == 'exit':
                break
            
            due_date_str = input("Дата выполнения (ДД.ММ.ГГГГ): ").strip()
            
            # Простая валидация даты
            parts = due_date_str.split('.')
            if len(parts) != 3:
                print("Ошибка: дата должна быть в формате ДД.ММ.ГГГГ")
                continue
            
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            
            from datetime import date
            due_date = date(year, month, day)
            
            # Проверка на прошлые даты
            today = date.today()
            if due_date < today:
                print("Ошибка: дата не может быть в прошлом")
                continue
            
            reminder_text = input("Текст напоминания: ").strip()
            
            reminders.append({
                'id': reminder_id,
                'check_name': check_name,
                'due_date': due_date,
                'reminder_text': reminder_text,
                'is_done': False
            })
            
            reminder_id += 1
            
        except ValueError:
            print("Ошибка: неверный формат даты")
            continue
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break
    
    if reminders:
        print("\nНапоминания добавлены:")
        for r in reminders:
            status = "✓ Выполнено" if r['is_done'] else "⏳ Ожидает"
            print(f"  [{r['id']}]. {status} - {r['due_date'].strftime('%d.%m.%Y')}: {r['reminder_text']}")
    else:
        print("\nНапоминания не добавлены.")

add_reminders()
