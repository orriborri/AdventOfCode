import math


def readfile():
    with open("input.txt", "r") as f:
        f_in = f.read()
        return f_in.split('\n')


def findSeat(binary):
    rowBin = binary[:7].replace('F', '0').replace('B', '1')
    row = int(rowBin, 2)
    placeBin = binary[7:].replace('R', '1').replace('L', '0')
    place = int(placeBin, 2)
    return row * 8 + place


maxId = 0
seats = []
for it in readfile():
    seats.append(findSeat(it))
    maxId = max(maxId, findSeat(it))

print(maxId)
seats.sort()

for i, it in enumerate(seats):
    if(seats[i+1]-it != 1):
        print(it+1)
        break
