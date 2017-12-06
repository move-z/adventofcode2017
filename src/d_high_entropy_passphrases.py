#!/usr/bin/env python3


def calculate(passphrase):
    words = passphrase.split()
    distinct = set(words)
    return len(distinct) == len(words)


if __name__ == '__main__':
    res = calculate("aa bb cc dd ee")
    print(">>> %s" % res)

    res = calculate("aa bb cc dd aa")
    print(">>> %s" % res)

    res = calculate("aa bb cc dd aaa")
    print(">>> %s" % res)
