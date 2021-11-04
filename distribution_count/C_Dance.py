n = int(input())
dancers = input()
 
psa, psb = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
 
for i in range(1,n+1):
    if dancers[i-1] == 'a':
        psa[i] = psa[i-1] + 1
        psb[i] = psb[i-1]
    elif dancers[i-1] == 'b':
        psb[i] = psb[i-1] + 1
        psa[i] = psa[i-1]
 
counting = [0 for _ in range(2*n+1)]
counting[n] = 1
res = 0
for i in range(1, n+1):
    idx = n + (psa[i] - psb[i])
    res += counting[idx]    
    counting[idx] += 1
print(res)