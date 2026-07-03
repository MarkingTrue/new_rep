# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: AuditTrail
import json, os

def save_to_json(data: dict, filename: str = "audit_trail.json") -> None:
    """Сохраняет данные журнала проверок в JSON файл с обработкой ошибок."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Данные сохранены в {filename}")
    except (json.JSONDecodeError, IOError) as e:
        print(f"[ERROR] Не удалось сохранить данные: {e}")

def load_from_json(filename: str = "audit_trail.json") -> dict | None:
    """Загружает данные из JSON файла или возвращает пустой словарь при ошибке."""
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError):
        pass
    return {}

def main():
    # Пример структуры данных для теста
    audit_data = {
        "checks": [
            {"id": 1, "item": "Проверка А", "result": "passed", "violations": [], "actions": []},
            {"id": 2, "item": "Проверка Б", "result": "failed", "violations": ["Нарушение 1"], "actions": ["Исправить"]}
        ],
        "metadata": {"version": "0.1", "author": "AuditTrail"}
    }

    # Сохранение данных
    save_to_json(audit_data)

    # Загрузка и вывод содержимого
    loaded = load_from_json()
    print(json.dumps(loaded, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
