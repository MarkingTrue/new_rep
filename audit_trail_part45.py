# === Stage 45: Добавь восстановление из резервной копии ===
# Project: AuditTrail
def restore_from_backup(file_path, backup_path):
    """Восстанавливает файл из резервной копии, создавая файл если он не существует."""
    import os
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"Резервная копия не найдена: {backup_path}")
    with open(backup_path, "r", encoding="utf-8") as src, open(file_path, "w", encoding="utf-8") as dst:
        dst.write(src.read())
    print(f"Резервная копия восстановлена: {backup_path} -> {file_path}")
