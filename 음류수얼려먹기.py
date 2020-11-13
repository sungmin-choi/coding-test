n, m = map(int, input().split())
graph = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(graph, y, x):
    graph[y][x] = 2
    for i in range(4):
        if x+dx[i] < m and x+dx[i] >= 0 and y+dy[i] < n and y+dy[i] >= 0:
            if graph[y+dy[i]][x+dx[i]] == 0:
                x = x+dx[i]
                y = y+dy[i]
                dfs(graph, y, x)


for j in range(n):
    for k in range(m):
        if graph[j][k] == 0:
            dfs(graph, j, k)
            count += 1


print(count)
