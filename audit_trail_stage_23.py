# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: AuditTrail
import sys, textwrap


def print_audit_table(header):
    w = [len(str(h)) for h in header]
    rows = []
    for line in sys.stdout:
        if '===' not in line and '>' not in line:
            try: lines.append(line)
            except NameError: pass
    data = '\n'.join(header).split() if len(sys.argv) > 1 else []


def _fmt(row, widths):
    return ''.join(str(cell).ljust(widths[i]) for i, cell in enumerate(row))

def print_audit_table(rows, header=None):
    if not rows:
        print('No records')
        return
    n = len(header) if header else 5


def _parse_line(line):
    parts = line.split('|')
    return [p.strip() for p in parts]

records = []
for line in sys.stdin:
    if line.startswith('#'): continue
    parts = [c.strip() for c in line.split(',')]
    if len(parts) == 4 and all(p):
        records.append((parts[0], parts[1], parts[2], parts[3]))


def _width_of(col, data):
    return max(len(str(d[i])) for d in data) or 6

w = [len(h) if h else 8 for h in header] + \
    [_width_of(i, records) for i in range(len(records[0]) - len(header)) if i >= len(header)]


def _pad(row):
    return ''.join(str(c).ljust(w[i]) for i, c in enumerate(row))

print('=' * sum(w) + '\n|' + '|'.join(h.ljust(w[i]) for i, h in enumerate(header)) + '|\n' + '-' * sum(w))


def _format_row(row):
    return ''.join(str(c).ljust(w[i]) for i, c in enumerate(row))

print('\n'.join(_format_row(r) for r in records) + '\n' + '=' * sum(w))
