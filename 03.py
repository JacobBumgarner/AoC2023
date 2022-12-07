# AoC Day 3


def load_data(file):
    data = [line.strip() for line in open(file).readlines()]
    return data


def get_priority(item: str) -> int:
    """Get the priority of an item.

    Convert the item to its order and subtract the corresponding values:
        - Lowercase: 96
        - Uppercase: 64  + 25
    """
    if item.islower():
        subtraction_value = 96
    elif item.isupper():
        subtraction_value = 64 - 26
    return ord(item) - subtraction_value


def solution_1(data):
    """Solve part 1.

    Find the priority of the items that appear in both sides of the
    bag.
    """
    both_comparment_items = []

    # Get the items in both bags
    for bag in data:
        compartment_index = int(len(bag) / 2)
        compartment_1 = set(bag[:compartment_index])
        compartment_2 = set(bag[compartment_index:])

        items_in_both = compartment_1.intersection(compartment_2)

        both_comparment_items.extend(items_in_both)

    # Get the priorities of the items
    priority_sum = sum([get_priority(item) for item in both_comparment_items])

    return priority_sum


def identify_badge(group) -> str:
    """Find the the unique badge for group that the first UI elf belongs to."""
    badge_set = set(group[0])

    for i in range(1, 3):
        badge_set = badge_set.intersection(set(group[i]))

    return list(badge_set)[0]


def solution_2(data):
    """Solve part 2.

    The elves are divided into groups of threes.

    Each group has a unique badge that identifies them.

    Find the items that identify the groups, and return the
    sum of their priorities.
    """
    badges = []

    for group in zip(*(iter(data),) * 3):
        # Find the badge for the first group
        badge = identify_badge(group)
        badges.append(badge)

    # Get the sum of the priorities of the badges
    priority_sum = sum([get_priority(badge) for badge in badges])

    return priority_sum


def solve(file):
    """Solve day 3 of the AoC.

    Overview:
    Each line represents a bag. The bag has an even number of items.
    The first half of items are the first compartment; so on for the second.

    Item priorities:
        - Lower case letters: 1-26
        - Upper case letters: 27-52
    """
    data = load_data(file)

    answer_1 = solution_1(data)
    print(answer_1)

    answer_2 = solution_2(data)
    print(answer_2)

    return


if __name__ == "__main__":
    solve("data/03.txt")
