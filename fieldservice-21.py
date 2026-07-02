# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: FieldService
def archive_record(record_id, target_dir="archive"):
    import os, shutil, datetime
    src_path = f"records/{record_id}.json"
    if not os.path.exists(src_path): return False
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dst_name = f"{target_dir}/{now}_{record_id}.json"
    shutil.move(src_path, dst_name)
    with open(f"records/.archived_{record_id}", "w") as f:
        f.write(dst_name)
    return True

def restore_record(record_id):
    import os, glob
    candidates = glob.glob(f"{target_dir}/{now}_*.json") if (target_dir := next((d for d in ["archive"] if any("records/.archived_" + r.replace(".json", "") in open(r).read()) for r in glob.glob("records/*.json")), None)) else []
    # Simplified restore logic: find exact match by ID in archive dir
    import os, glob
    src = next((p for p in glob.glob(f"archive/*_{record_id}.json") if record_id in p), None)
    if not src: return False
    shutil.move(src, f"records/{record_id}.json")
    os.remove(f"records/.archived_{record_id}")
    return True
