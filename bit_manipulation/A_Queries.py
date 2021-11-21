q, s, a, b = list(map(int, input().split(" ")))
print()
marked_array = [0 for i in range(2**26)]

def is_in(u, v):
    global marked_array
    return (marked_array[u] >> v) & 1 == 1

def switch_bit(u, v):
    global marked_array
    marked_array[u] ^= (1 << v)

sum = 0

def calculate(s):
    global sum
    if s & 1 == 1:
        p = s >> 1
        u = p >> 5
        v = p & 31
        if not is_in(u, v):
            sum += p
            switch_bit(u, v)
    else:
        p = s >> 1
        u = p >> 5
        v = p & 31
        if is_in(u, v):
            sum -= p
            switch_bit(u, v)
    

calculate(s)
for i in range(1,q):
    s = (a*s+b) % 2**32
    calculate(s)

print(sum)