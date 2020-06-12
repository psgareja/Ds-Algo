def linear_recursion(S,n):
    if n==0:
        return 0
    else:
        return linear_recursion(S,n-1)_S[n-1]

def reverse(S, start, stop):
”””Reverse elements in implicit slice S[start:stop].”””
if start < stop − 1:
S[start], S[stop−1] = S[stop−1], S[start] reverse(S, start+1, stop−1)
# if at least 2 elements: # swap first and last
# recur on rest