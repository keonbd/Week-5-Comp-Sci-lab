#######################################################################
##
## CS 101 Lab
## Program #program 3
## Name Katie O'Connor
## Email keonbd@umkc.edu
##
## PROBLEM : get the functions to work
##
## ALGORITHM :
##      1. Write out the algorithm define the functions: play of true or false, wager of value between 1-10, bank of running total of the chips, payout of the amount of chips increasing or decreasing)
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##wager 1-10 chips 1-100 random 1-100 play true of false payout *10 *3 *-1
## OTHER COMMENTS:
##      import 
##
########################################################################

# import modules needed
import random
import math


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play = input('Would you like to play again?')
    while play == 'Y' or play == 'Yes' or play == 'y' or play == 'yes' or play == 'YeS' or play == 'yEs' or play == 'yES' or play == 'YEs' or play == 'YE' or play == 'ye' or play == 'Ye' or play == 'yE':
        return True
    while play == 'NO' or play == 'no' or play == 'No' or play == 'nO' or play == 'n' or play == 'N':
        return False
    if play != False and play != True:
        play = input('Would you like to play again?')


def get_wager(bank: int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input('How much would you like to bet?'))
    while wager > 10 or wager < 1:
        print('You need to bet at least 1, but no more than 10.')
        wager = int(input('How much would you like to bet?'))
    if wager <= 10 and wager >= 1:
        return wager


def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    num_1 = 0
    num_2 = 0
    num_3 = 0
    # tup = ()
    # while i in len(tup) != 2:
    # random_num = randrange(1, 101, 1)
    # tup(random_num)
    num_1 = random.randrange(1, 101, 1)
    num_2 = random.randrange(1, 101, 1)
    num_3 = random.randrange(1, 101, 1)
    return (num_1, num_2, num_3)


def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    while reela == reelb and reela == reelc:
        return 3
    while reelc == reelb or reelc == reela or reela == reelb:
        return 2
    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        chips = int(input('How many chips would you like to start out with?'))
        if chips > 0 and chips < 101:
            return chips
        elif chips < 1:
            print('Please pick a value greater than 0')
        else:
            print('Please pick a number less that 101.')


def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 0:
        return wager * -1
    elif matches == 2:
        return wager * 3
    else:
        return wager * 10


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:  # Replace with condition for if they still have money.

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
