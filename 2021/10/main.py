from functools import reduce
import sys

MATCH = {'(': ')', '[': ']', '{': '}', '<': '>'}


def part1(nav: [str]) -> int:
    SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}

    illegal = []
    for line in nav:
        stack = []
        for c in line:
            if c in MATCH:
                stack.append(MATCH[c])
            elif not stack or c != stack.pop():
                illegal.append(c)

    return sum(SCORES[c] for c in illegal)


def part2(nav: [str]) -> int:
    SCORES = {')': 1, ']': 2, '}': 3, '>': 4}

    completion_scores = []
    for line in nav:
        stack = []
        for c in line:
            if c in MATCH:
                stack.append(MATCH[c])
            elif not stack or c != stack.pop():
                stack = None
                break
        if stack:
            completion_scores.append(
                reduce(lambda score, c: score * 5 + SCORES[c], reversed(stack), 0)
            )

    completion_scores.sort()
    return completion_scores[len(completion_scores) // 2]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        nav = [line.rstrip() for line in f]

    print(part1(nav))
    print(part2(nav))
