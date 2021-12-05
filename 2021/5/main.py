from collections import defaultdict
from itertools import repeat
from typing import Iterator
import sys


def line_range(start: int, end: int) -> Iterator[int]:
    if start == end:
        return repeat(start)
    elif start < end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)


def count_intersections(lines: [((int, int), (int, int))], diag: bool) -> int:
    points = defaultdict(int)
    for line in lines:
        (x1, y1), (x2, y2) = line
        if diag or x1 == x2 or y1 == y2:
            for x, y in zip(line_range(x1, x2), line_range(y1, y2)):
                points[(x, y)] += 1
    return len([1 for count in points.values() if count > 1])


def part1(lines: [((int, int), (int, int))]) -> int:
    return count_intersections(lines, False)


def part2(lines: [((int, int), (int, int))]) -> int:
    return count_intersections(lines, True)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [tuple(map(lambda point: tuple(map(int, point.split(","))), line.split(" -> "))) for line in f]

    print(part1(lines))
    print(part2(lines))
