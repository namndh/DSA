r, c, h, w = list(map(int, input().split(" ")))
A = [[0 for _ in range(c+1)] for __ in range(r+1)]
for i in range(1, r+1):
    row = list(map(int, input().split(" ")))
    A[i][1:] = row

def check(median):
    B = [[0 for _ in range(c+1)] for __ in range(r+1)]
    for i in range(1, r+1):
        for j in range(1, c+1):
            if A[i][j] < median:
                B[i][j] = 1
            else:
                B[i][j] = 0
            B[i][j] = (B[i - 1][j] + B[i][j - 1] - B[i - 1][j - 1] + B[i][j])
    for i in range(1, r+1-h):
        for j in range(1, c+1-w):
            total_num_lt_median = B[i+h-1][j+w-1] - B[i-1][j+w-1] - B[i+h-1][j-1] + B[i-1][j-1]
            if total_num_lt_median < median and total_num_lt_median >= (h*w+1)/2:
                return True
    return False


low  = float("INF")
high = -float("INF")
for row in A[1:]:
    low = min(low, min(row[1:]))
    high = max(high, max(row[1:]))

while high - low > 1:
    mid = (high + low) // 2
    if check(mid):
        high = mid
    else:
        low = mid

print(high)
