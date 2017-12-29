#!/usr/bin/env python3
from collections import defaultdict


def first(*instructions):
    registers = defaultdict(lambda: 0)
    current = 0
    last_played = None

    instructions = [x.split() for x in instructions]

    while True:
        instruction = instructions[current]

        operation = instruction[0]
        register = instruction[1]
        try:
            reg_value = int(register)
        except ValueError:
            reg_value = registers[register]
        if len(instruction) > 2:
            try:
                value = int(instruction[2])
            except ValueError:
                value = registers[instruction[2]]
        else:
            value = None

        if operation == 'snd':
            last_played = reg_value
        elif operation == 'set':
            registers[register] = value
        elif operation == 'add':
            registers[register] += value
        elif operation == 'mul':
            registers[register] *= value
        elif operation == 'mod':
            registers[register] %= value
        elif operation == 'rcv':
            if reg_value > 0:
                return last_played
        elif operation == 'jgz':
            if reg_value > 0:
                current += value
                continue

        current += 1


def second(*instructions):
    instructions = [x.split() for x in instructions]

    class Program:
        def __init__(self, pid):
            self.registers = defaultdict(lambda: 0)
            self.registers['p'] = pid
            self.current = 0
            self.queue = []
            self.linked = []
            self.sent = 0

        def done(self):
            return self.current >= len(instructions)

        def link(self, program):
            self.linked.append(program)

        def execute(self):
            while not self.done():
                instruction = instructions[self.current]

                operation = instruction[0]
                register = instruction[1]
                try:
                    reg_value = int(register)
                except ValueError:
                    reg_value = self.registers[register]
                if len(instruction) > 2:
                    try:
                        value = int(instruction[2])
                    except ValueError:
                        value = self.registers[instruction[2]]
                else:
                    value = None

                if operation == 'set':
                    self.registers[register] = value
                elif operation == 'add':
                    self.registers[register] += value
                elif operation == 'mul':
                    self.registers[register] *= value
                elif operation == 'mod':
                    self.registers[register] %= value
                elif operation == 'snd':
                    self.sent += 1
                    for program in self.linked:
                        program.queue.append(reg_value)
                elif operation == 'rcv':
                    # se la coda è vuota resto in busy waiting
                    if not self.queue:
                        return
                    self.registers[register] = self.queue.pop(0)
                elif operation == 'jgz':
                    if reg_value > 0:
                        self.current += value
                        continue

                self.current += 1

    a, b = Program(0), Program(1)
    a.link(b)
    b.link(a)

    while True:
        if not a.done():
            a.execute()
        if not b.done():
            b.execute()
        if a.done() and b.done():
            break
        if not a.queue and not b.queue:
            # deadlock
            break

    return b.sent


if __name__ == '__main__':
    data = (
        'set i 31',
        'set a 1',
        'mul p 17',
        'jgz p p',
        'mul a 2',
        'add i -1',
        'jgz i -2',
        'add a -1',
        'set i 127',
        'set p 952',
        'mul p 8505',
        'mod p a',
        'mul p 129749',
        'add p 12345',
        'mod p a',
        'set b p',
        'mod b 10000',
        'snd b',
        'add i -1',
        'jgz i -9',
        'jgz a 3',
        'rcv b',
        'jgz b -1',
        'set f 0',
        'set i 126',
        'rcv a',
        'rcv b',
        'set p a',
        'mul p -1',
        'add p b',
        'jgz p 4',
        'snd a',
        'set a b',
        'jgz 1 3',
        'snd b',
        'set f 1',
        'add i -1',
        'jgz i -11',
        'snd a',
        'jgz f -16',
        'jgz a -19',
    )

    res = first(*data)
    print(">>> %s" % res)

    res = second(*data)
    print(">>> %s" % res)
