n = input()
data = list(map(int, input().split()))

data.sort()
answer = 0
result = 0

for i in data:
    answer += i
    result += answer

print(result)
