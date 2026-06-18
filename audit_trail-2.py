# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: AuditTrail
from dataclasses import dataclass, field
import re
from typing import List, Optional, Dict, Any

@dataclass
class ControlPoint:
    id: str
    name: str
    description: str = ""
    required: bool = True
    
    def validate_input(self) -> tuple[bool, str]:
        if not self.id or not isinstance(self.id, str):
            return False, "ID должен быть непустой строкой"
        if len(self.id) > 50:
            return False, "ID не может превышать 50 символов"
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]*$', self.id):
            return False, "ID должен начинаться с буквы и содержать только латинские символы, цифры, дефис или нижнее подчеркивание"
        if not self.name or len(self.name) > 200:
            return False, "Имя должно быть непустым и не превышать 200 символов"
        return True, ""

@dataclass
class AuditResult:
    point_id: str
    passed: bool = True
    notes: str = ""
    
    def validate_input(self) -> tuple[bool, str]:
        if not self.point_id or len(self.point_id) > 50:
            return False, "point_id должен быть непустой строкой"
        if not isinstance(self.passed, bool):
            return False, "passed должен быть булевым значением"
        if len(self.notes) > 1000:
            return False, "notes не может превышать 1000 символов"
        return True, ""

def sanitize_notes(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[<>{}[\]\\|]', '', text)
    text = re.sub(r'&', '&amp;', text)
    text = re.sub(r'"', '&quot;', text)
    text = re.sub(r"'", '&#39;', text)
    return text

def validate_audit_data(data: Dict[str, Any]) -> tuple[bool, List[str]]:
    errors: List[str] = []
    
    if 'control_points' not in data or not isinstance(data['control_points'], list):
        errors.append("Ключ 'control_points' должен быть списком")
        return False, errors
        
    for i, point_data in enumerate(data['control_points']):
        if not isinstance(point_data, dict):
            errors.append(f"Пункт {i} не является словарем")
            continue
            
        cp = ControlPoint(**point_data)
        valid, msg = cp.validate_input()
        if not valid:
            errors.append(f"Ошибка в пункте {i}: {msg}")
            
    if 'results' in data and isinstance(data['results'], list):
        for i, res_data in enumerate(data['results']):
            if not isinstance(res_data, dict):
                errors.append(f"Результат {i} не является словарем")
                continue
                
            result = AuditResult(**res_data)
            valid, msg = result
