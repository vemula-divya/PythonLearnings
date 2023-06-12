# bubble sort
list1 = [5, 3, 8, 6, 7, 2]


def bubblesort(list1):
    for i in range(len(list1) - 1, 0, -1):
        for j in range(i):
            if list1[j] > list1[j + 1]:
                t = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = t


bubblesort(list1)
print(list1)

# selection sort
list2 = [5, 3, 8, 6, 7, 2]


def selectionsort(list2):
    for i in range(0, len(list2) - 1):
        minpos = i
        for j in range(i, len(list2)):
            if list2[j] < list2[minpos]:
                minpos = j
        temp = list2[i]
        list2[i] = list2[minpos]
        list2[minpos] = temp


selectionsort(list2)
print(list2)
