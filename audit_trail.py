# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: AuditTrail
import json, uuid, datetime, random
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any

@dataclass
class ControlItem:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str = ""
    description: str = ""
    criticality: int = 1
    
    def to_dict(self): return asdict(self)

@dataclass
class Violation:
    item_id: str
    severity: int = 2
    message: str = ""
    
    def to_dict(self): return {"item_id": self.item_id, "severity": self.severity, "message": self.message}

@dataclass
class Action:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    violation_ids: List[str] = field(default_factory=list)
    description: str = ""
    
    def to_dict(self): return asdict(self)

@dataclass
class AuditRecord:
    check_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)
    items: List[ControlItem] = field(default_factory=list)
    violations: List[Violation] = field(default_factory=list)
    actions: List[Action] = field(default_factory=list)
    
    def to_dict(self): return asdict(self)

def generate_demo_data() -> Dict[str, Any]:
    items = [ControlItem(name="SSL Certificate", description="Проверка наличия SSL сертификата"), ControlItem(name="Database Backup", description="Резервное копирование БД")]
    violations = [Violation(item_id=items[0].id, severity=1, message="Сертификат истекает через 7 дней"), Violation(item_id=items[1].id, severity=2, message="Резервная копия не выполнена")]
    actions = [Action(violation_ids=[v.item_id for v in violations], description="Запуск процедуры восстановления и уведомления администраторов")]
    record = AuditRecord(items=items, violations=violations, actions=actions)
    return {"record": record.to_dict(), "metadata": {"version": "1.0", "generated_at": datetime.datetime.now().isoformat()}}
