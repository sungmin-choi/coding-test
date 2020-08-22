# 왕실의 나이트
n = input()
count = 0

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


ri = int(row.index(n[0]))
ci = int(n[1])

a = [[ri-2, ci+1], [ri-2, ci-1], [ri-1, ci+2], [ri-1, ci-2],
     [ri+2, ci+1], [ri+2, ci-1], [ri+1, ci+2], [ri+1, ci-2]
     ]
for i in a:
    if i[0] < 0 or i[0] > 7 or i[1] < 1 or i[1] > 8:
        continue
    else:
        count += 1

print(count)
