import copy


def readfile():
    with open("input.txt", "r") as f:
        lines = f.read().split('\n')
        res = []
        for it in lines:
            temp = it.split(' ')
            res.append([temp[0], int(temp[1]), 0])
        return res


cmd = readfile()


def resetArray():
    for i, it in enumerate(cmd):
        cmd[i][2] = 0


def checkProgram(cmd):
    acc = 0
    i = 0
    succsess = False
    while(True):
        if(not (0 <= i < len(cmd))):
            break
        currCmd = cmd[i]
        if(currCmd[2] == 1):
            break
        if(i == len(cmd)-1):
            succsess = True
            break
        if(currCmd[0] == 'acc'):
            acc += currCmd[1]
            i += 1
        elif(currCmd[0] == 'nop'):
            i += 1
        elif(currCmd[0] == 'jmp'):
            i += currCmd[1]
        currCmd[2] += 1
    return(acc, succsess)


deepCmd = copy.deepcopy(cmd)
print(checkProgram(deepCmd)[0])
acc = 0

for i, derp in enumerate(cmd):
    deep = copy.deepcopy(cmd)
    if(cmd[i][0] == 'nop'):
        deep[i][0] = 'jmp'
    elif(cmd[i][0] == 'jmp'):
        deep[i][0] = 'nop'
    else:
        continue
    acc, succ = checkProgram(deep)
    if(succ):
        break


print(acc)
