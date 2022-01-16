from typing import *


n, k = list(map(int, input().split(" ")))
arr = [0, ]
arr.extend(list(map(int, input().split(" "))))
num_queries = int(input())
queries = []
for _ in range(num_queries):
    queries.append(list(map(int, input().split(" "))))

def left_rotate_by_one(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[-1] = temp
    return arr

def rotate_input_array(arr, ids):
    rotate_values = []
    for idx in ids:
        rotate_values.append(arr[idx])
    rotate_values = left_rotate_by_one(rotate_values)
    for i in range(len(ids)):
        arr[ids[i]] = rotate_values[i]
    return arr

class Node:
    def __init__(self, sum_value, l, r, right, left)-> None:
        self.sum_value = sum_value
        self.l = l
        self.r = r
        self.right = right
        self.left = left


class SegmentTree:
    @staticmethod
    def build_no_weight(l:int, r:int, arr: List[int]) -> Node:
        if l == r:
            return Node(arr[l], l, r, None, None)
        mid = (l+r)//2
        left = SegmentTree.build_no_weight(l, mid, arr)
        right = SegmentTree.build_no_weight(mid+1, r, arr)
        return Node(left.sum_value + right.sum_value, l, r, right, left)

    @staticmethod
    def build_with_weight(l: int, r:int, arr:List[int]) -> Node:
        if l == r:
            return Node(arr[l]*l, l, r, None, None)
        mid = (l+r)//2
        left = SegmentTree.build_with_weight(l, mid, arr)
        right = SegmentTree.build_with_weight(mid+1, r, arr)
        return Node(left.sum_value + right.sum_value, l, r, right, left)

    @staticmethod
    def update(p: Node, i: int, v:int):
        if(p.left == p.right):
            p.sum_value = v
            return
        if p.left.l <= i <= p.left.r:
            SegmentTree.update(p.left, i, v)
        else:
            SegmentTree.update(p.right, i, v)
        p.sum_value = p.left.sum_value + p.right.sum_value
    
    @staticmethod
    def get_sum_value(p: Node, i: int, j: int):
        if i > j:
            return 0
        if (i <= p.l) and (p.r <= j):
            return p.sum_value
        total_left = 0
        if (p.left.r >= i):
            total_left += SegmentTree.get_sum_value(p.left, i , j)
        total_right = 0
        if (p.right.l <= j):
            total_right += SegmentTree.get_sum_value(p.right, i, j)
        return total_left+total_right

root1 = SegmentTree.build_no_weight(1, n, arr)
root2 = SegmentTree.build_with_weight(1, n, arr)

for query in queries:
    if query[0] == 2:
        l, r, m = query[1:]
        if l + m - 1 > r - m + 1:
            m = r-l-m+2
        h = l + m - 1
        k = r - m + 1
        res = (
            m*SegmentTree.get_sum_value(root1, h, k) +
            (1-l)*SegmentTree.get_sum_value(root1, l, h-1) +
            SegmentTree.get_sum_value(root2, l, h-1) +
            (r+1)*SegmentTree.get_sum_value(root1, k+1, r)
            - SegmentTree.get_sum_value(root2, k+1, r)
        )
        print(res)
    else:
        rotate_ids = query[1:]
        rotate_pairs = {}
        for i, idx in enumerate(rotate_ids[:len(rotate_ids)-1]):
            rotate_pairs[idx] = rotate_ids[i+1]
        rotate_pairs[rotate_ids[len(rotate_ids)-1]] = rotate_ids[0]
        for k, v in rotate_pairs.items():
            SegmentTree.update(root1, k, arr[v])
            SegmentTree.update(root2, k, k*arr[v])
        arr = rotate_input_array(arr, rotate_ids)
        
            