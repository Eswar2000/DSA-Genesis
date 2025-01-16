"""
Problem Statement:
Given an array and target sum, print all subsets that can make up to the target.
Now, an element in the array can be taken multiple times.
"""

def combo_sum(ind, n, arr, s, subset, valid_subsets):
    if(ind >= n):
        if(s == 0 and subset not in valid_subsets):
            valid_subsets.append(subset[:])
        return        

    if(s < 0):
        return
    
    subset.append(arr[ind])
    combo_sum(ind + 1, n, arr, s - arr[ind], subset, valid_subsets)
    combo_sum(ind, n, arr, s - arr[ind], subset, valid_subsets)
    subset.pop()
    combo_sum(ind + 1, n, arr, s, subset, valid_subsets)

def is_combo_sum(ind, n, arr, s):
    if(ind >= n):
        if(s == 0):
            return True
        return False
    
    if(s < 0):
        return False
    
    take_and_move = is_combo_sum(ind + 1, n, arr, s - arr[ind])
    no_take_and_move = is_combo_sum(ind + 1, n, arr, s)
    take_and_no_move = is_combo_sum(ind, n, arr, s - arr[ind])

    return take_and_move or take_and_no_move or no_take_and_move


def count_combo_sum(ind, n, arr, s):
    if(ind >= n):
        if(s == 0):
            return 1
        return 0
    
    if(s < 0):
        return 0
    
    take_and_move = is_combo_sum(ind + 1, n, arr, s - arr[ind])
    no_take_and_move = is_combo_sum(ind + 1, n, arr, s)
    take_and_no_move = is_combo_sum(ind, n, arr, s - arr[ind])

    return take_and_move + take_and_no_move + no_take_and_move

if __name__ == '__main__':
    print("Enter size of the array")
    n = int(input())
    print("Enter the array as space separated elements")
    l = list(map(int, input().split(' ')))
    print("Enter a target sum")
    target = int(input())

    valid_subsets = []
    
    is_valid_combo_sum = is_combo_sum(0, n, l, target)
    valid_combo_sum_count = count_combo_sum(0, n, l, target)
    combo_sum(0, n, l, target, [], valid_subsets)

    
    print(f"Is there a combination sum to target {target}? {'Yes' if is_valid_combo_sum else 'No'}")
    print(f"Number of combinations to make up to {target} are {valid_combo_sum_count}")
    print(f"Possible combinations to make the target {target} are {valid_subsets}")
    