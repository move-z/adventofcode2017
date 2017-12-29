#!/usr/bin/env python3


def first(step):
    buffer = [0]
    idx = 0
    curr = 0

    for i in range(2017):
        idx += step
        if idx >= len(buffer):
            idx -= len(buffer)
        idx += 1
        curr += 1
        buffer.insert(idx, curr)

    idx += 1
    if idx >= len(buffer):
        idx = 0
    return buffer[idx]


def second(step):
    idx = 0
    curr = 0
    result = 0

    for i in range(50_000_000):
        idx += step
        if idx > i:
            idx %= i + 1
        idx += 1
        curr += 1
        if idx == 1:
            result = curr

    return result


if __name__ == '__main__':
    res = first(324)
    print(">>> %s" % res)

    res = second(324)
    print(">>> %s" % res)
