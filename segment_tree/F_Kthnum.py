from typing import *


n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
queries = []
for _ in range(m):
    queries.append(list(map(int, input().split(" "))))

class Node:
    def __init__(self, sorted_array, l, r, right, left)-> None:
        self.sorted_array = sorted_array
        self.l = l
        self.r = r
        self.right = right
        self.left = left


class SegmentTree:
    @staticmethod
    def build(l:int, r:int, arr: List[int]) -> Node:
        if l == r:
            return Node([arr[l], ], l, r, None, None)
        mid = (l+r)//2
        left = SegmentTree.build(l, mid, arr)
        right = SegmentTree.build(mid+1, r, arr)

        return Node(sorted(left.sorted_array + right.sorted_array), l, r, right, left)
    

    @staticmethod
    def bs(arr: List[int], target: int):
        l = -1
        r = len(arr)
        while r - l > 1:
            mid = (r+l)//2
            if arr[mid] > target:
                r = mid
            else:
                l = mid
        return r

    @staticmethod
    def get_count_value(p: Node, i: int, j: int, target: int):
        if (i <= p.l) and (p.r <= j):
            return SegmentTree.bs(p.sorted_array, target)
        total_left = 0
        if (p.left.r >= i):
            total_left += SegmentTree.get_count_value(p.left, i , j, target)
        total_right = 0
        if (p.right.l <= j):
            total_right += SegmentTree.get_count_value(p.right, i, j, target)
        return total_left+total_right


root = SegmentTree.build(0, n-1, a)

for i, j, k in queries:
    l = -10**9 - 1
    r = 10**9
    while r - l > 1:
        mid = l + (r-l)//2
        if SegmentTree.get_count_value(root, i-1, j-1, mid) < k:
            l = mid
        else:
            r = mid
    print(r)

# print(SegmentTree.bs([1,2,3,4,5], 4))