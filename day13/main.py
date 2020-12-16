import math


def readfile():
    with open("input.txt", "r") as f:
        startTime = int(f.readline())
        timeTable = f.readline().split(',')
    return (startTime, timeTable)


startTime, timeTabe = readfile()


def earielstBus(startTime, arr):
    t = startTime

    while True:
        for it in arr:
            if it != 'x':
                if t % int(it) == 0:
                    return (t, it)
        t += 1


leave, bussnr = earielstBus(startTime, timeTabe)

print((leave-startTime)*int(bussnr))

count = 0
res = []
for i, it in enumerate(timeTabe):
    if it != 'x':
        res.append((int(it), i))
        count = 0

t = 0


def main(res):
    r = 1
    t = 1
    used = []
    while True:
        check = True
        for it in res:
            if((t + it[1]) % (it[0]) != 0):
                t += r
                check = False
                break
            else:
                if(it[0] not in used):
                    r *= it[0]
                    used.append(it[0])
        if(check):
            return t


print(main(res))
