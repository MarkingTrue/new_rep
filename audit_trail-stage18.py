# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: AuditTrail
class Tag:
    def __init__(self, name: str):
        self.name = name.lower() if name else ""

    @property
    def is_empty(self) -> bool:
        return not self.name.strip()

    def __str__(self) -> str:
        return f"[{self.name}]"


class TagManager:
    _all_tags: dict[str, Tag] = {}

    @classmethod
    def add(cls, name: str) -> Tag:
        tag = cls._all_tags.setdefault(name.lower(), Tag(name))
        print(f"Добавлен тег: {tag}")
        return tag

    @classmethod
    def remove(cls, name: str):
        removed = cls._all_tags.pop(name.lower())
        if removed is None:
            raise KeyError(f"Тег '{name}' не найден")
        print(f"Удалён тег: {removed}")

    @classmethod
    def get(cls, name: str) -> Tag | None:
        return cls._all_tags.get(name.lower())

    @classmethod
    def list_all(cls):
        return [str(t) for t in sorted(cls._all_tags.values(), key=lambda x: x.name)]
