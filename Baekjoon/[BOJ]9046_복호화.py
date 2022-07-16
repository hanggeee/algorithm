N = int(input())


for _ in range(N):
    ans = [0] * 26
    sentence = input()
    for alpha in sentence:
        if alpha != ' ':
            ans[ord(alpha)-97] += 1
        # print(ord(alpha)-97)
    temp = sorted(ans)
    if temp[-1] == temp[-2]:
        print('?')
    else:
        print(chr(ans.index(max(ans)) + 97))