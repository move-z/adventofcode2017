#!/usr/bin/env python3


def distribute(banks):
    banks = banks[:]
    n_banks = len(banks)

    max_idx = 0
    for idx in range(0, n_banks):
        if banks[idx] > banks[max_idx]:
            max_idx = idx

    distr = banks[max_idx]
    each = distr // n_banks
    rem = distr - (n_banks * each)

    for idx in range(0, n_banks):
        relative_idx = idx - max_idx - 1
        if relative_idx < 0:
            relative_idx += n_banks

        new_num = 0 if relative_idx == n_banks - 1 else banks[idx]
        new_num += each
        if relative_idx < rem:
            new_num += 1

        banks[idx] = new_num

    return banks


def calculate(banks):
    collection = []
    num = 0
    while banks not in collection:
        num += 1
        collection.append(banks)
        banks = distribute(banks)

    return num


if __name__ == '__main__':
    res = calculate([0, 2, 7, 0])
    print(">>> %s" % res)
