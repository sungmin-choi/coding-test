def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
edges = []
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
result = []
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

result2 = 0
for i in range(len(result)-1):
    result2 += result[i]

print(result2)
