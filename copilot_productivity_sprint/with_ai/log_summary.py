import sys
import os
from collections import Counter

def run_analytics(filepath):
    if not os.path.exists(filepath):
        sys.exit("Execution Failed: Targeted log file missing.")

    severity_counts = Counter()
    error_cache = Counter()

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            tokens = line.strip().split()
            if len(tokens) >= 4:
                level = tokens[2]
                payload = " ".join(tokens[3:])
                
                severity_counts[level] += 1
                if level == "ERROR":
                    error_cache[payload] += 1

    print("Log Target Summary")
    for level in ["INFO", "WARN", "ERROR"]:
        print(f"{level}: {severity_counts[level]}")
    
    print("\nTop 3 Error Strings:")
    for payload, occurence in error_cache.most_common(3):
        print(f"- {occurence}x: {payload}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage Constraints: python log_summary.py <filepath>")
    run_analytics(sys.argv[1])
