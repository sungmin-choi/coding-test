from sys import stdin
n = int(input())
array = sorted(map(int, stdin.readline().split()))
m = int(input())
array2 = map(int, stdin.readline().split())

for i in array2:
    start = 0
    end = n-1
    result = 0
    flag = True
    while start <= end:
        mid = (start+end)//2
        if array[mid] == i:
            result = array[start:end+1].count(i)
            print(result, end=" ")
            flag = False
            break
        elif array[mid] > i:
            end = mid-1
        else:
            start = mid+1
    if flag:
        print("0", end=" ")
