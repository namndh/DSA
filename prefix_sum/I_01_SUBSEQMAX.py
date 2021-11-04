n = int(input())
nums = []
nums = list(map(int, input().split(" ")))
min_odd_prefix_sum = float("INF")
min_even_prefix_sum = float("INF")
 
res = -float('INF')
 
prefix_sum = [0 for _ in range(n+1)]
 
for i in range(1, n+1):
    prefix_sum[i] = nums[i-1] + prefix_sum[i-1]
    if prefix_sum[i-1] % 2 == 0:
        min_even_prefix_sum = min(min_even_prefix_sum, prefix_sum[i-1])
    else:
        min_odd_prefix_sum = min(min_odd_prefix_sum, prefix_sum[i-1])
    if prefix_sum[i] % 2 == 0:
        res = max(res, prefix_sum[i] - min_even_prefix_sum)
    else:
        res = max(res, prefix_sum[i] - min_odd_prefix_sum)
        
print(res)