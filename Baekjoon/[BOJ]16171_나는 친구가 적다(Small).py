note = input()

keyword = input()
note_without_num = ''

for s in note:
    if 48 <= ord(s) <= 57: # 숫자면
        pass
    else:
        note_without_num += s

for s in note:
    if s.isalpha():
        note_without_num += s

if keyword in note_without_num:
    print(1)
else:
    print(0)
