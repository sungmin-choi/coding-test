name = "ABAAAAABAB"


def solution(name):
    answer1 = 0
    answer2 = 0
    turn = 1
    name2 = []
    name1 = list(name)
    loc = 0
    p = 1
    for _ in range(len(name)):
        name2.append('A')
    while name1 != name2:
        if name1[loc] != name2[loc]:
            if ord(name[loc]) > 78:
                answer1 += 90-ord(name[loc])+1
            else:
                answer1 += ord(name[loc])-65
            name2[loc] = name1[loc]
        else:
            while loc+p < len(name) and name[loc+p] == 'A':
                p += 1
            if p > len(name)-p:
                turn = -1
            loc += turn
            answer1 += 1
    name2 = []
    for _ in range(len(name)):
        name2.append('A')
    loc = 0
    while name1 != name2:
        if name1[loc] != name2[loc]:
            if ord(name[loc]) > 78:
                answer2 += 90-ord(name[loc])+1
            else:
                answer2 += ord(name[loc])-65
            name2[loc] = name1[loc]
        else:
            loc -= 1
            answer2 += 1

    return min(answer1, answer2)


print(solution(name))
