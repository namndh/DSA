n = int(input())
arr = list(map(int, input().split(" ")))
m = int(input())
lrs = []
for i in range(m):
    lrs.append(list(map(int, input().split(" "))))
 
prefix_sum = [0]*n
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = arr[i] + prefix_sum[i-1]
for l, r in lrs:
    if l-2 < 0:
        print(prefix_sum[r-1])
    else:
        print(prefix_sum[r-1] - prefix_sum[l-2])