
paren = list(input())

stack = []

cnt1 = 0
cnt2 = 0
result = 0
before = ''
for i in range(len(paren)):
    if paren[i] == '(' or paren[i] == '[': # 여는 괄호면
        stack.append(paren[i])
        print(stack)
    elif paren[i] == ')' and stack[-1] == '(': # 가장 위에 있는 괄호랑 짝이 맞으면
        stack.pop()
        if before == ')':
            cnt1 *= 2
        else:
            if stack:
                cnt1 += 2
            else:
                if cnt2 > 0:
                    result += (cnt1 * cnt2)
            
    elif paren[i] == ']' and stack[-1] == '[':
        stack.pop()
        if before == ']':
            cnt2 *= 3
        else:
            if stack:
                cnt2 += 3
            else:
                pass
print(result)
