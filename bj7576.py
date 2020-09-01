from collections import deque

m, n = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(queue, n, m, graph):
    count = -1
    while queue:

        count += 1
        for _ in range(len(queue)):  # 여기서 존나 헤멧음
            x, y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx > n-1 or nx < 0 or ny > m-1 or ny < 0:
                    continue
                else:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]+1
                        queue.append((nx, ny))

    for i in graph:
        if 0 in i:
            count = -1

    return count


print(bfs(queue, n, m, graph))
