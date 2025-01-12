"""
Problem Statement:
Given an undirected graph, find if it has a cycle.
"""

def detect_cycle(g, v, source):
    visited = [False] * v

    return dfs_util(g, visited, source, -1)


def dfs_util(g, visited, cur, parent):
    visited[cur] = True
    for neighbour in g[cur]:
        if visited[neighbour]:
            if neighbour != parent:
                return True
        else:
            return dfs_util(g, visited, neighbour, cur)
    return False

if __name__ == '__main__':
    print("Enter the number of vertices in the graph")
    v = int(input())

    g = []

    for i in range(v):
        print(f"Enter the neighbours of vertex {i} as space separated nodes")
        nbr = input().strip()
        if(nbr):
            g.append(list(map(int, nbr.split(' '))))
        else:
            g.append([])
    
    if(detect_cycle(g, v, 0)):
        print("Yes, the graph has cycle")
    else:
        print("The graph is not cyclic")