from collections import deque
import sys
sys.setrecursionlimit(10000)


def bfs(c):
    q = deque([c])
    visited[c] = True
    while q:
        v = q.popleft()
        for e in graph[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0

for j in range(1, n+1):
    if not visited[j]:
        bfs(j)
        count += 1
print(count)
