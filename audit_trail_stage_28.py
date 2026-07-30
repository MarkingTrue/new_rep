# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: AuditTrail
def project_metrics():
    total_checks = len(checks) if checks else 0
    total_items = sum(len(c.get("items", [])) for c in checks if isinstance(c, dict))
    passed_count = sum(1 for c in checks if isinstance(c, dict) and c.get("result") == "passed")
    failed_count = sum(1 for c in checks if isinstance(c, dict) and c.get("result") == "failed")
    violation_count = sum(len(c.get("violations", [])) for c in checks if isinstance(c, dict))
    action_count = sum(len(c.get("actions", [])) for c in checks if isinstance(c, dict))
    print(f"Total checks: {total_checks}")
    print(f"Passed: {passed_count}, Failed: {failed_count}")
    print(f"Violations: {violation_count}, Actions: {action_count}")
