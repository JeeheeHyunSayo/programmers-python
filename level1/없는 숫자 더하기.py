# 과하게 복잡한 풀이
def solution1(numbers):
    d = {}
    answer = 0
    for i in range(1, 10):
        d[i] = 0
    for j in numbers:
        if j in d:
            d[j] += 1
    for k in d:
        if d[k] == 0:
            answer += k
    return answer

# 1 ~ 9 까지의 합에서 없는 수의 합 : 45 - 전체 배열의 합
def solution2(numbers):
    return 45 - sum(numbers)