n, m, i_0, j_0 = list(map(int, input().split(" ")))
matrice = [[0 for _ in range(m+1)] for __ in range(n+1)]
visited = [[False for _ in range(m+1)] for __ in range(n+1)]
distances = [[0 for _ in range(m+1)] for __ in range(n+1)]

for i in range(1, n+1):
    row = list(map(int, input().split(" ")))
    matrice[i][1:] = row

def check_edge(i, j):
    return i == 1 or i == n or j == 1 or j == m

dx = [-1,0,1,0]
dy = [0,1,0,-1]



queue = []
queue.append((i_0,j_0))
visited[i_0][j_0] = True

while len(queue) > 0:
    (i, j) = queue.pop(0)
    if check_edge(i, j):
        print(distances[i][j]+1)
        exit(0)
    for h in range(4):
        new_i = i+dx[h]
        new_j = j+dy[h]
        if not visited[new_i][new_j]:
            if matrice[new_i][new_j] == 0:
                distances[new_i][new_j] = distances[i][j] + 1
                visited[new_i][new_j] = True
                queue.append((new_i, new_j))
                
    


