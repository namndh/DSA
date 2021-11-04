n, m = list(map(int, input().split(" ")))
S1 = [0 for i in range(n+2)]
T1 = [0 for i in range(n+2)]
S2 = [0 for i in range(n+2)]
T2 = [0 for i in range(n+2)]
steps = []
for i in range(m):
    steps.append(list(map(int, input().split(" "))))
 
for l,r,x,y in steps:
    S1[l] += x-l*y
    S1[r+1] -= x-l*y
    S2[l] += y
    S2[r+1] -= y
 
for i in range(1, n+1):
    T1[i] = T1[i-1] + S1[i]
    T2[i] = T2[i-1] + S2[i]
    print(T1[i] + i*T2[i], end=" ")