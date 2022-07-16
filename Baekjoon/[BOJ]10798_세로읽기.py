word = [list(input()) for _ in range(5)]

ans = ''
for i in range(15):
    for j in range(5):
        try:
            ans += word[j][i]
        except IndexError:
            pass
print(ans)