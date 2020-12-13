import math


def readfile():
    l = []
    with open("input.txt", "r") as f:
        for row in f.read().split('\n'):
            l.append((row[0], int(row[1:])))
    return l


shipHdg = 'E'
shipPos = [0, 0]

cmd = readfile()

toDeg = ['N', 'E', 'S', 'W']


def turnShip(curr, deg):
    return toDeg[int(((toDeg.index(curr)*90 + deg) % 360)/90)]


def move(pos, hdg, n):
    if hdg == 'N':
        pos = [n+pos[0]] + [pos[1]]
    elif hdg == 'S':
        pos = [pos[0]-n] + [pos[1]]
    elif hdg == 'E':
        pos = [pos[0]] + [n+pos[1]]
    elif hdg == 'W':
        pos = [pos[0]] + [pos[1]-n]
    return pos


for it in cmd:
    if(it[0] == 'R'):
        shipHdg = turnShip(shipHdg, it[1])
    elif(it[0] == 'L'):
        shipHdg = turnShip(shipHdg, -it[1]+360)
    elif(it[0] == 'F'):
        shipPos = move(shipPos, shipHdg, it[1])
    else:
        shipPos = move(shipPos, it[0], it[1])

print('shipPos', abs(shipPos[0])+abs(shipPos[1]), 'ship hdg', shipHdg)

wpt = [1, 10]
shipPos = [0, 0]
shipHdg = 'E'


def moveShipToWpt(pos, wpt, n):
    for i in range(0, n):
        pos = [pos[0]+wpt[0]] + [pos[1]+wpt[1]]
    return pos


def rotWptR(wpt):
    wpt = [-1*wpt[1]]+[wpt[0]]
    return wpt


for it in cmd:
    if(it[0] == 'F'):
        shipPos = moveShipToWpt(shipPos, wpt, it[1])
    elif(it[0] in toDeg):
        wpt = move(wpt, it[0], it[1])

    elif(it[0] == 'R'):
        n = int(it[1] / 90)
        for i in range(0, n):
            wpt = rotWptR(wpt)
    elif(it[0] == 'L'):
        n = int((360-it[1]) / 90)
        for i in range(0, n):
            wpt = rotWptR(wpt)

print(abs(shipPos[0])+abs(shipPos[1]))
