def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
result = []
for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union_parent(parent, a, b)
    if k == 1:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            result.append(1)
        else:
            result.append(0)

for i in result:
    if i == 1:
        print('YES')
    else:
        print('NO')
