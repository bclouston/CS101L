print('**** Welcome to the LAB grade calculator! ****\n') 

userName = input('Who are we calculating grades for? ==> ')
print()

#assign values to each grading category and determine if they are valid
#if values are not valid they are changed to the closest value that is valid
gradeLab = int(input('Enter the Labs grade? ==> '))
if gradeLab > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    gradeLab = 100
elif gradeLab < 0:
    print('The lab value should have been zero or greater. It has been changed to zero')
    gradeLab = 0
print()

gradeExam = int(input('Enter the EXAMS grade? ==> '))
if gradeExam > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    gradeExam = 100
elif gradeExam < 0:
    print('The exam value should have been zero or greater. It has been changed to zero')
    gradeExam = 0
print()

gradeAtt = int(input('Enter the Attendance grade? ==> '))
if gradeAtt > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    gradeAtt = 100
elif gradeAtt < 0:
    print('The attendance value should have been zero or greater. It has been changed to zero')
    gradeAtt = 0
print()

#calculate final weighted grade and assign the appropriate letter grade
gradeFinal = (gradeLab * 0.7) + (gradeExam * 0.2) + (gradeAtt * 0.1)
if gradeFinal >= 90:
    gradeLetter = 'A'
elif gradeFinal >= 80:
    gradeLetter = 'B'
elif gradeFinal >= 70:
    gradeLetter = 'C'
elif gradeFinal >= 60:
    gradeLetter = 'D'
else:
    gradeLetter = 'F'

#return final weighted and letter grade to the user
print(f'The weighted grade for {userName} is {gradeFinal}')
print(f'{userName} has a letter grade of {gradeLetter}\n')

print('**** Thanks for using the Lab grade calculator ****')


