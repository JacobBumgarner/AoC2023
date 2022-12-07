# AoC Day 2

shape_hash = {"X": 1, "Y": 2, "Z": 3}

strategy_hash = {
    "X": {"A": "Z", "B": "X", "C": "Y"},
    "Y": {"A": "X", "B": "Y", "C": "Z"},
    "Z": {"A": "Y", "B": "Z", "C": "X"},
}


def load_data(file):
    data = [line.strip() for line in open(file).readlines()]
    return data


def game_score(opponent, you) -> int:
    """Returnt the result of the current game."""
    score = 0
    if (
        (opponent == "A" and you == "X")
        or (opponent == "B" and you == "Y")
        or (opponent == "C" and you == "Z")
    ):  # ties
        score += 3
    elif (
        (opponent == "A" and you == "Y")
        or (opponent == "B" and you == "Z")
        or (opponent == "C" and you == "X")
    ):  # wins
        score += 6

    return score + shape_hash[you]


def solution_1(data: list) -> int:
    """Solve the first puzzle.

    Hash the entry for each game and add the result to the final tally.

    Hash:
        A: 8
        B: 1
        C: 6
    """
    total_points = 0

    for game in data:
        total_points += game_score(game[0], game[-1])

    return total_points


def find_correct_hand(opponent, guide) -> str:
    """Find the hand that will win, tie, or lose the game."""
    hand = strategy_hash[guide][opponent]
    return hand


def solution_2(data: list) -> int:
    """Solve the second puzzle.

    Cheat sheet:
        X - Lose
        Y - Tie
        Z - Win

    """
    total_points = 0

    for game in data:
        hand = find_correct_hand(game[0], game[-1])
        total_points += game_score(game[0], hand)

    return total_points


def solve(file):
    """Solve day 2 of the AoC.

    Score guide:
        1 pt - Rock
        2 pt - Paper
        3 pt - Scissor
        0 pt - Loss
        3 pt - Draw
        6 pt - Win
    """
    data = load_data(file)

    answer_1 = solution_1(data)
    print(answer_1)

    answer_2 = solution_2(data)
    print(answer_2)
    return


if __name__ == "__main__":
    solve("data/02.txt")
