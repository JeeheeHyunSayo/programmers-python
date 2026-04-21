def solution(num):
    cnt = 0
    if num == 1:
        return 0
    for i in range(500):
        if num % 2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1
        cnt += 1
        if num == 1:
            return cnt
    return -1

# 틀린 이유 : 초기값이 1인 경우를 고려하지 않아서
def solution1(num):
    for cnt in range(500):
        if num == 1:
            return cnt
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    return -1