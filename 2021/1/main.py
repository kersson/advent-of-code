import sys


def part1(depths: [int]) -> int:
    return sum(1 for i in range(1, len(depths)) if depths[i] > depths[i-1])


def part2(depths: [int]) -> int:
    return sum(1 for i in range(3, len(depths)) if sum(depths[i-2:i+1]) > sum(depths[i-3:i]))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        depths = list(map(int, f))

    print(part1(depths))
    print(part2(depths))
