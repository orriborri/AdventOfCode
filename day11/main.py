import copy


def readfile():
    l = []
    with open("input.txt", "r") as f:
        for row in f.read().split('\n'):
            l.append(list(row))
    return l


def lookAround(i, j, arr, findEmpty, a, onlyNearest):
    count = 0
    for ii in [-1, 0, 1]:
        for jj in [-1, 0, 1]:
            k = 1
            while True:
                if(not (ii == 0 and jj == 0)):
                    di = i-(ii*k)
                    dj = j-(jj*k)
                    if(di >= 0 and di < len(arr) and dj >= 0 and dj < len(arr[0])):
                        if(arr[di][dj] == '#' and findEmpty):
                            return False
                        elif(arr[di][dj] == '#'):
                            count += 1
                            if(count >= a):
                                return True
                            break
                        if onlyNearest:
                            break
                        elif(arr[di][dj] == 'L'):
                            break
                        k += 1
                        continue
                break
    return False or findEmpty


# occAround(2, 0, old)
def simulate(old, nr, nearest):
    update = True
    new = copy.deepcopy(old)

    while(update):
        update = False
        for i, it in enumerate(old):
            for j, jt in enumerate(it):
                if(jt == 'L' and lookAround(i, j, old, True, nr, nearest)):
                    new[i][j] = '#'
                    update = True

                elif(jt == '#' and lookAround(i, j, old, False, nr, nearest)):
                    new[i][j] = 'L'
                    update = True
        old = copy.deepcopy(new)
    return new


def count(arr):
    count = 0
    for i in arr:
        for j in i:
            if(j == '#'):
                count += 1
    return count


old = readfile()


print(count(simulate(old, 4, True)))
print(count(simulate(old, 5, False)))
