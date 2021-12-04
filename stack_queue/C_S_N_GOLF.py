m, n = list(map(int, input().split(" ")))
matrix = [[] for _ in range(m)]

def cal_square(heights):
    recs = [-1]
    recs.extend(heights)
    l = [-1 for _ in range(n+1)]
    r = [-1 for _ in range(n+1)]
    stack_left, stack_right = [(-1, 0)], [(-1, n+1)]
    for i in range(1, n+1):
        while stack_left[-1][0] >= recs[i]:
            stack_left.pop()
        l[i] = stack_left[-1][1] + 1
        stack_left.append((recs[i], i))

    for i in range(n, 0, -1):
        while stack_right[-1][0] >= recs[i]:
            stack_right.pop()
        r[i] = stack_right[-1][1] - 1
        stack_right.append((recs[i], i))
    res = 0
    for i in range(n+1):
        res = max(res, (recs[i]+1)*(r[i] - l[i] + 2))
    return res


for i in range(m):
    matrix[i] = list(map(int, input().split(" ")))
incremental_check_matrix = [[0 for _ in range(n)] for __ in range(m)]
for i in range(1, m):
    for j in range(1, n):
        print('i, j', i, j)
        print('matrix value', matrix[i][j], matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
        incremental_check_matrix[i][j] = int(
            matrix[i][j] >= matrix[i-1][j]
            and matrix[i][j] >= matrix[i][j-1]
            and matrix[i-1][j-1] <= matrix[i-1][j]
            and matrix[i-1][j-1] <= matrix[i][j-1]
        )
        print('check value', incremental_check_matrix[i][j])
for row in incremental_check_matrix:
    print(row)
res = 0
for i in range(1, m):
    h = [0 for _ in range(n)]
    for j in range(1, n):
        if incremental_check_matrix[i][j] == 1:
            h[j] += 1
        elif incremental_check_matrix[i][j] == 0:
            h[j] = 0
    res = max(res, cal_square(h))
print(res)
