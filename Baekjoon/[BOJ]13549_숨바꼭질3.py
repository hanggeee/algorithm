'''
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는
가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''
from collections import deque

N, K = map(int, input().split())
if N==K:
    print(0)
    exit()
room = [-1]*100001
room[N] = 0


def bfs(N):
    q = deque()
    q.append(N)

    while q:
        present = q.popleft()
        if present == K:
            print(room[K])
            break
        left = present-1
        right = present+1
        jump = present*2
        if 0<=jump<=100000 and room[jump]==-1:
            room[jump]=room[present]
            q.appendleft(jump)
        if 0<=left<=100000 and room[left]==-1:
            room[left]=room[present]+1
            q.append(left)
        if 0<=right<=100000 and room[right]==-1:
            room[right]=room[present]+1
            q.append(right)

bfs(N)