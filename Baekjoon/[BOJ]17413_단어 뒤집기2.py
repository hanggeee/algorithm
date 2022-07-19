lst = input()

result = []
for alpha in lst:
    if alpha == '<':
        temp = lst[:lst.index(alpha)]
        if temp != '':
            result.append(temp)
        lst = lst[lst.index(alpha):]

    elif alpha == '>':
        temp = lst[:lst.index(alpha)+1]
        if temp != '':
            result.append(temp)
        lst = lst[lst.index(alpha)+1:]


    if alpha == ' ':
        temp = lst[:lst.index(alpha)]
        if temp[0] == '<':
            pass
        else:
            result.append(temp)
            result.append(' ')
            lst = lst[lst.index(alpha)+1:]

if lst != '':
    result.append(lst)

for s in result:
    if s[0] == '<':
        print(s, end='')
    else:
        print(s[::-1],end='')