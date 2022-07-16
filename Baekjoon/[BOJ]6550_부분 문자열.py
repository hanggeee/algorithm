
while True:
    try:
        s, t = input().split()
        cand = ''
        for alpha_s in s:
            for alpha_t in range(len(t)):
                if alpha_s == t[alpha_t]:
                    cand += t[alpha_t]
                    t = t[alpha_t+1:]
                    break
        if cand == s:
            print('Yes')
        else:
            print('No')
    except:
        break