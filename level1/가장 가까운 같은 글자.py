# 한 번 저장하고 재사용
def solution(s):
    answer = []
    d = {}
    for i, char in enumerate(s):
        if char not in d:
            answer.append(-1)
        else:
            answer.append(i-d[char])
        d[char] = i
    return answer