# === Stage 31: Add compact table rendering for long lists ===
# Project: FieldService
def render_compact_table(headers, rows):
    """Render a compact text table from headers and row data."""
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))

    def format_row(cells):
        return '  '.join(str(c).ljust(w) for c, w in zip(cells, col_widths))

    lines = ['+---' + '--'.join('-' * (w + 2) for w in col_widths) + '+']
    lines.append('| ' + ' | '.join(headers) + ' |')
    lines.append('+---' + '--'.join('-' * (w + 2) for w in col_widths) + '+')
    for row in rows:
        lines.append(format_row(row))
    return '\n'.join(lines)

# Example usage:
headers = ['ID', 'Task', 'Status']
rows = [['101', 'Inspection', 'Done'], ['102', 'Repair', 'Pending']]
print(render_compact_table(headers, rows))
