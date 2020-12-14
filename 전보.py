import heapq
import sys
input = sys.stdin.readline
n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

INF = int(1e9)

distance = [INF]*(n+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for i in graph[now]:
            if distance[i[1]] > dis+i[0]:
                distance[i[1]] = dis+i[0]
                heapq.heappush(q, (dis+i[0], i[1]))


dijkstra(c)
a, b = 0, 0
for i in range(1, len(distance)):
    if distance[i] == INF:
        continue
    else:
        a += 1
        if b < distance[i]:
            b = distance[i]

print(a-1, b)
