from collections import defaultdict
from typing import Counter
 
n = int(input())
points = []
 
 
def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (((x2-x1)**2 + (y2-y1)**2)**0.5)
 
def is_sub_arr(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i, j = 0, 0
    while (i < n and j < m):
        print(i, j, arr1[i], arr2[j])
        if arr1[i] == arr2[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            i = i - j + 1
            j = 0
    return False
 
for i in range(n):
    point = tuple(map(int, input().split(" ")))
    points.append(point)
 
distances = defaultdict(dict)
for i in range(n):
    for j in range(i+1, n):
        distances[get_distance(points[i], points[j])][points[i]] = 1
        distances[get_distance(points[i], points[j])][points[j]] = 1
res, count = [], 0
for key, val in distances.items():
    point_count = 0
    for point in points:
        if point in val:
            point_count += 1
            if point_count == n:
                count += 1
                res.append(key)
        else:
            break
print(count)
res = sorted(res)
for r in res:
    print(r)