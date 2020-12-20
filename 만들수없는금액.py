n = int(input())
array = []
array = list(map(int, input().split()))

array.sort(reverse=True)
print(array)
i = 1
while 1:
    a = i
    for j in array:
        if a < j:
            continue
        else:
            a = a-j
    if a != 0:
        break
    else:
        i += 1
print(i)
