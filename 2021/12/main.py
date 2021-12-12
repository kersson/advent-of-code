from collections import defaultdict
from typing import Callable
import sys


def part1_is_valid_cave(cave: str, path: list[str]) -> bool:
    return cave.isupper() or cave not in path


def part2_is_valid_cave(cave: str, path: list[str]) -> bool:
    if cave == 'start':
        return False
    if part1_is_valid_cave(cave, path):
        return True
    small_caves = set()
    for sc in (c for c in path if c.islower()):
        if sc in small_caves:
            return False
        else:
            small_caves.add(sc)
    return True


def count_paths(cave_map: dict[str, set[str]], is_valid_cave: Callable[[str, list[str]], bool]) -> int:
    path_count = 0
    paths: list[list[str]] = [['start']]
    
    while paths:
        new_paths = []
        for path in paths:
            if path[-1] == 'end':
                path_count += 1
            else:
                new_paths.extend(
                    path.copy() + [cave]
                    for cave in cave_map[path[-1]]
                    if is_valid_cave(cave, path)
                )   
        paths = new_paths

    return path_count


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        cave_map: dict[str, set[str]] = defaultdict(set)
        for line in f:
            cave1, cave2 = line.rstrip().split('-')
            cave_map[cave1].add(cave2)
            cave_map[cave2].add(cave1)

    print(count_paths(cave_map, part1_is_valid_cave))
    print(count_paths(cave_map, part2_is_valid_cave))
