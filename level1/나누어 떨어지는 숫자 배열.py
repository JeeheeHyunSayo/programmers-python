def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)

# 좀 더 효율적인 방법으로
def solution1(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0 ]) or [-1]
