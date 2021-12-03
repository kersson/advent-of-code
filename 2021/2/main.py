import sys


def part1(cmds: [[str]]) -> int:
    h = 0
    d = 0
    a = 0
    for cmd in cmds:
        x = int(cmd[1])
        if cmd[0].startswith('f'):
            h += x
        elif cmd[0].startswith('d'):
            d += x
        elif cmd[0].startswith('u'):
            d -= x

    return h * d


def part2(cmds: [[str]]) -> int:
    h = 0
    d = 0
    a = 0
    for cmd in cmds:
        x = int(cmd[1])
        if cmd[0].startswith('f'):
            h += x
            d += a * x
        elif cmd[0].startswith('d'):
            a += x
        elif cmd[0].startswith('u'):
            a -= x

    return h * d


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        cmds = list(map(lambda line: line.split(), f))

    print(part1(cmds))
    print(part2(cmds))
