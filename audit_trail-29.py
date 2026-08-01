# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: AuditTrail
class AppSettings:
    def __init__(self, config=None):
        self._config = config or {}
        self.max_log_entries = int(self._config.get('max_log_entries', 100))
        self.log_retention_days = int(self._config.get('log_retention_days', 30))
        self.default_severity = str(self._config.get('default_severity', 'INFO'))
        self.allowed_actions = list(self._config.get('allowed_actions', ['approve', 'reject']))

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        self._config[key] = value

    @property
    def config(self):
        return dict(self._config)
