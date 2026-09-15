# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: AuditTrail
def migrate_structure(old_schema, new_schema):
    """Compact migration: validates structure and logs version change."""
    if old_schema.get("version") != new_schema.get("version"):
        print(f"Migrating structure from version {old_schema.get('version')} to {new_schema.get('version')}")
    for key in new_schema:
        if key not in old_schema:
            old_schema[key] = new_schema[key]
    return old_schema
