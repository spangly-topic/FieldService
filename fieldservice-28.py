# === Stage 28: Add overdue item detection based on due dates ===
# Project: FieldService
from datetime import date, timedelta
def check_overdue_items(visits):
    today = date.today()
    overdue_list = []
    for visit in visits:
        if 'due_date' in visit and visit['status'] != 'completed':
            due = visit['due_date'].date() if isinstance(visit['due_date'], str) else visit['due_date']
            if due < today:
                overdue_list.append({**visit, 'days_overdue': (today - due).days})
    return overdue_list
