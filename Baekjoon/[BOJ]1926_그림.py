N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

num_painting = 0
max_painting = 0
def bfs(si, sj):
    global num_painting, max_painting

    q = []
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj]==1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    num_painting += 1
    if cnt > max_painting:
        max_painting = cnt

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(num_painting)
print(max_painting)
