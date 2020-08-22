n = int(input())
m = int(input())
count = 0
graph = []
array = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

for i in range(n+1):
    array[i].sort()


def dfs(array, v, visited):
    visited[v] = True
    for i in array[v]:
        if not visited[i]:
            dfs(array, i, visited)


dfs(array, 1, visited)
for i in visited:
    if i:
        count += 1
print(count-1)
