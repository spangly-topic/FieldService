# === Stage 42: Add CSV export without external dependencies ===
# Project: FieldService
import csv, io, sys, os
from collections import OrderedDict

def export_csv(records, filename=None):
    if not records: return None
    buf = io.StringIO()
    writer = csv.writer(buf)
    for row in records:
        if isinstance(row, dict):
            writer.writerow(list(row.values()))
        else:
            writer.writerow(row)
    text = buf.getvalue()
    out = filename or "fieldservice_export.csv"
    with open(out, 'w', newline='') as f: f.write(text)
    return out

def export_csv_to_memory(records, delimiter=','):
    if not records: return ''
    buf = io.StringIO()
    writer = csv.writer(buf, delimiter=delimiter)
    for row in records:
        if isinstance(row, dict):
            writer.writerow(list(row.values()))
        else:
            writer.writerow(row)
    return buf.getvalue()
