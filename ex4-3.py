# 게임 개발
# 한번 더 풀어보자!

n, m = map(int, input().split())
x, y, d = map(int, input().split())
dl = [[0, -1], [-1, 0], [0, 1], [1, 0]]
array = [[0]*m for i in range(n)]
dmap = [[0]*m for _ in range(n)]
flag = True
for i in range(n):
    a = list(map(int, input().split()))
    array[i] = a
count = 0
t = 0
while flag:
    d -= 1
    if d == -1:
        d = 3
    if array[x+dl[d][0]][y+dl[d][1]] == 0 and dmap[x+dl[d][0]][y+dl[d][1]] == 0:
        dmap[x+dl[d][0]][y+dl[d][1]] = 1
        x += dl[d][0]
        y += dl[d][1]
        count += 1
        t = 0
        continue
    else:
        t += 1
    if t == 4:
        if array[x-dl[d][0]][y-dl[d][1]] == 0:
            x -= dl[d][0]
            y -= dl[d][1]
        else:
            break
        t = 0

print(count)
