"""
Problem Statement:
Given a string, find out minimum insertions to make a string palindrome.
"""


def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)

    # Base Case 1: First row and first column is always 0 because LCS("", s1) and LCS("", s2) is 0.
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    # For remaining possibilities, on match, you increment 1 character or on fail, you take maximum of picking either possibilities.
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if(s1[i-1] == s2[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n1][n2]

def lps(s):
    # LPS = LCS of the string and the reverse of the same string
    return lcs(s, s[::-1])

if __name__ == '__main__':
    print("Please enter the string")
    s = input().strip()

    long_pal_seq = lps(s)
    print(f"Minimum insertions to make the string {s} a palindrome is {len(s) - long_pal_seq}")