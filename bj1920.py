n = int(input())
array = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

array.sort()
for i in array2:
    start = 0
    end = len(array)-1
    flag = False
    while start <= end:
        mid = (start+end)//2
        if i == array[mid]:
            flag = True
            break
        elif i < array[mid]:
            end = mid-1
        else:
            start = mid+1
    if flag:
        print("1", end="  ")
    else:
        print("0", end="  ")
