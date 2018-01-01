#!/usr/bin/env python3


class Component:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def weight(self):
        return self.a + self.b

    def attaches(self, port):
        if self.a == port:
            return self.b
        if self.b == port:
            return self.a
        return None


def first(*components):
    def get_max(available, root, port):
        own_weight = 0
        if root is not None:
            available = available - {root}
            own_weight = root.weight()
        good = [x for x in available if x.attaches(port) is not None]
        if not good:
            return own_weight
        return own_weight + max([get_max(available, x, x.attaches(port)) for x in good])

    return get_max(set(components), None, 0)


def second(*components):
    def get_chains(available, root, port):
        own_weight = 0
        if root is not None:
            available = available - {root}
            own_weight = root.weight()
        good = [x for x in available if x.attaches(port) is not None]
        if not good:
            return 1, own_weight
        chains = [get_chains(available, x, x.attaches(port)) for x in good]
        length = max(chains, key=lambda x: x[0])[0]
        chains = [x for x in chains if x[0] == length]
        weight = max(chains, key=lambda x: x[1])[1]
        return 1 + length, own_weight + weight

    result = get_chains(set(components), None, 0)
    return result[1]


if __name__ == '__main__':
    data = (
        Component(31, 13),
        Component(34, 4),
        Component(49, 49),
        Component(23, 37),
        Component(47, 45),
        Component(32, 4),
        Component(12, 35),
        Component(37, 30),
        Component(41, 48),
        Component(0, 47),
        Component(32, 30),
        Component(12, 5),
        Component(37, 31),
        Component(7, 41),
        Component(10, 28),
        Component(35, 4),
        Component(28, 35),
        Component(20, 29),
        Component(32, 20),
        Component(31, 43),
        Component(48, 14),
        Component(10, 11),
        Component(27, 6),
        Component(9, 24),
        Component(8, 28),
        Component(45, 48),
        Component(8, 1),
        Component(16, 19),
        Component(45, 45),
        Component(0, 4),
        Component(29, 33),
        Component(2, 5),
        Component(33, 9),
        Component(11, 7),
        Component(32, 10),
        Component(44, 1),
        Component(40, 32),
        Component(2, 45),
        Component(16, 16),
        Component(1, 18),
        Component(38, 36),
        Component(34, 24),
        Component(39, 44),
        Component(32, 37),
        Component(26, 46),
        Component(25, 33),
        Component(9, 10),
        Component(0, 29),
        Component(38, 8),
        Component(33, 33),
        Component(49, 19),
        Component(18, 20),
        Component(49, 39),
        Component(18, 39),
        Component(26, 13),
        Component(19, 32)
    )

    res = first(*data)
    print(">>> %s" % res)

    res = second(*data)
    print(">>> %s" % res)
