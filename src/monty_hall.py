from typing import List, Tuple
import random


def monty_hall(switch_door: bool) -> bool:
    """Simulate a single Monty Hall game.

    :param bool switch_door: If True, the contestant will switch their choice after a goat door is revealed.
    :return: True if the contestant won the car, False otherwise.
    """
    doors: List[str] = ["Car"] + ["Goat"] * 2
    random.shuffle(doors)
    
    initial_choice: int = random.choice([0, len(doors) - 1])

    if switch_door:
        revealed_door: int = random.choice(
            [i for i in range(len(doors)) if i != initial_choice and doors[i] == "Goat"]
        )
        final_choice = random.choice(
            [i for i in range(len(doors)) if i != initial_choice and i != revealed_door]
        )
    else:
        final_choice = initial_choice

    return doors[final_choice] == "Car"


def simulate_games(num_games: int = 1000) -> Tuple[float, float]:
    """Simulate a number of Monty Hall games and print the statistics.

    :param num_games: The number of times the monty_hall function has been called. Default is 1000
    :return: The number of winning the games depends on whether you switch the door or not. [num_wins_with_switching,num_wins_without_switching]
    """
    num_wins_with_switching = sum([monty_hall(True) for _ in range(num_games)])
    num_wins_without_switching = sum([monty_hall(False) for _ in range(num_games)])

    return num_wins_with_switching, num_wins_without_switching


if __name__ == "__main__":
    num_games = 100000
    num_wins_without_switching, num_wins_with_switching = simulate_games(num_games)
    print(
        f"Winning percentage without switching doors: {(num_wins_without_switching / num_games * 100):.2f}%"
    )
    print(
        f"Winning percentage with switching doors: {(num_wins_with_switching / num_games *100):.2f}%"
    )
