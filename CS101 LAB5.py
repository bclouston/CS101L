########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
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


# import statements

# functions
def get_school(id_num): 
    if id_num[5] == '1':
        return('School of Computing and Engineering SCE')
    elif id_num[5] == '2':
        return('School of Law')
    elif id_num[5] == '3':
        return('College of Arts and Sciences')
    else:
        return('Invalid School')

def get_grade(id_num):
    if id_num[6] == '1':
        return('Freshman')
    elif id_num[6] == '2':
        return('Sophomore')
    elif id_num[6] == '3':
        return('Junior')
    elif id_num[6] == '4':
        return('Senior')
    else:
        return('Invalid Grade')

def character_value(n): 
    if ord(n) >= 65:
        value = ord(n)
        value -= 65
    else:
        value = ord(n)
        value -= 48
    return(value)

def get_check_digit(id_num):
    value = 0
    for n in range(9):
        char_value = character_value(id_num[n])
        value += ((n + 1) * char_value)
    check_digit = value % 10
    return(str(check_digit))

def index5(id_num):
    for a in range(5):
        inte = int(ord(id_num[a]))
        if inte < 65:
            errormsg = 'The first 5 characters must be A-Z, the invalid character is at {} is {}.'.format(a, id_num[a])
            return(False, errormsg)
        else:
            return(True, '')

def index6(id_num):
    for b in range(3):
        if ord(id_num[(b+7)]) < 48 or ord(id_num[(b+7)]) > 57:
            errormsg1 = 'The last 3 characters must be 0-9, the invalid character is at {} is {}'.format((b+7), id_num[b+7])
            return(False, errormsg1)
        else:
            return(True, '')
    
def verify_check_digit(id_num):
    if len(id_num) != 10:
        return(False, 'The length of the number given must be 10')
    elif get_school(id_num) == 'Invalid School':
        return(False, 'The sixth character must be 1 2 or 3')
    elif get_grade(id_num) == 'Invalid Grade':
        return(False, 'The seventh character must be 1 2 3 or 4')
    elif index5(id_num)[0] == False:
        return(index5(id_num))
    elif index6(id_num)[0] == False:
        return(index6(id_num))
    elif id_num[9] != str(get_check_digit(id_num)):
        errormsg = 'Check Digit {} does not match calculated value {}'.format(id_num[9], get_check_digit(id_num))
        return(False, errormsg)
    else:
        return(True, '')

if __name__ == "__main__":

    # main program

    while True:
        id_num = input('Enter Libary Card. Hit enter to Exit ==> ')
        if verify_check_digit(id_num)[0] == False:
            print('Library card is invalid')
            print(verify_check_digit(id_num)[1])
        else:
            print('Library card is valid')
            print(f'The card belongs to a student in {get_school(id_num)}')
            print(f'The card belongs to a {get_grade(id_num)}\n')
