N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
flag = 0
def bfs(si, sj):
    global flag
    q = []

    q.append((si,sj))
    visited[si][sj]=1
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and not visited[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj]=1
                if ni==0:
                    flag = 1


for j in range(M):
    if arr[N-1][j]==0 and not visited[N-1][j]:
        bfs(N-1, j)

if flag==0:
    print('NO')
else:
    print('YES')