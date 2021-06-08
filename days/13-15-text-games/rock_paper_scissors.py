import random

class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    ROCK = 'r'
    PAPER = 'p'
    SCISSORS = 's'

def main():
    print_header()

    rolls = [f"{Roll.

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = None # TODO: get random roll
        p1_roll = None # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        # display winner for this round

        count += 1

    # Compute who won


def print_header():
    print("="*25)
    print("Rock Paper Scissors")
    print("="*25)


def get_players_name():
    return input("What is your name?")


def get_players_move():
    return input("Choose a move: [r]ock, [p]aper, [s]cissors.")


if __name__ == "__main__":
    main()
