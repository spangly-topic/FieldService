# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: FieldService
import re
from datetime import datetime


def parse_date(value):
    """Parse a date string from several common formats and return a datetime object."""
    if value is None:
        raise ValueError("Empty input – cannot parse.")
    value = str(value).strip()
    if not value or len(value) < 8:
        raise ValueError(f"Input too short to be a valid date: {value!r}")

    patterns = [
        (re.compile(r'^(\d{4})-(\d{1,2})-(\d{1,2})$'), '%Y-%m-%d'),
        (re.compile(r'^(\d{4})/(\d{1,2})/(\d{1,2})$'), '%Y/%m/%d'),
        (re.compile(r'^(\w+)\s+(\d{1,2}),?\s+(\d{4})$'), _parse_monthdayyear),
    ]

    for pattern, fmt in patterns:
        if pattern.match(value):
            return datetime.strptime(value, fmt)

    # Try "YYYY-MM-DD" with a date-like value but different separator
    try:
        return datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        pass

    raise ValueError(f"Unrecognized date format: {value!r}. Supported formats include YYYY-MM-DD, YYYY/MM/DD, and Month DD, YYYY.")


def _parse_monthdayyear(match):
    month_map = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
    }
    month_name = match.group(1).lower()
    if month_name in month_map:
        return datetime.strptime(f"{month_name} {match.group(2)}, {match.group(3)}", '%b %d, %Y')
    day = int(match.group(1))
    year = int(match.group(3))
    return datetime.strptime(f"01/{day}/{year}", '%m/%d/%Y')
