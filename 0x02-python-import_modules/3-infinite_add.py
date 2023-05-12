#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    out = 0

    for argz in args:
        out = out + int(argz)
    print(out)
