import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(a)
result = 0
while start <= end:
    l = 0
    mid = (start+end)//2
    for i in a:
        if i > mid:
            l += i-mid
    if l >= m:
        result = mid
        start = mid+1
    elif l < m:
        end = mid-1

print(result)
