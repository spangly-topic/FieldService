# === Stage 32: Add pagination helpers for long console output ===
# Project: FieldService
def page_lines(text, page_size=40):
    """Yield text split into chunks of at most `page_size` lines."""
    import os
    for chunk in [text[i:i+page_size] for i in range(0, len(text), page_size)]:
        yield chunk.strip().splitlines()

def print_page(text, page_size=40):
    """Print text split into readable pages of `page_size` lines."""
    for page in page_lines(text, page_size=page_size):
        if not any(l.strip() for l in page):
            continue
        print(f"--- Page {len(list(page))} ---")
        for line in page:
            print(line)
