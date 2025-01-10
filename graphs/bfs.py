"""
Problem Statement:
Given a graph as adjacency list and a starting vertex, do breadth first search (level order traversal).
Assume that vertices are 0, 1, 2.......(v-1).
"""

def bfs(v, graph, src):
    visited = [False] * v
    result = []
    queue = []

    visited[src] = True
    queue.append(src)

    while len(queue) > 0:
        cur_node = queue.pop(0)

        result.append(cur_node)

        for neighbour in graph[str(cur_node)]:
            if visited[neighbour] == False:
                visited[neighbour] = True
                queue.append(neighbour)
    return result


if __name__ == '__main__':
    print("Enter number of vertices")
    v = int(input())

    g = {}
    for i in range(v):
        print(f"Enter space separated nodes connected to current node {i}")
        g[str(i)] = list(map(int, input().split(' ')))
    
    bfs_traversal = bfs(v, g, 0)
    print(f"BFS traversal of given graph: {bfs_traversal}")