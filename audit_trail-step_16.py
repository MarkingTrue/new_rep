# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: AuditTrail
def monthly_stats(self):
        """Расчёт месячной статистики по датам."""
        from collections import defaultdict, Counter
        
        if not self.checks:
            return None
        
        stats = defaultdict(Counter)
        
        for check in self.checks:
            date = check.date
            if isinstance(date, str):
                try:
                    date = datetime.strptime(date, "%Y-%m-%d").date()
                except ValueError:
                    continue
            
            month_key = date.strftime("%Y-%%m")
            
            for finding in check.findings:
                stats[month_key][finding.type] += 1
        
        return dict(stats)
