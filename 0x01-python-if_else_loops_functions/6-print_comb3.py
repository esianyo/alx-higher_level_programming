#!/usr/bin/python3
for com in range(10):
    for second in range(com + 1, 10):
        print("{:d}{:d}".format(com, second), end="")
        if com == 8 and second == 9:
            print()
        else:
            print(", ", end="")
