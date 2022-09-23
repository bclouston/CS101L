########################################################################
##
## CS 101 Lab
## Program # 4
## Name: Brendan Clouston
## Email: bmcmnk@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    p = 0
    while p == 0: 
        response = input('Do you want to play again? ==> ')
        response = response.lower()  #convert string to lowercase
        if response == 'y': #check for y or yes
            return True
            p += 1  #increment p to close the loop
        if response == 'yes':
            return True
            p += 1
        elif response == 'n': #check for n or no
            return False
            p += 1
        elif response == 'no':
            return False
            p += 1
        else:
            print('You must enter Y/YES/N/NO to continue. Please try again')
            
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    validBet = True
    while True:
        betAmount = int(input('How many chips do you want to wager? ==> '))
        if betAmount <= 0:  #check if bet is greater than 0
            print('The wager amount must be greater than 0. Please enter again.')
            validBet = False
        elif betAmount > bank:  #check if bet is less than current bank
            print(f'The wager amount cannot be greater than how much you have. {bank}')
            validBet = False
        else:
            validBet = True
        if validBet == True: #check if bet is valid
            return betAmount
            False

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(0,10)    #returns random integer from and including to 0 and 10
    reel2 = random.randint(0,10)
    reel3 = random.randint(0,10)
    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    matches = 0
    if reela == reelb:  #increment to the requested return value of 2 if two reels match
        matches += 2
    elif reelb == reelc:
        matches += 2
    elif reela == reelc:
        matches += 2
    elif matches == 6:  #since all reels match, matches was incremented to six, set to the requested return value of 3
        matches = 3
    return matches

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    validBank = True
    while True:
        bankroll = int(input('How many chips do you want to start with? ==> '))
        if bankroll <= 0:
            print('Too low a value, you can only choose 1 - 100 chips')
            validBank = False
        elif bankroll > 101:
            print('Too high a value, you can only choose 1- 100 chips')
            validBank = False
        elif validBank == True:
            return bankroll
            False

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return (wager * 10) - wager     #since wager has not been taken before the spin, it is taken now with the payout
    elif matches == 2:
        return (wager * 3) - wager
    elif matches == 0:
        return wager * -1


if __name__ == "__main__":
    playing = True
    while playing:

        bank = get_bank()
        bankmax = bank
        bankstart = bank
        nspins = 0
        while bank > 0:  #close loop if bank is 0
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
            nspins += 1     #increment number of spins
            if bank > bankmax:  #keep track of the most amount of chips person had at one time
                bankmax = bank
        print(f'You lost all, {bankstart}, in, {nspins}, spins')
        print(f'The most chips you had was, {bankmax}')
        playing = play_again()
