"""
Problem Statement:
Given a grid size of m and n filled with 0's and 1's, Find the dimension of biggest square formed by group of 1's.
You may assume that m, n >= 0.
"""

def maximal_square(R, C, grid):
    dp = [[0 for _ in range(C)] for _ in range(R)]
    square_dimension = 0

    # Base Case 1: For the first row, maximum square dimension that can be formed is 1 if the cell is 1
    for i in range(C):
        if grid[0][i] == 1:
            dp[0][i] = 1

    # Base Case 2: For the first column, maximum square dimension that can be formed is 1 if the cell is 1
    for i in range(R):
        if grid[i][0] == 1:
            dp[i][0] = 1

    # For any other cell (if its 1), square dimension is minimum of (top, left and diagonally top node) + 1
    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0:
                square_dimension = max(square_dimension, dp[i][j])
            else:
                if grid[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    square_dimension = max(square_dimension, dp[i][j])
                else:
                    dp[i][j] = 0
    
    return square_dimension

if __name__ == '__main__':
    max_square_dim = 0
    print("Please enter space separated values for grid dimensions")
    m, n = map(int, input().split(' '))
    print(f"No.of Rows: {m}, No.of Columns: {n}")
    grid = []
    for i in range(m):
        print(f"Please enter space separated values for grid row {i+1}")
        path_row = list(map(int, input().split(' ')))
        if len(path_row) != n:
            max_square_dim = -3
            break
        else:
            grid.append(path_row)

    if max_square_dim == -3:
        print("Invalid input passed by user. Column dimensions inputted doesn't match the row size populated")
    else:
        max_square_dim = maximal_square(m, n, grid)
        print(f"Maximal square dimension within the grid is {max_square_dim}")