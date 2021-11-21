import collections

test_cases = int(input())

# calculate sieves
sieves = [0 for _ in range(100001)]
for i in range(2, 100001):
    if sieves[i] == 0:
        for j in range(i, 100001, i):
            sieves[j] = i


def decompose(num, count_prime, sieves):
    t = num
    while t > 1:
        count_prime[sieves[t]] += 1
        t //= sieves[t]
    return count_prime

M = 1000000007
for _ in range(test_cases):
    n, k = list(map(int, input().split()))
    # calculate number of exp of prime
    count_prime_A = [0 for _ in range(n+1)]
    for i in range(n-k+1, n+1):
        count_prime_A = decompose(i, count_prime_A, sieves)
    count_prime_B = [0 for _ in range(n+1)]
    for i in range(1, k+1):
        count_prime_B = decompose(i, count_prime_B, sieves)
    count_prime_all = collections.defaultdict(int)
    for i in range(n+1):
        if count_prime_A[i] != 0:
            count_prime_all[i] += count_prime_A[i]
        if count_prime_B[i] != 0:
            count_prime_all[i] -= count_prime_B[i]
    res = 1
    for prime, exp in count_prime_all.items():
        for i in range(exp):
            res = res*prime % M
    print(res)

