n, m = list(map(int, input().split(" ")))
arr = [0]*(n+1)
S = [0]*(n+1)
T = [0]*(n+1)
steps = []
for i in range(m):
    steps.append(list(map(int, input().split(" "))))
 
for l,r,v in steps:
    S[l] += v
    if r+1 <= n:
        S[r+1] -= v
for i in range(1, n+1):
    T[i] = T[i-1] + S[i]
    print(T[i], end=" ")