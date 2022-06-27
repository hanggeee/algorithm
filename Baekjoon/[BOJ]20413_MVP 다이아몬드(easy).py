N = int(input())
standards = list(map(int, input().split()))
grades = input()

last = 0 # 지난 달 과금액
now = 0 # 이번 달 과금액
cnt = 0 # 과금액 최대 합

for grade in grades:
    if grade == 'B':
        now = standards[0]-1-last
        cnt += now
    elif grade == 'S':
        now = standards[1] - 1 - last
        cnt += now

    elif grade == 'G':
        now = standards[2] - 1 - last
        cnt += now

    elif grade == 'P':
        now = standards[3] - 1 - last
        cnt += now

    elif grade == 'D':
        now = standards[3]
        cnt += now
    last = now
print(cnt)