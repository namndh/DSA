n, k = list(map(int, input().split(" ")))
input_nums = list(map(int, input().split(" ")))
result = 0
counting = [0] * 10 ** 6
 
def two_sums(target, nums, counting):
    result = 0
    for num in nums:
        pair_number = target - num
        result += counting[pair_number]
        counting[num] += 1
    for num in nums:
        counting[num] = 0
    
    return result, counting
    
for i in range(n):
    target = k - input_nums[i]
    two_sum_pairs, counting = two_sums(target, input_nums[:i], counting)
    result += two_sum_pairs
    
print(result)
