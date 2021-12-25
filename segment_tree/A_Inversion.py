from typing import Any, List


class Node:
    def __init__(self, count_value, l, r, right, left)-> None:
        self.count_value = count_value
        self.l = l
        self.r = r
        self.right = right
        self.left = left


class SegmentTree:
    @staticmethod
    def build(l:int, r:int) -> Node:
        if l == r:
            return Node(0, l, r, None, None)
        mid = (l+r)//2
        left = SegmentTree.build(l, mid)
        right = SegmentTree.build(mid+1, r)
        return Node(left.count_value + right.count_value, l, r, right, left)

    @staticmethod
    def update(p: Node, i: int, v=1):
        if(p.left == p.right):
            p.count_value = v
            return
        if p.left.l <= i <= p.left.r:
            SegmentTree.update(p.left, i, v)
        else:
            SegmentTree.update(p.right, i, v)
        p.count_value = p.left.count_value + p.right.count_value
    
    @staticmethod
    def get_count_value(p: Node, i: int, j: int):
        if (i <= p.l) and (p.r <= j):
            return p.count_value
        total_left = 0
        if (p.left.r >= i):
            total_left += SegmentTree.get_count_value(p.left, i , j)
        total_right = 0
        if (p.right.l <= j):
            total_right += SegmentTree.get_count_value(p.right, i, j)
        return total_left+total_right

n = int(input())
input_array = list(map(int, input().split(" ")))
arr = list(range(0, n+1))
root = SegmentTree.build(1, n)

res = 0
for num in input_array:
    if num < n:
        res += SegmentTree.get_count_value(root, num+1, n)
    else:
        res += SegmentTree.get_count_value(root, n, n)
    SegmentTree.update(root, num)

print(res)