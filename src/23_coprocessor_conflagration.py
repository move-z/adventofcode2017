#!/usr/bin/env python3


def first(*steps):
    register_names = "abcdefgh"
    registers = {x: 0 for x in register_names}
    mul = 0

    counter = 0
    while True:
        if counter < 0 or counter >= len(steps):
            break

        step = steps[counter]

        operation, reg, value = step.split()

        if value in register_names:
            value = registers[value]
        else:
            value = int(value)

        if operation == 'set':
            registers[reg] = value
        elif operation == 'sub':
            registers[reg] -= value
        elif operation == 'mul':
            registers[reg] *= value
            mul += 1
        elif operation == 'jnz':
            test = registers[reg] if reg in register_names else int(reg)
            if test != 0:
                counter += value
                continue

        counter += 1

    return mul


def second():
    def prime(x):
        for a in range(2, x):
            if x % a == 0:
                return False
        return True

    return len([x for x in range(108100, 125101, 17) if not prime(x)])


if __name__ == '__main__':
    data = (
        'set b 81',
        'set c b',
        'jnz a 2',
        'jnz 1 5',
        'mul b 100',
        'sub b -100000',
        'set c b',
        'sub c -17000',
        'set f 1',
        'set d 2',
        'set e 2',
        'set g d',
        'mul g e',
        'sub g b',
        'jnz g 2',
        'set f 0',
        'sub e -1',
        'set g e',
        'sub g b',
        'jnz g -8',
        'sub d -1',
        'set g d',
        'sub g b',
        'jnz g -13',
        'jnz f 2',
        'sub h -1',
        'set g b',
        'sub g c',
        'jnz g 2',
        'jnz 1 3',
        'sub b -17',
        'jnz 1 -23'
    )

    res = first(*data)
    print(">>> %s" % res)

    res = second()
    print(">>> %s" % res)
