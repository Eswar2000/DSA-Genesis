"""
Problem Statement:
Given a number n, provide all possible valid parantheses of this degree.
"""

def generate_valid_parantheses(n, open, close, par_str, valid_parantheses):
    if(open == n and close == n):
        valid_parantheses.append(par_str[:])
        return
    
    if(open < n):
        generate_valid_parantheses(n, open+1, close, par_str+'(', valid_parantheses)

    if(close < open):
        generate_valid_parantheses(n, open, close+1, par_str+')', valid_parantheses)


if __name__ == '__main__':
    print("Enter the number of open and close parantheses")
    n = int(input())

    if(n <= 0):
        print("No need to generate parantheses")
    else:
        valid_parantheses_list = []
        generate_valid_parantheses(n, 0, 0, "", valid_parantheses_list)
        print(f"Valid parantheses list of degree {n} are {valid_parantheses_list}")