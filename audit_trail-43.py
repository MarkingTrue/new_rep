# === Stage 43: Добавь пагинацию длинных списков ===
# Project: AuditTrail
def paginate(items, page_size=10):
    total_pages = (len(items) + page_size - 1) // page_size
    for p in range(total_pages):
        start = p * page_size
        end = start + page_size
        if end > len(items):
            end = len(items)
        yield items[start:end], p + 1, total_pages
