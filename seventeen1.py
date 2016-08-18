
from random import randint

def validate_choice(marbles_in_jar, choice):
    """ Validates if input is a number
        If it is, checks if it's between 1 and 3 or
        less or equal to # marbles in the jar
    """
    while True:
        try:
            choice = int(choice)
        except:
            choice = input("Sorry, that is not a valid option. Try again! ")
        else:
            if choice <= 0 or choice > 3 or marbles_in_jar - choice < 0:  # Conditions for valid input
                choice = input("Sorry, that is not a valid option. Try again! ")
            else:
                return choice


def human_turn(marbles_in_jar):
    """ Gets user's choice of # marbles to remove,
        validates choice
        removes from jar
        and returns remaining marbles and the choice
    """
    input_prompt = "Your turn: How many marbles will you remove (1-3)? "
    choice = input(input_prompt)
    choice = validate_choice(marbles_in_jar, choice)
    print("You removed {} marbles.".format(choice))
    marbles_in_jar -= choice
    return marbles_in_jar, choice


def computer_turn(marbles_in_jar, last_human_choice, strategy_type=1):
    """ Makes a valid choice of # marbles for the computer
        based on one of the strategies
    """
    # Random number, default
    if strategy_type == 1:
        if marbles_in_jar > 3:
            choice = randint(1, 3)
        else:
            choice = randint(1, marbles_in_jar)

    #  Replicates human choice
    if strategy_type == 2:
        choice = last_human_choice

    # Always win case
    # if strategy_type == 3:


    # Computer turn messaging
    print("Computer's turn...")
    print("Computer removed {} marbles.".format(choice))
    marbles_in_jar -= choice
    return marbles_in_jar


def check_jar(next_player, marbles_in_jar):
    """ Checks if there are any marbles left before the next player's turn
        If yes,  prints stock message
        If no, declares next player as winner and exits game
    """
    stock_msg = "Number of marbles left in jar : "
    if marbles_in_jar > 0:
        print(stock_msg+str(marbles_in_jar))
    else:
        print("\nThere are no marbles left. {} wins!".format(next_player))
        quit()

def play_seventeen():
    """ Game play
        Human goes first, followed by the computer
        They take turns until there are no marbles present in the jar
    """
    marbles_in_jar = 17
    stock_msg = "Number of marbles left in jar : "
  
    # Game onboarding
    print("\nLet's play the game of Seventeen!")
    print(stock_msg+str(marbles_in_jar))

    while True:
        # Human turn
        print("\n")
        marbles_in_jar, human_choice = human_turn(marbles_in_jar)
        check_jar("Computer", marbles_in_jar)
        print("\n")
        # Computer turn
        marbles_in_jar = computer_turn(marbles_in_jar, human_choice)
        check_jar("Human", marbles_in_jar)



def main():
    play_seventeen()

if __name__ == "__main__":
    main()
