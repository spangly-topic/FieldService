# === Stage 55: Add a setting to disable colorized output ===
# Project: FieldService
# Step 55: Add a setting to disable colorized output.
import os


def is_color_enabled() -> bool:
    """Check if terminal supports colors."""
    return "NO_COLOR" not in os.environ and "TERM" in os.environ and not os.isatty(0)


class ColorFormatter:
    """Simple color formatter with toggle capability."""

    def __init__(self, enable_colors=True):
        self.enable_colors = enable_colors

    def set_enabled(self, enabled: bool) -> None:
        """Enable or disable colored output."""
        self.enable_colors = enabled

    def is_enabled(self) -> bool:
        """Return whether colors are currently enabled."""
        return self.enable_colors and is_color_enabled()

    def colorize(self, text: str, color_code: str = "") -> str:
        """Add ANSI color codes to text if colors are enabled."""
        if not self.is_enabled():
            return text
        if not color_code:
            return text
        return f"\033[{color_code}m{text}\033[0m"

    def green(self, text: str) -> str:
        """Return text in green."""
        return self.colorize(text, "32")

    def red(self, text: str) -> str:
        """Return text in red."""
        return self.colorize(text, "31")

    def yellow(self, text: str) -> str:
        """Return text in yellow."""
        return self.colorize(text, "33")

    def cyan(self, text: str) -> str:
        """Return text in cyan."""
        return self.colorize(text, "36")

    def format_report(self, title: str, status: str, notes: str = "") -> str:
        """Format a visit report with optional colored sections."""
        lines = []
        if not self.is_enabled():
            return f"Report:\nTitle: {title}\nStatus: {status}"

        lines.append(self.green(f"\n=== {title} ==="))
        status_color = "31" if status.lower() in ("failed", "error") else "32"
        lines.append(f"Status: {self.colorize(status, status_color)}")
        if notes:
            lines.append(f"Notes: {notes}")

        return "\n".join(lines)


# Example usage:
if __name__ == "__main__":
    formatter = ColorFormatter()
    print(formatter.format_report("Site Visit", "Success", "All checks passed"))
