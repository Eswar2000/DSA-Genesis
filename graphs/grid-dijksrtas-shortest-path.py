"""
Problem Statement:
In a 2D grid with 1's and 0's, find the shortest path from a source to a destination. If a cell is marked as 1, user can walk over it else not.
Note: Since weight to travel from cell A to cell B is not given, you can assume it to be 1.
"""


def dijkstas(g, src):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    r, c = len(g), len(g[0])

    distance = [[float('inf') for _ in range(c)] for _ in range(r)]
    queue = []

    distance[src[0]][src[1]] = 0
    queue.append([0, src])

    while(len(queue) != 0):
        current_distance, current_cell = queue.pop(0)

        for dx, dy in directions:
            nbr_x, nbr_y = current_cell[0] + dx, current_cell[1] + dy
            if(is_valid(nbr_x, nbr_y, r, c) and g[nbr_x][nbr_y] == 1 and distance[nbr_x][nbr_y] > current_distance + 1):
                distance[nbr_x][nbr_y] = current_distance + 1
                queue.append([distance[nbr_x][nbr_y], [nbr_x, nbr_y]])
    
    return distance

def is_valid(x, y, r, c):
    return ((x >= 0 and x < r) and (y >=0 and y < c))

def print_grid(matrix):
    for row in matrix:
        print(' '.join([str(dist) for dist in row]))

if __name__ == '__main__':
    print("Enter the number of rows and columns in the grid")
    r, c = list(map(int, input().split(' ')))
    
    print("Enter the source in the grid")
    sx, sy = list(map(int, input().split(' ')))


    grid = []
    for i in range(r):
        print(f"Enter grid {i} as space separated values")
        row = list(map(int, input().split(' ')))
        grid.append(row)

    if not grid:
        print("No maze to navigate")
    elif grid[sx][sy] == 0:
        print("Source is not navigatable")
    else:
        distance = dijkstas(grid, [sx, sy])
        print("Printing the distance matrix")
        print_grid(distance)    