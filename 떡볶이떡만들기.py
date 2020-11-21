def binary_search(array, target, start, end, goal):
    goal = (start+end)//2
    count = 0
    for i in array:
        if i > goal:
            count += i-goal
    if count == target:
        print(goal)
        return
    elif count > target:
        if goal+1 > end:
            print(goal)
            return
        binary_search(array, target, goal+1, end, goal)
    else:
        binary_search(array, target, start, goal-1, goal)


n, m = map(int, input().split())

array = list(map(int, input().split()))

binary_search(array, m, 0, max(array), 0)
