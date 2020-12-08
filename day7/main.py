import math


def readfile():
    bags = {}
    with open("input.txt", "r") as f:
        for row in f.readlines():
            bag, inside = parseLine(row)
            bags[bag] = inside
    return bags


def parseLine(line):
    rawSplit = line.split('contain')
    key = " ".join(rawSplit[0].split(' ')[:2])
    value = []
    rawValue = rawSplit[1].split(",")
    for it in rawValue:
        it = str.strip(it)
        if(it != "no other bags."):
            nr = int(it.split(' ')[0])
            it = " ".join(it.split(' ')[1:3])
            value.append((nr, it))

    return key, value


def inspectBags(initList):
    inspectBags = initList
    for it in inspectBags:
        inspect = bags[it]
        for jt in inspect:
            if(jt[1] == 'shiny gold'):
                return 1
            inspectBags.append(jt[1])
    return 0


def countGold(bags, bag):
    contains = bags[bag]
    count = 1
    if not contains:
        return count
    for amount, bag in contains:
        count += amount * countGold(bags, bag)
    return count


def containGold(initBags):
    count = 0
    for it in initBags:
        count += inspectBags([it])
    return count


bags = readfile()
print(containGold(list(bags.keys())))
print(countGold(bags, 'shiny gold')-1)
