"""
Problem Statement:
Given a graph as adjacency list and a source, find the shortest path to reach all nodes.
"""
import heapq

def dijkstras(g, v, source):
    pq = []
    distance = [float('inf')] * v

    distance[source] = 0
    heapq.heappush(pq, [0, source])

    while(len(pq) != 0):
        cur_distance, cur_vertex = heapq.heappop(pq)
        
        for nbr_vertex, nbr_distance in g[cur_vertex]:
            if cur_distance + nbr_distance < distance[nbr_vertex]:
                distance[nbr_vertex] = cur_distance + nbr_distance
                heapq.heappush(pq, [cur_distance + nbr_distance, nbr_vertex])
    
    return distance

if __name__ == '__main__':
    print("Enter the number of vertices in the graph")
    v = int(input())

    print("Enter the source node")
    src = int(input())

    g = []
    for i in range(v):
        print(f"Enter the neighbours of node {i} in space separated manner (for each such node give node name and distance as comma separated values)")
        nbr = input().strip()
        if(nbr):
            nbrs = nbr.split(' ')
            nbrs = [list(map(int, edge.split(','))) for edge in nbrs]
            g.append(nbrs)
        else:
            g.append([])
        
    distance = dijkstras(g, v, src)
    print(f"Shortest distance from node {src} is {distance}")