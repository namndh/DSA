n, m = list(map(int, input().split(" "))) 
s_matrix = [[0 for _ in range(n+2)] for _ in range(n+2)]
steps = []
for i in range(m):
    steps.append(list(map(int, input().split(" "))))
for step in steps:
    x1, y1, x2, y2, v = step
    s_matrix[x1][y1] += v
    s_matrix[x1][y2+1] -= v
    s_matrix[x2+1][y1] -= v
    s_matrix[x2+1][y2+1] += v
 
psa_matrix = [[0 for _ in range(n+2)] for _ in range(n+2)]
for i in range(1, n+1) :
    for j in range(1, n+1) :
        psa_matrix[i][j] = (
            psa_matrix[i - 1][j] + psa_matrix[i][j - 1] - psa_matrix[i - 1][j - 1] + s_matrix[i][j]
        )
        if j == n:
            print(psa_matrix[i][j], end="\n")
        else:
            print(psa_matrix[i][j], end=" ")