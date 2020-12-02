with open('input.txt', 'r') as content:
    strings = content.readlines()


def check(min, max, char, str):
    min = int(min)
    max = int(max)
    count = 0
    for it in str:
        if char == it:
            count = count + 1
    return (min <= count) and (max >= count)


def check_v2(min, max, char, str):
    min = int(min)
    max = int(max)
    A = str[min-1] == char
    B = str[max-1] == char
    return (A and not B) or (not A and B)


def count_2():
    i = 0
    for it in strings:
        temp = it.split(' ')
        maxmin = temp[0].split('-')
        if(check_v2(maxmin[0], maxmin[1], temp[1][0], temp[-1])):
            i = i + 1
    print(i)


def count():
    i = 0
    for it in strings:
        temp = it.split(' ')
        maxmin = temp[0].split('-')
        if(check(maxmin[0], maxmin[1], temp[1][0], temp[-1])):
            i = i + 1
    print(i)


count_2()
