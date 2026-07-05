# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: AuditTrail
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [AuditItem.from_dict(i) for i in data]
        elif isinstance(data, dict):
            return AuditCheck.from_dict(data).items
        else:
            print("Ошибка: некорректный формат JSON")
            return []
    except FileNotFoundError:
        print(f"Файл {filepath} не найден")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке: {type(e).__name__}: {e}")
        return []
