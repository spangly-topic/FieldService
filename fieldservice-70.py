# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: FieldService
import json, os, shutil, sys
from pathlib import Path

class FieldService:
    def __init__(self, repo_path):
        self.repo = Path(repo_path)
    
    def clear_state(self, confirm=False):
        if not confirm:
            print("⚠️  Clearing state requires explicit confirmation. Use clear_state(True).")
            return False
        try:
            shutil.rmtree(self.repo / "notes", ignore_errors=True)
            shutil.rmtree(self.repo / "tasks", ignore_errors=True)
            shutil.rmtree(self.repo / "photos", ignore_errors=True)
            self.repo.mkdir(exist_ok=True)
            print("✅ State cleared successfully.")
            return True
        except Exception as e:
            print(f"❌ Error clearing state: {e}")
            return False
    
    def add_site_note(self, filename, content):
        notes_dir = self.repo / "notes"
        notes_dir.mkdir(exist_ok=True)
        with open(notes_dir / filename, 'w') as f:
            f.write(content)
        print(f"Note saved to {filename}")
    
    def add_service_task(self, task_id, description):
        tasks_dir = self.repo / "tasks"
        tasks_dir.mkdir(exist_ok=True)
        task_file = tasks_dir / f"{task_id}.json"
        with open(task_file, 'w') as f:
            json.dump({"id": task_id, "description": description}, f, indent=2)
        print(f"Task {task_id} saved.")
    
    def add_photo_link(self, filename):
        photos_dir = self.repo / "photos"
        photos_dir.mkdir(exist_ok=True)
        with open(photos_dir / filename, 'w') as f:
            f.write("link://photo")
        print(f"Photo linked as {filename}")
    
    def add_follow_up(self, task_id, followup_text):
        tasks_dir = self.repo / "tasks"
        if not (tasks_dir / f"{task_id}.json").exists():
            print(f"Task {task_id} does not exist.")
            return
        with open(tasks_dir / f"{task_id}.json", 'r') as f:
            task_data = json.load(f)
        task_data["follow_ups"] = [{"text": followup_text}]
        with open(tasks_dir / f"{task_id}.json", 'w') as f:
            json.dump(task_data, f, indent=2)
        print(f"Follow-up added to Task {task_id}")
    
    def generate_visit_report(self):
        notes = list((self.repo / "notes").glob("*.md")) if (self.repo / "notes").exists() else []
        tasks = list((self.repo / "tasks").glob("*.json")) if (self.repo / "tasks").exists() else []
        report = {"notes": len(notes), "tasks": len(tasks)}
        print(json.dumps(report, indent=2))

if __name__ == "__main__":
    fs = FieldService(sys.argv[1])
    confirm = sys.argv[2] if len(sys.argv) > 2 else False
    fs.clear_state(confirm)
