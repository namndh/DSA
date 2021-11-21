counter = 0

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


def lcm(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = lcm//gcd(lcm, arr[i])*arr[i]
    return lcm

def f(upper, number):
    return upper//number

while True:
    try:
        n, p, q, r = list(map(int, input().split(" ")))
        res = f(n, lcm([p, q])) + f(n, lcm([p, r])) + f(n, lcm([r, q])) - 3*f(n, lcm([p, q, r]))
        print(res)
    except EOFError as e:
        break

