#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("0 arguments")
        print(".")
    else:
        print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))
        for num, argz in enumerate(args):
            print("{}: {}".format(num + 1, argz))
