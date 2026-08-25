# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: AuditTrail
class ProfileManager:
    def __init__(self, profiles):
        self.profiles = profiles
        self.active = profiles[0] if profiles else None

    def switch_profile(self, name):
        for p in self.profiles:
            if p.name == name:
                self.active = p
                return p
        raise ValueError(f"Профиль '{name}' не найден")

    def get_active(self):
        return self.active
