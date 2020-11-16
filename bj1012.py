import sys
sys.setrecursionlimit(100000)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if xx < m and xx >= 0 and yy < n and yy >= 0:
            if graph[yy][xx] == 1:

                graph[yy][xx] = 0
                dfs(xx, yy)


answer = []
t = int(input())
for i in range(t):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for e in range(n):
        for q in range(m):
            if graph[e][q] == 1:
                dfs(q, e)
                count += 1
    answer.append(count)

for i in answer:
    print(int(i))
