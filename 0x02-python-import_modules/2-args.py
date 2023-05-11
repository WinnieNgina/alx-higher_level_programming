#!/usr/bin/python3
import sys
counter = 1

if __name__ == '__main__':
    if (len(sys.argv) == 2):    # handle 1 argument
        print(f"{(len(sys.argv) - 1):d} argument:")
    elif (len(sys.argv) == 1):  # handle 0 arguments
        print(f"{(len(sys.argv) - 1):d} arguments.")
    else:   # handle more than 1 argument
        print(f"{(len(sys.argv) - 1):d} arguments:")
    if (len(sys.argv) != 1):    # don't print if 0 args passed
        for args in sys.argv:
            if (counter != 1):
                print(f"{(counter - 1):d}: {args}")
            counter += 1
