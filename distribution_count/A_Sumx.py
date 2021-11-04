n = int(input())
num_inputs = list(map(int, input().split(" ")))
target = int(input())
counting = [0] * 10 ** 6
result = 0
for num in num_inputs:
    pair_number = target - num
    result += counting[pair_number]
    counting[num] += 1
 
print(result)