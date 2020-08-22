from collections import deque
n, m, v = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))
visited = [False]*n

graph2 = [[] for _ in range(n)]

for i in range(m):
    graph2[graph[i][0]-1].append(graph[i][1])
    graph2[graph[i][1]-1].append(graph[i][0])

for i in range(n):
    graph2[i].sort()


def dfs(graph2, v, visited):
    visited[v-1] = True
    print(v, end=' ')
    for i in graph2[v-1]:
        if visited[i-1] == True:
            continue
        else:
            dfs(graph2, i, visited)


def bfs(graph2, v, visited):
    queue = deque([v])
    visited[v-1] = True
    while queue:
        t = queue.popleft()
        print(t, end=' ')
        for i in graph2[t-1]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1] = True


dfs(graph2, v, visited)
print('')
visited = [False]*n
bfs(graph2, v, visited)
