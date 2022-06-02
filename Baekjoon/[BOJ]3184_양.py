import sys
from collections import deque

input = sys.stdin.readline
"""
울타리 안을 bfs 돌면서
양, 늑대, 길(?)일 경우만 q에 추가
양과 늑대의 수를 카운트한 후에
while문 종료 시 두 수를 비교 후
전체 ans_wolf, ans_sheep에 추가 결정
"""
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
ans_wolf = 0
ans_sheep = 0
def bfs(i, j):
    global ans_wolf, ans_sheep
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    wolf = 0
    sheep = 0
    while q:
        ci, cj = q.popleft()
        if arr[ci][cj] == 'o':
            sheep += 1
        elif arr[ci][cj] == 'v':
            wolf += 1
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<= ni < N and 0<= nj < M and visited[ni][nj]==0 and arr[ni][nj] != '#':
                q.append((ni, nj))
                visited[ni][nj] = 1
    if wolf >= sheep:
        ans_wolf += wolf
    elif wolf < sheep:
        ans_sheep += sheep


for i in range(N):
    for j in range(M):
        if (arr[i][j]=='o' or arr[i][j]=='v') and visited[i][j]==0:
            bfs(i,j)

print(ans_sheep, ans_wolf)