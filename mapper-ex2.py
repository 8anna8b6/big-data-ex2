#!/usr/bin/env python
"""mapper.py"""

import sys

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # Normalize the word:
            # 1. convert to lowercase
            # 2. strip trailing commas and dots
            clean = word.lower().rstrip(',.')
            
            if clean:  # avoid empty strings
                print('%s%s%d' % (clean, separator, 1))

if __name__ == "__main__":
    main()
