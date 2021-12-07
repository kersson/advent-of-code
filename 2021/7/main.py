from typing import Callable
import sys


def calc_fuel(positions: [int], fuel_func: Callable[[int], int]) -> int:
    return min(sum(fuel_func(abs(p - align)) for p in positions) for align in range(max(positions)))


def part1(positions: [int]) -> int:
    return calc_fuel(positions, lambda d: d)


def part2(positions: [int]) -> int:
    return calc_fuel(positions, lambda d: d * (d + 1) // 2)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        positions = list(map(int, f.readline().rstrip().split(',')))

    print(part1(positions))
    print(part2(positions))
