import sys

input = sys.stdin.readline


n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

sheep = 0
wolf = 0


def bfs(si, sj):
    global sheep, wolf
    q = []
    q.append((si, sj))
    visited[si][sj] = 1
    k = 0
    v = 0
    if arr[si][sj] == 'k':
        k += 1
    else:
        v += 1
    while q:
        ci, cj = q.pop()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and arr[ni][nj] != '#':
                if arr[ni][nj] == 'k':
                    k += 1
                elif arr[ni][nj] == 'v':
                    v += 1
                q.append((ni, nj))
                visited[ni][nj] = 1
    if v < k:
        sheep += k
    else:
        wolf += v


for i in range(n):
    for j in range(m):
        if not visited[i][j] and (arr[i][j] == 'k' or arr[i][j] == 'v'):
            bfs(i, j)

print(sheep, wolf)