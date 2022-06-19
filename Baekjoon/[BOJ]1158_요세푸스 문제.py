N, K = map(int, input().split())

q = [i+1 for i in range(N)]
idx = K-1
ans = []
while q:
    ans.append(q.pop(idx))
    if not q:
        break
    idx += K-1
    idx = idx % len(q)

print("<",', '.join(str(i) for i in ans), ">", sep='')