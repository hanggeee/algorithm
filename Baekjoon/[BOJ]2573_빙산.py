import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())                                            # arr 크기
arr = [list(map(int, input().split())) for _ in range(N)]
check_visited = [[0]*M for _ in range(N)]                                   # check 함수에 대한 visited

# 빙산의 갯수를 세는 check 함수
# check 함수 도는 횟수만큼 while문 내의 cnt가 증가
def check(i, j):
    q = deque()
    q.append((i,j))
    check_visited[i][j] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = ci + di
            nj = cj + dj
            if arr[ni][nj] > 0 and not check_visited[ni][nj]:
                q.append((ni, nj))
                check_visited[ni][nj] = 1


year = 0                                        # 년
while True:
    # 여기에 빙산 갯수 check 함수 넣기
    # 빙산 갯수가 2개 되면 break 걸고 년수 print
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and not check_visited[i][j]:
                check(i, j)
                cnt += 1 # 빙산의 갯수
    if cnt > 1: # 빙산이 2개 이상이면 쪼개진 거니까 년 수 출력
        print(year)
        break
    elif cnt == 1: # 빙산이 1개면 계속 진행
        pass
    elif cnt == 0: # 빙산이 다 사라졌으면 0을 출력
        print(0)
        break
    check_visited = [[0] * M for _ in range(N)] # checked_visited 초기화


    visited = [[0] * M for _ in range(N)] # visited 초기화
    '''
    상하좌우를 탐색하면서 0의 갯수만큼 빼주는 이중 포문
    지금 python3에서는 시간초과가 나는데 포문 두개 합치면 괜찮으려나?
    '''
    for i in range(N-2):
        for j in range(M-2):
            cnt = 0
            if arr[i+1][j+1] > 0:
                for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
                    ni = di + i+1
                    nj = dj + j+1
                    if arr[ni][nj]==0:
                        cnt += 1
                visited[i+1][j+1] = cnt
            # if arr[i+1][j+1]-visited[i+1][j+1] < 0:
            #     arr[i+1][j+1] = 0
            # else:
            #     arr[i+1][j+1] -= visited[i+1][j+1]
    for i in range(N-2):
        for j in range(M-2):
            if arr[i+1][j+1]-visited[i+1][j+1]<0:
                arr[i+1][j+1] = 0
            else:
                arr[i+1][j+1] -= visited[i+1][j+1]

    year += 1
