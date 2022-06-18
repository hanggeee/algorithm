board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if "X" in board:
    print(-1)
else:
    print(board)

# 처음에는 for문을 모두 돌면서 cnt랑 idx 체크하면서
# 일일이 하려고 계산하려 했는데 너무 무식한 방법이었다.
# 파이썬 문자열의 강력함을 느낄 수 있는 replace