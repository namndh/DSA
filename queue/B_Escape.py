from collections import defaultdict
from queue import Queue


m = int(input())
n = int(input())
matrice = [[0 for _ in range(n+1)] for __ in range(m+1)]
visited = [[False for _ in range(n+1)] for __ in range(m+1)]
possibles = defaultdict(list)
value_check = defaultdict(bool)
for i in range(1, m+1):
    for j in range(1, n+1):
        possibles[i*j].append((i,j))
        value_check[i*j] = False

for i in range(1, m+1):
    row = list(map(int, input().split(" ")))
    matrice[i][1:] = row


queue = Queue()
queue.put((1, 1))
visited[1][1] = True

while queue.qsize() > 0:
    (i, j) = queue.get()
    if i == m and j == n:
        print('yes')
        exit(0)
    if value_check[matrice[i][j]]:
        continue
    for new_i, new_j in possibles[matrice[i][j]]:
        if not visited[new_i][new_j]:
            visited[new_i][new_j] = True
            queue.put((new_i, new_j))
    value_check[matrice[i][j]] = True

print('no')