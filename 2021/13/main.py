import sys


def do_fold(points: set[tuple[int, int]], axis: str, value: int) -> set[tuple[int, int]]:
    if axis == 'x':
        return {(x, y) if x < value else (value - (x - value), y) for x, y in points}
    elif axis == 'y':
        return {(x, y) if y < value else (x, value - (y - value)) for x, y in points}


def part1(points: set[tuple[int, int]], folds: list[tuple[str, int]]) -> int:
    return len(do_fold(points, *folds[0]))


def part2(points: set[tuple[int, int]], folds: list[tuple[str, int]]) -> str:
    for fold in folds:
        points = do_fold(points, *fold)

    paper = ""
    for y in range(max(points, key=lambda p: p[1])[1] + 1):
        for x in range(max(points, key=lambda p: p[0])[0] + 1):
            paper += "█" if (x, y) in points else " "
        paper += "\n"

    return paper


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        points = set()
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            points.add(tuple(map(int, line.split(','))))

        folds = []
        for line in f:
            line = line.lstrip('fold along ').rstrip().split('=')
            folds.append((line[0], int(line[1])))

    print(part1(points, folds))
    print(part2(points, folds))
