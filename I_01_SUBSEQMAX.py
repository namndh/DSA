n = int(input())
nums = []
nums = list(map(int, input().split(" ")))
globalSum = nums[0]
curSum = nums[0]
for i in nums[1:]:
    curSum = max(curSum + i, i)
    globalSum = max(globalSum, curSum)
print(globalSum)