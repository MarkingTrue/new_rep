# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: AuditTrail
def get_recommendation(audit):
    """Возвращает рекомендацию следующего действия на основе текущего состояния аудита."""
    rec = "Продолжить проверку."
    if audit.get("completed", False):
        rec = "Аудит завершён."
    elif audit.get("blocked", False) and audit.get("pending_actions"):
        rec = "Заблокировано до устранения нарушений. Выполните необходимые действия."
    elif audit.get("pending_actions"):
        rec = "Завершите оставшиеся действия перед подписанием."
    elif audit.get("violations"):
        rec = "Устраните нарушения перед подписанием."
    return rec
