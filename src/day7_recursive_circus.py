#!/usr/bin/env python3


class Program:
    def __init__(self, name, weight, childnames=None):
        self.name = name
        self.weight = weight
        self.childnames = childnames


def calculate(programs):
    children = [x for program in programs if program.childnames for x in program.childnames]
    fathers = {program.name: program for program in programs if program.name not in children}
    assert len(fathers) == 1
    for father in fathers.values():
        return father


if __name__ == '__main__':
    data = (
        Program('pbga', 66),
        Program('xhth', 57),
        Program('ebii', 61),
        Program('havc', 66),
        Program('ktlj', 57),
        Program('fwft', 72, ('ktlj', 'cntj', 'xhth')),
        Program('qoyq', 66),
        Program('padx', 45, ('pbga', 'havc', 'qoyq')),
        Program('tknk', 41, ('ugml', 'padx', 'fwft')),
        Program('jptl', 61),
        Program('ugml', 68, ('gyxo', 'ebii', 'jptl')),
        Program('gyxo', 61),
        Program('cntj', 57)
    )
    res = calculate(data)
    print(">>> %s" % res.name)
