import math
import sys
from typing import Callable


def most_common_bit(nums: [str], bit: int) -> str:
    threshold = math.ceil(len(nums) / 2)
    num_ones = len([None for num in nums if num[bit] == '1'])
    return '1' if num_ones >= threshold else '0'


def least_common_bit(nums: [str], bit: int) -> str:
    return '0' if most_common_bit(nums, bit) == '1' else '1'


def reduce(nums: [str], func: Callable[[[str], int], str]) -> int:
    nums = nums.copy()
    num_bits = len(nums[0])

    for bit in range(num_bits):
        bit_match = func(nums, bit)
        nums = [n for n in nums if n[bit] == bit_match]
        if len(nums) == 1:
            break

    return int(nums[0], 2)


def part1(nums: [str]) -> int:
    num_bits = len(nums[0])

    most_common_bits = "".join(map(lambda bit: most_common_bit(nums, bit), range(num_bits)))
    least_common_bits = "".join(map(lambda bit: least_common_bit(nums, bit), range(num_bits)))

    gamma = int(most_common_bits, 2)
    epsilon = int(least_common_bits, 2)

    return gamma * epsilon


def part2(nums: [str]) -> int:
    o2 = reduce(nums, most_common_bit)
    co2 = reduce(nums, least_common_bit)

    return o2 * co2


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        nums = list(map(lambda line: line.rstrip(), f))

    print(part1(nums))
    print(part2(nums))
