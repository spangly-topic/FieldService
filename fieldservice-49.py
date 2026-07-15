# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: FieldService
import unittest
from datetime import datetime, timedelta

class TestUpdateDelete(unittest.TestCase):
    def setUp(self):
        from models import SiteNote
        self.note = SiteNote(
            id=1,
            title="Test",
            body="Hello",
            site_id=42,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

    def test_update_changes_title(self):
        from models import update_site_note
        now = datetime.now()
        self.note.title = "Updated"
        result = update_site_note(1, {"title": "Updated"}, now)
        self.assertEqual(result["title"], "Updated")
        self.assertEqual(result["updated_at"], now)

    def test_update_preserves_created(self):
        from models import update_site_note
        now = datetime.now()
        result = update_site_note(1, {"body": "Changed"}, now)
        self.assertEqual(result["created_at"], self.note.created_at)

    def test_delete_returns_success(self):
        from models import delete_site_note
        result = delete_site_note(1)
        self.assertTrue(result)

    def test_delete_nonexistent_raises(self):
        from models import delete_site_note
        with self.assertRaises(Exception):
            delete_site_note(999)

if __name__ == "__main__":
    unittest.main()
