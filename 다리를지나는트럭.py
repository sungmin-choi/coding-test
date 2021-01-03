from collections import deque
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    array = deque()
    q = deque(truck_weights)
    array.append((q.popleft(), 1))
    answer += 1
    while array:
        if array[0][1] > bridge_length:
            array.popleft()
        if sum(array[0])+q[0] <= 10:
            array.append((q.popleft(), 1))
        for i in range(len(array)):
            array[i][1] += 1
        answer += 1

    return answer
