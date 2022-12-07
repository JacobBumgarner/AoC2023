# AoC Day 1


def read_data(file) -> list:
    data = [line.strip() for line in open(file).readlines()]
    return data


def solution_1(data) -> int:
    """Find the index of the elf with the most calories."""
    # Add all of the calories for each elf

    elves = [0]
    for i in range(len(data)):
        if data[i]:
            elves[-1] += int(data[i])
        else:
            elves.append(0)

    # Find the index of the largest number
    most_calories = max(elves)
    return elves, most_calories


def solution_2(elves) -> int:
    """Find the total calories of the top three calorie carrying elves."""
    # Iterate through the list and pop the max three times.
    top_three_calories = 0
    for _ in range(3):
        largest_carrier = max(elves)
        elves.pop(elves.index(largest_carrier))

        top_three_calories += largest_carrier

    return top_three_calories


def solve(file):
    data = read_data(file)

    elves, answer_1 = solution_1(data)
    print(answer_1)

    answer_2 = solution_2(elves)
    print(answer_2)


if __name__ == "__main__":
    solve("data/01.txt")
