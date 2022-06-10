import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
water_list = list(map(int, input().split()))
visit = set() # 범위가 -1억~1억이라 list 하면 메모리 초과
q = deque()

for i in water_list:
    q.append((i, 1))
    visit.add(i)

result = 0                      # 불행도 합
now_build = 0                   # 지어진 집 수

while q:
    now, dist = q.popleft()     # 위치, 거리(불행도)
    for d in [1, -1]:
        nx = now + d
        if nx in visit:
            continue
        visit.add(nx)
        result += dist
        now_build += 1
        q.append((nx, dist+1))
        if now_build == K:
            # print(q) # deque([(4, 2), (2, 2), (-2, 3)])
            q = list() # deque를 list로 바꾸면 안에 있는 거 다 사라
            # print(q) # []
            break
print(result)