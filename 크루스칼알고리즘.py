# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두원소가 속한 집합 합치기


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


# 노드의 개수와 간선 의 개수입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용 담을 변수

edges = []
result = 0

# 모든 간선 정보 입력받기

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, edge[1], edge[2])
        result += cost

print(result)
