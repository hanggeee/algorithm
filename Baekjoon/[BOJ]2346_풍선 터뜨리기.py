from collections import deque

N = int(input())

q = deque(enumerate(map(int,(input().split()))))

# enumerate를 사용하여 index와 풍선 속 종이값이 같이 나오게 한다.

ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx+1)
    if paper > 0:
        q.rotate(-(paper-1))
    else:
        q.rotate(-paper)

print(*ans)