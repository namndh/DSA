inputs = list(map(int, input().split(" ")))
L, M, N = inputs[:3]
values_iter = iter(inputs[3:])
rec_prism = [[[0 for _ in range(L+1)] for __ in range(M+1)] for ___ in range(N+1)]
 
for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, L+1):
            rec_prism[i][j][k] = next(values_iter)
            rec_prism[i][j][k] += (rec_prism[i][j][k-1] - rec_prism[i][j-1][k-1] + rec_prism[i][j-1][k] - rec_prism[i-1][j][k-1] + 
                rec_prism[i-1][j][k] - rec_prism[i-1][j-1][k] + rec_prism[i-1][j-1][k-1])
while True:
    try:
        xyz = list(map(int, input().split(" ")))
        if len(xyz) != 6:
            break
        x1,y1,z1,x2,y2,z2 = xyz
        print(rec_prism[z2][y2][x2] - rec_prism[z2][y2][x1] - rec_prism[z2][y1][x2] + rec_prism[z2][y1][x1] -
                    rec_prism[z1][y2][x2] + rec_prism[z1][y2][x1] - rec_prism[z1][y1][x1] + rec_prism[z1][y1][x2])
    except:
        break