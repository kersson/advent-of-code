from itertools import product
from math import prod
import sys


def is_low_point(row: int, col: int, depth_map: [[int]]) -> bool:
    height = depth_map[row][col]
    return all(
        height < depth_map[r][c]
        for r, c in [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
        if 0 <= r < len(depth_map) and 0 <= c < len(depth_map[r])
    )


def find_low_points(depth_map: [[int]]) -> [(int, int)]:
    return [
        (row, col)
        for row, col in product(range(len(depth_map)), range(len(depth_map[0])))
        if is_low_point(row, col, depth_map)
    ]


def find_uphill_points(row: int, col: int, depth_map: [[int]]) -> {(int, int)}:
    return {
        (r, c)
        for r, c in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
        if 0 <= r < len(depth_map) and 0 <= c < len(depth_map[r]) and depth_map[row][col] <= depth_map[r][c] < 9
    }


def get_basin_size(row: int, col: int, depth_map: [[int]]) -> int:
    points = {(row, col)}
    new_points = find_uphill_points(row, col, depth_map)
    while len(new_points) > 0:
        point = new_points.pop()
        points.add(point)
        new_points.update(find_uphill_points(*point, depth_map) - points)
    return len(points)


def part1(depth_map: [[int]]) -> int:
    return sum(
        1 + depth_map[row][col]
        for row, col in find_low_points(depth_map)
    )


def part2(depth_map: [[int]]) -> int:
    basin_sizes = [get_basin_size(row, col, depth_map) for row, col in find_low_points(depth_map)]
    basin_sizes.sort(reverse=True)
    return prod(basin_sizes[0:3])


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        depth_map = [list(map(int, line.rstrip())) for line in f]

    print(part1(depth_map))
    print(part2(depth_map))
