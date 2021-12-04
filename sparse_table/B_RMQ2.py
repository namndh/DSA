import math

m, n = list(map(int, input().split(" ")))

matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().split(" "))))

n_testcases = int(input())
testcases = []
for _ in range(n_testcases):
    testcases.append(list(map(lambda x: int(x) - 1, input().split(" "))))

st = [
        
            [
                [
                    [0 for _ in range(int(math.log2(n))+1)] 
                    for __ in range(n)
                ] for ___ in range(int(math.log2(m)) + 1)
            ] for ___ in range(m)
    ]
for i in range(m):
    for j in range(n):
        st[i][0][j][0] = matrix[i][j]
    h = 1
    while (1<<h) <= n:
        j = 0
        while j + (1<<h) -1 < n:
            st[i][0][j][h] = min(st[i][0][j][h-1], st[i][0][j+(1<<(h-1))][h-1])
            j += 1
        h += 1

k = 1
while (1<<k) <= m:
    i = 0
    while i + (1<<k) - 1 < m:
        h = 0
        while (1<<h) <= n:
            j = 0
            while j + (1<<h) - 1 < n:
                st[i][k][j][h] = min(
                    st[i][k-1][j][h],
                    st[i + (1<<(k-1))][k-1][j][h]
                )
                j += 1
            h += 1
        i += 1
    k += 1

for x1, y1, x2, y2 in testcases:
    kx = int(math.log2(x2-x1+1))
    ky = int(math.log2(y2-y1+1))
    print(min(
        min(st[x1][kx][y1][ky], st[x1][kx][y2-(1<<ky)+1][ky]),
        min(st[x2-(1<<kx)+1][kx][y1][ky], st[x2-(1<<kx)+1][kx][y2-(1<<ky)+1][ky])
    ))
