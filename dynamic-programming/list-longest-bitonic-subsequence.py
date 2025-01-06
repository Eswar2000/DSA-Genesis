"""
Problem Statement:
Given an array, find the length of longest bitonic subsequence.
A bitonic subsequence is a sequence which is increasing and decreasing or decreasing and increasing.
It can't monotonously increase or decrease.
"""

def lis(arr):
    n = len(arr)
    
    # Base Case 1: For every element, LIS is 1 because by itself, the subsequence length is 1
    dp = [1] * n

    # For every element, if current element arr[i] is greater than any previous element arr[j], LIS is maximum by taking it or omitting it
    for i in range(1, n):
        for j in range(i):
            if(arr[i] > arr[j]):
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Unlike LIS, I am returning DP array itself, because for bitonic, I have to look from forward and backward and take a maximum together
    return dp

def lbs(arr):
    n = len(arr)

    # Forward DP array gives increasing subsequence info (from front)
    forward_dp = lis(arr)

    # It should not monotonously decrease (then, LIS would be as it is initialized, untouched)
    if(max(forward_dp) == 1):
        return 0

    # Backward DP array give decreasing subsequence info (from front) or increasing subsequence (from back)
    backward_dp = lis(arr[::-1])

    # It should not monotonously increase (then, LIS would be as it is initialized, untouched)
    if(max(backward_dp) == 1):
        return 0


    lbs_len = -1

    # Maximum bitonic sequence length is increasing subsequence length + decreasing subsequence length - 1 (the common element)
    for i in range(n):
        lbs_len = max(lbs_len, forward_dp[i] + backward_dp[i] - 1)

    return lbs_len


if __name__ == '__main__':
    print("Please input space separated array items")
    l = list(map(int, input().split(' ')))

    lbs_len = lbs(l)
    print(f"Longest bitonic subsequence length of the array {lbs_len}")