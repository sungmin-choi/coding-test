import sys


def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start+end)//2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        binary_search(array, target, start, mid-1)
    else:
        binary_search(array, target, mid+1, end)


n = int(input())
list1 = []
list1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
list2 = []
list2 = list(map(int, sys.stdin.readline().rstrip().split()))
list1.sort()
for i in list2:
    if binary_search(list1, i, 0, len(list1)-1):
        print("no")
    else:
        print("yes")
