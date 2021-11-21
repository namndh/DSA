l = int(input())
d = int(input())
divisor_88 = []
sum_map = [0 for i in range(l)]
for i in range(1, l):
    for j in range(2*i, l, i):
        sum_map[j] += i
        
res = 0
for i in range(1, l):
    if abs(i - sum_map[i]) <= d:
        res += 1
print(res)
        