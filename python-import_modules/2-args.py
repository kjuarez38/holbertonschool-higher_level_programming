#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    print("{} arguments:".format(len - 1))
    for i in range(1, len):
        print("{}: {}".format(i, sys.argv[i]))
