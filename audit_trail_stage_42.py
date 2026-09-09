# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: AuditTrail
import sys
import os

if sys.platform.startswith("win"):
    sys.stdout = os.fdopen(sys.stdout.fileno(), "wb", closefd=True)

def _colorize(text, color):
    return f"\033[{color}m{text}\033[0m"

class AuditColor:
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    _disabled = False

    @classmethod
    def disable(cls):
        cls._disabled = True

    @classmethod
    def enable(cls):
        cls._disabled = False

    @classmethod
    def _c(cls, text, color):
        if cls._disabled:
            return text
        return f"{color}{text}{cls.RESET}"

    def info(cls, text):
        return cls._c(text, cls.CYAN)

    def success(cls, text):
        return cls._c(text, cls.GREEN)

    def error(cls, text):
        return cls._c(text, cls.RED)

    def warning(cls, text):
        return cls._c(text, cls.YELLOW)

    def bold(cls, text):
        return cls._c(text, cls.BOLD)
