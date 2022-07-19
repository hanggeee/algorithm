T = int(input())

for tc in range(T):

    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    q = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '#' and visited[i][j] == 0:
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    ci, cj = q.pop(0)
                    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ni = ci + di
                        nj = cj + dj
                        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == '#':
                            q.append((ni, nj))
                            visited[ni][nj] = 1
                cnt += 1
    print(cnt)
