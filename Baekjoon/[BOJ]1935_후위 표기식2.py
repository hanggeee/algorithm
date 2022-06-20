
N = int(input())

formula = input()
num_lst = [int(input()) for i in range(N)]

stack = []
for i in formula:
    if i == '*':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 * num2)
    elif i == '/':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 / num2)
    elif i == '+':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 + num2)
    elif i == '-':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 - num2)
    else:
        stack.append(num_lst[ord(i)-65])

print(f'{stack.pop():.2f}')