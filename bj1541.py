s = input().split('-')
b = []
answer = 0
for i in s:
    cnt = 0
    k = i.split('+')
    for t in k:
        cnt += int(t)
    b.append(cnt)

answer = b[0]
print(len(b))
for i in range(1, len(b)):
    answer -= b[i]

print(answer)
