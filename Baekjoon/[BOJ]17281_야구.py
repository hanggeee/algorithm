# import sys
# from itertools import permutations
# from collections import deque
#
# input = sys.stdin.readline
# inning = int(input())
# hitting = [list(map(int, input().split())) for _ in range(inning)]
#
# max_score = 0
# def game(line_ups):
#     idx = 0
#     score = 0
#     for each_inning in hitting:
#         out = 0
#         base = deque([0, 0, 0])
#         while True:
#             if out == 3:
#                 break
#             if each_inning[line_ups[idx]] == 0:
#                 out += 1
#             elif each_inning[line_ups[idx]] == 1:
#                 base.appendleft(1)
#                 score += base.pop()
#             elif each_inning[line_ups[idx]] == 2:
#                 base.appendleft(1)
#                 base.appendleft(0)
#                 score += base.pop()
#                 score += base.pop()
#             elif each_inning[line_ups[idx]] == 3:
#                 base.appendleft(1)
#                 base.appendleft(0)
#                 base.appendleft(0)
#                 score += base.pop()
#                 score += base.pop()
#                 score += base.pop()
#             elif each_inning[line_ups[idx]] == 4:
#                 base.appendleft(1)
#                 base.appendleft(0)
#                 base.appendleft(0)
#                 base.appendleft(0)
#                 score += base.pop()
#                 score += base.pop()
#                 score += base.pop()
#                 score += base.pop()
#             idx = (idx + 1) % 9
#     return score
#
# for line_ups in permutations(range(1, 9), 8):
#     line_ups = list(line_ups[:3]) + [0] + list(line_ups[3:])
#     max_score = max(max_score, game(line_ups))
#
# print(max_score)

import sys
from itertools import permutations
from collections import deque

input = sys.stdin.readline
inning = int(input())
hitting = [list(map(int, input().split())) for _ in range(inning)]

max_score = 0
def game(line_ups):
    idx = 0
    score = 0
    for each_inning in hitting:
        out = 0
        # base = deque([0, 0, 0])
        b1, b2, b3 = 0, 0, 0
        while True:
            if out == 3:
                break
            if each_inning[line_ups[idx]] == 0:
                out += 1
            elif each_inning[line_ups[idx]] == 1:
                # base.appendleft(1)
                # score += base.pop()

                score += b3
                b1, b2, b3 = 1, b1, b2
            elif each_inning[line_ups[idx]] == 2:
                # base.appendleft(1)
                # base.appendleft(0)
                # score += base.pop()
                # score += base.pop()
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif each_inning[line_ups[idx]] == 3:
                # base.appendleft(1)
                # base.appendleft(0)
                # base.appendleft(0)
                # score += base.pop()
                # score += base.pop()
                # score += base.pop()

                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif each_inning[line_ups[idx]] == 4:
                # base.appendleft(1)
                # base.appendleft(0)
                # base.appendleft(0)
                # base.appendleft(0)
                # score += base.pop()
                # score += base.pop()
                # score += base.pop()
                # score += base.pop()
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9
    return score

for line_ups in permutations(range(1, 9), 8):
    print(line_ups)
    line_ups = list(line_ups[:3]) + [0] + list(line_ups[3:])
    max_score = max(max_score, game(line_ups))

print(max_score)