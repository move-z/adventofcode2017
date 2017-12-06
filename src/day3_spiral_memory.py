#!/usr/bin/env python3
import sys


def calculate(address):
    # calcolo in che livello è finito il mio elemento
    level = 0
    side_size = 0
    base_addr = 0

    for level in range(0, sys.maxsize):
        side_size = 2 * level + 1
        base_addr = side_size ** 2
        if base_addr >= address:
            break

    # trovo il centro del lato
    while base_addr > address:
        base_addr -= side_size - 1
    base_addr += (side_size - 1) / 2

    return abs(address - base_addr) + level


if __name__ == '__main__':
    res = calculate(1)
    print(">>> %d" % res)

    res = calculate(12)
    print(">>> %d" % res)

    res = calculate(23)
    print(">>> %d" % res)

    res = calculate(1024)
    print(">>> %d" % res)
