n = int(input())
array = []
group = 0

array = list(map(int, input().split()))
array.sort(reverse=True)
print(array)
i = 0
while i < n:
    a = array[i]
    if a+i <= n:
        group += 1
        i = i+a
    else:
        break

print(group)
