def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    engDict = {}
    for e, i in zip(eng, range(0, 10)):
        engDict[e] = i

    term = ''
    answer = ''

    # 아래 부분 아이디어는 있었는데, 구현을 잘 못함
    for char in s:
        if char.isdigit():
            answer += char
        else:
            term += char
            if term in engDict:
                answer += str(engDict[term])
                term = ''

    return int(answer)

