import sys
import os
from collections import Counter

def process_logs(filepath):
    """
    Parses CLI argument path, validates it independently and calculates line configurations 
    while bypassing broken error formatting smoothly.
    """
    if not os.path.isfile(filepath):
        print(f"Error: Log file '{filepath}' definitively not found or invalid format constraints.")
        sys.exit(1)

    counts = {"INFO": 0, "WARN": 0, "ERROR": 0}
    error_messages = Counter()

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            # Format Expected: YYYY-MM-DD HH:MM:SS LEVEL Message...
            if len(parts) >= 4:
                level = parts[2]
                message = " ".join(parts[3:])
                
                # Dynamic matching gracefully bypasses non-system lines without exception throwing 
                if level in counts:
                    counts[level] += 1
                if level == "ERROR":
                    error_messages[message] += 1

    # Printing formatting
    print("Log Target Summary")
    print("------------------")
    print(f"INFO: {counts['INFO']}")
    print(f"WARN: {counts['WARN']}")
    print(f"ERROR: {counts['ERROR']}\n")
    
    print("Top 3 Error Root Messages:")
    top_errors = error_messages.most_common(3)
    if not top_errors:
        print("None Registered")
    else:
        for msg, count in top_errors:
            print(f"- {count}x: {msg}")

if __name__ == '__main__':
    # Argument path bindings parsing requirement handling
    if len(sys.argv) < 2:
        print("Argument Missing! Usage Command: python3 log_summary.py <path-to-log-file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    process_logs(file_path)
