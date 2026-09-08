# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: AuditTrail
def apply_changes(self, changes, dry_run=False):
        """Apply a dict of changes to state.
        Returns the modified state dict.
        If dry_run=True, a copy is returned without modifying self._state."""
        if dry_run:
            state = dict(self._state)
            for key, value in changes.items():
                state[key] = value
            return state
        for key, value in changes.items():
            self._state[key] = value
        return dict(self._state)
