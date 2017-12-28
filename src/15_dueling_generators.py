#!/usr/bin/env python3


def first(init1, init2):
    good = 0

    def factory(seed):
        def generator(initial):
            n = initial
            while True:
                n = (n * seed) % 2147483647
                yield n

        return generator

    gen1 = factory(16807)(init1)
    gen2 = factory(48271)(init2)

    for i in range(40_000_000):
        if (0xFFFF & next(gen1)) == (0xFFFF & next(gen2)):
            good += 1

    return good


def second(init1, init2):
    good = 0

    def factory(seed, denom):
        def generator(initial):
            n = initial
            while True:
                n = (n * seed) % 2147483647
                if (n % denom) == 0:
                    yield n

        return generator

    gen1 = factory(16807, 4)(init1)
    gen2 = factory(48271, 8)(init2)

    for i in range(5_000_000):
        if (0xFFFF & next(gen1)) == (0xFFFF & next(gen2)):
            good += 1

    return good


if __name__ == '__main__':
    res = first(618, 814)
    print(">>> %s" % res)

    res = second(618, 814)
    print(">>> %s" % res)
