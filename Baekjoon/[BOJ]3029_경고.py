start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

if start == end:
    print('24:00:00')
    exit()

if end[2] >= start[2]: # 초가 더 크면
    end[2] -= start[2]
else:
    end[1] -= 1
    end[2] = end[2] - start[2] + 60

if end[1] >= start[1]: # 분이 더 크면
    end[1] -= start[1]
else:
    end[0] -= 1
    end[1] = end[1] - start[1] + 60

if end[0] >= start[0] : # 시가 더 크면
    end[0] -= start[0]
else:
    end[0] = end[0] - start[0] + 24
for i in range(3):
    if len(str(end[i])) == 1:
        end[i] = '0' + str(end[i])
    else:
        end[i] = str(end[i])

print(':'.join(end))