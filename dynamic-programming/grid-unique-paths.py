"""
Problem Statement:
Given a grid size of m and n where they correspond to no.of rows and columns of a 2D matrix respectively, find the number of unique paths that might enable an user to reach bottom right cell.
At any time, a move can be made to the right or down.
You may assume that m, n >= 0.
"""


def grid_unique_paths(R, C):
    dp = [[0 for _ in range(C)] for _ in range(R)]

    # Base Case 1: First row is always 1 (from (0,0), we can only move right)
    for i in range(C):
        dp[0][i] = 1

    # Base Case 2: First column is always 1 (from (0,0), we can only move down)
    for i in range(R):
        dp[i][0] = 1

    # For any other cell, no.of of ways to reach it is sum of no.of ways to reach from top and no.of ways to reach from left
    for i in range(1, R):
        for j in range(1, C):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[R-1][C-1]

if __name__ == '__main__':
    print("Please enter space separated values for grid dimensions")
    m, n = map(int, input().split(' '))
    print(f"No.of Rows: {m}, No.of Columns: {n}")
    total_paths = grid_unique_paths(m, n)
    print(f"Number of unique paths in a grid to reach ({m-1}, {n-1}) from (0, 0) is {total_paths}")
    
