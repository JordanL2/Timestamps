#!/usr/bin/python3

import argparse
from datetime import *
import sys


def main():
    parser = argparse.ArgumentParser(prog='timestamps')
    parser.add_argument('-f', '--format', dest='format',  nargs='?', type=str, default='%Y-%m-%d %H:%M:%S ', help='Timestamp format')
    parser.add_argument('-t', '--total', dest='total', action='store_true', default=False, help='Display total time taken at the end')
    args = parser.parse_args()
    timestamp_format = args.format
    total = args.total
    
    start = datetime.now()
    for line in sys.stdin:
        timestamp = datetime.now().strftime(timestamp_format)
        print(timestamp + line.rstrip("\n"), flush=True)
    
    if total:
        end = datetime.now()
        diff = end - start
        print(diff)

if __name__ == '__main__':
    main()
