"""
Problem Statement:
Given an array, identofy the length of longest decreasing subsequence.
"""


def lds(arr):
    n = len(arr)

    # Base Case 1: Each element is a decreasing subsequence by itself, so initialize with 1
    dp = [1] * n
    
    # For every item at index i, if item i is less than any item j, then LDS i will be maximum of LDS i and (LDS j + 1)
    for i in range(1, n):
        for j in range(i):
            if(arr[i] < arr[j] and dp[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == '__main__':
    print("Enter the array as space separated numbers")
    l = list(map(int, input().split(' ')))

    lds_len = lds(l)
    print(f"Length of longest decreasing subsequence is {lds_len}")