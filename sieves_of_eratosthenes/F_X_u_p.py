def bs(one_idx, zeros_before_one, no_zeros, previous_pos):
    left = previous_pos
    right = len(one_idx)-1
    if right <= left:
        return
    while right - left > 1:
        mid = (left+right)//2
        if zeros_before_one[mid] < no_zeros:
            left = mid
        else:
            right = mid
    if zeros_before_one[right] < no_zeros:
        return 
    return one_idx[right], right
    
n = int(input())
bits = list(map(int, input()))
mask_zeros = [0 for _ in range(n+1)]
for i in range(n):
    if bits[i] == 0:
        mask_zeros[i+1] = 1
psa_one = [0 for _ in range(n+1)]
p = [0]
f = [0]
res = 0
for i in range(1, n+1):
    if bits[i-1] == 1:
        p.append(i)
        psa_one[i] = mask_zeros[i-1]
        f.append(psa_one[i])
    mask_zeros[i] += mask_zeros[i-1]
res = 0
for x in range(0, n//2+1):
    cur_pos = 0
    count = 0
    bs_res = bs(p, f, f[cur_pos] + x, cur_pos)
    while bs_res is not None:
        string_idx, cur_pos = bs_res
        count += 1
        if mask_zeros[n] - psa_one[string_idx] < x:
            count -= 1
        bs_res = bs(p, f, f[cur_pos] + x, cur_pos)
    if count > 0:
        res = max(res, (x+1)*count+x)
print(res)