T = int(input())

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for tc in range(T):
    N, M = map(int, input().split())
    bridge = factorial(M) // (factorial(N) * factorial(M-N))
    print(bridge)