from math import log2, floor
import sys
from collections import defaultdict


sys.setrecursionlimit(10**6)

def get_bit(number, pos):
    return (number >> pos) & 1

while True:
    n = int(input())
    if n == 0:
        break
    c = defaultdict(list)
    p = [0 for _ in range(n)]
    for i in range(1, n):
        parent, d_to_p = map(int, input().split(" "))
        c[parent].append((i, d_to_p))
        p[i] = parent
    d = [0 for _ in range(n)]
    len_to_root = [0 for _ in range(n)]

    def get_depth(r):
        for child, d_to_p in c[r]:
            d[child] = d[r] + 1
            len_to_root[child] = len_to_root[r] + d_to_p
            get_depth(child)


    get_depth(0)

    def swap_node(u, v):
        if d[u] > d[v]:
            u, v = v, u
        delta = d[v] - d[u]
        for i in range(int(log2(n)), -1, -1):
            if get_bit(delta, i) == 1:
                v = a[v][i]
        return u, v

    def get_dist(u, v):
        swapped_u, swapped_v = swap_node(u, v)
        if swapped_u == swapped_v: return abs(len_to_root[u] - len_to_root[v]);
        else:
            for i in range(int(log2(n)), -1, -1):
                if a[swapped_u][i] != a[swapped_v][i]:
                    swapped_u = a[swapped_u][i]
                    swapped_v = a[swapped_v][i]
            lca = p[swapped_u]
            return (len_to_root[u] + len_to_root[v])-2*len_to_root[lca]

    a = [[0 for _ in range(int(log2(n)) + 1)] for __ in range(n)]
    for i in range(n):
        a[i][0] = p[i]
    for j in range(1, int(log2(n)) + 1):
        for i in range(1, n):
            a[i][j] = a[a[i][j-1]][j-1]

    n_queries = int(input())
    for _ in range(n_queries):
        u, v = map(int, input().split(" "))
        print(get_dist(u, v), end=' ')
    print("")
        