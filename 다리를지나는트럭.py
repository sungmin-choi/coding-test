from collections import deque
bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    array = deque()
    q = deque(truck_weights)
    w = q.popleft()
    array.append([w, 1])
    answer += 1
    while array:

        if array[0][1] > bridge_length:
            a, _ = array.popleft()
            w -= a
        if q:

            if w+q[0] <= weight:
                b = q.popleft()
                array.append([b, 1])
                w += b
        for i in range(len(array)):
            array[i][1] += 1
        answer += 1
    return answer


solution(bridge_length, weight, truck_weights)
