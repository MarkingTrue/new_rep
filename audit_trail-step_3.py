# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: AuditTrail
class AuditTrail:
    def __init__(self):
        self._records = []

    def add_record(self, check_id, item_name, result, violation_type=None, action_taken=None):
        record = {
            'check_id': check_id,
            'item_name': item_name,
            'result': result,  # True/False
            'violation_type': violation_type,
            'action_taken': action_taken,
            'timestamp': datetime.now().isoformat()
        }
        self._records.append(record)

    def get_records(self, check_id=None):
        if check_id is None:
            return self._records.copy()
        return [r for r in self._records if r['check_id'] == check_id]
