# linear search
list1 = [7, 8, 9, 4, 3]
t = 4
pos = -1


def searchtarget(list1, t):
    i = 0
    while i < len(list1):
        if list1[i] == t:
            globals()['pos'] = i
            return True
        i += 1
    return False


if searchtarget(list1, t):
    print('target found', pos)
else:
    print('not found')

# Binary search(values need to be sorted)
list2 = [7, 8, 9, 67, 89, 600]
t = 89
pos2 = -1


def bsearchtarget(list2, t):
    s = 0;
    e = len(list2) - 1
    while s <= e:
        m = (s + e) // 2
        if list2[m] > t:
            e = m - 1
        elif list2[m] < t:
            s = m + 1
        else:
            globals()['pos2'] = m
            return True
    return False


if bsearchtarget(list2, t):
    print('target found-binary', pos2)
else:
    print('not found')
