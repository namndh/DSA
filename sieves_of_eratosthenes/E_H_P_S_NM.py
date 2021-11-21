n = int(input())
m = int(input())

sieves = [0 for _ in range(10**m+1)]
primes = []
for i in range(2, 10**m+1):
    if sieves[i] == 0:
        for j in range(2*i, 10**m+1, i):
            sieves[j] = 1
        if i > 10**(m-1):
            primes.append(i)
res = 0

def f(n, k):
    return n//k

for prime in primes:
    s = prime % 10
    res += f((s+1)*(10**(n-m-1))-1, prime) - f(s*(10**(n-m-1))-1, prime)  

print(res)