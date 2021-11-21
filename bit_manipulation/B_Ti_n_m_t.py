n, k = list(map(int, input().split(" ")))
notes = list(map(int, input().split(" ")))
res = -1


def get_bit(number, index):
    return (number >> index) & 1

notes_1 = notes[0:n//2]
notes_2 = notes[n//2:]

def search_set_bits_notes_2(notes2_sum, value):
    low = 0
    high = len(notes2_sum)
    while high - low > 1:
        mid = (high+low)//2
        if notes2_sum[mid][0] <= value:
            low = mid
        else:
            high = mid
    if notes2_sum[low][0] == value:
        return notes2_sum[low][1]
    else:
        return -1

notes_2_sums = []

for number in range(0, 1 << len(notes_2)):
    notes_sum = 0
    counter = 0
    for i in range(len(notes_2)):
        bit_at_index = get_bit(number, i)
        notes_sum += bit_at_index*notes_2[i]
        if bit_at_index == 1:
            counter += 1
    notes_2_sums.append((notes_sum, counter))

notes_2_sums = sorted(notes_2_sums)
for number in range(0, 1 << len(notes_1)):
    notes_sum = 0
    counter = 0
    for i in range(len(notes_1)):
        notes_sum += get_bit(number, i)*notes_1[i]  
        if get_bit(number, i) == 1:
            counter += 1
    num_notes_in_2 = search_set_bits_notes_2(notes_2_sums, k - notes_sum)
    if num_notes_in_2 == -1:
        continue
    else:
        res = max(res, counter+search_set_bits_notes_2(notes_2_sums, k - notes_sum))

print(res)