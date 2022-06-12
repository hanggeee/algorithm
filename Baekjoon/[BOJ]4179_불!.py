# import sys
# from collections import deque
# from pprint import pprint
# N, M = map(int, input().split())
# arr = [list(input()) for _ in range(N)]
# q = deque()
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == "J":
#             ji, jj = i, j
#             q.append((ji, jj))
#         if arr[i][j] == "F":
#             fi, fj = i, j
#             q.append((fi, fj))
#
# cnt = 1
#
# for j in range(N):
#     if arr[j][0] == "J" or arr[j][-1] == "J":
#         print(cnt)
#         exit()
#
#
#
#
# while q:
#     ci, cj = q.popleft()
#     if ci==0 and arr[ci][cj]=="J":
#         print(cnt)
#         exit()
#     elif cj==0 and arr[ci][cj]=="J":
#         print(cnt)
#         exit()
#     elif ci==N-1 and arr[ci][cj]=="J":
#         print(cnt)
#         exit()
#     elif cj==M-1 and arr[ci][cj]=="J":
#         print(cnt)
#         exit()
#     if arr[ci][cj] == "J":
#         for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
#             ni = ci + di
#             nj = cj + dj
#             if 0<=ni<N and 0<=nj<M and arr[ni][nj] == ".":
#                 q.append((ni, nj))
#                 arr[ni][nj] = "J"
#                 cnt += 1
#     elif arr[ci][cj] == "F":
#         for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#             ni = ci + di
#             nj = cj + dj
#             if 0<=ni<N and 0<=nj<M and (arr[ni][nj] == "." or arr[ni][nj] == "J"):
#                 q.append((ni, nj))
#                 arr[ni][nj] = "F"
#
# print('IMPOSSIBLE')

from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    global q, f
    while q:
        temp = deque()
        while q:
            x, y = q.popleft()
            if (x == r - 1 or y == c - 1 or x == 0 or y == 0) and s[x][y] != "F": return s[x][y] + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and s[nx][ny] == "." and s[x][y] != "F":
                    temp.append([nx, ny])
                    s[nx][ny] = s[x][y] + 1
        q = temp
        if not q: break
        temp = deque()
        while f:
            x, y = f.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and s[nx][ny] != "#":
                    temp.append([nx, ny])
                    visit[nx][ny] = 1
                    s[nx][ny] = "F"
        f = temp
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
r, c = map(int, input().split())
s = []
q = deque()
f = deque()
visit = [[0] * c for i in range(r)]
for i in range(r):
    a = list(input().strip())
    s.append(a)
    for j in range(c):
        if a[j] == "J":
            q.append([i, j])
            s[i][j] = 0
        elif a[j] == "F":
            f.append([i, j])
            visit[i][j] = 1
result = bfs()
print(result if result != None else "IMPOSSIBLE")