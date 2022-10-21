import math

def gradeMenu():
    """Prints the grade menu"""
    print('            Grade Menu')
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')

def addTest():
    """Adds score to test list, checks for valid input"""
    while True:
        score = float(input('Enter the new test score 0-100 ==> '))
        if score < 0:
            print('Please enter a valid score')
        else:
            tests.append(score)
            break

def addAssign():
    """Adds score to assignment list, checks for valid input"""
    while True:
        score = float(input('Enter the new assignment score 0-100 ==> '))
        if score < 0:
            print('Please enter a valid score')
        else:
            assignments.append(score)
            break

def removeTest():
    """Removes score from the tests list, checks for valid input"""
    while True:
        score = float(input('Enter the test score to remove 0-100 ==> '))
        if score < 0:
            print('Please enter a valid score')
        elif score in tests:
            tests.remove(score)
            break
        else:
            print('Could not find that score to remove')

def removeAssign():
    """Removes score from the assignments list, checks for valid input"""
    while True:
        score = float(input('Enter the assignment score to remove 0-100 ==> '))
        if score < 0:
            print('Please enter a valid score')
        elif score in assignments:
            assignments.remove(score)
            break
        else:
            print('Could not find that score to remove')

def clearList(listx):
    """Clears list of all values"""
    listx.clear()

def display():
    print(f'{"Type":<15}{"#":^5}{"min":^10}{"max":^10}{"avg":^10}{"std":^10}')
    print('=' * 60)
    print(f'{"Tests":<15}{len(tests):^5}{minimum(tests):^10}{maximum(tests):^10}{mean(tests):^10}{std(tests):^10}')
    print(f'{"Programs":<15}{len(assignments):^5}{minimum(assignments):^10}{maximum(assignments):^10}{mean(assignments):^10}{std(assignments):^10}')

def std(listx):
    """calculates the standard deviation of list"""
    n = 0
    if len(listx) == 0:
        return 'n/a'
    else:
        for x in listx:
            n += (x - mean(listx)) ** 2
        std = math.sqrt(n / len(listx))
        return round(std,2)
    
def mean(listx):
    """Calculates the mean/average of a list"""
    if len(listx) == 0:
        return 'n/a'
    else:
        mean = sum(listx) / len(listx)
        return round(mean,2)

def minimum(listx):
    """Returns min value of list or n/a if list length is zero"""
    if len(listx) == 0:
        return 'n/a'
    else:
        return min(listx)

def maximum(listx):
    """Returns max value of list or n/a if list length is zero"""
    if len(listx) == 0:
        return 'n/a'
    else:
        return max(listx)

assignments = []
tests = []

#main program

while True:
    gradeMenu()
    print()
    userInput = input()
    if userInput == '1':
        addTest()
    elif userInput == '2':
        removeTest()
    elif userInput == '3':
        clearList(tests)
    elif userInput == '4':
        addAssign()
    elif userInput == '5':
        removeAssign()
    elif userInput == '6':
        clearList(assignments)
    elif userInput == 'D' or userInput == 'd':
        display()
    elif userInput == 'Q' or userinput == 'q':
        break
    else:
        print('Please enter a valid input')


