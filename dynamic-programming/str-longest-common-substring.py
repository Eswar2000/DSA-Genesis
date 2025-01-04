"""
Problem Statement:
Given 2 strings, find out the length of longest substring (contiguous subarry) that is common among both strings.
"""


def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)
    max_len = 0

    # Base Case 1: First row and first column is always 0 because LCS("", s1) and LCS("", s2) is 0.
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    # If there is a match, increment the value of LCS for that cell and update the global maximum variable. If no match, then LCS for that cell is 0 because its a substring
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if(s1[i-1] == s2[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
                if(max_len < dp[i][j]):
                    max_len = dp[i][j]
                    ending_index = i-1
            else:
                dp[i][j] = 0
    return max_len

if __name__ == '__main__':
    print("Please enter string 1: ")
    s1 = input().strip()
    print("Please enter string 2: ")
    s2 = input().strip()

    lcs_len = lcs(s1, s2)
    print(f"Longest common substring of {s1} and {s2} is {lcs_len}")