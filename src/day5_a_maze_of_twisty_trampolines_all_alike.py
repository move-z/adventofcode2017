#!/usr/bin/env python3


def calculate(steps):
    index = 0
    counter = 0

    while 0 <= index < len(steps):
        cur = steps[index]
        steps[index] += 1
        index += cur
        counter += 1

    return counter


if __name__ == '__main__':
    res = calculate([0, 3, 0, 1, -3])
    print(">>> %s" % res)
