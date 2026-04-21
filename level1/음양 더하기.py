def solution1(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        if not s:
            answer += a * -1
        else:
            answer += a
    return answer

# 삼항 연산자
def solution2(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        answer += a if s else -a
    return answer

# sum()
def solution3(absolutes, signs):
    return sum(a if s else -a for a, s in zip(absolutes, signs))