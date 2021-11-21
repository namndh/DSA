n, k = list(map(int, input().split(" ")))

def get_prime_factors(number):
    i = 2 
    factors = [] 
    
    while i <= number**0.5: 
        if number % i == 0: 
            number //= i 
            if i not in factors: 
                factors.append(i) 
        else: 
            i += 1
    if number not in factors:
        factors.append(number) 
    return factors

factors = get_prime_factors(k)
factors_v = list()

for factor in factors:
    k_factor = k // factor
    counter = 1
    while k_factor % factor == 0:
        k_factor //= factor
        counter += 1
    factors_v.append((factor, counter))



def get_number_in_range_has_divisor(upper, divisor):
    return upper // divisor

res = float("INF")
for factor, v in factors_v:
    i = 1
    counter = 0
    while factor ** i <= n:
        counter += get_number_in_range_has_divisor(n, factor**i)
        i += 1

    res = min(res, counter//v)

print(res)