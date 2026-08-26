# === Stage 32: Добавь журнал действий пользователя ===
# Project: AuditTrail
class ActionLog:
    """Журнал действий пользователя: кто, что, когда, результат."""

    def __init__(self):
        self._actions = []

    def log(self, user, action_type, target, description, status="ok"):
        """Записать действие: user, тип, объект, описание, статус."""
        record = {
            "user": user,
            "action_type": action_type,
            "target": target,
            "description": description,
            "status": status,
            "timestamp": datetime.now().isoformat(),
        }
        self._actions.append(record)
        return record

    def get_actions(self, user=None, status=None):
        """Получить действия с фильтрацией."""
        result = self._actions
        if user is not None:
            result = [a for a in result if a["user"] == user]
        if status is not None:
            result = [a for a in result if a["status"] == status]
        return result

    def summary(self):
        """Краткая сводка по действиям."""
        from collections import Counter
        total = len(self._actions)
        by_status = Counter(a["status"] for a in self._actions)
        by_user = Counter(a["user"] for a in self._actions)
        return {
            "total": total,
            "by_status": dict(by_status),
            "by_user": dict(by_user),
        }
