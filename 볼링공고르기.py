n, m = map(int, input().split())
w = []
w = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i, n):
        if w[i] != w[j]:
            result += 1

print(result)
