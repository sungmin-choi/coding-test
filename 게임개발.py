n, m = map(int, input().split())
x, y, d = map(int, input().split())

count = 1
flag1 = True
flag2 = True
gmap = []
xd = [-1, 0, 1, 0]
yd = [0, -1, 0, 1]
xb = [0, -1, 0, 1]
yb = [-1, 0, 1, 0]

for i in range(n):
    gmap.append(list(map(int, input().split())))

c = 0

gmap[y][x] = 2
while flag1:
    if (x+xd[d] < m and x+xd[d] >= 0 and y+yd[d] < n and y+yd[d] >= 0):
        if gmap[y+yd[d]][x+xd[d]] == 0:
            x = x+xd[d]
            y = y+yd[d]
            if d == 0:
                d = 3
            else:
                d -= 1
            c = 0
            count += 1
            gmap[y][x] = 2

        else:
            if c == 4:
                if gmap[y+yb[d]][x+xb[d]] == 1:
                    flag1 = False
                    break
                else:
                    x = x+xb[d]
                    y = y+yb[d]
                c = 0
            else:
                if d == 0:
                    d = 3
                else:
                    d -= 1
                c += 1


print(count)
