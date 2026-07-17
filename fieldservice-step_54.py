# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: FieldService
class Color:
    """ANSI color codes for console output."""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    @classmethod
    def c(cls, text, color):
        return f"{cls.BOLD}{color}{text}{cls.RESET}"
