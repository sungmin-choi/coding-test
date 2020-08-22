
from collections import deque
n, m = map(int, input().split())
graph = []


for i in range(n):
    graph.append(list(map(int, input())))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        for k in range(4):
            x, y = queue.popleft()
            nx = x+dx[k]
            ny = y+dy[k]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            else:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] += 1
    return graph[n-1][m-1]
