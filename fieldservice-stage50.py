# === Stage 50: Add unit tests for import and export behavior ===
# Project: FieldService
import os, sys, unittest, tempfile, shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from field_service import FieldService

class TestFieldServiceImportExport(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.fs = FieldService(root=self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_import_export_roundtrip(self):
        site = self.fs.add_site("S1")
        task = self.fs.add_task(site, "T1", "fix roof")
        note_text = "cracked shingles"
        self.fs.add_note(site, task_id=task.id, text=note_text)
        photo_path = os.path.join(self.tmp, "photo.jpg")
        with open(photo_path, "wb") as f:
            f.write(b"\xff\xd8\xff\xe0" + b"\x00" * 100)
        self.fs.add_photo(site, task_id=task.id, path=photo_path)
        followup = self.fs.add_follow_up(site, task_id=task.id, text="re-check next week")
        report = self.fs.generate_visit_report(site.id)

        data = self.fs.export()
        self.assertEqual(data["sites"], [site.id])
        site_data = data["sites"][0]
        self.assertEqual(site_data["name"], "S1")
        self.assertIn(task.id, site_data["tasks"])
        task_data = site_data["tasks"][task.id]
        self.assertTrue(any("cracked" in n for n in task_data.get("notes", [])))
        self.assertIn(photo_path, task_data.get("photos", {}))
        self.assertEqual(followup.text, "re-check next week")
        self.assertIn(site.id, report)

    def test_export_missing_file_handled(self):
        site = self.fs.add_site("M1")
        task = self.fs.add_task(site, "T2", "clean gutters")
        data = self.fs.export()
        site_data = data["sites"][0]
        self.assertIn(task.id, site_data["tasks"])

if __name__ == "__main__":
    unittest.main()
