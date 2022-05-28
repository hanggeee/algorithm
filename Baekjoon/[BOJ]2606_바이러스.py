# 양방향 연결 된 그래프 만들어주고 BFS

computer = int(input())
edge = int(input())

visited = [0]*(computer+1) # 방문처리 할 컴퓨터의 개수니까 인덱스 맞추기 위해 +1
adj_list = [[] for _ in range(computer+1)]
for _ in range(edge):
    c1, c2 = map(int, input().split())
    adj_list[c1].append(c2)
    adj_list[c2].append(c1) # 양방향이므로 반대 방향도 추가

# print(adj_list)

virus = 0
def bfs(start):
    q = []

    q.append(start)

    while q:
        current = q.pop(0)
        visited[current] = 1
        for i in range(len(adj_list[current])):
            if visited[adj_list[current][i]]==0:
                q.append(adj_list[current][i])
                visited[adj_list[current][i]] = 1

bfs(1)

# 1번 컴퓨터를 통해 바이러스가 걸리는 컴퓨터의 수이므로
# 1번 컴퓨터는 제외
print(sum(visited)-1)
