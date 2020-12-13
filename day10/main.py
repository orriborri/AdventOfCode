
from collections import defaultdict


def readfile():
    with open("input.txt", "r") as f:
        lines = list(map(lambda x: int(x), f.read().split('\n')))
        return lines


arr = readfile()

arr.sort()
arr2 = arr.copy()
arr = [0] + arr + [arr[-1] + 3]
i = 0
one = 0
three = 0
while(i+1 < len(arr)):
    diff = arr[i+1]-arr[i]
    if(diff > 3):
        break
    if(diff == 1):
        one += 1
    elif(diff == 3):
        three += 1
    i += 1

print((one)*(three))

# No idea why this works, got the quite a lot of help from reddit
dyn = [1] + [2] + [0] + [0] * (max(arr2)-1)
for i in arr2:
    for j in [1, 2, 3]:
        if (i-j in arr2):
            dyn[i] += dyn[i-j]

print(dyn[-2])
