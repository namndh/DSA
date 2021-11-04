n, m = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))
arr = [[num, idx] for idx, num in enumerate(nums)]
arr = sorted(arr, key=lambda x: x[0])
max_prod = -float("INF")
i = 0
j = n - 1
pairs = []
if n < 2:
    print(0)
    exit(0)
 
while i < j:
    if arr[i][0]*arr[j][0] <= m:
        if max_prod <= arr[i][0]*arr[j][0]:
            max_prod = arr[i][0] * arr[j][0]
            pairs = [str(arr[i][1]+1), str(arr[j][1]+1)]
        i += 1
    elif  arr[i][0]*arr[j][0] > m:
        j -= 1
max_prod = max(max_prod, 0)
print(max_prod)
print(" ".join(pairs))