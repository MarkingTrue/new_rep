# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: AuditTrail
def export_to_text(report, filename=None):
    if filename is None:
        filename = f"audit_report_{report['date']}.txt"
    lines = [f"=== Audit Report: {report['title']} ===", f"Date: {report['date']}", f"Total checks: {report['total_checks']}", f"Passed: {report['passed']}", f"Failed: {report['failed']}", f"Warnings: {report['warnings']}", f"=== Violations ==="]
    for v in report.get('violations', []):
        lines.append(f"- [{v['severity']}] {v['description']}")
    lines.append(f"=== Actions Taken ===")
    for a in report.get('actions', []):
        lines.append(f"- {a['description']}")
    lines.append("===========================================")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"Report exported to {filename}")
    return filename
