"""
Problem Statement:
Given an array, find the length of longest subset where any 2 elements from it are divisible.
Note: Subset is not same as subsequence - subset means in any order
"""


def divisble_subset(arr):
    n = len(arr)
    
    # optional - this will allow us to check ONLY arr[i] % arr[j] alone because 0 < j < i < n
    arr.sort()

    # An element by itself is part of the divisible subset (a trivial case, because we can't pick 2 elements)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if(arr[i] == 0 or arr[j] == 0 or arr[i]%arr[j] == 0):
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


if __name__ == '__main__':
    print("Enter array as space separated items")
    l = list(map(int, input().split(' ')))

    divisible_subset_len = divisble_subset(l)
    print(f"Length of longest subset where any 2 items picks is divisble by any of them are: {divisible_subset_len}")