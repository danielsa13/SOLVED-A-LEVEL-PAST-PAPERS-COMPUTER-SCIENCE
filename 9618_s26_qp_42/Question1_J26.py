TheData = ['laptop', 'tablet', 'printer', 'computer', 'processor', 'monitor', 'memory', 'cable', 'touchscreen']

def FindLongestShortest(TheArray):
    pos_short = 0
    pos_long = 0

    short = 999
    long = 0
    for index in range(len(TheArray)):
        if short > len(TheArray[index]):
            pos_short = index
            short = len(TheArray[index])

        if long < len(TheArray[index]):
            pos_long = index
            long = len(TheArray[index])

    print(f'Shortest string: {TheArray[pos_short]}')
    print(f'Longest string: {TheArray[pos_long]}')
    
FindLongestShortest(TheData)

def InsertionSort(TheArray):
    for i in range(len(TheArray)):
        j = i
        while TheArray[j-1] > TheArray[j] and j > 0:
            TheArray[j-1], TheArray[j] = TheArray[j], TheArray[j-1]
            j -= 1

    return TheArray

print("Before sorting")
print(TheData)
sorted_arr = InsertionSort(TheData)
print("After sorting")
print(sorted_arr)