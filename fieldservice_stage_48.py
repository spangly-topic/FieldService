# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: FieldService
import unittest

from field_service.models import SiteNote, ServiceTask, FollowUp


class TestSiteNote(unittest.TestCase):
    def test_create_site_note(self):
        note = SiteNote(site_id="101", title="Inspection OK", content="All clear")
        self.assertEqual(note.site_id, "101")
        self.assertEqual(note.title, "Inspection OK")

    def test_validate_required_fields(self):
        with self.assertRaises(ValueError):
            SiteNote(site_id="", title="", content="")


class TestServiceTask(unittest.TestCase):
    def test_create_task_with_priority(self):
        task = ServiceTask(
            site_id="102",
            task_name="Clean gutter",
            priority=3,
            status="pending"
        )
        self.assertEqual(task.priority, 3)

    def test_status_transitions(self):
        task = ServiceTask(site_id="103", task_name="Test")
        task.mark_pending()
        task.mark_in_progress()
        task.mark_done("Completed today")
        self.assertEqual(task.status, "done")


class TestFollowUp(unittest.TestCase):
    def test_create_follow_up(self):
        fu = FollowUp(
            site_id="104",
            title="Re-check after rain",
            due_date="2025-06-01"
        )
        self.assertEqual(fu.due_date, "2025-06-01")

    def test_overdue_check(self):
        fu = FollowUp(site_id="104", title="Test", due_date="2020-01-01")
        self.assertTrue(fu.is_overdue())


if __name__ == "__main__":
    unittest.main()
