n, k = map(int, input().split())
list = []
count = 0

for i in range(n):
    t = input()
    list.append(int(t))

list.sort(reverse=True)
for i in list:
    if k//i > 0:
        count += k//i
        k %= i

print(count)
