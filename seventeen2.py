# The program reads from an input file (named 'i206_placein_input.txt') a sequence of comma delimited numbers 
# representing the sequence of moves made by Player 1. Each line of the input file represents a different game. 
# For example, the sample input file contains data for ten games. In the first game, 
# Player 1 removes 3 marbles during its first turn, 1 marble during its second turn, 
# three marbles during its third turn, and so on.

# If the number of marbles left in the jar is fewer than the next number in the play sequence, 
# then Player 1 should remove all the remaining marbles. For example, if there are two marbles left in the jar, 
# and the next number in the sequence is 3, then Player 1 should remove two marbles, not three.
# Player 2 will play the same marble-removal strategy as in Version 1.

# Note that not all numbers in each line may be used, depending on the progress of the game 
# (which in turn depends on the strategy used by Player 2). 
# Conversely, the play sequences are generated such that there will always be enough numbers for each game.

# The program will play the game as many times as there are lines in the input file, 
# printing the sequence of moves and the game winner into an output text file 
# (named i206_placein_output2_<ischool_userid>.txt'), one line per game. 
# 	At the end of all the games, the program will print the number of games won by each player. 
# 	See below for what an output file for ten games might look like.

from random import randint


def read_file(filename):
    with open(filename, "r") as f:
        file_contents = f.readlines()
    return file_contents

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

def human_turn(marbles_in_jar, choice):
    """ Gets user's choice of # marbles to remove from file,
        validates choice [checks if it's less than the number of marbles in jar]
        removes from jar
        and returns remaining marbles
    """
    if marbles_in_jar < choice:
        choice = marbles_in_jar
        marbles_in_jar = 0
    else:
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

    # Computer turn messaging
    marbles_in_jar -= choice
    return marbles_in_jar, choice


def check_jar(marbles_in_jar, next_player, game_play_seq):
    """ Checks if there are any marbles left before the next player's turn
        If yes, 
        If no, declares next player as winner and writes game results to file

        Parameters :
        marbles_in_jar : Number of marbles left in jar
        next_player : The winning player if no marbles are left
        game_play_sequence : Game play sequence so far
    """
    if marbles_in_jar > 0:
        return 
    else:
        game_play_seq = game_play_seq[:-1]+". Winner: {}".format(next_player)
        print(game_play_seq)
        with open("i206_placein_output2_malavika.txt", "a") as f:
            f.write(game_play_seq+"\n")
        return "Over"




def play_seventeen():
    """ Game play 
    """
    games = read_file("i206_placein_input_0.txt")
    winner_list = []

    for idx, line in enumerate(games):
        
        marbles_in_jar = 17
        human_choice_list = line.strip().split(",")[::-1]  # Splitting the string and reversing so that it is easier to pop choices
        game_play_seq = "Game #{}. Play sequence: ".format(idx+1)
        
        # For every round, turns are taken in picking marbles until there are none
        while marbles_in_jar >= 0:
                # Human turn
                choice = int(human_choice_list.pop())
                marbles_in_jar, choice = human_turn(marbles_in_jar, choice)
                # print("Human", choice, marbles_in_jar)
                game_play_seq += str(choice)+"-"
                status = check_jar(marbles_in_jar, "P2", game_play_seq)
                if status == "Over":
                    winner_list.append("P2")
                    break

                # Computer turn
                marbles_in_jar, choice = computer_turn(marbles_in_jar, choice)
                # print("Comp", choice, marbles_in_jar)
                game_play_seq += str(choice)+"-"
                status = check_jar(marbles_in_jar, "P1", game_play_seq)
                if status == "Over":
                    winner_list.append("P1")
                    break

    # Getting rounds won by each player
    P1_rounds = len([i for i in winner_list if i == "P1"])
    P2_rounds = len([i for i in winner_list if i == "P2"])
    print("Player 1 won {} times. Player 2 won {} times.".format(P1_rounds, P2_rounds))



def main():
    play_seventeen()

if __name__ == "__main__":
    main()