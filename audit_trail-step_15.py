# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: AuditTrail
def weekly_stats():
    """Расчёт недельной статистики по датам."""
    week_counts = {}
    for record in records:
        date_str = record.get("date") or str(record["created_at"])
        try:
            dt = datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            continue
        iso_week = dt.isocalendar()[1]
        week_counts[iso_week] = week_counts.get(iso_week, 0) + 1
    return sorted(week_counts.items())
