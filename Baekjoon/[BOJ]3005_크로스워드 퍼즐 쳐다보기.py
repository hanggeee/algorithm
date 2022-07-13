R, C = map(int, input().split())
word = [list(input()) for _ in range(R)]
ans = []

for i in range(R):
    cand = ''
    for j in range(C):
        if word[i][j] != '#':
            cand += word[i][j]
        else:
            if len(cand) >= 2:
                ans.append(cand)
            cand = ''

    if len(cand) >= 2:
        ans.append(cand)

for i in range(C):
    cand2 = ''
    for j in range(R):
        if word[j][i] != '#':
            cand2 += word[j][i]
        else:
            if len(cand2) >= 2:
                ans.append(cand2)
            cand2 = ''

    if len(cand2) >= 2:
        ans.append(cand2)


ans.sort()
print(ans)