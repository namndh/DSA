from typing import *


n, m, z = map(int, input().split(" "))
queries = []
for _ in range(z):
    queries.append(list(map(int, input().split(" "))))


class Node:
    def __init__(self, max_value, lazy, l, r, right, left)-> None:
        self.max_value = max_value
        self.lazy = lazy
        self.l = l
        self.r = r
        self.right = right
        self.left = left


class SegmentTree:
    @staticmethod
    def build(l:int, r:int) -> Node:
        if l == r:
            return Node(0, 0, l, r, None, None)
        mid = (l+r)//2
        left = SegmentTree.build(l, mid)
        right = SegmentTree.build(mid+1, r)
        return Node(max(left.max_value, right.max_value), 0, l, r, right, left)

    @staticmethod
    def propogate(p: Node):
        p.left.max_value += p.lazy
        p.left.lazy += p.lazy
        p.right.max_value += p.lazy
        p.right.lazy += p.lazy
        p.lazy = 0

    @staticmethod
    def update(p: Node, i: int, j: int, v:int):
        if i <= p.l and p.r <= j:
            p.max_value += v
            p.lazy += v
            return
        SegmentTree.propogate(p)
        if i <= p.left.r:
            SegmentTree.update(p.left, i, j, v)
        if p.right.l <= j:
            SegmentTree.update(p.right, i, j, v)
        p.max_value = max(p.left.max_value,p.right.max_value)
    
    @staticmethod
    def get_max(p: Node, i: int, j: int):
        if (i <= p.l) and (p.r <= j):
            return p.max_value
        max_left = -float("INF")
        SegmentTree.propogate(p)
        if (p.left.r >= i):
            max_left = SegmentTree.get_max(p.left, i , j)
        max_right = -float("INF")
        if (p.right.l <= j):
            max_right = SegmentTree.get_max(p.right, i, j)
        return max(max_left, max_right)


root = SegmentTree.build(1, n)
for u, v, w  in queries:
    current_seats = SegmentTree.get_max(root, u, v-1)
    if current_seats+w > m:
        print("N") 
    else:
        print("T")
        SegmentTree.update(root, u, v-1, w)