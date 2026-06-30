# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: AuditTrail
import json, base64, uuid, datetime

INITIAL_DATA = '''
{
  "checks": [
    {
      "id": "chk_001",
      "name": "Проверка безопасности сети",
      "status": "pending",
      "items": [
        {"control": "Открытые порты", "result": true, "violation": false},
        {"control": "SSL/TLS шифрование", "result": false, "violation": true}
      ],
      "actions": []
    }
  ]
}'''

def load_initial_data(data_str: str) -> dict:
    try:
        data = json.loads(data_str)
        for check in data.get("checks", []):
            if not check.get("id"):
                check["id"] = f"chk_{uuid.uuid4().hex[:8]}"
            for item in check.get("items", []):
                if "timestamp" not in item:
                    item["timestamp"] = datetime.datetime.now().isoformat()
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON данных: {e}")
        return {"checks": [], "metadata": {"loaded_at": datetime.datetime.now().isoformat(), "error": str(e)}}

if __name__ == "__main__":
    loaded_data = load_initial_data(INITIAL_DATA)
    print(f"Загружено проверок: {len(loaded_data.get('checks', []))}")
