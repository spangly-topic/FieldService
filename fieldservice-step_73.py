# === Stage 73: Add a lightweight HTML report export ===
# Project: FieldService
def export_report(visit):
    """Export a visit dict to a compact HTML report."""
    lines = ["<html><head><style>body{font-family:monospace}table{border-collapse:collapse}td,th{padding:4px;border:1px solid #ccc}</style></head><body>"]
    lines.append(f"<h2>{visit.get('title','Visit')}</h2>")
    for k in ('date', 'site', 'technician'):
        if visit.get(k):
            lines.append(f"<p><b>{k}:</b> {visit[k]}</p>")
    tasks = visit.get('tasks', [])
    if tasks:
        lines.append("<h3>Tasks</h3><table><tr><th>Status</th><th>Description</th></tr>")
        for t in tasks:
            status, desc = (t['status'] if isinstance(t, dict) else 'done'), (t.get('description') or '')
            lines.append(f"<tr><td>{status}</td><td>{desc}</td></tr>")
        lines.append("</table>")
    notes = visit.get('notes', [])
    if notes:
        lines.append("<h3>Notes</h3><ul>")
        for n in notes:
            lines.append(f"<li>{n}</li>")
        lines.append("</ul>")
    photos = visit.get('photos', [])
    if photos:
        lines.append("<h3>Photos</h3><ul>")
        for p in photos:
            link = p['url'] if isinstance(p, dict) else p
            lines.append(f"<li><a href='{link}'>{p.get('caption','Photo')}</a></li>")
        lines.append("</ul>")
    followups = visit.get('followups', [])
    if followups:
        lines.append("<h3>Follow-ups</h3><table><tr><th>Action</th><th>Due</th></tr>")
        for f in followups:
            act, due = (f['action'] if isinstance(f, dict) else 'review'), (f.get('due') or '')
            lines.append(f"<tr><td>{act}</td><td>{due}</td></tr>")
        lines.append("</table>")
    return "\n".join(lines) + "</body></html>"
