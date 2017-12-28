#!/usr/bin/env python3


class Level:
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.period = range * 2 - 2

    def at_top(self, time):
        if time == 0 or time % self.period == 0:
            return True
        else:
            return False


def first(*levels):
    levels = sorted(levels, key=lambda x: x.depth)
    severity = 0
    curr_depth = 0
    curr_level_idx = 0
    curr_level = levels[curr_level_idx]

    while curr_depth <= levels[-1].depth:
        while curr_level.depth < curr_depth and curr_level_idx < len(levels):
            curr_level_idx += 1
            curr_level = levels[curr_level_idx]

        if curr_level.depth == curr_depth and curr_level.at_top(curr_depth):
            severity += curr_level.depth * curr_level.range

        curr_depth += 1

    return severity


def second(*levels):
    levels = sorted(levels, key=lambda x: x.depth)
    delay = 0

    while True:
        curr_depth = 0
        curr_level_idx = 0
        curr_level = levels[curr_level_idx]

        try:
            while curr_depth <= levels[-1].depth:
                while curr_level.depth < curr_depth and curr_level_idx < len(levels):
                    curr_level_idx += 1
                    curr_level = levels[curr_level_idx]

                if curr_level.depth == curr_depth and curr_level.at_top(delay + curr_depth):
                    raise StopIteration

                curr_depth += 1

            return delay

        except StopIteration:
            delay += 1


if __name__ == '__main__':
    data = (
        Level(0, 4),
        Level(1, 2),
        Level(2, 3),
        Level(4, 4),
        Level(6, 6),
        Level(8, 5),
        Level(10, 6),
        Level(12, 6),
        Level(14, 6),
        Level(16, 12),
        Level(18, 8),
        Level(20, 9),
        Level(22, 8),
        Level(24, 8),
        Level(26, 8),
        Level(28, 8),
        Level(30, 12),
        Level(32, 10),
        Level(34, 8),
        Level(36, 12),
        Level(38, 10),
        Level(40, 12),
        Level(42, 12),
        Level(44, 12),
        Level(46, 12),
        Level(48, 12),
        Level(50, 14),
        Level(52, 14),
        Level(54, 12),
        Level(56, 12),
        Level(58, 14),
        Level(60, 14),
        Level(62, 14),
        Level(66, 14),
        Level(68, 14),
        Level(70, 14),
        Level(72, 14),
        Level(74, 14),
        Level(78, 18),
        Level(80, 14),
        Level(82, 14),
        Level(88, 18),
        Level(92, 17)
    )

    res = first(*data)
    print(">>> %s" % res)

    res = second(*data)
    print(">>> %s" % res)
