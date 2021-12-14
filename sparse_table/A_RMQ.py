import math


n = int(input())
a = list(map(int, input().split(" ")))
m = int(input())
pairs = []
for _ in range(m):
    pairs.append(list(map(int, input().split(" "))))

st = [[0 for _ in range(int(math.log2(n)) + 1)] for __ in range(n)]

for i in range(n):
    st[i][0] = a[i]

j = 1
while (1<<j) <= n:
    i = 0
    while i + (1<<j) - 1 < n:
        st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        i += 1
    j += 1

res = 0
for l, r in pairs:
    k = math.floor(math.log2(r-l+1))
    res += min(st[l][k], st[r - (1 << k) + 1][k])

