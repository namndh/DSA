from math import factorial
from collections import defaultdict
from fractions import Fraction

n = int(input())
# decompose number from 1 -> n
# in each decompose result P: 
# - find a number V that is multiplication of primes in P with exponential = 1
# - if V exist, increase value of count V
# Final result = sigma(3CcountV) 1 <= V <= N and countV >= 3

#build sieves
sieves = [0 for _ in range(2*(10**5)+1)]
for i in range(2, 2*(10**5)+1):
    if sieves[i] == 0:
        for j in range(i, 2*(10**5)+1, i):
            sieves[j] = i


def decompose(num, count_prime, sieves):
    t = num
    while t > 1:
        count_prime[sieves[t]] += 1
        t //= sieves[t]
    return count_prime

count_res = defaultdict(int)
for num in range(1, n+1):
    count_prime = defaultdict(int)
    decompose(num, count_prime, sieves)
    legit_number = 1
    for prime, exp in count_prime.items():
        if exp % 2 != 0:
            legit_number *= prime
    count_res[legit_number] += 1


def choose(n,k):
    if k > n//2: k = n - k
    p = Fraction(1)
    for i in range(1,k+1):
        p *= Fraction(n - i + 1, i)
    return int(p)

res = 0
for val, count in count_res.items():
    if count >= 3:
        res += choose(count, 3)

print("%d" % res)