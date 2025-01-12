"""
Problem Statement:
Given a graph as adjacency list and a source, find the no.of shortest paths to reach all nodes.
"""
import heapq

def dijkstras(g, v, src):
    pq = []
    distance = [float('inf')] * v
    ways = [0] * v

    distance[src] = 0
    ways[0] = 1

    heapq.heappush(pq, [0, src])

    while(len(pq) != 0):
        current_distance, current_vertex = heapq.heappop(pq)

        for nbr_vertex, nbr_distance in g[current_vertex]:
            if(current_distance + nbr_distance < distance[nbr_vertex]):
                distance[nbr_vertex] = current_distance + nbr_distance
                ways[nbr_vertex] = ways[current_vertex]
                heapq.heappush(pq, [current_distance + nbr_distance, nbr_vertex])
            elif(current_distance + nbr_distance == distance[nbr_vertex]):
                ways[nbr_vertex] += ways[current_vertex]
            else:
                continue
    return ways
    

if __name__ == '__main__':
    print("Enter the number of vertices in the graph")
    v = int(input())

    print("Enter the source node")
    src = int(input())

    print("Enter the destination node")
    dest = int(input())

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
        
    ways = dijkstras(g, v, src)
    print(f"No.of ways to reach {dest} from {src} is {ways[dest]}")