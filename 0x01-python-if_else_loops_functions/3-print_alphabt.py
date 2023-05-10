#!/usr/bin/python3
for Ascii in range(97, 123):
    if chr(Ascii) not in ('q', 'e'):
        print("{}".format(chr(Ascii)), end="")
