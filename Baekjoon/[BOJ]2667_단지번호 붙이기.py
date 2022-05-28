N = int(input())

arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

cnt = 0
house = []

def bfs(si, sj):
    q = []
    q.append((si,sj))

    visited[si][sj] = 1
    house_num = 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = 1
                house_num += 1  # BFS 돌면서 집의 개수를 1개씩 카운트

    house.append(house_num)     # BFS 종료 후 단지 내 집의 개수를 house list에 append

# 전체 arr를 순회하면서 집이 있으면 BFS 실행

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1            # BFS 한 번할 때마다 카운트 -> 단지 수

print(cnt)
house.sort()
for i in range(len(house)):
    print(house[i])