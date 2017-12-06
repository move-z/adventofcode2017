#!/usr/bin/env python3


def calculate(captcha):
    num = str(captcha)

    result = 0
    last = int(num[-1])
    for char in num:
        digit = int(char)
        if digit == last:
            result += last
        last = digit

    return result


if __name__ == '__main__':
    res = calculate(1122)
    print(">>> %d" % res)

    res = calculate(1111)
    print(">>> %d" % res)

    res = calculate(1234)
    print(">>> %d" % res)

    res = calculate(91212129)
    print(">>> %d" % res)
