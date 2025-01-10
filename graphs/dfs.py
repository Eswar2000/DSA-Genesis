"""
Problem Statement:
Given a graph as adjacency list and a starting vertex, do depth first search.
Assume that vertices are 0, 1, 2.......(v-1).
"""

def dfs(vertices, graph, src):
    visited = [False] * vertices
    result = []
    dfs_util(graph, visited, src, result)
    return result

def dfs_util(graph, visited, vert, res):
    visited[vert] = True
    res.append(vert)

    for neighbour in graph[str(vert)]:
        if visited[neighbour] == False:
            dfs_util(graph, visited, neighbour, res)


if __name__ == '__main__':
    print("Enter number of vertices")
    v = int(input())

    g = {}
    for i in range(v):
        print(f"Enter space separated nodes connected to current node {i}")
        g[str(i)] = list(map(int, input().split(' ')))
    
    dfs_traversal = dfs(v, g, 0)
    print(f"DFS traversal of given graph: {dfs_traversal}")