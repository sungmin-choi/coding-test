from collections import deque
n, m = map(int, input().split())
graph = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(graph, n, m):
    count = 0
    queue = deque([(0, 0)])
    graph[0][0] = 0
    while queue:
        if (n-1, m-1) in queue:
            count += 1
            break
        x, y = queue.popleft()
        for i in range(4):
            if x+dx[i] >= 0 and x+dx[i] < n and y+dy[i] >= 0 and y+dy[i] < m:
                if graph[x+dx[i]][y+dy[i]] == 1:
                    queue.append((x+dx[i], y+dy[i]))
                    graph[x+dx[i]][y+dy[i]] = 0
                    break
        count += 1
    print(count)


bfs(graph, n, m)
