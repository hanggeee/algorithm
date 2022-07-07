'''
뭉쳐있다 -> BFS 탐색
'''

N, M = map(int, input().split()) # 가로 N, 세로 M
arr = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
white = 0
blue = 0
def bfs(si, sj):
    global white, blue
    q = []
    q.append((si, sj))
    visited[si][sj] = 1
    color = arr[si][sj] # 현재 탐색하는 옷의 색 ( W or B )
    cnt = 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0,1), (1,0), (0,-1), (-1, 0)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj]:
                if color == arr[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1
    if color == 'W':
        white += cnt**2
    else:
        blue += cnt**2

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

print(white, blue)