#!/usr/bin/python3
"""Logs parse"""


import sys


def print_metrics(total_size, status_counts):
    """Prints the computed metrics."""
    print("File size: {:d}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print("{:s}: {:d}".format(status_code, count))


def compute_metrics():
    """Reads stdin line by line and computes metrics."""
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            line = line.strip()
            elements = line.split(" ")
            if len(elements) >= 7:
                size = int(elements[-1])
                status_code = elements[-2]
                total_size += size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1
            if i % 10 == 0:
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)

compute_metrics()
