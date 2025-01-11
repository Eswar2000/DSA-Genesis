"""
Problem Statement:
Given a DAG, provide the topological ordering of the vertices.
Topological ordering - a node can't be visited / processed without all its prerequisite nodes being visited first.
"""

def topology_sort(g, v):
    in_degree = [0] * v
    traversal = []
    queue = []

    for i in range(v):
        for nbr in g[i]:
            in_degree[nbr] += 1
    
    for i in range(v):
        if(in_degree[i] == 0):
            queue.append(i)
    
    while(len(queue) != 0):
        vert = queue.pop(0)
        traversal.append(vert)

        for nbr in g[vert]:
            in_degree[nbr] -= 1
            if(in_degree[nbr] == 0):
                queue.append(nbr)
    return traversal

if __name__ == '__main__':
    print("Enter the number of vertices in the graph")
    v = int(input())

    g = []
    for i in range(v):
        print(f"Enter the neighbours of node {i} in space separated manner")
        nbr = input().strip()
        if(nbr):
            g.append(list(map(int, nbr.split(' '))))
        else:
            g.append([])
        

    top_sort = topology_sort(g, v)
    print(f"Topological sorted order of given graph is {top_sort}")