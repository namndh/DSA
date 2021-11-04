n = int(input())
rows = []
for i in range(n):
    rows.append(list(input()))
m = len(rows[0])
matrix = [[0 for _ in range(m+1)] for __ in range(n+1)]
for i in range(n):
    matrix[i+1][1:] = rows[i]
psm = [[[0 for _ in range(m+1)] for __ in range(n+1)] for ___ in range(5)]
for i in range(1,n+1):
    for j in range(1,m+1):
        psm[ord(matrix[i][j])-65][i][j] = 1
for c in range(5):
    for i in range(1, n+1):
        for j in range(1, m+1):
            psm[c][i][j] += (
                psm[c][i-1][j] +
                psm[c][i][j-1] -
                psm[c][i-1][j-1]
            )
 
def calculate_diff_chars(psm, i1, j1, i2, j2):
    sum_chars = 0
    for c in range(5):
        s = psm[c][i2][j2] - psm[c][i1-1][j2] - psm[c][i2][j1-1] + psm[c][i1-1][j1-1]
        if s > 0:
            sum_chars += 1
    return sum_chars
 
res = 0
for i1 in range(1,n+1):
    for i2 in range(i1, n+1):
        l, r = 0, 0
        for j1 in range(1, m+1):
            while l < m and calculate_diff_chars(psm, i1, j1, i2, l+1) < 3:
                l += 1
            while r < m and calculate_diff_chars(psm, i1, j1, i2, r+1) <= 3:
                r += 1
            res += r - l
print(res)