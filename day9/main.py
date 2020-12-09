def readfile():
    with open("input.txt", "r") as f:
        lines = list(map(lambda x: int(x), f.read().split('\n')))
        return lines


def findSum(arr, target):
    for i in arr:
        for j in arr:
            if i + j == target:
                #print("found: ", i, "+", j, "=", target)
                return True
    return False


def verify(arr, preamble):
    for i, it in enumerate(arr):
        if(i < preamble):
            continue
        if(not findSum(arr[i-preamble:i], it)):
            return it


def findMinMax(arr):
    return min(arr)+max(arr)


def verify2(arr, target):
    res = []
    sum = 0
    for i, it in enumerate(arr):
        for jt in arr[i:]:
            sum += jt
            res.append(jt)
            if(sum == target):
                return res
            elif(sum > target):
                sum = 0
                res = []
                break


arr = readfile()
target = verify(arr, 25)

print(target)
print(findMinMax(verify2(arr, target)))
