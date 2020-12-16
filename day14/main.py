import math
import re
import itertools


def readfile():
    with open("input.txt", "r") as f:
        res = []
        temp = []
        for row in f.read().split('\n'):
            if(row.split('=')[0] == 'mask '):
                res.append(temp)
                temp = []
                temp.append(row.split('=')[1].strip().rstrip())
            else:
                s = row.split('=')
                pos = s[0].strip('mem[')[:-2]
                nr = int(s[1])
                temp.append((int(pos), nr))
        res.append(temp)
    return res


arr = readfile()


def maskC(mask, number):
    res = []
    number = number[::-1]
    mask = mask[::-1]
    for i, it in enumerate(mask):
        if(it != 'X'):
            res.append(it)
        elif(i < len(number)):
            res.append(number[i])
        else:
            res.append('0')
    return res[::-1]


def genAll(n):
    return list(itertools.product([0, 1], repeat=n))


def solve(arr):
    res = {}
    for it in arr:
        if(it != []):
            mask = it[0]
            for jt in it[1:]:
                byteString = "{0:b}".format(jt[1])
                res[jt[0]] = int("".join(maskC(mask, byteString)), 2)
    return sum(list(res.values()))


print(solve(arr))


def mask2(mask, number):
    res = []
    varRes = []
    number = number[::-1]
    mask = mask[::-1]
    countx = 0
    for i, it in enumerate(mask):
        if(it == 'X'):
            res.append('X')
            countx += 1
        elif(it == '1'):
            res.append('1')
        elif(i < len(number)):
            res.append(number[i])
        else:
            res.append('0')

    res = res[::-1]
    var = genAll(countx)
    for it in var:
        temp = "".join(res.copy())
        for jt in it:
            temp = "".join(temp).replace('X', str(jt), 1)
        varRes.append(int(temp, 2))
    return(varRes)


def solve2(arr):
    res = {}
    for it in arr:
        if(it != []):
            mask = it[0]
            for jt in it[1:]:
                byteString = "{0:b}".format(jt[0])
                for kt in mask2(mask, byteString):
                    res[kt] = jt[1]
    return sum(list(res.values()))


print(solve2(arr))
