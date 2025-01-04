"""
Problem Statement:
Given a grid of size m and n repectively with NON-NEGATIVE values corresponding to weight when user travels through that cell, find minimum cost to reach bottom right cell from top left cell.
At any time, a move can be made to the right, down or diagonally.
You may assume that m, n >= 0.
"""


def minimum_cost_path(R, C, grid):
    dp = [[0 for _ in range(C)] for _ in range(R)]

    # Base Case 1: Top left cell is source, so minimum cost to reach the cell is its own cost
    dp[0][0] = grid[0][0]

    # Base Case 2: For the first row, cost to reach that node is cost to reach the left node + value at current node
    for i in range(1, C):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    # Base Case 3: For the first column, cost to reach that node is cost to reach the top node + value at current node
    for i in range(1, R):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, R):
        for j in range(1, C):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + grid[i][j]
    
    return dp[R-1][C-1]


if __name__ == '__main__':
    min_cost = 0
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

    if min_cost == -3:
        print("Invalid input passed by user. Column dimensions inputted doesn't match the row size populated")
    else:
        min_cost = minimum_cost_path(m, n, grid)
        print(f"Minimum cost to reach ({m-1}, {n-1}) from (0, 0) is {min_cost}")