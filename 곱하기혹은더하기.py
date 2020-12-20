s = input()
array = []

for i in range(len(s)):
    array.append(int(s[i]))

array.sort(reverse=True)
result = array[0]
for i in range(1, len(array)):
    if array[i] == 0:
        continue
    elif array[i] == 1:
        result += array[i]
    else:
        result *= array[i]

print(result)
