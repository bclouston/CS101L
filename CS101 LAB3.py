game = True
userInput = ''

print('Welcome to the Flarsheim Guesser!\n')
print('Please think of a number between and including 1 and 100\n')

while game:                 #while boolean value of game == True, game will continue to run
    #get user input for remainder of their number divided by 3
    remainder_3 = int(input('What is the remainder when your number is divided by 3 ?'))
    while remainder_3 < 0 or remainder_3 > 3:
        if remainder_3 < 0:
            print('The value entered must be 0 or greater')
            remainder_3 = int(input('What is the remainder when your number is divided by 3 ?'))
        elif remainder_3 > 3:
            print('The value entered must be less than 3')
            remainder_3 = int(input('What is the remainder when your number is divided by 3 ?'))

    #get user input for remainder of their number divided by 7
    remainder_5 = int(input('What is the remainder when your number is divided by 5 ?'))
    while remainder_5 < 0 or remainder_5 > 5:
        if remainder_5 < 0:
            print('The value entered must be 0 or greater')
            remainder_5 = int(input('What is the remainder when your number is divided by 5 ?'))
        elif remainder_5 > 5:
            print('The value entered must be less than 5')
            remainder_5 = int(input('What is the remainder when your number is divided by 5 ?'))

    #get user input for remainder of their number divided by 7
    remainder_7 = int(input('What is the remainder when your number is divided by 7 ?'))
    while remainder_7 < 0 or remainder_7 > 7:   
        if remainder_7 < 0:
            print('The value entered must be 0 or greater')
            remainder_7 = int(input('What is the remainder when your number is divided by 7 ?'))
        elif remainder_7 > 7:
            print('The value entered must be less than 7')
            remainder_7 = int(input('What is the remainder when your number is divided by 7 ?'))

    #for loop that checks every number up to 100 to determine players number
    for n in range(101):
        if (n % 3) != remainder_3:
            continue            #if remainder does not match for n we move on to the next number
        if (n % 5) != remainder_5:
            continue
        if (n % 7) != remainder_7:
            continue
        print(f'\nYour number was {n}')

    print('How amazing is that?')

    #ask player if they would like to continue
    while userInput != 'n' or 'y':
        userInput = input('Do you want to play again? y to continue, n to quit  ==> ')
        if userInput == 'n':    #set game boolean value to false and break user prompt loop
            game = False
            break
        elif userInput == 'y':  #breaks prompt loop and restart the game
            break
        else:
            continue            #repeat the prompt for invalid inputs
        
    
