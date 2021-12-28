n = int(input())
a = [0]
a.extend(list(map(int, input().split(" "))))

class Node:
    def __init__(self, count_value, l, r, right, left)-> None:
        self.count_value = count_value
        self.l = l
        self.r = r
        self.right = right
        self.left = left


class SegmentTree1:
    @staticmethod
    def build(l:int, r:int) -> Node:
        if l == r:
            return Node(0, l, r, None, None)
        mid = (l+r)//2
        left = SegmentTree1.build(l, mid)
        right = SegmentTree1.build(mid+1, r)
        return Node(left.count_value + right.count_value, l, r, right, left)

    @staticmethod
    def update(p: Node, i: int, v:int):
        if(p.left == p.right):
            p.count_value = v
            return
        if p.left.l <= i <= p.left.r:
            SegmentTree1.update(p.left, i, v)
        else:
            SegmentTree1.update(p.right, i, v)
        p.count_value = p.left.count_value + p.right.count_value
    
    @staticmethod
    def get_count_value(p: Node, i: int, j: int):
        if i > j:
            return 0
        if (i <= p.l) and (p.r <= j):
            return p.count_value
        total_left = 0
        if (p.left.r >= i):
            total_left += SegmentTree1.get_count_value(p.left, i , j)
        total_right = 0
        if (p.right.l <= j):
            total_right += SegmentTree1.get_count_value(p.right, i, j)
        return total_left+total_right


class SegmentTree2:
    @staticmethod
    def update(p: Node, i: int, v:int):
        if p.l == p.r:
            p.count_value += v
            return
        mid = (p.l + p.r) // 2
        if i <= mid:
            if p.left is None:
                p.left = Node(0, p.l, mid, None, None)
            SegmentTree2.update(p.left, i, v)
        else:
            if p.right is None:
                p.right = Node(0, mid+1, p.r, None, None)
            SegmentTree2.update(p.right, i, v)
        if p.left is None:
            p.count_value = p.right.count_value
        elif p.right is None:
            p.count_value = p.left.count_value
        else:
            p.count_value = p.left.count_value + p.right.count_value
    
    @staticmethod
    def get_count_value(p: Node, i: int, j: int):
        if p is None or i > j:
            return 0
        if (i <= p.l) and (p.r <= j):
            return p.count_value
        
        mid = (p.l + p.r) // 2
        res = 0
        if mid >= i:
            res += SegmentTree2.get_count_value(p.left, i, j)
        if mid + 1 <= j:
            res += SegmentTree2.get_count_value(p.right, i, j)
        return res 
    

root1 = SegmentTree1.build(1, n)
root2 = Node(0, 1, 10**9, None, None)
num_map = {}
for i in range(1,n+1):
    if a[i] in num_map:
        prev = num_map[a[i]]
        s = SegmentTree1.get_count_value(root1, prev+1, i-1)
        print(s+1, end=' ')
        SegmentTree1.update(root1, prev, 0)
        SegmentTree1.update(root1, i, 1)
    else:
        s = SegmentTree2.get_count_value(root2, a[i]+1, 10**9)
        print(s + a[i], end=' ')
        SegmentTree2.update(root2, a[i], 1)
        SegmentTree1.update(root1, i, 1)
    num_map[a[i]] = i

