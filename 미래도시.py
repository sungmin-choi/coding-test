import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

x, k = map(int, input().split())
start = 1


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


dijkstra(start)
cost = distance[k]
distance = [INF]*(n+1)
dijkstra(k)
if distance[x] == INF:
    print(-1)
else:
    print(cost+distance[x])
