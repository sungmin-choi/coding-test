array = [5, 3, 8, 4, 9, 1, 6, 2, 7]


def quick(array, start, end):
    if start >= end:
        return
    pivot = start  # 첫원소 피벗으로 지정
    left = start
    right = end
    while left <= right:
        while left <= end and array[left] < array[pivot]:  # 피벗보다 큰 숫자 나올때 까지 수행
            left += 1
        while end >= right and array[end] > array[pivot]:
            end -= 1
        if left > right:  # 엇갈리면 피벗이랑 교환
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 안 엇갈렷으면 작은데이터와 큰 데이터 교환
            array[right], array[left] = array[left], array[right]
    quick(array, start, right-1)
    quick(array, right+1, end)


quick(array, 0, len(array)-1)
print(array)
