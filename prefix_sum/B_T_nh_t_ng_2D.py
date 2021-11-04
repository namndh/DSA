n = int(input())
matrix = [[0]*(n+1)]
for i in range(n):
    row = list(map(int, input().split(" ")))
    row.insert(0, 0)
    matrix.append(row)
 
psa = [[0 for x in range(n+1)]
          for y in range(n+1)]
 
for i in range(1, n+1) :
    for j in range(1, n+1) :
        psa[i][j] = (psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + matrix[i][j])
 
m = int(input())
rcs = []
for i in range(m):
    rcs.append(list(map(int, input().split(" "))))
 
for r1, c1, r2, c2 in rcs:
    print(psa[r2][c2] - psa[r1-1][c2] - psa[r2][c1-1] + psa[r1-1][c1-1])