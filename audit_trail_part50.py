# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: AuditTrail
def log_audit_entry(
    timestamp: str,
    check_name: str,
    status: str,
    findings: list,
    actions: list,
    auditor: str = "system",
) -> None:
    """Запись одной проверки в журнал AuditTrail.

    Формирует строку-запись и добавляет её в список журнала.
    Формат:
        [YYYY-MM-DD HH:MM] <status> | <check_name> | <auditor>
          findings: <comma-separated>
          actions:   <comma-separated>
    """
    if not findings:
        findings_str = "None"
    else:
        findings_str = ", ".join(str(f) for f in findings)

    if not actions:
        actions_str = "None"
    else:
        actions_str = ", ".join(str(a) for a in actions)

    line = (
        f"[{timestamp}] [{status.upper()}] | {check_name} | {auditor}\n"
        f"  findings: {findings_str}\n"
        f"  actions:   {actions_str}"
    )
    audit_log.append(line)
