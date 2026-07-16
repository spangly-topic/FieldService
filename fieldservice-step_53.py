# === Stage 53: Add command help text and usage examples ===
# Project: FieldService
def print_help():
    """Print usage help and examples for FieldService."""
    print("FieldService - Field Operations Notebook")
    print("=" * 40)
    print("\nUsage:")
    print("  python field_service.py <command>")
    print()
    print("Commands:")
    print("  notes       - Add or view site notes (e.g. 'add', 'list')")
    print("  tasks       - Manage service tasks (e.g. 'add', 'complete', 'list')")
    print("  photos      - Link photos to sites via URL")
    print("  followups   - Track pending actions and deadlines")
    print("  reports     - Generate visit reports with summary stats")
    print()
    print("Examples:")
    print('  python field_service.py notes add "Inspected north fence"')
    print('  python field_service.py tasks list')
    print('  python field_service.py photos link https://example.com/img.jpg --site "Gate A"')
    print('  python field_service.py followups overdue')
    print('  python field_service.py reports weekly')
