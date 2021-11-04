n, m = list(map(int, input().split(" ")))
input_segments = []
l_points = []
r_points = []
for i in range(n):
    segment = list(map(int, input().split(" ")))
    if segment[0] > segment[1]:
        segment[0], segment[1] = segment[1], segment[0]
    l_points.append(segment[0])
    r_points.append(segment[1])
 
points = list(map(int, input().split(" ")))
 
l_points = sorted(l_points)
r_points = sorted(r_points)
 
def binary_search(points, low, high, point):
    while low + 1 < high:
        mid = (high+low) // 2
        if points[mid] > point:
            high = mid
        else:
            low = mid
    return high
 
for point in points:
    s_l = binary_search(l_points, -1, len(l_points), point)
    s_r = binary_search(r_points, -1, len(r_points), point-1)
    print(s_l - s_r, end=" ")