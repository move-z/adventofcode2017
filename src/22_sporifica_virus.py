#!/usr/bin/env python3
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def turn_right(self):
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.UP

    def turn_left(self):
        if self == Direction.UP:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.UP

    def reverse(self):
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.LEFT:
            return Direction.RIGHT
        elif self == Direction.DOWN:
            return Direction.UP
        elif self == Direction.RIGHT:
            return Direction.LEFT


class Status(Enum):
    CLEAN = auto()
    WEAKENED = auto()
    INFECTED = auto()
    FLAGGED = auto()

    def __next__(self):
        if self == Status.CLEAN:
            return Status.WEAKENED
        elif self == Status.WEAKENED:
            return Status.INFECTED
        elif self == Status.INFECTED:
            return Status.FLAGGED
        elif self == Status.FLAGGED:
            return Status.CLEAN


def first(nodemap):
    nodemap = [[True if x == '#' else False for x in line] for line in nodemap.split()]

    direction = Direction.UP
    position = len(nodemap) // 2, len(nodemap) // 2

    infections = 0

    for cycle in range(10000):
        x, y = position
        if nodemap[y][x]:
            direction = direction.turn_right()
            nodemap[y][x] = False
        else:
            direction = direction.turn_left()
            nodemap[y][x] = True
            infections += 1

        if direction == Direction.UP:
            y -= 1
        elif direction == Direction.DOWN:
            y += 1
        elif direction == Direction.LEFT:
            x -= 1
        elif direction == Direction.RIGHT:
            x += 1

        if y < 0:
            nodemap.insert(0, [False for i in range(len(nodemap[0]))])
            y = 0
        elif y >= len(nodemap):
            nodemap.append([False for i in range(len(nodemap[0]))])
        elif x < 0:
            for line in nodemap:
                line.insert(0, False)
            x = 0
        elif x >= len(nodemap[0]):
            for line in nodemap:
                line.append(False)

        position = x, y

    return infections


def second(nodemap):
    nodemap = [[Status.INFECTED if x == '#' else Status.CLEAN for x in line] for line in nodemap.split()]

    direction = Direction.UP
    position = len(nodemap) // 2, len(nodemap) // 2

    infections = 0

    for cycle in range(10_000_000):
        x, y = position
        current_node = nodemap[y][x]

        if current_node == Status.CLEAN:
            direction = direction.turn_left()
        elif current_node == Status.INFECTED:
            direction = direction.turn_right()
        elif current_node == Status.FLAGGED:
            direction = direction.reverse()

        status = next(nodemap[y][x])
        if status == Status.INFECTED:
            infections += 1
        nodemap[y][x] = status

        if direction == Direction.UP:
            y -= 1
        elif direction == Direction.DOWN:
            y += 1
        elif direction == Direction.LEFT:
            x -= 1
        elif direction == Direction.RIGHT:
            x += 1

        if y < 0:
            nodemap.insert(0, [Status.CLEAN for i in range(len(nodemap[0]))])
            y = 0
        elif y >= len(nodemap):
            nodemap.append([Status.CLEAN for i in range(len(nodemap[0]))])
        elif x < 0:
            for line in nodemap:
                line.insert(0, Status.CLEAN)
            x = 0
        elif x >= len(nodemap[0]):
            for line in nodemap:
                line.append(Status.CLEAN)

        position = x, y

    return infections


if __name__ == '__main__':
    data = ("""
...#.##.#.#.#.#..##.###.#
......##.....#####..#.#.#
#..####.######.#.#.##...#
...##..####........#.#.#.
.#.#####..#.....#######..
.#...#.#.##.#.#.....#....
.#.#.#.#.#####.#.#..#...#
###..##.###.#.....#...#.#
#####..#.....###.....####
#.##............###.#.###
#...###.....#.#.##.#..#.#
.#.###.##..#####.....####
.#...#..#..###.##..#....#
##.##...###....##.###.##.
#.##.###.#.#........#.#..
##......#..###.#######.##
.#####.##..#..#....##.##.
###..#...#..#.##..#.....#
##..#.###.###.#...##...#.
##..##..##.###..#.##..#..
...#.#.###..#....##.##.#.
##.##..####..##.##.##.##.
#...####.######.#...##...
.###..##.##..##.####....#
#.##....#.#.#..#.###..##.
""")[1:-1]

    res = first(data)
    print(">>> %s" % res)

    res = second(data)
    print(">>> %s" % res)
