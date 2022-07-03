from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

'''
direction
0 == 가로
1 == 대각선
2 == 세로
'''
def bfs(si, sj, direction):
    global cnt
    q = deque()
    q.append((si, sj, direction))

    while q:
        ci, cj, dir = q.popleft()
        if ci == N-1 and cj == N-1:
            cnt += 1
            continue
        if dir == 0: # 가로 방향일 때
            ni, nj = ci+0, cj+1 # 가로로 이동
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
                q.append((ni, nj, 0))
            ni, nj = ci+1, cj+1 # 대각선으로 이동
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and arr[ci+1][cj] == 0 and arr[ci][cj+1] == 0:
                q.append((ni, nj, 1))
        elif dir == 1: # 대각선 방향일 때
            ni, nj = ci+0, cj+1 # 가로로 이동
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
                q.append((ni, nj, 0))
            ni, nj = ci+1, cj+1 # 대각선으로 이동
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and arr[ci+1][cj] == 0 and arr[ci][cj+1] == 0:
                q.append((ni, nj, 1))
            ni, nj = ci+1, cj+0 # 세로로 이동
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
                q.append((ni, nj, 2))
        elif dir == 2:
            ni, nj = ci+1, cj # 세로로 이동
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
                q.append((ni, nj, 2))
            ni, nj = ci+1, cj+1 # 대각선으로 이동
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and arr[ci+1][cj] == 0 and arr[ci][cj+1] == 0:
                q.append((ni, nj, 1))

bfs(0, 1, 0)

print(cnt)

def dfs(si, sj, direction):
    global cnt
    if si == N-1 and sj == N-1:
        cnt += 1
    if direction == 0: # 가로
        if sj + 1 < N and arr[si][sj+1] == 0:
            dfs(si, sj+1, 0)
        if si + 1 < N and sj + 1 < N:
            if arr[si][sj+1] == 0 and arr[si+1][sj+1] == 0 and arr[si+1][sj] == 0:
                dfs(si+1, sj+1, 2) # 대각선으로 변경
    elif direction == 1: # 세로
        if si + 1 < N and arr[si+1][sj] == 0:
            dfs(si+1, sj, 1)
        if si + 1 < N and sj + 1 < N:
            if arr[si+1][sj+1] == 0 and arr[si][sj+1] == 0 and arr[si+1][sj] == 0:
                dfs(si+1, sj+1, 2)
    elif direction == 2: # 대각선
        if sj + 1 < N and arr[si][sj+1] == 0:
            dfs(si, sj+1, 0)
        if si + 1 < N and arr[si+1][sj] == 0:
            dfs(si+1, sj, 1)
        if si + 1 < N and sj + 1 < N:
            if arr[si+1][sj+1] == 0 and arr[si+1][sj] == 0 and arr[si][sj+1] == 0:
                dfs(si+1, sj+1, 2)

dfs(0, 1, 0)
print(cnt)