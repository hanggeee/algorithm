N = int(input())

ans = dict()
for _ in range(N):
    name = input().split('.')
    if name[1] in ans:
        ans[name[1]] += 1
    else:
        ans[name[1]] = 1

result = []

for key, value in ans.items():
    result.append((key, value))

result.sort()
for i in range(len(result)):
    print(result[i][0], result[i][1])

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# file = dict()
# for _ in range(n):
#     extend = (input().split('.'))[1]
#     if not extend in file:
#         file[extend] = 1
#     else:
#         file[extend] += 1
#
# sort_file = sorted(file.items())
#
# for key, value in sort_file:
#     print(key.rstrip(), value)