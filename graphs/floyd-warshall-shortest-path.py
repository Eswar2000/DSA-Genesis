"""
Problem Description:
Given a graph as a matrix, find shortest path from all sources to all destination.
Traditionally, dijkstra's is a single source shortest path (finding shortest path from single source to all other vertices).
"""


def floyd_warshal(g, v):

    for i in range(v):
        for j in range(v):
            if(i != j and g[i][j] == 0):
                g[i][j] = float('inf')
            if(i == j):
                g[i][j] = 0

    for via in range(v):
        for i in range(v):
            for j in range(v):
                g[i][j] = min(g[i][j], g[i][via] + g[via][j])
    
    return g

def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(dist) for dist in row]))

if __name__ == '__main__':
    print("Please provide number of vertices in graph")
    v = int(input())

    g = []
    for i in range(v):
        print(f"Please provide weight to travel from {i} to all other nodes as space separated entries")
        wts = list(map(int, input().split(' ')))
        g.append(wts)
    
    distance_matrix = floyd_warshal(g, v)

    print("Printing Floyd Warshall Distance Matrix")
    print_matrix(distance_matrix)
