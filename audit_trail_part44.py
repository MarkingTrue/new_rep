# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: AuditTrail
def backup_data_file(filepath, backup_dir=None):
    """Создает резервную копию файла данных с автоматической генерацией пути и времени."""
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(filepath), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, os.path.basename(filepath).replace(".", "_") + f"_{timestamp}.bak")
    with open(filepath, "rb") as src:
        with open(backup_path, "wb") as dst:
            dst.write(src.read())
    return backup_path
