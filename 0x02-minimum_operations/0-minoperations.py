#!/usr/bin/python3
"""The minimum operations coding challenge"""


def minOperations(n):
    """Computes the fewest number of operations"""
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            # init
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
    return ops_count
