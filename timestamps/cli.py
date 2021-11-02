#!/usr/bin/python3

from datetime import *
import sys


def main():
    format = '%Y-%m-%d %H:%M:%S '
    
    for line in sys.stdin:
        timestamp = datetime.now().strftime(format)
        print(timestamp + line.rstrip("\n"), flush=True)


if __name__ == '__main__':
    main()
