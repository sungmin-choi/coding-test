from collections import deque
n, k = map(int, input().split())
answer = 0
visited = []


def bfs(n, k, answer, visited):
    queue = deque([n])
    while queue:
        n = queue.popleft()
        if n in visited:
            continue
        else:
            visited.append(n)
            queue.append(n+1)
            queue.append(n-1)
            queue.append(n*2)
        answer += 1
        if k in queue:
            break
    print(answer)


bfs(n, k, answer, visited)
