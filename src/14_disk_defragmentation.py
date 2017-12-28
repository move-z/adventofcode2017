#!/usr/bin/env python3
from functools import reduce


def knot_hash(in_string, list_size=256):
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

    return ''.join([("{0:08b}".format(x)) for x in dense])


def first(key):
    used = 0
    for i in range(0, 128):
        seed = "%s-%d" % (key, i)
        row = knot_hash(seed)
        used += row.count("1")
    return used


def second(key):
    rows = []
    next_region = 1

    for i in range(0, 128):
        seed = "%s-%d" % (key, i)
        row_str = knot_hash(seed)
        row = [1 if x == '1' else 0 for x in row_str]

        for idx in range(0, len(row)):
            if not row[idx]:
                continue

            prev_region = 0
            if idx > 0 and row[idx-1]:
                prev_region = row[idx-1]
            upper_region = 0
            if rows and rows[-1][idx]:
                upper_region = rows[-1][idx]

            if not prev_region and not upper_region:
                region = next_region
                next_region += 1
            elif not upper_region:
                region = prev_region
            elif not prev_region:
                region = upper_region
            elif prev_region == upper_region:
                region = prev_region
            else:
                region = min(prev_region, upper_region)
                # fondo le 2 regioni
                delete = max(prev_region, upper_region)
                for r in rows + [row]:
                    for p in range(0, len(r)):
                        if r[p] == delete:
                            r[p] = region
                        elif r[p] > delete:
                            r[p] -= 1
                next_region -= 1

            row[idx] = region

        rows.append(row)

    return next_region - 1


if __name__ == '__main__':
    res = first('vbqugkhl')
    print(">>> %s" % res)

    res = second('vbqugkhl')
    print(">>> %s" % res)
