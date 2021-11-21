n = int(input())

def build_sieve_eratos(n):
    prime = [1 for i in range(n+1)]
    for i in range(2, n+1):
        if prime[i] == 1:
            for j in range(2*i, n+1, i):
                prime[j] = 0
    return prime

prime = build_sieve_eratos(2*n)
print(sum(prime[n+1:2*n]))