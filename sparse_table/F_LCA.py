from math import log2, floor
import sys
from collections import defaultdict


sys.setrecursionlimit(10**6)
n = int(input())
tree_raw_input = list(map(int, input().split(" ")))
no_queries = int(input())
queries = []
for _ in range(no_queries):
    queries.append(list(map(int, input().split(" "))))

p = [0 for _ in range(n+1)]
for i in range(1, n+1):
    p[i] = tree_raw_input[i-1]


c = defaultdict(list)
a = [[0 for _ in range(int(log2(n)) + 1)] for __ in range(n+1)]

for i in range(1, n+1):
    c[p[i]].append(i)
    a[i][0] = p[i]


d = [0 for _ in range(n+1)]
def get_depth(r):
    global d
    for child in c[r]:
        d[child] = d[r] + 1
        get_depth(child)
get_depth(0)

for j in range(1, int(log2(n)) + 1):
    for i in range(1, n+1):
        a[i][j] = a[a[i][j-1]][j-1]


def get_bit(number, i):
    return (number >> i) & 1


def swap_node(u, v):
    if d[u] > d[v]:
        u, v = v, u
    delta = d[v] - d[u]
    for i in range(int(log2(n)), -1, -1):
        if get_bit(delta, i) == 1:
            v = a[v][i]
    return u, v
    

def get_lca(u, v):
    u, v = swap_node(u, v)
    if u == v: return u;
    else:
        for i in range(int(log2(n)), -1, -1):
            if a[u][i] != a[v][i]:
                u = a[u][i]
                v = a[v][i]
        return p[u]

for u, v in queries:
    print(get_lca(u, v))