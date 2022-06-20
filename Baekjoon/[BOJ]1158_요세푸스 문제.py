N, K = map(int, input().split())

q = [i+1 for i in range(N)]
idx = K-1 # 여기서 1을 빼는 이유는 인덱스 번호는 0부터 시작하니
ans = []
while q:
    ans.append(q.pop(idx))
    if not q:
        break
    idx += K-1 # 여기서 1을 빼는 이유는 q에서 하나 pop 했으니까 ㄲ
    idx = idx % len(q)

print("<",', '.join(str(i) for i in ans), ">", sep='')