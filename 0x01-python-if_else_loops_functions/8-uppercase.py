#!/usr/bin/python3
def uppercase(str):
    for Ascii in str:
        if ord(Ascii) >= ord('a') and ord(Ascii) <= ord('z'):
            Ascii = chr(ord(Ascii) - 32)
        print("{:s}".format(Ascii), end="")
    print()
