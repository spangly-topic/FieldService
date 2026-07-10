# === Stage 38: Add data integrity checks for broken references ===
# Project: FieldService
def check_references(repo_path, report_path=None):
    """Verify that all referenced files exist and are intact."""
    import os
    errors = []
    if report_path:
        with open(report_path) as f:
            for line in f:
                ref = line.strip()
                if ref.startswith("![") or ref.startswith("["):
                    target = ref[ref.index("(")+1:-1]
                    if not os.path.exists(target):
                        errors.append(f"Missing reference: {target}")
    else:
        for root, dirs, files in os.walk(repo_path):
            for fname in files:
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        content = f.read()
                    if "broken" in content.lower():
                        errors.append(f"Integrity issue found in {fpath}")
                except Exception as e:
                    errors.append(f"Error reading {fpath}: {e}")
    return errors
