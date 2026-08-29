# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: AuditTrail
TEMPLATE_DIR = "templates"

def add_template(name: str, items: dict, default_result: str = "pending", default_action: str = "none") -> None:
    """Save a template as a JSON file for quick record creation."""
    import os
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    path = os.path.join(TEMPLATE_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({
            "name": name,
            "items": items,
            "default_result": default_result,
            "default_action": default_action,
        }, f, ensure_ascii=False, indent=2)
