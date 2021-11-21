n = int(input())
if n == 1:
    print(0)
    exit(0)


def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(set(factors))

def get_bit(number, v):
    return (number >> v) & 1 == 1


prime_factors = get_prime_factors(n)
k = len(prime_factors)

def get_number_in_range_has_divisor(upper, divisor):
    return upper // divisor

res = 0
for mask in range(1, 2**k):
    lcm = 1
    counter = 0
    for i in range(0, k):
        if get_bit(mask, i):
            lcm *= prime_factors[i]
            counter += 1
    if counter % 2 == 0:
        res -= get_number_in_range_has_divisor(n, lcm)
    else:
        res += get_number_in_range_has_divisor(n, lcm)
print(n - res)
    
