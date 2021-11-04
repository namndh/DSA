n, m = list(map(int, input().split(" ")))
heights = list(map(int, input().split(" ")))

max_height = max(heights)

high = max_height+1
low = 0

def get_wood(h):
    total_wood = 0
    for height in heights:
        if height > h:
            total_wood += height - h
    return total_wood
        

while high - low > 1:
    mid = (high+low) // 2
    if get_wood(mid) < m:
        high = mid
    else:
        low = mid
print(low)

    