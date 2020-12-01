with open('input.txt', 'r') as content:
    numbers = content.readlines()
    
from datetime import datetime

start=datetime.now()

def calc():
    for x in numbers:
        for y in numbers:
            if int(x) + int(y) == 2020:
                print(int(x)*int(y))
                return

def calc_3():
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if int(x) + int(y) + int(z) == 2020:
                    print(int(x)*int(y)*int(z))
                    return



start=datetime.now()
calc()
print(datetime.now()-start)
start=datetime.now()
calc_3()
print(datetime.now()-start)
