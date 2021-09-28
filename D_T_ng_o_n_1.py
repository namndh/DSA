n, m = list(map(int, input().split(" ")))
arr = [0]*(n+1)
steps = []
for i in range(m):
    steps.append(list(map(int, input().split(" "))))

for l,r,v in steps:
    for i in range(l, r+1):
        arr[i] += v

for num in arr[1:]:
    print(num, end=" ")

