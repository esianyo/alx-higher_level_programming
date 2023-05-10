#!/usr/bin/python3
for com in range(10):
    for second in range(com + 1, 10):
        print("{:02d}, ".format(com * 10 + second), end=" ")
