# region  - Imports
import random
import re
import os
import time

# endregion - Imports

# region - Constants 
WAIT = 2
DICT = {
    1 : 'Rock',
    2 : 'Paper',
    3 : 'Scissors'
}
REV_DICT = {
    'R' : 1 ,
    'P' : 2 ,
    'S' : 3,
    'r' : 1 ,
    'p' : 2 ,
    's' : 3
}
SLEEP = 2
# endregion - Constants

# region - Functions
def clear_screen():
    os.system('cls')


def opening_menu():
    print("Welcome to Rock-Paper-Scissors!")
    print()
    print("You can play by yourself (1 Player) or with your friend (2 Player)")
    print()
    print("Please enter '1' for 1 Player, or '2' for 2 Players.")

def single():
    clear_screen()
    print("Single-Player Mode!")
    print()
    p1_name = str(input("Enter your name: "))

    if not p1_name:
        name = "Player 1"
    else:
        name = p1_name

    score_tracker   = {
        'Robot'    : 0,
        'Player 1' : 0
    }
    round_counter = 1
    round_enum    = 1
    clear_screen() 

    while True:
        score_indicator = 0
        clear_screen()
        print("--Round " + str(round_enum) + "--")
        print("Score: " + str(score_tracker))
        print()
        print(str(name) + " - Choose your hand")
        print()
        print("Enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
        print()
        player1 = input("Enter your hand: ")
        while not re.fullmatch('^[RrSsPp]$', player1):
            print("Enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
            player1 = input("Enter your hand: ")
        print()

        robot = int(random.randrange(1,4))
        player1 = int(REV_DICT[player1])

        if robot == 1 and player1 == 1:
            print("Robot: " + str(DICT[robot]))
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print("Draw!")
            score_indicator = False
        elif (robot == 1 and player1 == 2):
            print("Robot: " + str(DICT[robot]) )
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print ( str(name) + " wins this round!")
            score_tracker["Player 1"] += 1
            score_indicator = True
        elif (robot == 1 and player1 == 3):
            print("Robot: " + str(DICT[robot]))
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print ("Robot wins this round!")
            score_indicator = True
            score_tracker["Robot"] += 1
        elif (robot == 2 and player1 == 1):
            print("Robot: " + str(DICT[robot]))
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print ("Robot wins this round!")
            score_indicator = True
            score_tracker["Robot"] += 1
        elif (robot == 2 and player1 == 2):
            print("Robot: " + str(DICT[robot]))
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print ("Draw!")
            score_indicator = False
        elif (robot == 2 and player1 == 3):
            print("Robot: " + str(DICT[robot]))
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print ( str(name) + " wins this round!")
            score_tracker["Player 1"] += 1
            score_indicator = True
        elif (robot == 3 and player1 == 1):
            print("Robot: " + str(DICT[robot]))
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print ( str(name) + " wins this round!")
            score_tracker["Player 1"] += 1
            score_indicator = True
        elif (robot == 3 and player1 == 2):
            print("Robot: " + str(DICT[robot]))
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print ("Robot wins this round!")
            score_tracker["Robot"] += 1
            score_indicator = True
        elif (robot == 3 and player1 == 3):
            print("Robot: " + str(DICT[robot]))
            print( str(name) + ": " + str((DICT[player1])))
            print()
            print ("Draw!")
            score_indicator = False
        print()
        input("Press ANY key for the next round...")

        if score_indicator:
            round_counter = round_counter + 1
        round_enum = round_enum + 1
    
        if round_counter >= 3 and (score_tracker["Player 1"] != score_tracker["Robot"]):
            break
    
    clear_screen()
    print("That's the game!")
    print()
    print("The final score after " + str(round_enum - 1) + " rounds:")
    print(score_tracker)
    print()
    if score_tracker["Player 1"] > score_tracker["Robot"]:
        print("You won the game! Congratulations!")
    else:
        print("The Robot won the game! Better luck next time.")

def multi():
    clear_screen()
    print("Multi-Player Mode!")

    print()
    p1_name = str(input("Player 1 - Enter your name: "))

    if not p1_name:
        namep1 = "Player 1"
    else:
        namep1 = p1_name

    print()
    p2_name = str(input("Player 2 - Enter your name: "))

    if not p2_name:
        namep2 = "Player 2"
    else:
        namep2 = p2_name

    score_tracker   = {
        namep1 : 0,
        namep2 : 0
    }
    round_counter = 1
    round_enum    = 1
    clear_screen() 

    while True:
        score_indicator = 0
        clear_screen()
        print("--Round " + str(round_enum) + "--")
        print("Score: " + str(score_tracker))
        print()
        print( "Choose your hands")
        print()
        print("Enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
        print()
        player1 = input( str(namep1) + " - Enter your hand: ")
        while not re.fullmatch('^[RrSsPp]$', player1):
            print("Enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
            player1 = input( str(namep1) + " - Enter your hand: ")
        player2 = input( str(namep2) + " - Enter your hand: ")
        while not re.fullmatch('^[RrSsPp]$', player2):
            print("Enter 'R' for Rock, 'P' for Paper or 'S' for Scissors")
            player2 = input( str(namep2) + " - Enter your hand: ")
        print()

        player1 = int(REV_DICT[player1])
        player2 = int(REV_DICT[player2])
        

        if player1 == 1 and player2 == 1:
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print("Draw!")
            score_indicator = False
        elif (player1 == 1 and player2 == 2):
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print ( str(namep2) + " wins this round!")
            score_tracker[namep2] += 1
            score_indicator = True
        elif (player1 == 1 and player2 == 3):
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print ( str(namep1) + " wins this round!")
            score_tracker[namep1] += 1
            score_indicator = True
        elif (player1 == 2 and player2 == 1):
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print ( str(namep1) + " wins this round!")
            score_tracker[namep1] += 1
            score_indicator = True
        elif (player1 == 2 and player2 == 2):
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print ("Draw!")
            score_indicator = False
        elif (player1 == 2 and player2 == 3):
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print ( str(namep2) + " wins this round!")
            score_tracker[namep2] += 1
            score_indicator = True
        elif (player1 == 3 and player2 == 1):
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print ( str(namep1) + " wins this round!")
            score_tracker[namep1] += 1
            score_indicator = True
        elif (player1 == 3 and player2 == 2):
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print ( str(namep1) + " wins this round!")
            score_tracker[namep1] += 1
            score_indicator = True
        elif (player1 == 3 and player2 == 3):
            print( str(namep1) + ": " + str((DICT[player1])))
            print( str(namep2) + ": " + str((DICT[player2])))
            print()
            print ("Draw!")
            score_indicator = False
        print()
        print("DEBUG-'round_counter'-'" + str(round_counter) + "'")
        print("DEBUG-'score_tracker[namep1]'-'" + str(score_tracker[namep1])+ "'")
        print("DEBUG-'score_tracker[namep2]'-'" + str(score_tracker[namep2])+ "'")
        print()
        input("Press ANY key for the next round...")

        if score_indicator:
            round_counter = round_counter + 1
        round_enum = round_enum + 1
    
        if round_counter >= 3 and ( int(score_tracker[namep1]) != int(score_tracker[namep2]) ):
            break
    
    clear_screen()
    print("That's the game!")
    print()
    print("The final score after " + str(round_enum - 1) + " rounds:")
    print(score_tracker)
    print()
    if score_tracker[namep1] > score_tracker[namep2]:
        print( str(namep1) + " you won the game! Congratulations!")
    else:
        print( str(namep2) + " you won the game! Congratulations!")

def main():
    clear_screen()
    opening_menu()

    player = input("How many players? ")
    while not re.fullmatch('^[12]$', player):
        print("Please enter '1' for 1 player, or '2' for 2 players.")
        player = input("How many players? ")
    player = int(player)

    if player == 1:
        single()
    else:
        multi()


if __name__ == "__main__":
    main() 
