
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=",")
    # 현재 노드와 연결된 다른 노그를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [1, 2],
    [0, 3, 4, 5],
    [0, 6],
    [1],
    [1],
    [1],
    [2]
]

visited = [False]*9

dfs(graph, 0, visited)
