from utils import SegmentTree, Node

n, no_queries = map(int, input().split(" "))
queries = []
for _ in range(no_queries):
    query = list(map(int, input().split(" ")))
    queries.append(query)

array = [0 for _ in range(n+1)]
root = SegmentTree.build(1, n, array)
for query, i, j in queries:
    if query == 1:
        SegmentTree.update(root, i, j)
    elif query == 2:
        print(SegmentTree.get_max(root, i, j))