"""
Problem Statement:
Given an array, find the length of longest increasing subsequence.
"""


def lis(arr):
    n = len(arr)

    # Base Case 1: By default, every element in an array is an increasing subsequence by itself, with length 1
    dp = [1] * n
    parent = [-1] * n

    # For every element in index i, dp[i] is length of the longest subsequence that is increasing till index i
    for i in range(1, n):
        for j in range(i):

            # if current element arr[i] greater than an of its previous element arr[j] and max(dp[j]+1, dp[i]) = dp[j] + 1, then update the lis of i and update parent array to track it
            if(arr[i] > arr[j] and dp[j]+1 > dp[i]):
                dp[i] = dp[j] + 1
                parent[i] = j

    # LIS is maximum value in DP array
    max_len = max(dp)

    # Find index of maximum length, to fetch the array
    temp = dp.index(max_len)
    lis_arr = []

    # As long as parent is not -1, append the element to LIS array and go to its parent
    while temp != -1:
        lis_arr.append(arr[temp])
        temp = parent[temp]
    
    return max_len, lis_arr[::-1]


if __name__ == '__main__':
    print("Please input space separated array items")
    l = list(map(int, input().split(' ')))

    lis_len, lis_arr = lis(l)
    print(f"Longest increasing subsequence of the array is {lis_arr} with length {lis_len}")
    