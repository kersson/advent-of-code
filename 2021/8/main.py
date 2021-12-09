import sys

UNIQUE_DIGITS = {2: "1", 4: "4", 3: "7", 7: "8"}


class bidict(dict):
    def inv(self, value):
        keys = [k for k, v in self.items() if v == value]
        assert len(keys) == 1
        return keys[0]


def decode(patterns: [str], output: [str]) -> int:
    digits = bidict({frozenset(pattern): UNIQUE_DIGITS.get(len(pattern), "-") for pattern in patterns})

    six_nine_zero = set(p for p in digits.keys() if len(p) == 6)
    six = set(p for p in six_nine_zero if not digits.inv("1").issubset(p))
    assert len(six) == 1
    six_nine_zero -= six
    digits[six.pop()] = "6"

    nine = set(p for p in six_nine_zero if digits.inv("4").issubset(p))
    assert len(nine) == 1
    six_nine_zero -= nine
    digits[nine.pop()] = "9"

    assert len(six_nine_zero) == 1
    digits[six_nine_zero.pop()] = "0"

    two_three_five = set(p for p in digits.keys() if len(p) == 5)
    three = set(p for p in two_three_five if digits.inv("1").issubset(p))
    assert len(three) == 1
    two_three_five -= three
    digits[three.pop()] = "3"

    five = set(p for p in two_three_five if p.issubset(digits.inv("9")))
    assert len(five) == 1
    two_three_five -= five
    digits[five.pop()] = "5"

    assert len(two_three_five) == 1
    digits[two_three_five.pop()] = "2"

    return int("".join(map(lambda d: digits[frozenset(d)], output)))


def part1(notes: [([str], [str])]) -> int:
    return sum(sum(1 for digit in digits if len(digit) in UNIQUE_DIGITS) for _, digits in notes)


def part2(notes: [([str], [str])]) -> int:
    return sum(decode(patterns, output) for patterns, output in notes)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        notes = [tuple(map(lambda x: x.split(), line.split(" | "))) for line in f]

    print(part1(notes))
    print(part2(notes))
