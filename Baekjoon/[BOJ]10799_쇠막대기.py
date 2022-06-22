'''
() -> 레이저
( -> 막대기
) -> 바로 앞에 '('가 오면 스택에 남은 '(' 개수만큼 조각 증가
  -> 바로 앞에 ')'가 오면 cnt += 1
'''
iron = input()

stack = []
before = ''
cnt = 0
for i in iron:
    if i == '(':
        stack.append(i)
        before = i
    elif i == ')':
        if before == '(':
            stack.pop()
            cnt += len(stack)
        elif before == ')':
            stack.pop()
            cnt += 1
        before = i
print(cnt)

