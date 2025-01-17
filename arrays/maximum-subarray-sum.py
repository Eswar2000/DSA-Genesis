"""
Problem Statement:
Given an array, find the maximum sum possible with any subarray.
Given array contains positive and negative numbers.
"""

def kadane_algorithm(arr, n):
    cur_sum, max_sum = 0, -float('inf')
    for i in range(n):
        cur_sum += arr[i]
        max_sum = max(max_sum, cur_sum)
        cur_sum = max(cur_sum, 0)
    return max_sum

if __name__ == '__main__':
    print("Enter the size of the array")
    n = int(input())

    print("Enter the array as space separated elements")
    arr = list(map(int, input().split()))

    s = kadane_algorithm(arr, n)
    print(f"Maximum subarray sum for {arr} is {s}")