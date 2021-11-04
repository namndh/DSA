n, k = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))
max_num = max(nums)
min_num = min(nums)
def check(avg):
    b = [0]
    b.extend([num - avg for num in nums])
    psa_b = [0 for _ in range(len(b))]
    p_min_b = [0 for _ in range(len(b))]

    for i in range(len(b)):
        psa_b[i] = psa_b[i-1] + b[i]
        p_min_b[i] = min(p_min_b[i-1], psa_b[i])
    for i in range(k, len(b)):
        if psa_b[i] - p_min_b[i-k] >= 0:
            return True
    return False
low = min_num
high = max_num

for i in range(60):
    avg = (high + low) / 2
    if check(avg):
        low = avg
    else:
        high = avg

print("%.3f" % low)
