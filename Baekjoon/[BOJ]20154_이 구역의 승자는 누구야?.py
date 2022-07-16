from collections import deque

strokes = '32123333113133122212112221'

word = input()

ans = []

for i in word:
    ans.append(int(strokes[ord(i)-65]))

if sum(ans) % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")