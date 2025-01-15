"""
Problem Statement:
Given an array and a target sum, print all subsets that form the target sum. At a time, you can pick the element only once.
"""

def subset_sum(ind, sum, arr, n, subset, valid_subsets):
    if(ind >= n):
        if(sum == 0):
            valid_subsets.append(subset[:])
        return
    
    subset.append(arr[ind])
    subset_sum(ind + 1, sum - arr[ind], arr, n, subset, valid_subsets)

    subset.pop()
    subset_sum(ind + 1, sum, arr, n, subset, valid_subsets)

def count_subset_sum(ind, sum, arr, n):
    if(ind >= n):
        if(sum == 0):
            return 1
        return 0

    take = count_subset_sum(ind+1, sum - arr[ind], arr, n)
    not_take = count_subset_sum(ind+1, sum, arr, n)

    return take + not_take

def is_subset_sum(ind, sum, arr, n):
    if(ind >= n):
        if(sum == 0):
            return True
        return False

    take = count_subset_sum(ind+1, sum - arr[ind], arr, n)
    not_take = count_subset_sum(ind+1, sum, arr, n)

    return take or not_take


if __name__ == '__main__':
    print("Enter the number of elements in the array")
    n = int(input())

    print("Enter the target sum")
    target = int(input())

    print("Enter the array as space separated elements")
    l = list(map(int, input().split(' ')))

    valid_subsets = []

    is_valid_subset = is_subset_sum(0, target, l, n)
    num_valid_subsets = count_subset_sum(0, target, l, n)
    subset_sum(0, target, l, n, [], valid_subsets)
    
    print(f"Is there a subset from {l} that make up to {target}? {'Yes' if is_valid_subset else 'No'}")
    print(f"Number of valid subsets that make up to {target} are {num_valid_subsets}")
    print(f"All valid subsets that make up to {target} are {valid_subsets}")