a, b = list(map(int, input().split(" ")))
x = [0 for _ in range(64)]
m = 10**9 + 7
x[0] = a**(2**0) % m
for i in range(1, 64):
    x[i] = x[i-1]**2 % m

def get_bit(index):
    global b
    return (b >> index) & 1

res = 1
for i in range(64):
    if get_bit(i) == 1:
        res *= x[i]

print(res%m)
