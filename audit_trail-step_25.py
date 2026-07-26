# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: AuditTrail
def validate_and_parse_date(date_str):
    """Разрешает формат YYYY-MM-DD, возвращает datetime.date или raises ValueError."""
    if not date_str or not isinstance(date_str, str):
        raise ValueError("Дата должна быть строкой в формате 'YYYY-MM-DD'")
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        raise ValueError(f"Некорректный формат даты: '{date_str}' (ожидался YYYY-MM-DD)")
