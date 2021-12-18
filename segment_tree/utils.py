from typing import Any, List


class Node:
    def __init__(self, max_value, l, r, right, left)-> None:
        self.max_value = max_value
        self.l = l
        self.r = r
        self.right = right
        self.left = left


class SegmentTree:
    @staticmethod
    def build(l:int, r:int, a: List[Any]) -> Node:
        if l == r:
            return Node(a[r], l, r, None, None)
        mid = (l+r)//2
        left = SegmentTree.build(l, mid, a)
        right = SegmentTree.build(mid+1, r, a)
        return Node(max(left.max_value, right.max_value), l, r, right, left)
    
    @staticmethod
    def update(p: Node, i: int, v: Any):
        if(p.left == p.right):
            p.max_value = v
            return
        if p.left.l <= i <= p.left.r:
            SegmentTree.update(p.left, i, v)
        else:
            SegmentTree.update(p.right, i, v)
        p.max_value= max(p.left.max_value, p.right.max_value)
    
    @staticmethod
    def get_max(p: Node, i: int, j: int):
        if (i <= p.l) and (p.r <= j):
            return p.max_value
        max_left = -float("INF")
        if (p.left.r >= i):
            max_left = SegmentTree.get_max(p.left, i , j)
        max_right = -float("INF")
        if (p.right.l <= j):
            max_right = SegmentTree.get_max(p.right, i, j)
        return max(max_left, max_right)