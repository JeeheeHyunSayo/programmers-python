def solution1(arr):
    return sum(arr) / len(arr)
# 피드백) len(arr) == 0 인 경우도 있고, 내장 함수 사용 말고 다른 걸로


def solution2(arr):
    total = 0
    for i in arr:
        total += i
    return total / len(arr)