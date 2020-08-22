n = int(input())
array = []
array2 = []
k = 0
array2.append(0)
for i in range(n):
    array.append(list(map(int, input())))


def dsf(array, i, j, array2, k):
    if i >= n or i < 0 or j >= n or j < 0:
        return False
    if array[i][j] == 1:
        array[i][j] = 2
        array2[k] += 1
        dsf(array, i+1, j, array2, k)
        dsf(array, i, j+1, array2, k)
        dsf(array, i-1, j, array2, k)
        dsf(array, i, j-1, array2, k)


for i in range(n):
    for j in range(n):
        dsf(array, i, j, array2, k)
        k += 1
        array2.append(0)

array2.sort()

print(len(array2)-array2.count(0), end='\n')
for i in array2:
    if i != 0:
        print(i, end='\n')
