from collections import deque


def bfs(n):
    count = 0
    queue = deque([[n, count]])
    while queue:
        s = queue.popleft()
        v = s[0]
        count = s[1]

        if not visited[v]:
            visited[v] = True
            if v == k:
                return count
            count += 1
            if v*2 <= 100000:
                queue.append([v*2, count])
            if v+1 <= 100000:
                queue.append([v+1, count])
            if v-1 >= 0:
                queue.append([v-1, count])
    return count


n, k = map(int, input().split())
visited = [False]*100001
print(bfs(n))
