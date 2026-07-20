# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: FieldService
def score_task(task: dict) -> float:
    """Simple priority scoring for a service task."""
    score = 0.0
    if task.get('status') == 'critical':
        score += 100
    elif task.get('status') == 'open':
        score += 50
    else:
        score += 10

    deadline = task.get('deadline', '')
    if isinstance(deadline, str):
        try:
            from datetime import datetime
            now = datetime.now()
            dl = datetime.strptime(deadline, '%Y-%m-%d')
            days_left = (dl - now).days
            if days_left <= 0:
                score += 150
            elif days_left <= 3:
                score += 80
            elif days_left <= 7:
                score += 40
        except Exception:
            pass

    priority = task.get('priority', 'normal')
    if isinstance(priority, str):
        priority_map = {'high': 25, 'medium': 10, 'low': -5}
        score += priority_map.get(priority, 0)

    return score


def recommend_order(tasks: list[dict]) -> list[dict]:
    """Sort tasks by descending priority score and return with scores."""
    scored = [(score_task(t), t) for t in tasks]
    scored.sort(key=lambda x: -x[0])
    result = []
    for s, t in scored:
        t['priority_score'] = s
        result.append(t)
    return result


if __name__ == '__main__':
    sample_tasks = [
        {'id': 1, 'status': 'open', 'deadline': '2025-12-31', 'priority': 'high'},
        {'id': 2, 'status': 'critical', 'deadline': '', 'priority': 'normal'},
        {'id': 3, 'status': 'closed', 'deadline': '', 'priority': 'low'},
    ]
    ordered = recommend_order(sample_tasks)
    for i, t in enumerate(ordered):
        print(f"{i+1}. Task {t['id']} - Score: {t.get('priority_score')}, Status: {t['status']}")
