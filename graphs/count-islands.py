"""
Problem Statement:
Given a 2D matrix / grid filled with 1 (representing land) and 0 (representing water), count the number of islands in it.
"""

def count_islands(g, m, n):
    visited = [[False for _ in range(n)] for _ in range(m)]
    islands = {}
    count = 0

    for i in range(m):
        for j in range(n):
            if(grid[i][j] == 1 and visited[i][j] == False):
                island_nodes = []
                dfs(i, j, g, visited, m, n, island_nodes)
                island_src = f"({i}, {j})"
                islands[island_src] = island_nodes
                count += 1
    return count

def dfs(x, y, g, visited, m, n, island_nodes):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited[x][y] = True
    island_nodes.append([x, y])

    for dir in directions:
        dx, dy = dir
        new_x, new_y = x + dx, y + dy

        if((new_x >= 0 and new_x < m) and (new_y >= 0 and new_y < n) and (g[new_x][new_y] == 1) and (not visited[new_x][new_y])):
            dfs(new_x, new_y, g, visited, m, n, island_nodes)

if __name__ == '__main__':
    islands = 0
    print("Please enter space separated values for grid dimensions")
    m, n = map(int, input().split(' '))
    print(f"No.of Rows: {m}, No.of Columns: {n}")
    
    grid = []
    for i in range(m):
        print(f"Please enter space separated values for grid row {i+1}")
        path_row = list(map(int, input().split(' ')))
        if len(path_row) != n:
            min_cost = -3
            break
        else:
            grid.append(path_row)

    if islands == -3:
        print("Invalid input passed by user. Column dimensions inputted doesn't match the row size populated")
    islands = count_islands(grid, m, n)
    print(f"Total islands in the grid is {islands}")