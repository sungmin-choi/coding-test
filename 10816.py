import sys


def binary_search(array, target, start, end, count):
    l = len(array)
    while start <= end:
        mid = (end+start)//2
        if array[mid] == target:
            count += 1
            i, j = 1, 1
            while mid-i >= 0:
                if array[mid-i] != target:
                    break
                i += 1
                count += 1
            while mid+j <= l-1:
                if array[mid+j] != target:
                    break
                j += 1
                count += 1
            break
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

    print(count, end=" ")


n = int(input())
array1 = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
array2 = list(map(int, sys.stdin.readline().split()))


for i in array2:
    binary_search(array1, i, 0, len(array1)-1, 0)

print(array2)
