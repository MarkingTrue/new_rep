# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: AuditTrail
class AuditLogEntry:
    """Compact record of a data change with timestamp."""
    def __init__(self, entity, field, old_value, new_value, user, ts):
        self.entity = entity
        self.field = field
        self.old_value = old_value
        self.new_value = new_value
        self.user = user
        self.ts = ts

    def __repr__(self):
        return (f"AuditLogEntry({self.entity}.{self.field}: "
                f"{self.old_value!r} -> {self.new_value!r} "
                f"by {self.user} @ {self.ts})")
