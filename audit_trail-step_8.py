# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: AuditTrail
def show_menu():
    print("\n=== Меню AuditTrail ===")
    print("1. Показать список проверок")
    print("2. Добавить новую проверку")
    print("3. Редактировать пункты контроля проверки")
    print("4. Вывести отчет по нарушениям")
    print("5. Сохранить и выйти")
    try:
        choice = input("Выберите действие (1-5): ").strip()
        if not choice.isdigit():
            raise ValueError
        return int(choice)
    except ValueError:
        print("Неверный ввод.")
        return None
