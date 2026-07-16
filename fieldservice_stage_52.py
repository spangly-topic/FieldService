# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: FieldService
def clean_text(text: str) -> str:
    """Strip surrounding whitespace and collapse internal spaces."""
    return re.sub(r'\s+', ' ', text.strip())


def format_date(date_str: str, fmt: str = '%Y-%m-%d') -> str:
    """Parse a date string in the given format and return it reformatted."""
    try:
        dt = datetime.strptime(date_str, fmt)
        return dt.strftime(fmt)
    except ValueError as exc:
        raise ValueError(f"Unparseable date '{date_str}': {exc}") from exc


def ensure_dir(path: Path) -> None:
    """Create a directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)
