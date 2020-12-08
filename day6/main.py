import math


def readfile():
    with open("input.txt", "r") as f:
        f_in = f.read()
        return f_in.split('\n\n')


def countOneYes(arr):
    count = 0
    for it in arr:
        resSet = set()
        for jt in it:
            if(jt != '\n'):
                resSet.add(jt)

        count += len(resSet)
    return(count)


def countAllYes(arr):
    count = 0
    for it in arr:
        first = True
        resSet = set()
        tempSet = set()
        for jt in it:
            if(jt == '\n'):
                if first:
                    resSet = tempSet
                    first = False
                else:
                    resSet = resSet.intersection(tempSet)
                tempSet = set()
            else:
                tempSet.add(jt)
        if(first):
            resSet = tempSet
        else:
            resSet = resSet.intersection(tempSet)
        count += (len(resSet))
    return(count)


arr = readfile()
print(countOneYes(arr))
print(countAllYes(arr))
