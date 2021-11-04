brackets = input()
num_brackets = [1 if b  == "(" else -1 for b in brackets]
n = len(num_brackets)
psa = [n for _ in range(len(num_brackets)+ 1)]
for i in range(1, len(num_brackets)+1):
    psa[i] = psa[i-1] + num_brackets[i-1]
counting = [0 for _ in range(2*n+1)]
res = 0
for i in range(0, n+1):
    if psa[i] < psa[i-1]:
        counting[psa[i-1]] = 0
    res += counting[psa[i]]
    counting[psa[i]] += 1
 
print(res)