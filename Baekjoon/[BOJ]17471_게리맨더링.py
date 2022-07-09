# 양방향 그래프 만들고 어떻게 탐색할 것인가?
import itertools
from collections import deque

def bfs(same):
    start = same[0]
    q = deque([start])
    visited = set([start])
    cnt = 0

    while q:
        v = q.popleft()
        cnt += num[v]
        for u in graph[v]:
            if u not in visited and u in same:
                q.append(u)
                visited.add(u)
    return cnt, len(visited)

N = int(input())
num = [0]+list(map(int, input().split()))
# print(f'num is {num}')
graph = [[] for _ in range(N+1)]
result = 987654321

for i in range(N):
    info = list(map(int, input().split()))
    # info[0] = 인접한 구역의 수
    # info[1~] = 인접한 구역의 번호
    graph[i+1] = info[1:]
# print(graph)

for i in range(1, N//2 + 1):
    combis = list(itertools.combinations(range(1, N+1), i))
    # print(combis)
# # bfs와 combination의 조합으로 두 선거구로 나누어지는 모든
# # 경우의 수 중 인구 차이의 최솟값을 구하면 될 것 같음

    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(1, N+1) if i not in combi])

        if v1 + v2 == N:
            result = min(result, abs(sum1-sum2))
            # print(result)
if result == 987654321:
    print(-1)
else:
    print(result)