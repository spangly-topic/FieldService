# === Stage 26: Add weekly summary calculations ===
# Project: FieldService
from datetime import datetime, timedelta
import os

def calculate_weekly_summary(visit_reports):
    if not visit_reports:
        return {}
    
    today = datetime.now()
    week_start = (today - timedelta(days=today.weekday())).strftime("%Y-%m-%d")
    week_end = (week_start + timedelta(days=6)).strftime("%Y-%m-%d")
    
    weekly_data = {
        "total_visits": 0,
        "completed_tasks": 0,
        "pending_followups": [],
        "sites_visited": set()
    }
    
    for report in visit_reports:
        if isinstance(report.get("date"), str):
            date_obj = datetime.strptime(report["date"], "%Y-%m-%d")
        else:
            continue
            
        if week_start <= date_obj.strftime("%Y-%m-%d") <= week_end:
            weekly_data["total_visits"] += 1
            weekly_data["sites_visited"].add(report.get("site_id", "unknown"))
            
            if report.get("status") == "completed":
                weekly_data["completed_tasks"] += 1
                
            followup = report.get("follow_ups", [])
            for fu in followup:
                if isinstance(fu.get("date"), str):
                    fu_date = datetime.strptime(fu["date"], "%Y-%m-%d")
                else:
                    continue
                    
                if date_obj < fu_date and not fu.get("completed"):
                    weekly_data["pending_followups"].append({
                        "site": report.get("site_id"),
                        "due_date": fu["date"]
                    })
    
    return {
        **weekly_data,
        "sites_visited_count": len(weekly_data["sites_visited"]),
        "completion_rate": round((weekly_data["completed_tasks"] / weekly_data["total_visits"]) * 100, 2) if weekly_data["total_visits"] > 0 else 0.0
    }
