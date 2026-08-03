# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: AuditTrail
from dataclasses import dataclass, field
from enum import Enum
import json
from pathlib import Path


class ProfileLevel(Enum):
    ADMIN = "admin"
    OPERATOR = "operator"
    VIEWER = "viewer"


@dataclass
class UserProfile:
    username: str
    password_hash: str  # placeholder for real hashing
    level: ProfileLevel
    permissions: list = field(default_factory=lambda: ["view"])

    def can_access(self, resource_type: str) -> bool:
        allowed = {"admin": ["check", "violation", "action"], "operator": ["check", "violation"], "viewer": []}
        return resource_type in allowed[self.level.value]


class ProfileManager:
    _profiles: dict[str, UserProfile] = field(default_factory=dict)

    @classmethod
    def load(cls) -> None:
        data_file = Path(__file__).parent / "profiles.json"
        if not data_file.exists():
            return
        with open(data_file, "r") as f:
            raw = json.load(f)
            for info in raw:
                cls._profiles[info["username"]] = UserProfile(**info)

    @classmethod
    def save(cls) -> None:
        data_file = Path(__file__).parent / "profiles.json"
        with open(data_file, "w") as f:
            json.dump([p.__dict__ for p in cls._profiles.values()], f, indent=2)

    @classmethod
    def register(cls, profile: UserProfile) -> None:
        cls._profiles[profile.username] = profile

    @classmethod
    def authenticate(cls, username: str, password_hash: str) -> UserProfile | None:
        for p in cls._profiles.values():
            if p.username == username and p.password_hash == password_hash:
                return p
        return None

    @classmethod
    def get_profile(cls, username: str) -> UserProfile | None:
        return cls._profiles.get(username)
