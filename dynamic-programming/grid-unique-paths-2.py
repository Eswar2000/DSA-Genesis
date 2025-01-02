"""
Problem Statement:
Given a grid size of m and n where they correspond to no.of rows and columns of a 2D matrix respectively, find the number of unique paths that might enable an user to reach bottom right cell.
At any time, a move can be made to the right or down. If encountered with an obstactle (1 in the matrix), user can't move through it
You may assume that m, n >= 0.
"""


def grid_unique_path_with_obstacle(R, C, grid):
    dp = [[0 for _ in range(C)] for _ in range(R)]

    # Base Case 1: If grid is empty, exit out
    if not path:
        return -2
    
    # Base Case 2: If source or destination node is an obstacle, exit out
    elif path[0][0] == 1 or path[m-1][n-1] == 1:
        return -1
    
    else:
        # Source node is marked as valid (1 way to reach source node)
        dp[0][0] = 1

        # Base Case 3: First row is always 1 until an obstacle is encounterd
        for i in range(1, C):
            if grid[0][i] == 1:
                break
            dp[0][i] = 1

        # Base Case 4: First column is always 1 until an obstacle is encounterd
        for i in range(1, R):
            if grid[i][0] == 1:
                break
            dp[i][0] = 1

        # For any other cell (if not blocked), no.of of ways to reach it is sum of no.of ways to reach from top and no.of ways to reach from left
        for i in range(1, R):
            for j in range(1, C):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[R-1][C-1]

if __name__ == '__main__':
    total_paths = 0
    print("Please enter space separated values for grid dimensions")
    m, n = map(int, input().split(' '))
    print(f"No.of Rows: {m}, No.of Columns: {n}")
    path = []
    for i in range(m):
        print(f"Please enter space separated values for grid row {i+1}")
        path_row = list(map(int, input().split(' ')))
        if len(path_row) != n:
            total_paths = -3
            break
        else:
            path.append(path_row)

    if total_paths == -3:
        print("Invalid input passed by user. Column dimensions inputted doesn't match the row size populated")
    else:
        total_paths = grid_unique_path_with_obstacle(m, n, path)
        
        if total_paths == -2:
            print("Invalid grid")
        elif total_paths == -1:
            print("Source or destination node is blocked")
        else:
            print(f"Number of ways to reach ({m-1}, {n-1}) cell from (0, 0): {total_paths}")


    
