# === Stage 44: Add backup creation for the data file ===
# Project: FieldService
def create_backup(filepath, backup_dir="backups"):
    """Create a timestamped backup of the data file."""
    import shutil, os, datetime
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    src = os.path.abspath(filepath)
    dst = os.path.join(os.path.abspath(backup_dir), f"fieldservice_backup_{ts}.dat")
    shutil.copy2(src, dst)
    return dst

def restore_from_backup(backups_dir="backups"):
    """Restore the latest backup into a temporary location for review."""
    import glob, os
    if not os.path.isdir(backups_dir):
        print("No backups directory found.")
        return None
    candidates = sorted(glob.glob(os.path.join(backups_dir, "fieldservice_backup_*.dat")), reverse=True)
    if not candidates:
        print("No backup files found.")
        return None
    latest = candidates[0]
    tmp = os.path.join(backups_dir, f"restored_{os.path.basename(latest)}")
    shutil.copy2(latest, tmp)
    return tmp
