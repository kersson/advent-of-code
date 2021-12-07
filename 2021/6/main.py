import sys

REPRO_TIMER = 7
NEW_REPRO_OFFSET = 2


def brute_force_simulate(fish: [int], days: int) -> int:
    fish = fish.copy()
    for _ in range(days):
        fish.extend(REPRO_TIMER + NEW_REPRO_OFFSET for timer in fish if timer == 0)
        fish[:] = [timer - 1 if timer > 0 else REPRO_TIMER - 1 for timer in fish]
    return len(fish)


def simulate(fish: [int], days: int) -> int:
    # Initial number of fish
    num_fish = len(fish)

    # Number of fish that will breed on a certain day
    num_fish_on_day = [len([f for f in fish if f == num]) for num in range(REPRO_TIMER)]

    # Number of new fish that will breed on a certain day
    new_fish_on_day = [0 for _ in range(REPRO_TIMER)]

    for day in range(days):
        # Day of reproduction cycle
        day_of_cycle = day % REPRO_TIMER

        # Breed the fish on this day of the cycle
        num_new_fish = num_fish_on_day[day_of_cycle]
        num_fish += num_new_fish

        # Separately keep track of the new fish (who take NEW_REPRO_OFFSET days longer to reproduce)
        new_fish_on_day[(day + NEW_REPRO_OFFSET) % REPRO_TIMER] += num_new_fish

        # Transfer over the new fish that will breed on this day next cycle
        num_fish_on_day[day_of_cycle] += new_fish_on_day[day_of_cycle]
        new_fish_on_day[day_of_cycle] = 0

    return num_fish


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        fish = list(map(int, f.readline().rstrip().split(',')))

    print(simulate(fish, 80))
    print(simulate(fish, 256))
