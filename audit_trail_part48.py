# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: AuditTrail
def _compact_audit_log(
    checks: dict[str, list[dict]],
    violations: dict[str, list[dict]],
    actions: dict[str, list[dict]],
    results: dict[str, list[dict]],
) -> dict:
    """Упаковывает все подданные аудита в единый плоский словарь для JSON-сериализации."""
    def _flatten(lst: list[dict]) -> list:
        return [
            {k: v for k, v in item.items() if v is not None}
            for item in lst
        ]

    return {
        "checks": _flatten(checks.get("items", [])),
        "violations": _flatten(violations.get("items", [])),
        "actions": _flatten(actions.get("items", [])),
        "results": _flatten(results.get("items", [])),
        "meta": {
            "total_checks": len(checks.get("items", [])),
            "total_violations": len(violations.get("items", [])),
            "total_actions": len(actions.get("items", [])),
            "total_results": len(results.get("items", [])),
        },
    }
