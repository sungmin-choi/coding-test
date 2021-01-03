import heapq
n = int(input())
k = int(input())
smap = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    smap[x][y] = 1

l = int(input())

q = []
for _ in range(l):
    x, c = input().split()
    heapq.heappush(q, (int(x), c))

snake = [[0, 0]]
play = True
shx, shy = 0, 0
sl = 1
time = 0
while(play):
    if shx < 0 or shy < 0 or shx >= n or shy >= n:
        print(time)
        break
