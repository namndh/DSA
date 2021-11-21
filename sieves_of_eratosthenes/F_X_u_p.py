
def bs(one_idx, zeros_before_one, no_zeros, previous_pos):
    left = previous_pos
    right = len(one_idx)
    mid = (left+right)//2
    while right - left > 1:
        if zeros_before_one[mid] < no_zeros:
            left += 1
        else:
            right -= 1
    return one_idx[right], right
    



n = int(input())
bits = list(map(int, input()))
mask_zeros = [0 for _ in range(n+1)]
for i in range(n):
    if bits[i] == 0:
        mask_zeros[i+1] = 1
print(mask_zeros)
psa_one = [0 for _ in range(n+1)]
p = [0]
f = [0]

for i in range(1, n+1):
    if bits[i-1] == 1:
        p.append(i)
        psa_one[i] = mask_zeros[i-1]
        f.append(psa_one[i])
    mask_zeros[i] += mask_zeros[i-1]
print(p)
print(f)
print(psa_one)

string_idx, cur_one = bs(p, f, 1, 0)
print(bs(p,f, f[cur_one]+1, cur_one))
# print(bs(p, f, 1, 2))


