number = list(map(int, input()))

number.sort()
number = number[::-1]

for i in range(len(number)):
    print(number[i], end='')