import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    word = input().strip()
    start = 0
    end = len(word)-1
    chance = 1
    while True:
        if start >= end:
            if chance == 1:
                print(0)
            elif chance == 0:
                print(1)
            break
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            if chance > 0 and word[start+1] == word[end]:
                while start > end:

            if chance > 0 and word[start] == word[end-1]:
                check = word[start:end]
                if check == check[::-1]:
                    print(1)
                    break
            else:
                print(2)
                break
