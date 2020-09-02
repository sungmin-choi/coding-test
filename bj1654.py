import sys  # 이렇게 써야 매우 입력할때 많은양의 데이터도 빠르게 입력됨
k, n = map(int, sys.stdin.readline().split())
array = []
for i in range(k):
    array.append(int(sys.stdin.readline()))

start = 1
end = max(array)
result = 0
while start <= end:
    count = 0
    mid = (start+end)//2
    for i in array:
        count += i//mid
    if count >= n:  # 여기 존나 헷갈린다...
        result = mid
        start = mid+1
    elif count < n:
        end = mid-1

print(result)
