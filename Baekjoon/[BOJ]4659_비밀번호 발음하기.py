while True:
    word = input()
    if word == 'end':
        break
    vowels = 'aeiou'

    vowel_cnt = 0
    vowel_repeat, consonant_repeat = 0,0
    temp = ''
    flag = True
    for i in word:
        if i in vowels:
            consonant_repeat = 0
            vowel_cnt += 1
            vowel_repeat += 1
            if vowel_repeat >= 3:
                flag = False
            if temp == i:
                if i == 'e' or i == 'o':
                    pass
                else:
                    flag = False

        else:
            vowel_repeat = 0
            consonant_repeat += 1
            if consonant_repeat >= 3:
                flag = False
            if temp == i:
                flag = False
        temp = i

    if vowel_cnt < 1:
        flag = False

    if flag:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')

