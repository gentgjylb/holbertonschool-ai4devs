#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ./count_words.py <filename>")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        words = content.split()
        print(len(words))
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
