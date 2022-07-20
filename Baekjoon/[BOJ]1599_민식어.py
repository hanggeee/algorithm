n = int(input())

cand = []
minSick = {"a": "A", "b": "B", "k":"C",
            "d": "D", "e":"E", "g":"F",
            "h":"G", "i":"H", "l":"I",
            "m":"J", "n":"K", "ng": "L",
            "o":"M", "p":"N", "r":"O",
            "s":"P", "t":"Q", "u":"R",
            "w":"S","y":"T"
            }


for _ in range(n):
    word = input()
    result = word.replace('ng', 'L')
    for k, v in minSick.items():
        result = result.replace(k, v)

    cand.append(result)


cand.sort()
for i in range(len(cand)):
    answer = ''.join(cand[i])
    for k, v in minSick.items():
        answer = answer.replace(v, k)
    print(answer)

