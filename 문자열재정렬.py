data = input()
data = list(data)
alpha = []
number = 0
for i in data:
    if i.isalpha():
        alpha.append(i)
    else:
        number += int(i)

alpha.sort()
print(''.join(alpha)+str(number))
