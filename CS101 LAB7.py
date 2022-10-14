def get_mpg():
    """Gathers value for mpg and determines if it is valid"""
    while True:
        try:
            mmpg = int(input('Enter the minimum mpg ==>'))
            if mmpg <= 0:
                print('Fuel economy must be greater than 0')
            elif mmpg > 100:
                print('Fuel economy must be less than 100')
            else:
                return mmpg
        except ValueError:
            print("You must enter a number for the fuel economy")

def get_input():
    """Gathers input file and determines if it is valid"""
    while True:
        try:
            filename = input('Enter the name of the input vehicle file ==> ')
            f = open(filename)
            f.close()
            return filename
        except FileNotFoundError:
            print(f'Could not open file {filename}')

def get_output():
    """Gathers output file and determines if it is valid"""
    while True:
        try:
            filename = input('Enter the name of the file to output to ==> ')
            f = open(filename)
            f.close()
            return filename
        except FileNotFoundError:
            print(f'Could not open file {filename}')

mmpg = get_mpg()
infile = get_input()
outfile = get_output()

fi = open(infile)       #open input file
fo = open(outfile, 'w') #open output file for writing
lines = fi.readlines()

for l in lines:
    x = l.split('\t')   #splits string with a tab seperating each object into a list
    if l == lines[0]:   #ignore first line as it contains only labels
        continue
    
    try:
        if int(x[7]) >= mmpg:
            fo.write("{:<6}{:<6}{:<10} {:<10}\n".format(x[0], x[1], x[2], x[7]))
    except:
        print(f'Could not convert value {x[7]} for vehicle {x[0]} {x[1]} {x[2]}')

fi.close()      #close both the files
fo.close()
