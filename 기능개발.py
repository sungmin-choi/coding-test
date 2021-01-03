from collections import deque
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    answer = []
    qp = deque(progresses)
    qs = deque(speeds)
    while qp:
        count = 1
        op = qp.popleft()
        os = qs.popleft()
        while op < 100:
            op += os
            for i in range(len(qp)):
                if qp[i] >= 100:
                    continue
                else:
                    qp[i] += qs[i]
        flag = True
        i = 0
        while flag:
            if qp:
                if qp[0] >= 100:
                    count += 1
                    i += 1
                    qp.popleft()
                    qs.popleft()
                else:
                    answer.append(count)
                    break

            else:
                answer.append(count)
                break
    return answer


solution(progresses, speeds)
