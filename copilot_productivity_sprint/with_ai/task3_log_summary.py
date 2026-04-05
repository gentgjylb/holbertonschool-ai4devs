import sys
import os
from collections import Counter

def summarize_logs(filepath):
    if not os.path.exists(filepath):
        sys.exit(f"Error: {filepath} not found.")

    counts = Counter()
    errors = Counter()

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 4:
                level = parts[2]
                msg = " ".join(parts[3:])
                
                counts[level] += 1
                if level == "ERROR":
                    errors[msg] += 1

    print("Log Summary")
    print("-----------")
    for level in ["INFO", "WARN", "ERROR"]:
        print(f"{level}: {counts[level]}")
    
    print("\nTop 3 Error Messages:")
    for msg, count in errors.most_common(3):
        print(f"- {count}x: {msg}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: python log_summary.py <file>")
    summarize_logs(sys.argv[1])
