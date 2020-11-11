
oid search(Node root) {
    if (root == null) return
    # 1. root 노드 방문
    visit(root)
    root.visited = true  # 1-1. 방문한 노드를 표시
    # 2. root 노드와 인접한 정점을 모두 방문
    for each(Node n in root.adjacent) {
        if (n.visited == false) {  # 4. 방문하지 않은 정점을 찾는다.
            search(n)  # 3. root 노드와 인접한 정점 정점을 시작 정점으로 DFS를 시작
        }
    }
}
