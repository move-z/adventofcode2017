#!/usr/bin/env python3
from functools import reduce


def first(*lengths, list_size=256):
    lis = list(range(list_size))
    cur = 0
    skip = 0
    for length in lengths:
        if cur + length <= list_size:
            selected = list(range(cur, cur + length))
        else:
            selected = list(range(cur, list_size))
            remain = cur + length - list_size
            while remain > list_size:
                selected.extend(lis)
                remain -= list_size
            selected.extend(range(0, remain))

        for i in range(0, len(selected) // 2):
            v = lis[selected[i]]
            lis[selected[i]] = lis[selected[-i - 1]]
            lis[selected[-i - 1]] = v

        cur += length + skip
        cur %= list_size
        skip += 1

    return lis[0] * lis[1]


def second(in_string, list_size=256):
    lis = list(range(list_size))
    lengths = [ord(c) for c in in_string]
    lengths.extend((17, 31, 73, 47, 23))
    cur = 0
    skip = 0

    for n in range(64):
        for length in lengths:
            if cur + length <= list_size:
                selected = list(range(cur, cur + length))
            else:
                selected = list(range(cur, list_size))
                remain = cur + length - list_size
                while remain > list_size:
                    selected.extend(lis)
                    remain -= list_size
                selected.extend(range(0, remain))

            for i in range(0, len(selected) // 2):
                v = lis[selected[i]]
                lis[selected[i]] = lis[selected[-i - 1]]
                lis[selected[-i - 1]] = v

            cur += length + skip
            cur %= list_size
            skip += 1

    dense = []
    while len(lis) > 0:
        chunk, lis = lis[0:16], lis[16:]
        n = reduce(lambda x, y: x ^ y, chunk)
        dense.append(n)

    return ''.join([("%02X" % x).lower() for x in dense])


if __name__ == '__main__':
    res = first(157, 222, 1, 2, 177, 254, 0, 228, 159, 140, 249, 187, 255, 51, 76, 30)
    print(">>> %s" % res)

    res = second("157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30")
    print(">>> %s" % res)

