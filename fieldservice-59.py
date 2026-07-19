# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: FieldService
def bulk_delete_records(self, table_name: str, confirmation_flag: bool = True) -> int:
    """Delete multiple records from a table with an optional confirmation guard."""
    if confirmation_flag:
        response = input(f"Are you sure you want to delete all records from '{table_name}'? (yes/no): ")
        if response.lower() != "yes":
            print("Deletion cancelled.")
            return 0
    count = self._execute(
        f"DELETE FROM {self.escape(table_name)} WHERE 1=1",
        table_name=table_name,
    )
    return count
