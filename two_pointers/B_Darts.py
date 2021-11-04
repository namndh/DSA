n, m = list(map(int, input().split(" ")))
nums = []
for i in range(n):
    nums.append(int(input()))
pair_sums = nums[:]
for i in range(n):
    for j in range(i, n):
        pair_sums.append(nums[i] + nums[j])
 
pair_sums = sorted(pair_sums)
N = len(pair_sums)
i = 0
j = N - 1
max_sum = 0
while i < N and j > 0:
    if pair_sums[i] + pair_sums[j] <= m:
        max_sum = max(max_sum, pair_sums[i] + pair_sums[j])
        i += 1
    else:
        if pair_sums[j] <= m:
            max_sum = max(max_sum, pair_sums[j])
        elif pair_sums[i] <= m:
            max_sum = max(max_sum, pair_sums[i])
        j -= 1
print(max_sum)