def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(len(t)-l+1):
        part = t[i:i+l]
        if part <= p:
            answer+=1
    return answer


# 불필요한 부분을 줄이고 좀 더 효율적이게
def solution1(t, p):
    answer = 0
    l = len(p)
    for i in range(len(t)-l+1):
        if int(t[i:i+l]) <= int(p):
            answer +=1
    return answer