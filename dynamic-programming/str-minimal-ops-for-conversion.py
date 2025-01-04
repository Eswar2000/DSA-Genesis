"""
Problem Statement:
Given 2 strings S1 and S2, find out minimum operations (insertions and deletions) to convert S1 to S2.
"""

def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)

    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if(s1[i-1] == s2[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n1][n2]

if __name__ == '__main__':
    print("Please enter string 1: ")
    s1 = input().strip()
    print("Please enter string 2: ")
    s2 = input().strip()

    lcs_len = lcs(s1, s2)
    print(f"Longest common subsequence length for {s1} and {s2} is {lcs_len}")
    total_deletions = len(s1) - lcs_len
    total_insertions = len(s2) - lcs_len
    print(f"Minimum insertions and deletions to convert {s1} to {s2} is {total_deletions + total_insertions}")