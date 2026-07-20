# === Stage 61: Add performance timing for core list and search operations ===
# Project: FieldService
import time

def benchmark_list_and_search(records, query=None):
    """Benchmark list and search operations on a record collection."""
    start = time.perf_counter()
    total = len(records)
    if query:
        filtered = [r for r in records if any(query in str(v) for v in r.values())]
    else:
        filtered = records[:]
    elapsed = time.perf_counter() - start
    return {
        "total_records": total,
        "filtered_count": len(filtered),
        "elapsed_seconds": round(elapsed, 6),
        "throughput_per_sec": round(total / elapsed, 2) if elapsed > 0 else float("inf"),
    }
