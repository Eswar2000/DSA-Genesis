"""
Problem Statement:
Given an array, return the length of longest subsequence where all the elements are in a difference of 1.
"""

def lcs(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if(abs(arr[i] - arr[j]) == 1):
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


if __name__ == '__main__':
    print("Please input the array as space separated elements")
    l = list(map(int, input().split(' ')))

    con_max_len = lcs(l)
    print(f"Length of longest consecutive (whose value differ by 1) subsequence is {con_max_len}")