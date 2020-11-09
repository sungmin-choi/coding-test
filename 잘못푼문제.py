n = int(input())

list = [0, 0, 0, 0, 0, 0]

m = n*60*60
count = 0
for i in range(m):
    m1 = int(i/3600)
    if m1 > 10:
        list[0] = int(m1/10)
        list[1] = m1 % 10
    else:
        list[0] = 0
        list[1] = m1
    m2 = int((i % 3600)/60)
    if m2 > 10:
        list[2] = int(m2/10)
        list[3] = m2 % 10
    else:
        list[2] = 0
        list[3] = m2
    m3 = i % 60
    if m3 > 10:
        list[4] = int(m3/10)
        list[5] = m3 % 10
    else:
        list[4] = 0
        list[5] = m3
    if 3 in list:
        count += 1

print(count)


# 이거 정답

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
