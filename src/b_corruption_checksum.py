#!/usr/bin/env python3


def calculate(table):
    result = 0
    for row in table:
        lower = min(row)
        upper = max(row)
        result += upper - lower
    return result


if __name__ == '__main__':
    table = [[5, 1, 9, 5],
             [7, 5, 3],
             [2, 4, 6, 8]]
    res = calculate(table)
    print(">>> %d" % res)
