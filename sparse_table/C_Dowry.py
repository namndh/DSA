import math


def get_bit(number, index):
    return (number >> index) & 1

def get_i(jews, lower_bound):
    l = -1
    r = len(jews)
    while r - l > 1:
        mid = (l+r)//2
        if jews[mid][0] >= lower_bound:
            r = mid
        else:
            l = mid
    return r

def get_j(jews, upper_bound):
    l = -1
    r = len(jews)
    while r - l > 1:
        mid = (r+l)//2
        if jews[mid][0] <= upper_bound:
            l = mid
        else:
            r = mid
    return l

def get_max_in_range(st, i, j):
    k = math.floor(math.log2(j-i+1))
    return max(st[i][k], st[j-(1<<k)+1][k])


def get_sum_value(jews):
    sum_val_map = []
    for number in range(0, 1 << len(jews)):
        sum_value = 0 
        sum_weight = 0
        for i in range(len(jews)):
            bit_at_index = get_bit(number, i)
            sum_value += bit_at_index*jews[i][1]
            sum_weight += bit_at_index*jews[i][0]
        sum_val_map.append([sum_weight, sum_value])
    return sum_val_map


n, l, r = list(map(int, input().split(" ")))
jew = []
for _ in range(n):
    jew.append(list(map(int, input().split(" "))))



jew1 = jew[:n//2]
jew2 = jew[n//2:]

sum_val_map_1 = get_sum_value(jew1)
sum_val_map_2 = get_sum_value(jew2)

sum_val_map_2 = sorted(sum_val_map_2, key=lambda x: x[0])


st = [[0 for _ in range(int(math.log2(len(sum_val_map_2))) + 1)] for __ in range(len(sum_val_map_2))]
for i in range(len(sum_val_map_2)):
    st[i][0] = sum_val_map_2[i][1]

j = 1
while (1<<j) <= len(sum_val_map_2):
    i = 0 
    while i + (1<<j) - 1 < len(sum_val_map_2):
        st[i][j] = max(st[i][j-1], st[i + (1 << (j-1))][j-1])
        i += 1
    j += 1

v_max = 0
for w, v in sum_val_map_1:
    s2_i = get_i(sum_val_map_2, l - w)
    s2_j = get_j(sum_val_map_2, r - w)
    if s2_i <= s2_j:
        v_max_2 = get_max_in_range(st, s2_i, s2_j)
        v_max = max(v_max, v + v_max_2)
    else:
        continue

print(v_max)
