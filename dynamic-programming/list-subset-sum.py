"""
Problem Statement:
Given an array of numbers and a target sum, state if that sum is achievable with the numbers from the array.
Subset means that order and whether an element is picked or not doesn't matter.
"""


def subset_sum(arr, target):
    n = len(arr)

    dp = [[False for _ in range(target + 1)] for __ in range(n+1)]

    # Base Case 1: For 1st column (target = 0) all are true because without picking any item, we can achieve target sum of 0
    for i in range(n):
        dp[i][0] = True

    # For any other cell, if target > the value, then we can try either picking them (so, dp[i-1][j - arr[i-1]] is for picking remaining part of target) or not picking them dp[i-1][j]
    for i in range(1, n+1):
        for j in range(1, target + 1):
            if(j >= arr[i-1]):
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][target]

if __name__ == '__main__':
    print("Enter space separated array items")
    l = list(map(int, input().split(' ')))

    print("Enter target sum")
    s = int(input().strip())

    possible_subset = subset_sum(l, s)
    if(possible_subset):
        print(f"Yes, one or more subset present which can make the target sum {s}")
    else:
        print(f"No subset available to make target {s}")
