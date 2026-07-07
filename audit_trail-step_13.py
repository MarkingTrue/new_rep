# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: AuditTrail
def search_checks(query: str, field: str = "title") -> list[dict]:
    """Поиск проверок по нескольким полям без учёта регистра."""
    normalized_query = query.lower()
    results = []
    for check in checks:
        value = getattr(check, field, "")
        if isinstance(value, str) and normalized_query in value.lower():
            results.append(check)
    return results
