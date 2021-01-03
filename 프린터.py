from collections import deque
priorities = [2, 1, 3, 2]
location = 2


def solution(priorities, location):
    array = []
    answer = 0
    p_que = deque()

    for i in range(len(priorities)):
        p_que.append((priorities[i], i))
    while p_que:
        a, index = p_que.popleft()
        flag = True
        for n, i in p_que:
            if n > a:
                p_que.append((a, index))
                flag = False
                break
        if flag:
            array.append(index)
    answer = array.index(location)+1
    return answer


solution(priorities, location)
