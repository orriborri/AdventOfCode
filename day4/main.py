import re


def readfile():
    result = []
    with open("input.txt", "r") as f:
        tempArr = []
        for row in f:
            if row == '\n':
                result.append(tempArr)
                tempArr = []
            else:
                tempArr = tempArr + row.split(' ')
        result.append(tempArr)
    return result


def check(arr, req):
    count = 0
    validCount = 0
    for rec in arr:
        reqFilled = 0
        reqValid = False
        valid = True

        for it in rec:
            key = it.split(':')[0]
            value = it.split(':')[1].split('\n')[0]
            if(key in req):
                reqFilled += 1
            if not checkValid(key, value) and valid:
                valid = False

        if(reqFilled == len(req)):
            count += 1
            reqValid = True
        if(valid and reqValid):
            validCount += 1

    return count, validCount


def checkInt(min, max, value):
    value = int(value)
    r = min <= value <= max
    return min <= value <= max


def checkValid(key, value):
    if(key == 'byr'):
        return checkInt(1920, 2002, value)
    elif(key == 'iyr'):
        return checkInt(2010, 2020, value)
    elif(key == 'eyr'):
        return checkInt(2020, 2030, value)
    elif(key == 'hgt'):
        unit = value[-2:]
        value = value.split(unit)[0]
        if(unit == 'cm'):
            return checkInt(150, 193, value)
        elif(unit == 'in'):
            return checkInt(59, 76, value)
        else:
            return False
    elif key == 'hcl':
        return not not re.match(r'(^#[0-9a-f]{6}$)', value)
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return not not re.match(r'^[0-9]{9}$', value)
    else:
        return True


def main():
    arr = readfile()
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    print(check(arr, req))


main()
