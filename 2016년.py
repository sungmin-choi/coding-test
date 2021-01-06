a, b = 3, 6


def solution(a, b):
    answer = ''
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    position = 5
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(len(month)):
        if i == a-1:
            for _ in range(b-1):
                if position == 6:
                    position = 0
                else:
                    position += 1
            answer = week[position]
            break
        else:
            for _ in range(month[i]):
                if position == 6:
                    position = 0
                else:
                    position += 1

    return answer


print(solution(a, b))
