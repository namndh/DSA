num_testcases = int(input())
def check(n, stalls, space, cows):
    counter = 1
    cur_stall = stalls[0]
    for i in range(1, n):
        if stalls[i] - cur_stall >= space:
            counter += 1
            cur_stall = stalls[i]
    return counter >= cows

for _ in range(num_testcases):
    n, c = list(map(int, input().split(" ")))
    stalls = []
    for i in range(n):
        stalls.append(int(input()))
    stalls = sorted(stalls)
    low = 0
    high = stalls[n-1]
    min_space = 0
    while high - low > 1:
        mid = (high + low)//2
        if check(n, stalls, mid, c):
            min_space = max(min_space, mid)
            low = mid
        else: 
            high = mid
    print(min_space)
