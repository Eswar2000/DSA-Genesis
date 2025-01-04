"""
Problem Statement:
Given 2 strings, find out the length of longest subsequence that is common among both strings.
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
    
    lcs_str = get_lcs(s1, s2, dp)
    return dp[n1][n2], lcs_str

def get_lcs(s1, s2, dp):
    m, n = len(s1), len(s2)
    s = ""

    while(m > 0 and n > 0):
        if(s1[m-1] == s2[n-1]):
            s += s1[m-1]
            m -= 1
            n -= 1
        elif(dp[m-1][n] > dp[m][n-1]):
            m -= 1
        else:
            n -= 1
    return s[::-1]

if __name__ == '__main__':
    print("Please enter string 1: ")
    s1 = input().strip()
    print("Please enter string 2: ")
    s2 = input().strip()

    lcs_len, lcs_str = lcs(s1, s2)
    print(f"Longest common subsequence of {s1} and {s2} is {lcs_str} with length {lcs_len}")
