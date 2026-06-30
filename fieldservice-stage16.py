# === Stage 16: Add argparse support for the most common commands ===
# Project: FieldService
import argparse

def main():
    parser = argparse.ArgumentParser(description="FieldService: Field operations notebook")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # New visit command
    visit_parser = subparsers.add_parser('visit', help='Create a new site visit report')
    visit_parser.add_argument('--site', required=True, help='Site identifier or name')
    visit_parser.add_argument('--notes', default='', help='Field notes for the visit')
    visit_parser.add_argument('--photo', action='append', dest='photos', help='Path to photo (becomes a link)')

    # Follow-up command
    followup_parser = subparsers.add_parser('followup', help='Add or update a follow-up task')
    followup_parser.add_argument('--visit-id', required=True, help='ID of the visit to add follow-up to')
    followup_parser.add_argument('--task', required=True, help='Task description for follow-up')

    # Export command
    export_parser = subparsers.add_parser('export', help='Export current notebook state')
    export_parser.add_argument('--format', choices=['json', 'csv'], default='json', help='Output format')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Placeholder logic for command execution (implement specific handlers here)
    print(f"Executing command: {args.command}")
    if hasattr(args, 'site'):
        print(f"Site: {args.site}, Photos: {args.photos or []}")
    elif hasattr(args, 'visit_id'):
        print(f"Follow-up task added for visit {args.visit_id}: {args.task}")
    elif hasattr(args, 'format'):
        print(f"Exporting to {args.format} format")

    return 0

if __name__ == '__main__':
    exit(main())
