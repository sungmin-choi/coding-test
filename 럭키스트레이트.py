s = input()
mid = len(s)/2
a = 0
b = 0
for i in range(len(s)):
    if i < mid:
        a += int(s[i])
    else:
        b += int(s[i])

if a == b:
    print('LUCKY')
else:
    print('READY')
