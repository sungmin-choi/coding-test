from collections import deque
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
    array = []
    answer = 0
    for skill_tree in skill_trees:
        for i in skill_tree:
            if i in skill:
                array.append(i)

        flag = True
        for k in range(len(array)):
            if skill[k] != array[k]:
                flag = False
                break

        if flag:
            answer += 1
        array = []
    print(answer)
    return answer


solution(skill, skill_trees)
