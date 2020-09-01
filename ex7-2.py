n = int(input())
array = list(map(int, input().split()))

m = int(input())
array2 = list(map(int, input().split()))

array.sort()


def binary_search(array, start, end, target):
    if start >= end:
        return None
    middle = int((start+end)//2)
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search(array, start, middle-1, target)
    else:
        return binary_search(array, middle+1, end, target)


for i in array2:
    print(binary_search(array, 0, n-1, i), end=' ')
