n, l = list(map(int, input().split(" ")))
points = list(map(int, input().split(" ")))
points = sorted(points)

def check(mid_l):
    segment_count = 0
    f = 0
    for i in range(n):
        f += mid_l
        if f >= points[i]:
            if i < n - 1:
                f = min(f, points[i+1])
            segment_count += 1
    return segment_count == n and f >= l

low = 0 
high = l

for i in range(60):
    mid = (high+low) / 2
    if check(mid):
        high = mid
    else:
        low = mid
print(high)
