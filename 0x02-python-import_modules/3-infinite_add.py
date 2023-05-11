#!/usr/bin/python3
import sys

counter = 0
total = 0

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        total += int(arg)
        counter += 1

    if counter == 0:
        print("{:d}".format(total))
    else:
        print("{:d}".format(total))
