from collections import defaultdict
from enum import IntEnum, auto
import csv
import random
import time


class Action(IntEnum):
    Rock = auto()
    Gun = auto()
    Lightning = auto()
    Devil = auto()
    Dragon = auto()
    Water = auto()
    Air = auto()
    Paper = auto()
    Sponge = auto()
    Wolf = auto()
    Tree = auto()
    Human = auto()
    Snake = auto()
    Scissors = auto()
    Fire = auto()


class Player:
    def __init__(self, name, wins=0):
        self.name = name
        self.wins = wins


def main():
    print_header()
    name = input("Enter your name: ")
    player1 = Player(name)
    player2 = Player("Computer")
    print(f"Welcome {player1.name}")
    BEST_OF_NUM = 3
    game_loop(player1, player2, BEST_OF_NUM)


def print_header():
    print("=" * 30)
    print("  15-way Rock Paper Scissors")
    print("=" * 30)


def game_loop(player1, player2, BEST_OF_NUM=3):
    while max([player1.wins, player2.wins]) < BEST_OF_NUM-1:
        try:
            p1_turn = get_user_selection()
        except ValueError as e:
            range_str = f"[1, {len(Action)}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue
        p2_turn = get_computers_selection()

        determine_winner(p1_turn, p2_turn, player1, player2, victories)
        get_score(player1, player2)

    print()
    print("Thanks for playing!")


victories = defaultdict(list)
with open("data/battle-table.csv", "r") as csvfile:
    fieldnames = "Attacker,Rock,Gun,Lightning,Devil,Dragon,Water,Air,Paper,Sponge,Wolf,Tree,Human,Snake,Scissors,Fire".split( ",")
    for line in csv.DictReader(csvfile, fieldnames=fieldnames):
        action = line["Attacker"]
        for fieldname in fieldnames:
            if line[fieldname] == "win":
                victories[action].append(fieldname)



def determine_winner(p1_turn, p2_turn, player1, player2, victories):
    defeats = victories[p1_turn.name]
    if p1_turn.name == p2_turn.name:
        print()
        print(f"Both players selected {p1_turn.name}. It's a tie!")
    elif p2_turn.name in defeats:
        print()
        print(f"{p1_turn.name} beats {p2_turn.name}! You win!")
        player1.wins += 1
    else:
        print()
        print(f"{p2_turn.name} beats {p1_turn.name}! You lose.")
        player2.wins += 1


def get_user_selection():
    choices = [f"{action.name} [{action.value}]" for action in Action]
    choices_str = "\n".join(choices)
    selection = int(input(f"Enter a choice:\n{choices_str}\n"))
    action = Action(selection)
    return action


def get_computers_selection():
    selection = random.choice([action for action in Action])
    action = Action(selection)
    return action


def get_score(player1, player2):
    print()
    print(f"{player1.name} has won {player1.wins} times.")
    print(f"{player2.name} has won {player2.wins} times.")
    print()


if __name__ == "__main__":
    main()
