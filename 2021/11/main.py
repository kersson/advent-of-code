from copy import deepcopy
from itertools import product
import sys

FLASH_ENERGY = 10


def step(energies: [[int]]) -> int:
    for row in energies:
        for col in range(len(row)):
            row[col] += 1

    flashes = {
        (row, col)
        for row, col in product(range(len(energies)), range(len(energies[0])))
        if energies[row][col] == FLASH_ENERGY
    }
    while flashes:
        r, c = flashes.pop()
        flashed = {
            (row, col)
            for row, col in [
                (r-1, c-1), (r+1, c+1), (r-1, c+1), (r+1, c-1),
                (r, c-1), (r, c+1), (r-1, c), (r+1, c)
            ]
            if 0 <= row < len(energies) and 0 <= col < len(energies[row])
        }
        for row, col in flashed:
            energies[row][col] += 1
            if energies[row][col] == FLASH_ENERGY:
                flashes.add((row, col))

    flash_count = 0
    for row in energies:
        for col in range(len(row)):
            if row[col] >= FLASH_ENERGY:
                flash_count += 1
                row[col] = 0

    return flash_count


def part1(energies: [[int]]) -> int:
    energies = deepcopy(energies)
    flashes = 0
    for s in range(100):
        flashes += step(energies)
    return flashes


def part2(energies: [[int]]) -> int:
    energies = deepcopy(energies)
    num_oct = (len(energies) * len(energies[0]))
    num_steps = 1
    while step(energies) != num_oct:
        num_steps += 1
    return num_steps


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        energies = [list(map(int, line.rstrip())) for line in f]

    print(part1(energies))
    print(part2(energies))
