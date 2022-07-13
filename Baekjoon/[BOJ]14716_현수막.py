from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

cnt = 0
def bfs(si, sj):
    global cnt
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
    cnt += 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(cnt)