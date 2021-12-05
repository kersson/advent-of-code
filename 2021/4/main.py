import sys


def has_won(board: [[int]]) -> bool:
    return \
        any(sum(1 for col in range(5) if board[row][col] < 0) == 5 for row in range(5)) or \
        any(sum(1 for row in range(5) if board[row][col] < 0) == 5 for col in range(5))


def play_number(num, board: [[int]]):
    for row in range(5):
        for col in range(5):
            if board[row][col] == num:
                board[row][col] = -1


def unmarked_sum(board: [[int]]) -> int:
    return sum(sum(board[row][col] for col in range(5) if board[row][col] >= 0) for row in range(5))


def part1(nums: [int], boards: [[[int]]]) -> int:
    boards = boards.copy()
    for num in nums:
        for board in boards:
            play_number(num, board)
            if has_won(board):
                return unmarked_sum(board) * num

    assert False


def part2(nums: [int], boards: [[[int]]]) -> int:
    boards = boards.copy()
    for num in nums:
        winning_indexes = []

        for index, board in enumerate(boards):
            play_number(num, board)
            if has_won(board):
                winning_indexes.append(index)

        if len(winning_indexes) == len(boards):
            return unmarked_sum(boards[winning_indexes[-1]]) * num
        else:
            for index in reversed(winning_indexes):
                boards.pop(index)

    assert False


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        nums = list(map(int, f.readline().rstrip().split(',')))
        boards = [[]]
        for line in f:
            row = line.split()
            if row:
                if len(boards[-1]) == 5:
                    boards.append([])
                boards[-1].append(list(map(int, row)))

    print(part1(nums, boards))
    print(part2(nums, boards))
