"""
Given an n input, generate all possible binary string
"""
n = int(input())
arr = [None] * n
 
def solution(n, arr, i):
    if i == n:
        print("".join(arr))
        return
    
    arr[i] = "0"
    solution(n, arr, i+1)
    
    arr[i] = "1"
    solution(n, arr, i+1)
 
solution(n, arr, 0)
