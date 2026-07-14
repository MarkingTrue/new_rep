# === Stage 17: Добавь группировку записей по категориям ===
# Project: AuditTrail
def group_by_category(self) -> dict:
        """Группирует записи журнала по категориям нарушений."""
        categories = {}
        for record in self._records:
            cat = record.get('category', 'Uncategorized')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(record)
        return dict(sorted(categories.items()))
