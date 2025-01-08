"""
Problem Statement:
Given a string and list of dictionary words, see if the string can be partitioned in a way where both strings are found in the dictionary.
"""


def word_break(s, dict):
    # If given word is empty, it can still be broken, so it is valid
    if not s:
        return True
    
    # DP[i] represents if the word can be broken in index i -> so 0....i and i....n must be present in dictionary
    n = len(s)
    dp = [False for _ in range(n + 1)]

    # Base Case 1: word of length 0 (or empty) can be broken, so it is valid
    dp[0] = True

    # For every other index i in string, if there is an index j such that 0....j is present (dp[j]==True) and j....i is in dictionary, then dp[i] is True
    for i in range(1, n + 1):
        for j in range(i):
            if(dp[j] and s[j:i] in dict):
                dp[i] = True
                break
    return dp[n]

if __name__ == '__main__':
    print("Enter the string")
    s = input().strip()

    print("Enter the dictionary words as spaced separated entries")
    words = input().split(' ')

    check_word_break = word_break(s, words)
    if(check_word_break):
        print("Yes, the word can be broken into smaller words")
    else:
        print("No, the words can't be broken into dictionary words")