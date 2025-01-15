"""
Problem Statement:
Given an array, print all possible subsequences.
Note: For a subsequence, order must be maintained, but it need not be contigious.
"""

def generate_subsequences(ind, n, l, subsequence, all_subsequences):
    if(ind >= n):
        all_subsequences.append(subsequence[:])
        return
    
    subsequence.append(l[ind])
    generate_subsequences(ind + 1, n, l, subsequence, all_subsequences)

    subsequence.pop()
    generate_subsequences(ind + 1, n, l, subsequence, all_subsequences)

if __name__ == '__main__':
    print("Enter the number of elements in the list")
    n = int(input())

    print("Enter the numbers as space separated items")
    arr = list(map(int, input().split(' ')))

    subequences = []

    generate_subsequences(0, n, arr, [], subequences)
    print(f"All possible subsequences of the array are: {subequences}")




